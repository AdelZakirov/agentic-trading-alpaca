from __future__ import annotations

import argparse
import json
import math
from collections.abc import Iterable, Mapping
from dataclasses import replace
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from .client import AlpacaAPIError, AlpacaClient
from .config import Settings
from .models import Bar, FetchError, Stage0Summary
from .store import MarketStore, utc_now


def chunks(values: list[str], size: int) -> Iterable[list[str]]:
    for offset in range(0, len(values), size):
        yield values[offset : offset + size]


def _as_float(raw: Any, field: str) -> float:
    value = float(raw)
    if not math.isfinite(value):
        raise ValueError(f"{field} is not finite")
    return value


def _as_int(raw: Any, field: str) -> int:
    value = int(raw)
    if value < 0:
        raise ValueError(f"{field} must be non-negative")
    return value


def _is_eligible_asset(asset: Mapping[str, Any]) -> bool:
    return (
        asset.get("status") == "active"
        and asset.get("tradable") is True
        and asset.get("class", asset.get("asset_class")) == "us_equity"
        and bool(str(asset.get("symbol", "")).strip())
    )


def parse_bar(raw: Mapping[str, Any]) -> Bar:
    symbol = str(raw["symbol"]).upper()
    timestamp = str(raw.get("t", ""))
    normalized_timestamp = timestamp.replace("Z", "+00:00")
    if not normalized_timestamp:
        raise ValueError("bar has no timestamp")
    bar_datetime = datetime.fromisoformat(normalized_timestamp)
    bar_date = bar_datetime.date()
    open_price = _as_float(raw["o"], "open")
    high_price = _as_float(raw["h"], "high")
    low_price = _as_float(raw["l"], "low")
    close_price = _as_float(raw["c"], "close")
    volume = _as_int(raw["v"], "volume")
    if close_price <= 0:
        raise ValueError("close must be positive")
    if high_price < low_price:
        raise ValueError("high must be >= low")
    if not low_price <= open_price <= high_price:
        raise ValueError("open must be between low and high")
    if not low_price <= close_price <= high_price:
        raise ValueError("close must be between low and high")
    return Bar(symbol, bar_date, open_price, high_price, low_price, close_price, volume)


def _latest_completed_market_date() -> date:
    """Return the most recent weekday in New York.

    This avoids using an in-progress daily candle and avoids needless weekend
    refreshes when the cache already contains Friday's completed bar.
    """

    market_date = datetime.now(ZoneInfo("America/New_York")).date()
    completed = market_date - timedelta(days=1)
    while completed.weekday() >= 5:
        completed -= timedelta(days=1)
    return completed


