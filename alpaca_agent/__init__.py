"""Local market data primitives for the Alpaca trading agent."""

from .models import Asset, Bar, MarketDataset, Snapshot
from .store import MarketStore

__all__ = [
    "Asset",
    "Bar",
    "Candidate",
    "DEFAULT_SCREENING_CONFIG",
    "MarketDataset",
    "MarketStore",
    "ScreenResult",
    "ScreeningConfig",
    "Snapshot",
    "Stage1Screener",
    "TickerFeatures",
    "screen",
]


def __getattr__(name: str):
    if name in {
        "Candidate",
        "DEFAULT_SCREENING_CONFIG",
        "ScreenResult",
        "ScreeningConfig",
        "Stage1Screener",
        "TickerFeatures",
        "screen",
    }:
        from . import stage1

        return getattr(stage1, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
