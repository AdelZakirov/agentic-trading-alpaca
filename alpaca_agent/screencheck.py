"""Persist a bounded, resumable moneyheap first pass for every shortlist ticker."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import time
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import URLError
import fcntl

from .config import load_dotenv
from .moneyheap import _atomic_write


def candidates(text: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    section = ""
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:]
        if re.match(r"^\|\s*\d+\s*\|", line):
            ticker = line.split("|")[2].strip().upper()
            if not re.fullmatch(r"[A-Z0-9][A-Z0-9.\-^=]{0,31}", ticker):
                raise ValueError("Invalid shortlist ticker")
            if section not in result.setdefault(ticker, []):
                result[ticker].append(section)
    if not result:
        raise ValueError("Shortlist has no candidates")
    return result


def validate(data: dict, ticker: str) -> None:
    if not isinstance(data, dict) or data.get("ticker") != ticker:
        raise ValueError("Response ticker mismatch")
    if data.get("status") not in ("ok", "partial", "error"):
        raise ValueError("Invalid response status")
    for key in ("generated_at", "data_as_of", "technical", "fundamental", "missing_data", "research_questions", "sources", "error"):
        if key not in data:
            raise ValueError(f"Missing response field: {key}")
    if datetime.fromisoformat(data["generated_at"].replace("Z", "+00:00")).tzinfo is None:
        raise ValueError("Missing response timezone")
    if not isinstance(data["data_as_of"], dict):
        raise ValueError("Invalid data timestamps")
    for key in ("technical", "fundamental"):
        if data[key] is not None and not isinstance(data[key], dict):
            raise ValueError(f"Invalid {key}")
    for key in ("missing_data", "research_questions"):
        if not isinstance(data[key], list) or not all(isinstance(x, str) for x in data[key]):
            raise ValueError(f"Invalid {key}")
    ids = [s["id"] for s in data["sources"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate source IDs")
    def walk(value):
        if isinstance(value, dict):
            if "source_ids" in value:
                refs = value["source_ids"]
                if not refs or len(refs) != len(set(refs)) or not set(refs) <= set(ids):
                    raise ValueError("Invalid source references")
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    walk(data)
    if (data["status"] == "error") != (data["error"] is not None):
        raise ValueError("Status/error mismatch")


def fetch(base_url: str, ticker: str, timeout: float) -> dict:
    request = Request(base_url.rstrip("/") + "/v1/analysis/screencheck",
                      data=json.dumps({"ticker": ticker, "prompt": None}).encode(),
                      headers={"Content-Type": "application/json", "Accept": "application/json"})
    with urlopen(request, timeout=timeout) as response:
        return json.load(response)


def run(shortlist: Path, output: Path, *, timeout=20.0, interval=61.0, budget=2700.0):
    text = shortlist.read_text()
    names = candidates(text)
    digest = hashlib.sha256(text.encode()).hexdigest()
    day = datetime.now(timezone.utc).date().isoformat()
    root = output / day / digest[:16]
    root.mkdir(parents=True, exist_ok=True)
    with (output / '.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return collect(text, names, digest, root, timeout, interval, budget)


def collect(text, names, digest, root, timeout, interval, budget):
    started = time.monotonic()
    rows = [{"ticker": t, "sources": sources, "status": "not_reviewed", "path": str(root / f"{t}.json")} for t, sources in names.items()]
    _atomic_write(root / "shortlist.md", text)
    _atomic_write(root / "coverage.json", json.dumps({"shortlist_sha256": digest, "rows": rows}, ensure_ascii=False))
    # This is a first-pass acquisition ledger, not an investment decision ledger.
    for row in rows:
        ticker = row["ticker"]
        path = Path(row["path"])
        if path.exists() and time.time() - path.stat().st_mtime < 3600:
            data = json.loads(path.read_text())
            validate(data, ticker)
            row["status"] = data["status"]
        else:
            pacing = root.parent.parent / "last-request.json"
            last = json.loads(pacing.read_text())["started_at"] if pacing.exists() else 0
            delay = max(0, interval - (time.time() - last))
            if time.monotonic() - started + delay + timeout > budget:
                row["reason"] = "Run time budget exhausted; not a ticker rejection"
            else:
                time.sleep(delay)
                _atomic_write(pacing, json.dumps({"started_at": time.time()}))
                try:
                    data = fetch(os.getenv("MONEYHEAP_API_URL", "http://127.0.0.1:8000"), ticker, timeout)
                except (URLError, TimeoutError, OSError, ValueError) as exc:
                    row.update(status="error", reason=f"Request failed: {type(exc).__name__}")
                else:
                    # Invalid captured responses are retained separately for diagnosis.
                    try:
                        validate(data, ticker)
                    except (ValueError, TypeError, KeyError, AttributeError) as exc:
                        _atomic_write(root / f"{ticker}.invalid.json", json.dumps(data, ensure_ascii=False))
                        row.update(status="error", reason=f"Invalid response: {type(exc).__name__}")
                    else:
                        _atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2))
                        row["status"] = data["status"]
        if row["status"] in ("ok", "partial"):
            row.update(data_as_of=data["data_as_of"], technical=data["technical"],
                       fundamental=data["fundamental"], missing_data=data["missing_data"],
                       research_questions=data["research_questions"])
        print(f"{ticker}: {row['status']}", flush=True)
        _atomic_write(root / "coverage.json", json.dumps({"shortlist_sha256": digest, "rows": rows}, ensure_ascii=False, indent=2))
    _atomic_write(root / "shortlist.md", text)
    _atomic_write(root / "summary.json", json.dumps({"shortlist_sha256": digest, "rows": rows}, ensure_ascii=False, separators=(',', ':')))
    print(json.dumps({"summary": str(root / "summary.json"), "counts": {s: sum(r['status'] == s for r in rows) for s in ('ok', 'partial', 'error', 'not_reviewed')}}))
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--shortlist', type=Path, default=Path('data/stage1_shortlist.md'))
    parser.add_argument('--output', type=Path, default=Path('memory/screenchecks'))
    parser.add_argument('--timeout', type=float, default=20)
    parser.add_argument('--interval', type=float, default=61)
    parser.add_argument('--budget', type=float, default=2700)
    args = parser.parse_args(argv)
    if args.timeout <= 0 or args.interval < 0 or args.budget <= 0:
        parser.error('timeout/budget must be positive; interval must be nonnegative')
    load_dotenv()
    rows = run(args.shortlist, args.output, timeout=args.timeout, interval=args.interval, budget=args.budget)
    return 0 if all(r['status'] in ('ok', 'partial') for r in rows) else 2


if __name__ == '__main__':
    raise SystemExit(main())