class Stage0Fetcher:
    def __init__(
        self,
        settings: Settings,
        client: AlpacaClient,
        store: MarketStore,
        max_symbols: int | None = None,
    ) -> None:
        self.settings = settings
        self.client = client
        self.store = store
        if max_symbols is not None and max_symbols < 1:
            raise ValueError("max_symbols must be >= 1")
        self.max_symbols = max_symbols

    def run(self) -> Stage0Summary:
        error_id_at_start = self.store.latest_error_id()
        self.store.set_metadata(
            {
                "feed": self.settings.feed,
                "last_run_started_at": utc_now().isoformat(),
            }
        )

        assets = self._load_assets()
        symbols = sorted(asset["symbol"].upper() for asset in assets)
        if self.max_symbols is not None:
            symbols = symbols[: self.max_symbols]
        snapshots_loaded = self._fetch_snapshots(symbols)
        self._fetch_history(symbols)

        errors = self.store.errors_since(error_id_at_start)
        summary = Stage0Summary(
            feed=self.settings.feed,
            symbols_requested=len(symbols),
            symbols_loaded=len(snapshots_loaded),
            history_days_target=self.settings.history_days,
            history_symbols_loaded=sum(
                1
                for symbol in symbols
                if self.store.count_bars(symbol) >= self.settings.history_days
            ),
            errors=errors,
        )
        self.store.set_metadata({"last_run_finished_at": utc_now().isoformat()})
        return summary

    def _load_assets(self) -> list[dict[str, Any]]:
        try:
            raw_assets = self.client.list_assets()
        except AlpacaAPIError as error:
            self.store.record_error("assets", str(error))
            raise

        filtered = []
        for asset in raw_assets:
            if not isinstance(asset, Mapping):
                self.store.record_error("assets", "invalid asset payload")
                continue
            if _is_eligible_asset(asset):
                filtered.append(asset)
        self.store.upsert_assets(filtered)
        return filtered

    def _fetch_snapshots(self, symbols: list[str]) -> set[str]:
        fetched_at = utc_now()
        loaded: set[str] = set()
        for batch_number, batch in enumerate(chunks(symbols, self.settings.batch_size), start=1):
            try:
                response = self.client.fetch_snapshots(batch)
                valid_snapshots = {}
                for symbol, raw in response.items():
                    if isinstance(raw, Mapping):
                        valid_snapshots[symbol] = raw
                    else:
                        self.store.record_error(
                            "snapshots", "invalid snapshot payload", str(symbol).upper()
                        )
                self.store.upsert_snapshots(valid_snapshots, fetched_at)
                batch_symbols = set(batch)
                returned_symbols = {symbol.upper() for symbol in valid_snapshots}
                loaded.update(returned_symbols & batch_symbols)
                for symbol in sorted(batch_symbols - returned_symbols):
                    self.store.record_error(
                        "snapshots",
                        f"symbol missing from snapshot response (batch {batch_number})",
                        symbol,
                    )
            except AlpacaAPIError as error:
                self.store.record_error(
                    "snapshots", f"batch {batch_number} failed: {error}"
                )
        return loaded

    def _fetch_history(self, symbols: list[str]) -> None:
        completed_through = _latest_completed_market_date()
        bootstrap_start = completed_through - timedelta(
            days=max(180, int(self.settings.history_days * 1.8))
        )

        for batch_number, batch in enumerate(chunks(symbols, self.settings.batch_size), start=1):
            last_dates = [self.store.last_bar_date(symbol) for symbol in batch]
            if all(
                last_date is not None and last_date >= completed_through
                for last_date in last_dates
            ):
                continue
            start = self._history_start(last_dates, bootstrap_start)
            bars: list[Bar] = []
            returned_symbols: set[str] = set()
            try:
                for raw_bar in self.client.iter_daily_bars(batch, start, completed_through):
                    symbol = str(raw_bar.get("symbol", "")).upper()
                    try:
                        bar = parse_bar(raw_bar)
                    except (KeyError, TypeError, ValueError) as error:
                        self.store.record_error("history", f"invalid bar: {error}", symbol or None)
                        continue
                    bars.append(bar)
                    returned_symbols.add(symbol)
                self.store.upsert_bars(bars)
                for symbol in sorted(set(batch) - returned_symbols):
                    self.store.record_error(
                        "history",
                        f"symbol missing from historical bars response (batch {batch_number})",
                        symbol,
                    )
            except AlpacaAPIError as error:
                self.store.record_error("history", f"batch {batch_number} failed: {error}")

    def _history_start(
        self, last_dates: list[date | None], bootstrap_start: date
    ) -> date:
        if any(last_date is None for last_date in last_dates):
            return bootstrap_start
        return min(
            last_date + timedelta(days=1)
            for last_date in last_dates
            if last_date is not None
        )


def write_manifest(path: Path, summary: Stage0Summary, db_path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = summary.to_dict()
    payload.update(
        {
            "db_path": str(db_path),
            "assets_table": "assets",
            "snapshots_table": "snapshots",
            "history_table": "bars",
        }
    )
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Fetch Alpaca whole-market Stage 0 data")
    parser.add_argument("--db-path", type=Path, help="Override the SQLite cache path")
    parser.add_argument("--manifest-path", type=Path, help="Override the JSON manifest path")
    parser.add_argument(
        "--max-symbols",
        type=int,
        help="Limit the run to the first N sorted active/tradable US equities",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Write the manifest without printing the full JSON summary",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    settings = Settings.from_env()
    settings = replace(
        settings,
        db_path=args.db_path or settings.db_path,
        manifest_path=args.manifest_path or settings.manifest_path,
    )

    with MarketStore(settings.db_path) as store:
        summary = Stage0Fetcher(
            settings,
            AlpacaClient(settings),
            store,
            max_symbols=args.max_symbols,
        ).run()
    write_manifest(settings.manifest_path, summary, settings.db_path)
    if not args.quiet:
        print(json.dumps(summary.to_dict(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
