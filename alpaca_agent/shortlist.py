"""Build the Stage 1 investigation shortlist.

The shortlist has three independent selections:

* the top community-interest tickers, deduplicated across community feeds;
* the top expert-attention candidates, using the order in the expert JSON;
* the top technical candidates by Reciprocal Rank Fusion (RRF).

Technical category ranks are calculated from descending category scores.  A
candidate only participates in RRF for categories where it has a finite score.
This intentionally excludes community interest and scoreless exploration
signals from the technical RRF calculation.
"""

from __future__ import annotations

import argparse
import json
import math
import numbers
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Mapping


DEFAULT_SCREEN_PATH = Path("data/stage1_screen.json")
DEFAULT_EXPERTS_PATH = Path("data/stage1_experts.json")
DEFAULT_OUTPUT_PATH = Path("data/stage1_shortlist.md")
DEFAULT_RRF_K = 10

COMMUNITY_CATEGORY_NAMES = frozenset({"community_attention", "community_interest"})
TECHNICAL_CATEGORY_ORDER = (
    "volume_anomaly",
    "momentum_breakout",
    "stretched_reversal",
    "volatility_expansion",
    "compression_breakout",
    "wildcard",
)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as error:
        raise ValueError(f"could not read {path}: {error}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON in {path}: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object in {path}")
    return value


def _text(value: Any, default: str = "") -> str:
    return default if value is None else str(value)


def _finite_number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        return None
    number = float(value)
    return number if math.isfinite(number) else None


def _positive_integer(value: int, name: str) -> int:
    if value < 1:
        raise ValueError(f"{name} must be positive")
    return value


def _escape_cell(value: Any) -> str:
    """Return a compact, safe Markdown table cell."""

    return _text(value, "—").replace("|", "\\|").replace("\n", " ").strip()


def _format_number(value: Any, digits: int = 4) -> str:
    number = _finite_number(value)
    if number is None:
        return "—"
    return f"{number:.{digits}f}".rstrip("0").rstrip(".")


def _format_price(value: Any) -> str:
    number = _finite_number(value)
    return "—" if number is None else f"${number:,.2f}"


def _format_date_range(dates: Iterable[Any]) -> str:
    normalized = sorted({_text(value) for value in dates if value is not None and _text(value)})
    if not normalized:
        return "—"
    if len(normalized) == 1:
        return normalized[0]
    return f"{normalized[0]} to {normalized[-1]}"


def _community_groups(mentions: Iterable[Mapping[str, Any]]) -> dict[str, list[Mapping[str, Any]]]:
    grouped: dict[str, list[Mapping[str, Any]]] = defaultdict(list)
    for mention in mentions:
        ticker = _text(mention.get("ticker")).strip().upper()
        if ticker:
            grouped[ticker].append(mention)
    return dict(grouped)


def select_community(mentions: Any, top_k: int) -> list[dict[str, Any]]:
    """Select unique tickers by their best rank across community feeds.

    The Stage 1 file contains one ranked list per source.  A ticker appearing
    in both lists is one community candidate, so its selection rank is the
    lowest source rank; source-specific ranks and counts remain in the output.
    """

    _positive_integer(top_k, "community top_k")
    if not isinstance(mentions, list):
        raise ValueError("stage1_screen community_interest must be a list")

    selected: list[dict[str, Any]] = []
    for ticker, ticker_mentions in _community_groups(mentions).items():
        valid_ranks = [
            int(rank)
            for mention in ticker_mentions
            if (rank := _finite_number(mention.get("rank"))) is not None
            and rank >= 1
            and rank.is_integer()
        ]
        if not valid_ranks:
            continue
        best_rank = min(valid_ranks)
        names = [_text(mention.get("name")).strip() for mention in ticker_mentions]
        selected.append(
            {
                "ticker": ticker,
                "rank": best_rank,
                "name": next((name for name in names if name), ""),
                "mentions": ticker_mentions,
            }
        )

    selected.sort(key=lambda item: (item["rank"], item["ticker"]))
    for index, item in enumerate(selected[:top_k], start=1):
        item["shortlist_rank"] = index
    return selected[:top_k]


def select_experts(expert_candidates: Any, top_k: int) -> list[dict[str, Any]]:
    """Select experts in explicit-rank order, or source JSON order if absent."""

    _positive_integer(top_k, "expert top_k")
    if not isinstance(expert_candidates, list):
        raise ValueError("stage1_experts candidates must be a list")

    ranked: list[tuple[int, int, Mapping[str, Any]]] = []
    for index, candidate in enumerate(expert_candidates):
        if not isinstance(candidate, Mapping):
            raise ValueError("each expert candidate must be a JSON object")
        explicit_rank = _finite_number(candidate.get("rank"))
        rank_key = (
            int(explicit_rank)
            if explicit_rank is not None and explicit_rank >= 1 and explicit_rank.is_integer()
            else index + 1
        )
        ranked.append((rank_key, index, candidate))

    ranked.sort(key=lambda item: (item[0], item[1]))
    selected: list[dict[str, Any]] = []
    for shortlist_rank, (_, _, candidate) in enumerate(ranked[:top_k], start=1):
        item = dict(candidate)
        item["shortlist_rank"] = shortlist_rank
        selected.append(item)
    return selected


