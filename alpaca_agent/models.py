from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Iterable, Mapping


@dataclass(frozen=True, slots=True)
class Asset:
    symbol: str
    exchange: str | None
    status: str
    asset_class: str
    tradable: bool
    shortable: bool
    fractionable: bool
    is_etf: bool = False


@dataclass(frozen=True, slots=True)
class Bar:
    symbol: str
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int


@dataclass(frozen=True, slots=True)
class Snapshot:
    symbol: str
    fetched_at: datetime
    latest_trade_price: float | None
    latest_trade_timestamp: datetime | None
    latest_quote_bid_price: float | None
    latest_quote_ask_price: float | None
    minute_open: float | None
    minute_high: float | None
    minute_low: float | None
    minute_close: float | None
    minute_volume: int | None
    daily_open: float | None
    daily_high: float | None
    daily_low: float | None
    daily_close: float | None
    daily_volume: int | None
    previous_daily_close: float | None


@dataclass(frozen=True, slots=True)
class FetchError:
    occurred_at: datetime
    stage: str
    symbol: str | None
    message: str


@dataclass(frozen=True, slots=True)
class Stage0Summary:
    feed: str
    symbols_requested: int
    symbols_loaded: int
    history_days_target: int
    history_symbols_loaded: int
    errors: tuple[FetchError, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "feed": self.feed,
            "symbols_requested": self.symbols_requested,
            "symbols_loaded": self.symbols_loaded,
            "history_days_target": self.history_days_target,
            "history_symbols_loaded": self.history_symbols_loaded,
            "errors": [
                {
                    "occurred_at": error.occurred_at.isoformat(),
                    "stage": error.stage,
                    "symbol": error.symbol,
                    "message": error.message,
                }
                for error in self.errors
            ],
        }


class MarketDataset:
    """Read-only local representation consumed by screening code.

    The data is loaded from ``MarketStore`` and exposed as the conceptual
    ``assets``, ``snapshots`` and ``history`` mappings described by Stage 0.
    Stage 1 can depend on this class without knowing anything about Alpaca.
    """

    def __init__(
        self,
        assets: Mapping[str, Asset],
        snapshots: Mapping[str, Snapshot],
        history: Mapping[str, Iterable[Bar]],
    ) -> None:
        self.assets = dict(assets)
        self.snapshots = dict(snapshots)
        self.history = {symbol: tuple(bars) for symbol, bars in history.items()}
