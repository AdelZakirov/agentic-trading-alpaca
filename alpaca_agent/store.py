from __future__ import annotations

import json
import sqlite3
from collections.abc import Iterable, Iterator, Mapping
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from .models import Asset, Bar, FetchError, MarketDataset, Snapshot


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def _float_or_none(value: Any) -> float | None:
    return None if value is None else float(value)


def _int_or_none(value: Any) -> int | None:
    return None if value is None else int(value)


def _mapping_or_empty(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _raw_asset_is_etf(raw_json: str) -> bool:
    """Read ETF hints from the raw asset payload when Alpaca provides one."""

    try:
        raw = json.loads(raw_json)
    except (TypeError, ValueError):
        return False
    if not isinstance(raw, Mapping):
        return False
    if raw.get("is_etf") is True:
        return True
    if str(raw.get("type", raw.get("asset_type", ""))).upper() == "ETF":
        return True
    attributes = raw.get("attributes")
    return isinstance(attributes, list) and any(str(item).lower() == "etf" for item in attributes)


class MarketStore:
    """SQLite persistence and the API-independent Stage 1 read interface."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA journal_mode=WAL")
        self.connection.execute("PRAGMA foreign_keys=ON")
        self._create_schema()

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> "MarketStore":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def _create_schema(self) -> None:
        self.connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS assets (
                symbol TEXT PRIMARY KEY,
                exchange TEXT,
                status TEXT NOT NULL,
                asset_class TEXT NOT NULL,
                tradable INTEGER NOT NULL,
                shortable INTEGER NOT NULL,
                fractionable INTEGER NOT NULL,
                raw_json TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS snapshots (
                symbol TEXT PRIMARY KEY,
                fetched_at TEXT NOT NULL,
                latest_trade_price REAL,
                latest_trade_timestamp TEXT,
                latest_quote_bid_price REAL,
                latest_quote_ask_price REAL,
                minute_open REAL,
                minute_high REAL,
                minute_low REAL,
                minute_close REAL,
                minute_volume INTEGER,
                daily_open REAL,
                daily_high REAL,
                daily_low REAL,
                daily_close REAL,
                daily_volume INTEGER,
                previous_daily_close REAL,
                raw_json TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS bars (
                symbol TEXT NOT NULL,
                bar_date TEXT NOT NULL,
                open REAL NOT NULL,
                high REAL NOT NULL,
                low REAL NOT NULL,
                close REAL NOT NULL,
                volume INTEGER NOT NULL,
                PRIMARY KEY (symbol, bar_date)
            );

            CREATE TABLE IF NOT EXISTS fetch_errors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                occurred_at TEXT NOT NULL,
                stage TEXT NOT NULL,
                symbol TEXT,
                message TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS metadata (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );
            """
        )
        self.connection.commit()

    def set_metadata(self, values: Mapping[str, str]) -> None:
        self.connection.executemany(
            "INSERT INTO metadata(key, value) VALUES (?, ?) "
            "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
            values.items(),
        )
        self.connection.commit()

    def upsert_assets(self, assets: Iterable[Mapping[str, Any]]) -> int:
        rows = []
        for asset in assets:
            symbol = str(asset.get("symbol", "")).strip().upper()
            if not symbol:
                continue
            rows.append(
                (
                    symbol,
                    asset.get("exchange"),
                    str(asset.get("status", "")),
                    str(asset.get("class", asset.get("asset_class", ""))),
                    int(bool(asset.get("tradable"))),
                    int(bool(asset.get("shortable"))),
                    int(bool(asset.get("fractionable"))),
                    json.dumps(asset, separators=(",", ":"), sort_keys=True),
                    utc_now().isoformat(),
                )
            )
        self.connection.executemany(
            """
            INSERT INTO assets(
                symbol, exchange, status, asset_class, tradable, shortable,
                fractionable, raw_json, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(symbol) DO UPDATE SET
                exchange=excluded.exchange,
                status=excluded.status,
                asset_class=excluded.asset_class,
                tradable=excluded.tradable,
                shortable=excluded.shortable,
                fractionable=excluded.fractionable,
                raw_json=excluded.raw_json,
                updated_at=excluded.updated_at
            """,
            rows,
        )
        self.connection.commit()
        return len(rows)

    def upsert_snapshots(self, snapshots: Mapping[str, Mapping[str, Any]], fetched_at: datetime) -> int:
        rows = []
        for symbol, raw in snapshots.items():
            latest_trade = _mapping_or_empty(raw.get("latestTrade"))
            latest_quote = _mapping_or_empty(raw.get("latestQuote"))
            minute_bar = _mapping_or_empty(raw.get("minuteBar"))
            daily_bar = _mapping_or_empty(raw.get("dailyBar"))
            previous_daily_bar = _mapping_or_empty(raw.get("prevDailyBar"))
            rows.append(
                (
                    symbol.upper(),
                    fetched_at.isoformat(),
                    _float_or_none(latest_trade.get("p")),
                    latest_trade.get("t"),
                    _float_or_none(latest_quote.get("bp")),
                    _float_or_none(latest_quote.get("ap")),
                    _float_or_none(minute_bar.get("o")),
                    _float_or_none(minute_bar.get("h")),
                    _float_or_none(minute_bar.get("l")),
                    _float_or_none(minute_bar.get("c")),
                    _int_or_none(minute_bar.get("v")),
                    _float_or_none(daily_bar.get("o")),
                    _float_or_none(daily_bar.get("h")),
                    _float_or_none(daily_bar.get("l")),
                    _float_or_none(daily_bar.get("c")),
                    _int_or_none(daily_bar.get("v")),
                    _float_or_none(previous_daily_bar.get("c")),
                    json.dumps(raw, separators=(",", ":"), sort_keys=True),
                )
            )
        self.connection.executemany(
            """
            INSERT INTO snapshots(
                symbol, fetched_at, latest_trade_price, latest_trade_timestamp,
                latest_quote_bid_price, latest_quote_ask_price, minute_open,
                minute_high, minute_low, minute_close, minute_volume, daily_open,
                daily_high, daily_low, daily_close, daily_volume,
                previous_daily_close, raw_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(symbol) DO UPDATE SET
                fetched_at=excluded.fetched_at,
                latest_trade_price=excluded.latest_trade_price,
                latest_trade_timestamp=excluded.latest_trade_timestamp,
                latest_quote_bid_price=excluded.latest_quote_bid_price,
                latest_quote_ask_price=excluded.latest_quote_ask_price,
                minute_open=excluded.minute_open,
                minute_high=excluded.minute_high,
                minute_low=excluded.minute_low,
                minute_close=excluded.minute_close,
                minute_volume=excluded.minute_volume,
                daily_open=excluded.daily_open,
                daily_high=excluded.daily_high,
                daily_low=excluded.daily_low,
                daily_close=excluded.daily_close,
                daily_volume=excluded.daily_volume,
                previous_daily_close=excluded.previous_daily_close,
                raw_json=excluded.raw_json
            """,
            rows,
        )
        self.connection.commit()
        return len(rows)

    def upsert_bars(self, bars: Iterable[Bar]) -> int:
        rows = [
            (bar.symbol, bar.date.isoformat(), bar.open, bar.high, bar.low, bar.close, bar.volume)
            for bar in bars
        ]
        self.connection.executemany(
            """
            INSERT INTO bars(symbol, bar_date, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(symbol, bar_date) DO UPDATE SET
                open=excluded.open,
                high=excluded.high,
                low=excluded.low,
                close=excluded.close,
                volume=excluded.volume
            """,
            rows,
        )
        self.connection.commit()
        return len(rows)

    def record_error(self, stage: str, message: str, symbol: str | None = None) -> None:
        self.connection.execute(
            "INSERT INTO fetch_errors(occurred_at, stage, symbol, message) VALUES (?, ?, ?, ?)",
            (utc_now().isoformat(), stage, symbol, message),
        )
        self.connection.commit()

    def record_errors(self, errors: Iterable[FetchError]) -> None:
        self.connection.executemany(
            "INSERT INTO fetch_errors(occurred_at, stage, symbol, message) VALUES (?, ?, ?, ?)",
            [(e.occurred_at.isoformat(), e.stage, e.symbol, e.message) for e in errors],
        )
        self.connection.commit()

    def last_bar_date(self, symbol: str) -> date | None:
        row = self.connection.execute(
            "SELECT MAX(bar_date) AS latest FROM bars WHERE symbol = ?", (symbol,)
        ).fetchone()
        return None if row is None or row["latest"] is None else date.fromisoformat(row["latest"])

    def count_bars(self, symbol: str) -> int:
        row = self.connection.execute(
            "SELECT COUNT(*) AS count FROM bars WHERE symbol = ?", (symbol,)
        ).fetchone()
        return int(row["count"])

    def errors(self) -> tuple[FetchError, ...]:
        rows = self.connection.execute(
            "SELECT occurred_at, stage, symbol, message FROM fetch_errors ORDER BY id"
        ).fetchall()
        return self._errors_from_rows(rows)

    def latest_error_id(self) -> int:
        row = self.connection.execute("SELECT COALESCE(MAX(id), 0) AS latest FROM fetch_errors").fetchone()
        return int(row["latest"])

    def errors_since(self, error_id: int) -> tuple[FetchError, ...]:
        rows = self.connection.execute(
            "SELECT occurred_at, stage, symbol, message FROM fetch_errors WHERE id > ? ORDER BY id",
            (error_id,),
        ).fetchall()
        return self._errors_from_rows(rows)

    @staticmethod
    def _errors_from_rows(rows: Iterable[sqlite3.Row]) -> tuple[FetchError, ...]:
        return tuple(
            FetchError(
                occurred_at=_parse_datetime(row["occurred_at"]) or utc_now(),
                stage=row["stage"],
                symbol=row["symbol"],
                message=row["message"],
            )
            for row in rows
        )

    def load_dataset(self) -> MarketDataset:
        assets = {
            row["symbol"]: Asset(
                symbol=row["symbol"],
                exchange=row["exchange"],
                status=row["status"],
                asset_class=row["asset_class"],
                tradable=bool(row["tradable"]),
                shortable=bool(row["shortable"]),
                fractionable=bool(row["fractionable"]),
                is_etf=_raw_asset_is_etf(row["raw_json"]),
            )
            for row in self.connection.execute("SELECT * FROM assets ORDER BY symbol")
        }
        snapshots = {
            row["symbol"]: Snapshot(
                symbol=row["symbol"],
                fetched_at=_parse_datetime(row["fetched_at"]) or utc_now(),
                latest_trade_price=row["latest_trade_price"],
                latest_trade_timestamp=_parse_datetime(row["latest_trade_timestamp"]),
                latest_quote_bid_price=row["latest_quote_bid_price"],
                latest_quote_ask_price=row["latest_quote_ask_price"],
                minute_open=row["minute_open"],
                minute_high=row["minute_high"],
                minute_low=row["minute_low"],
                minute_close=row["minute_close"],
                minute_volume=row["minute_volume"],
                daily_open=row["daily_open"],
                daily_high=row["daily_high"],
                daily_low=row["daily_low"],
                daily_close=row["daily_close"],
                daily_volume=row["daily_volume"],
                previous_daily_close=row["previous_daily_close"],
            )
            for row in self.connection.execute("SELECT * FROM snapshots ORDER BY symbol")
        }
        history: dict[str, list[Bar]] = {}
        rows = self.connection.execute(
            "SELECT symbol, bar_date, open, high, low, close, volume "
            "FROM bars ORDER BY symbol, bar_date"
        )
        for row in rows:
            history.setdefault(row["symbol"], []).append(
                Bar(
                    symbol=row["symbol"],
                    date=date.fromisoformat(row["bar_date"]),
                    open=row["open"],
                    high=row["high"],
                    low=row["low"],
                    close=row["close"],
                    volume=row["volume"],
                )
            )
        return MarketDataset(assets, snapshots, history)

    def symbol_counts(self) -> dict[str, int]:
        rows = self.connection.execute(
            "SELECT symbol, COUNT(*) AS count FROM bars GROUP BY symbol"
        ).fetchall()
        return {row["symbol"]: int(row["count"]) for row in rows}