def _category_sort_key(category: str) -> tuple[int, str]:
    try:
        return TECHNICAL_CATEGORY_ORDER.index(category), category
    except ValueError:
        return len(TECHNICAL_CATEGORY_ORDER), category


def calculate_rrf(candidates: Any, k: int = DEFAULT_RRF_K) -> list[dict[str, Any]]:
    """Calculate technical RRF rows from candidate category scores."""

    _positive_integer(k, "RRF k")
    if not isinstance(candidates, list):
        raise ValueError("stage1_screen candidates must be a list")

    by_ticker: dict[str, Mapping[str, Any]] = {}
    scores_by_category: dict[str, dict[str, float]] = defaultdict(dict)
    for candidate in candidates:
        if not isinstance(candidate, Mapping):
            raise ValueError("each stage1 candidate must be a JSON object")
        ticker = _text(candidate.get("ticker")).strip().upper()
        if not ticker:
            raise ValueError("each stage1 candidate must have a ticker")
        if ticker in by_ticker:
            raise ValueError(f"duplicate stage1 candidate ticker: {ticker}")
        by_ticker[ticker] = candidate

        scores = candidate.get("scores", {})
        if not isinstance(scores, Mapping):
            continue
        for raw_category, raw_score in scores.items():
            category = _text(raw_category).strip()
            if not category or category in COMMUNITY_CATEGORY_NAMES:
                continue
            score = _finite_number(raw_score)
            if score is not None:
                scores_by_category[category][ticker] = score

    ranks_by_category: dict[str, dict[str, int]] = {}
    for category, ticker_scores in scores_by_category.items():
        ordered = sorted(ticker_scores.items(), key=lambda item: (-item[1], item[0]))
        ranks_by_category[category] = {
            ticker: rank for rank, (ticker, _) in enumerate(ordered, start=1)
        }

    rrf_rows: list[dict[str, Any]] = []
    for ticker, candidate in by_ticker.items():
        contributions: list[dict[str, Any]] = []
        rrf_score = 0.0
        for category in sorted(ranks_by_category, key=_category_sort_key):
            rank = ranks_by_category[category].get(ticker)
            score = scores_by_category[category].get(ticker)
            if rank is None or score is None:
                continue
            contribution = 1.0 / (k + rank)
            rrf_score += contribution
            contributions.append(
                {
                    "category": category,
                    "rank": rank,
                    "score": score,
                    "rrf_contribution": contribution,
                }
            )
        if contributions:
            reasons_by_category = {
                category: reason
                for category, reason in zip(
                    candidate.get("categories", []), candidate.get("reasons", [])
                )
                if isinstance(category, str)
            }
            rrf_rows.append(
                {
                    "ticker": ticker,
                    "rrf_score": rrf_score,
                    "contributions": contributions,
                    "candidate": candidate,
                    "reasons": [
                        reasons_by_category[item["category"]]
                        for item in contributions
                        if item["category"] in reasons_by_category
                    ],
                }
            )

    rrf_rows.sort(key=lambda item: (-item["rrf_score"], item["ticker"]))
    for rank, row in enumerate(rrf_rows, start=1):
        row["rank"] = rank
    return rrf_rows


def _community_source_details(mentions: Iterable[Mapping[str, Any]]) -> str:
    details = []
    for mention in sorted(
        mentions,
        key=lambda item: (
            _text(item.get("source")),
            _finite_number(item.get("rank")) or math.inf,
        ),
    ):
        source = _text(mention.get("source"), "unknown")
        rank = _format_number(mention.get("rank"), 0)
        facts = [f"{source} #{rank}"]
        if mention.get("mentions") is not None:
            facts.append(f"{mention['mentions']} mentions")
        if mention.get("upvotes") is not None:
            facts.append(f"{mention['upvotes']} upvotes")
        details.append(" ".join(facts))
    return "; ".join(details) or "—"


def _expert_sources(candidate: Mapping[str, Any]) -> str:
    sources = sorted(
        {
            _text(event.get("source")).strip()
            for event in candidate.get("events", [])
            if isinstance(event, Mapping) and _text(event.get("source")).strip()
        }
    )
    return "; ".join(sources) or "—"


def _technical_reasons(row: Mapping[str, Any]) -> str:
    reasons = [_text(reason).strip() for reason in row.get("reasons", []) if _text(reason).strip()]
    return "; ".join(reasons) or "—"


