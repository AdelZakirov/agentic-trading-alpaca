"""Request moneyheap research and persist the response locally.

The model should provide the request, but this module owns the HTTP response
after it arrives.  That keeps response persistence out of hand-authored
Markdown or patch text.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from .config import load_dotenv


AMSTERDAM = ZoneInfo("Europe/Amsterdam")
ANALYSIS_TYPES = frozenset({"fundamental", "technical"})
SAFE_COMPONENT = re.compile(r"^[A-Za-z0-9._-]+$")


class MoneyheapError(RuntimeError):
    """Raised when a moneyheap request or its required persistence fails."""


@dataclass(frozen=True, slots=True)
class ArtifactPaths:
    markdown: Path
    response_json: Path


def _validate_request(ticker: str, analysis_type: str) -> tuple[str, str]:
    normalized_ticker = ticker.strip().upper()
    normalized_type = analysis_type.strip().lower()
    if not normalized_ticker or not SAFE_COMPONENT.fullmatch(normalized_ticker):
        raise ValueError("ticker must contain only letters, numbers, '.', '_' or '-'")
    if normalized_type not in ANALYSIS_TYPES:
        raise ValueError("analysis_type must be 'fundamental' or 'technical'")
    return normalized_ticker, normalized_type


def _analysis_text(analysis: Any) -> str:
    if isinstance(analysis, str):
        return analysis.rstrip() + "\n"
    return "```json\n" + json.dumps(analysis, indent=2, ensure_ascii=False) + "\n```\n"


def render_markdown(
    *,
    ticker: str,
    analysis_type: str,
    request_time: datetime,
    prompt: str | None,
    previous_context: Any,
    response: Mapping[str, Any],
) -> str:
    """Render one human-readable artifact without duplicating ``analysis``."""

    lines = [
        f"# moneyheap research: {ticker} {analysis_type}",
        "",
        f"- Request time: {request_time.astimezone(AMSTERDAM).isoformat()}",
        f"- Ticker: {ticker}",
        f"- Analysis type: {analysis_type}",
        f"- Endpoint: /v1/analysis/{analysis_type}",
    ]
    response_model = response.get("model") or response.get("response_model")
    if response_model is not None:
        lines.append(f"- Response model: {response_model}")

    previous_text = (
        "null"
        if previous_context is None
        else json.dumps(previous_context, indent=2, ensure_ascii=False)
    )
    prompt_text = "null" if prompt is None else prompt
    lines.extend(
        [
            "",
            "## Prompt",
            "",
            prompt_text,
            "",
            "## Previous context",
            "",
            previous_text,
            "",
            "## Analysis",
            "",
        ]
    )
    analysis = response.get("analysis")
    if analysis is None:
        raise MoneyheapError("moneyheap response is missing a non-null analysis field")
    lines.append(_analysis_text(analysis).rstrip())
    return "\n".join(lines) + "\n"


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        fd, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
        )
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                Path(temporary_name).unlink()
            except FileNotFoundError:
                pass


def artifact_paths(
    root: Path,
    *,
    ticker: str,
    analysis_type: str,
    request_time: datetime,
) -> ArtifactPaths:
    ticker, analysis_type = _validate_request(ticker, analysis_type)
    local_time = request_time.astimezone(AMSTERDAM)
    stem = f"{local_time:%H%M%S}-{ticker}-{analysis_type}"
    directory = root / f"{local_time:%Y-%m-%d}"
    markdown = directory / f"{stem}.md"
    return ArtifactPaths(markdown=markdown, response_json=directory / f"{stem}.json")


def persist_response(
    paths: ArtifactPaths,
    *,
    ticker: str,
    analysis_type: str,
    request_time: datetime,
    prompt: str | None,
    previous_context: Any,
    response: Mapping[str, Any],
) -> None:
    """Persist the exact response object and a single rendered Markdown view."""

    response_json = json.dumps(response, indent=2, ensure_ascii=False) + "\n"
    markdown = render_markdown(
        ticker=ticker,
        analysis_type=analysis_type,
        request_time=request_time,
        prompt=prompt,
        previous_context=previous_context,
        response=response,
    )

    # Keep the raw parsed object as durable recovery data before rendering the
    # human-facing view.  The caller may retry this local operation without
    # making another moneyheap request if the Markdown write fails.
    _atomic_write(paths.response_json, response_json)
    _atomic_write(paths.markdown, markdown)

    if json.loads(paths.response_json.read_text(encoding="utf-8")) != dict(response):
        raise MoneyheapError("saved moneyheap JSON did not round-trip correctly")
    if paths.markdown.read_text(encoding="utf-8") != markdown:
        raise MoneyheapError("saved moneyheap Markdown did not round-trip correctly")


def _decode_response(body: bytes, status: int) -> dict[str, Any]:
    try:
        decoded = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise MoneyheapError(f"moneyheap returned invalid JSON (HTTP {status})") from error
    if not isinstance(decoded, dict):
        raise MoneyheapError("moneyheap response must be a JSON object")
    if "analysis" not in decoded:
        raise MoneyheapError("moneyheap response is missing the analysis field")
    return decoded


def fetch_response(
    *,
    base_url: str,
    ticker: str,
    analysis_type: str,
    prompt: str | None,
    previous_context: Any,
    timeout: float,
) -> dict[str, Any]:
    ticker, analysis_type = _validate_request(ticker, analysis_type)
    payload: dict[str, Any] = {
        "ticker": ticker,
        "prompt": prompt,
        "previous_context": previous_context,
    }
    endpoint = f"{base_url.rstrip('/')}/v1/analysis/{analysis_type}"
    request = Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as result:
            body = result.read()
            status = getattr(result, "status", 200)
    except HTTPError as error:
        error_body = error.read().decode("utf-8", errors="replace")
        raise MoneyheapError(f"moneyheap HTTP {error.code}: {error_body}") from error
    except URLError as error:
        raise MoneyheapError(f"moneyheap request failed: {error.reason}") from error
    if not 200 <= status < 300:
        error_body = body.decode("utf-8", errors="replace")
        raise MoneyheapError(f"moneyheap HTTP {status}: {error_body}")
    return _decode_response(body, status)


def fetch_and_persist(
    *,
    base_url: str,
    root: Path,
    ticker: str,
    analysis_type: str,
    prompt: str | None,
    previous_context: Any,
    timeout: float = 360.0,
    request_time: datetime | None = None,
) -> tuple[dict[str, Any], ArtifactPaths]:
    """Make one request and retry persistence locally once if needed."""

    captured_time = request_time or datetime.now(AMSTERDAM)
    response = fetch_response(
        base_url=base_url,
        ticker=ticker,
        analysis_type=analysis_type,
        prompt=prompt,
        previous_context=previous_context,
        timeout=timeout,
    )
    paths = artifact_paths(
        root,
        ticker=ticker,
        analysis_type=analysis_type,
        request_time=captured_time,
    )

    last_error: OSError | MoneyheapError | None = None
    for _ in range(2):
        try:
            persist_response(
                paths,
                ticker=ticker.strip().upper(),
                analysis_type=analysis_type.strip().lower(),
                request_time=captured_time,
                prompt=prompt,
                previous_context=previous_context,
                response=response,
            )
            return response, paths
        except (OSError, MoneyheapError) as error:
            last_error = error
    raise MoneyheapError(
        f"moneyheap succeeded but local persistence failed after two attempts: {last_error}"
    ) from last_error


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Call moneyheap once and persist its response locally."
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("memory/research")
    )
    parser.add_argument("--timeout", type=float, default=360.0)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        load_dotenv()
        raw_request = sys.stdin.read()
        request = json.loads(raw_request)
        if not isinstance(request, dict):
            raise ValueError("stdin must contain one JSON object")
        response, paths = fetch_and_persist(
            base_url=os.getenv("MONEYHEAP_API_URL", "http://127.0.0.1:8000"),
            root=args.output_dir,
            ticker=str(request["ticker"]),
            analysis_type=str(request["analysis_type"]),
            prompt=request.get("prompt"),
            previous_context=request.get("previous_context"),
            timeout=args.timeout,
        )
    except (KeyError, TypeError, ValueError, json.JSONDecodeError, MoneyheapError) as error:
        print(f"moneyheap research failed: {error}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "response": response,
                "markdown_path": str(paths.markdown),
                "response_json_path": str(paths.response_json),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