def render_markdown(
    screen: Mapping[str, Any],
    experts: Mapping[str, Any],
    community: list[Mapping[str, Any]],
    expert_rows: list[Mapping[str, Any]],
    rrf_rows: list[Mapping[str, Any]],
    rrf_k: int,
    community_top_k: int,
    expert_top_k: int,
    rrf_top_k: int,
) -> str:
    """Render the three selections as fact-only Markdown."""

    selected_rrf = rrf_rows[:rrf_top_k]
    unique_tickers = {
        _text(item.get("ticker")).upper()
        for item in [*community, *expert_rows, *selected_rrf]
    }
    lines = [
        "# Stage 1 investigation shortlist",
        "",
        f"- Stage 1 as-of date: {_escape_cell(screen.get('as_of_date'))}",
        f"- Expert data generated at: {_escape_cell(experts.get('generated_at'))}",
        f"- Community selection: top {community_top_k} unique tickers by best rank across community sources",
        f"- Expert selection: top {expert_top_k} candidates in expert source rank order",
        f"- Technical selection: top {rrf_top_k} by RRF score, with k={rrf_k}",
        "- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based",
        f"- Unique tickers across sections: {len(unique_tickers)}",
        "",
        f"## Community attention — top {community_top_k}",
        "",
        "| Rank | Ticker | Name | Best source rank | Source details |",
        "|---:|:---|:---|---:|:---|",
    ]
    for item in community:
        lines.append(
            "| "
            + " | ".join(
                (
                    _escape_cell(item.get("shortlist_rank")),
                    _escape_cell(item.get("ticker")),
                    _escape_cell(item.get("name")),
                    _escape_cell(item.get("rank")),
                    _escape_cell(_community_source_details(item.get("mentions", []))),
                )
            )
            + " |"
        )

    lines.extend(
        [
            "",
            f"## Expert attention — top {expert_top_k}",
            "",
            "| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |",
            "|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|",
        ]
    )
    for item in expert_rows:
        events = [event for event in item.get("events", []) if isinstance(event, Mapping)]
        lines.append(
            "| "
            + " | ".join(
                (
                    _escape_cell(item.get("shortlist_rank")),
                    _escape_cell(item.get("ticker")),
                    _escape_cell(item.get("company")),
                    _escape_cell(item.get("direction")),
                    _escape_cell(item.get("strength")),
                    _escape_cell(_format_date_range(event.get("date") for event in events)),
                    _escape_cell(len(events)),
                    _escape_cell(item.get("distinct_firms")),
                    _escape_cell(_expert_sources(item)),
                    _escape_cell(item.get("summary")),
                    _escape_cell(item.get("reason")),
                )
            )
            + " |"
        )

    lines.extend(
        [
            "",
            f"## Technical RRF — top {rrf_top_k}",
            "",
            "| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |",
            "|---:|:---|---:|:---|:---|:---|---:|:---|",
        ]
    )
    for row in selected_rrf:
        candidate = row["candidate"]
        evidence = "; ".join(
            f"{item['category']} r{item['rank']} s={_format_number(item['score'])}"
            for item in row["contributions"]
        )
        lines.append(
            "| "
            + " | ".join(
                (
                    _escape_cell(row.get("rank")),
                    _escape_cell(row.get("ticker")),
                    _format_number(row.get("rrf_score"), 6),
                    _escape_cell(evidence),
                    _escape_cell(candidate.get("direction_hint")),
                    _escape_cell(candidate.get("risk_level")),
                    _escape_cell(_format_price((candidate.get("features") or {}).get("price"))),
                    _escape_cell(_technical_reasons(row)),
                )
            )
            + " |"
        )
    lines.append("")
    return "\n".join(lines)


def build_shortlist(
    screen: Mapping[str, Any],
    experts: Mapping[str, Any],
    *,
    community_top_k: int = 10,
    expert_top_k: int = 10,
    rrf_top_k: int = 20,
    rrf_k: int = DEFAULT_RRF_K,
) -> str:
    """Build Markdown from loaded Stage 1 and expert JSON objects."""

    _positive_integer(community_top_k, "community top_k")
    _positive_integer(expert_top_k, "expert top_k")
    _positive_integer(rrf_top_k, "RRF top_k")
    community_mentions = screen.get("community_attention")
    if community_mentions is None:
        community_mentions = screen.get("community_interest")
    community = select_community(community_mentions, community_top_k)
    expert_rows = select_experts(experts.get("candidates"), expert_top_k)
    rrf_rows = calculate_rrf(screen.get("candidates"), rrf_k)
    return render_markdown(
        screen,
        experts,
        community,
        expert_rows,
        rrf_rows,
        rrf_k,
        community_top_k,
        expert_top_k,
        rrf_top_k,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build the Stage 1 agent investigation shortlist")
    parser.add_argument("--screen", type=Path, default=DEFAULT_SCREEN_PATH)
    parser.add_argument("--experts", type=Path, default=DEFAULT_EXPERTS_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--community-top-k", type=int, default=10)
    parser.add_argument("--expert-top-k", type=int, default=10)
    parser.add_argument("--rrf-top-k", type=int, default=20)
    parser.add_argument("--rrf-k", type=int, default=DEFAULT_RRF_K)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        screen = _load_json(args.screen)
        experts = _load_json(args.experts)
        markdown = build_shortlist(
            screen,
            experts,
            community_top_k=args.community_top_k,
            expert_top_k=args.expert_top_k,
            rrf_top_k=args.rrf_top_k,
            rrf_k=args.rrf_k,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding="utf-8")
    except (OSError, ValueError) as error:
        print(f"shortlist: {error}", file=sys.stderr)
        return 2
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
