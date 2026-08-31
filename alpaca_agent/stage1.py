"""Deterministic Stage 1 market screening.

Stage 1 only turns completed daily OHLCV bars into explainable candidate
signals.  It deliberately has no strategy, options, news, fundamentals, or
LLM dependencies.
"""

from __future__ import annotations

import argparse
import json
import logging
import math
import random
import sys
import time
from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import asdict, dataclass, replace
from datetime import date, timedelta
from pathlib import Path
from statistics import mean, median, pstdev
from typing import Any

from .community import (
    ApeWisdomClient,
    ApeWisdomError,
    CommunityMention,
)
from .models import Asset, Bar, MarketDataset
from .store import MarketStore

LOGGER = logging.getLogger(__name__)

LANE_LABELS = (
    ("volume_anomaly", "Volume anomaly"),
    ("momentum_breakout", "Momentum/breakout"),
    ("stretched_reversal", "Stretched/reversal"),
    ("volatility_expansion", "Vol expansion"),
    ("compression_breakout", "Compression breakout"),
    ("wildcard", "Wildcard"),
    ("community_interest", "Community interest"),
    ("exploration", "Exploration"),
)
LANE_NAMES = tuple(name for name, _ in LANE_LABELS)


@dataclass(frozen=True, slots=True)
class EligibilityConfig:
    min_price: float
    min_median_dollar_volume_20: float


@dataclass(frozen=True, slots=True)
class CommunityConfig:
    base_url: str = "https://apewisdom.io/api/v1.0"
    sources: tuple[str, ...] = ("all-stocks", "options")
    top_k: int = 50
    timeout_seconds: float = 10.0


@dataclass(frozen=True, slots=True)
class LaneConfig:
    volume_min_relative_volume: float = 1.5
    volume_top_k: int = 30
    momentum_percentile: float = 0.85
    momentum_top_k: int = 30
    stretched_min_normalized_move: float = 1.5
    stretched_min_stretch_atr: float = 1.5
    stretched_top_k: int = 30
    volatility_min_ratio: float = 1.5
    volatility_min_percentile: float = 0.90
    volatility_top_k: int = 25
    compression_max_percentile: float = 0.20
    compression_min_relative_volume: float = 1.5
    compression_top_k: int = 20
    wildcard_multi_feature_percentile: float = 0.90
    wildcard_single_extreme_percentile: float = 0.995
    wildcard_extreme_floor: float = 0.80
    wildcard_top_k: int = 15
    exploration_top_k: int = 10


@dataclass(frozen=True, slots=True)
class ScreeningConfig:
    """All Stage 1 thresholds and limits in one immutable configuration."""

    normal: EligibilityConfig = EligibilityConfig(5.0, 2_000_000.0)
    wildcard: EligibilityConfig = EligibilityConfig(2.0, 500_000.0)
    min_history_days: int = 80
    include_etfs: bool = True
    feed: str = "iex"
    community: CommunityConfig = CommunityConfig()
    lane: LaneConfig = LaneConfig()

    def __post_init__(self) -> None:
        if self.min_history_days < 1:
            raise ValueError("min_history_days must be positive")
        for value in (
            self.normal.min_price,
            self.normal.min_median_dollar_volume_20,
            self.wildcard.min_price,
            self.wildcard.min_median_dollar_volume_20,
        ):
            if value < 0:
                raise ValueError("eligibility thresholds must be non-negative")


DEFAULT_SCREENING_CONFIG = ScreeningConfig()


@dataclass(frozen=True, slots=True)
class TickerFeatures:
    ticker: str
    as_of_date: date
    price: float
    return_1d: float
    return_5d: float
    return_20d: float
    dollar_volume_t: float
    median_dollar_volume_20: float
    relative_volume_20: float | None
    atr14: float | None
    atr14_pct: float | None
    normalized_move_1d: float | None
    rv5: float
    rv20: float
    vol_expansion: float | None
    sma20: float
    distance_sma20: float
    stretch_atr: float | None
    previous_20d_high: float
    previous_20d_low: float
    bull_breakout_strength: float | None
    bear_breakout_strength: float | None
    breakout_strength: float | None
    breakout_direction: str
    bb_width_percentile_60: float | None
    pct_relative_volume: float | None = None
    pct_abs_return_5d: float | None = None
    pct_normalized_move: float | None = None
    pct_vol_expansion: float | None = None
    pct_stretch_atr: float | None = None
    pct_breakout_strength: float | None = None
    wildcard_p_volume: float | None = None
    wildcard_p_move: float | None = None
    wildcard_p_vol_expansion: float | None = None
    wildcard_p_stretch: float | None = None

    def to_dict(self) -> dict[str, Any]:
        values = asdict(self)
        values.pop("ticker")
        values.pop("as_of_date")
        return values


@dataclass(frozen=True, slots=True)
class CandidateSignal:
    ticker: str
    category: str
    score: float | None
    direction_hint: str
    risk_level: str
    reason: str
    community: tuple[CommunityMention, ...] = ()


@dataclass(frozen=True, slots=True)
class Candidate:
    ticker: str
    categories: tuple[str, ...]
    primary_category: str
    category_count: int
    direction_hint: str
    risk_level: str
    scores: dict[str, float]
    features: TickerFeatures | None
    reasons: tuple[str, ...]
    community: tuple[CommunityMention, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "ticker": self.ticker,
            "categories": list(self.categories),
            "primary_category": self.primary_category,
            "category_count": self.category_count,
            "direction_hint": self.direction_hint,
            "risk_level": self.risk_level,
            "scores": self.scores,
            "features": self.features.to_dict() if self.features else None,
            "reasons": list(self.reasons),
        }
        if self.community:
            result["community_interest"] = [item.to_dict() for item in self.community]
        return result


@dataclass(frozen=True, slots=True)
class ScreenResult:
    as_of_date: date
    feed: str
    universe_size: int
    normal_eligible: int
    wildcard_eligible: int
    candidates: tuple[Candidate, ...]
    lane_counts: dict[str, int]
    exclusions: dict[str, int]
    runtime_seconds: float
    community_interest: tuple[CommunityMention, ...] = ()

    @property
    def candidate_count(self) -> int:
        return len(self.candidates)

    @property
    def multi_category_counts(self) -> dict[str, int]:
        return {
            "2_plus": sum(candidate.category_count >= 2 for candidate in self.candidates),
            "3_plus": sum(candidate.category_count >= 3 for candidate in self.candidates),
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "as_of_date": self.as_of_date.isoformat(),
            "feed": self.feed,
            "universe_size": self.universe_size,
            "normal_eligible": self.normal_eligible,
            "wildcard_eligible": self.wildcard_eligible,
            "candidate_count": self.candidate_count,
            "candidates": [candidate.to_dict() for candidate in self.candidates],
            "lane_counts": self.lane_counts,
            "exclusions": self.exclusions,
            "multi_category": self.multi_category_counts,
            "community_interest": [item.to_dict() for item in self.community_interest],
        }

    def summary_text(self) -> str:
        lines = [
            f"Stage-1 Screen — {self.as_of_date.isoformat()}",
            "",
            f"Universe:                 {self.universe_size:>6}",
            f"Normal eligible:          {self.normal_eligible:>6}",
            f"Wildcard eligible:        {self.wildcard_eligible:>6}",
            f"Unique candidates:        {self.candidate_count:>6}",
            "",
        ]
        lines.extend(
            f"{label + ':':<27}{self.lane_counts.get(key, 0):>6}"
            for key, label in LANE_LABELS
        )
        lines.extend(
            (
                "",
                f"Multi-category (2+):      {self.multi_category_counts['2_plus']:>6}",
                f"Multi-category (3+):      {self.multi_category_counts['3_plus']:>6}",
            )
        )
        return "\n".join(lines)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, allow_nan=False) + "\n"


def _finite(value: float | int) -> bool:
    return math.isfinite(float(value))


def _parse_as_of_date(value: date | str) -> date:
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)


def _safe_ratio(numerator: float, denominator: float, cap: float = 1_000_000.0) -> float | None:
    if not _finite(numerator) or not _finite(denominator) or denominator < 0:
        return None
    if denominator <= 1e-12:
        return 0.0 if numerator <= 1e-12 else cap
    return numerator / denominator


def _true_ranges(bars: Sequence[Bar]) -> list[float]:
    return [
        max(
            bar.high - bar.low,
            abs(bar.high - bars[index - 1].close),
            abs(bar.low - bars[index - 1].close),
        )
        for index, bar in enumerate(bars[1:], 1)
    ]


def average_true_range(bars: Sequence[Bar], window: int = 14) -> float | None:
    """Return ATR using the sessions before the last bar in ``bars``."""

    if len(bars) < window + 2:
        return None
    return mean(_true_ranges(bars)[-window - 1 : -1])


def relative_volume_20(volumes: Sequence[int | float]) -> float | None:
    """Compare the last volume with the previous 20 volumes."""

    if len(volumes) < 21:
        return None
    baseline = median(float(value) for value in volumes[-21:-1])
    return _safe_ratio(float(volumes[-1]), baseline)


def realized_volatility(bars: Sequence[Bar], window: int) -> float | None:
    """Return population standard deviation of the last ``window`` log returns."""

    if len(bars) < window + 1:
        return None
    return pstdev(
        math.log(bars[index].close / bars[index - 1].close)
        for index in range(len(bars) - window, len(bars))
    )


def bollinger_width(closes: Sequence[float], window: int = 20) -> float | None:
    if len(closes) < window:
        return None
    values = closes[-window:]
    average = mean(values)
    if average <= 0:
        return None
    return 4.0 * pstdev(values) / average


def percentile_rank(value: float | None, values: Iterable[float | None]) -> float | None:
    """Return an empirical percentile in [0, 1], with ties ranked inclusively."""

    if value is None or not _finite(value):
        return None
    valid = [float(item) for item in values if item is not None and _finite(item)]
    return sum(item <= value for item in valid) / len(valid) if valid else None


def _pre_breakout_bb_percentile(bars: Sequence[Bar], current_index: int) -> float | None:
    """Rank the width at t-1 against the 60 widths preceding it."""

    closes = [bar.close for bar in bars]
    widths = [
        bollinger_width(closes[: index + 1], 20) if index >= 19 else None
        for index in range(len(bars))
    ]
    pre_breakout_index = current_index - 1
    if pre_breakout_index < 0 or widths[pre_breakout_index] is None:
        return None
    baseline = [
        value
        for value in widths[max(19, pre_breakout_index - 60) : pre_breakout_index]
        if value is not None
    ]
    return percentile_rank(widths[pre_breakout_index], baseline)


def calculate_features(
    bars: Sequence[Bar],
    as_of_date: date | str | None = None,
) -> TickerFeatures | None:
    """Calculate all Stage 1 features for the last completed bar.

    Every rolling baseline excludes the current bar.  If ``as_of_date`` is
    supplied, bars after it are ignored, which makes the function suitable for
    historical screening.
    """

    if not bars:
        return None
    screen_date = None if as_of_date is None else _parse_as_of_date(as_of_date)
    selected = sorted(
        (bar for bar in bars if screen_date is None or bar.date <= screen_date),
        key=lambda bar: bar.date,
    )
    if len(selected) < 21:
        return None
    current_index = len(selected) - 1
    current = selected[current_index]
    previous = selected[current_index - 1]
    previous_20 = selected[current_index - 20 : current_index]
    return_1d = current.close / previous.close - 1.0
    return_5d = current.close / selected[current_index - 5].close - 1.0
    return_20d = current.close / selected[current_index - 20].close - 1.0
    median_dollar_volume = median(bar.close * bar.volume for bar in previous_20)
    relative_volume = relative_volume_20([bar.volume for bar in selected])

    atr = average_true_range(selected)
    atr_pct = _safe_ratio(atr, current.close) if atr is not None else None
    normalized_move = (
        _safe_ratio(abs(current.close - previous.close), atr) if atr is not None else None
    )

    rv5 = realized_volatility(selected, 5) or 0.0
    rv20 = realized_volatility(selected, 20) or 0.0
    vol_expansion = _safe_ratio(rv5, rv20)

    sma20 = mean(bar.close for bar in previous_20)
    distance_sma20 = (current.close - sma20) / current.close
    stretch_atr = (
        _safe_ratio(abs(current.close - sma20), atr) if atr is not None else None
    )
    previous_high = max(bar.high for bar in previous_20)
    previous_low = min(bar.low for bar in previous_20)
    bull_breakout = (
        _safe_ratio(current.close - previous_high, atr) if atr is not None else None
    )
    bear_breakout = (
        _safe_ratio(previous_low - current.close, atr) if atr is not None else None
    )
    breakout_strength = max(
        (value for value in (bull_breakout, bear_breakout) if value is not None and value > 0),
        default=0.0,
    )
    if bull_breakout is not None and bull_breakout > 0 and bull_breakout >= (bear_breakout or 0.0):
        breakout_direction = "bullish"
    elif bear_breakout is not None and bear_breakout > 0:
        breakout_direction = "bearish"
    else:
        breakout_direction = "none"

    return TickerFeatures(
        ticker=current.symbol,
        as_of_date=screen_date or current.date,
        price=current.close,
        return_1d=return_1d,
        return_5d=return_5d,
        return_20d=return_20d,
        dollar_volume_t=current.close * current.volume,
        median_dollar_volume_20=median_dollar_volume,
        relative_volume_20=relative_volume,
        atr14=atr,
        atr14_pct=atr_pct,
        normalized_move_1d=normalized_move,
        rv5=rv5,
        rv20=rv20,
        vol_expansion=vol_expansion,
        sma20=sma20,
        distance_sma20=distance_sma20,
        stretch_atr=stretch_atr,
        previous_20d_high=previous_high,
        previous_20d_low=previous_low,
        bull_breakout_strength=bull_breakout,
        bear_breakout_strength=bear_breakout,
        breakout_strength=breakout_strength,
        breakout_direction=breakout_direction,
        bb_width_percentile_60=_pre_breakout_bb_percentile(selected, current_index),
    )


def _add_percentiles(
    features: Sequence[TickerFeatures],
    fields: Mapping[str, str],
    absolute: frozenset[str] = frozenset(),
) -> list[TickerFeatures]:
    def value(item: TickerFeatures, source: str) -> float | None:
        raw = getattr(item, source)
        return abs(raw) if source in absolute and raw is not None else raw

    values = {
        output: [value(item, source) for item in features]
        for output, source in fields.items()
    }
    return [
        replace(
            item,
            **{
                output: percentile_rank(value(item, source), values[output])
                for output, source in fields.items()
            },
        )
        for item in features
    ]


def add_cross_sectional_percentiles(
    features: Sequence[TickerFeatures],
) -> list[TickerFeatures]:
    return _add_percentiles(
        features,
        {
            "pct_relative_volume": "relative_volume_20",
            "pct_abs_return_5d": "return_5d",
            "pct_normalized_move": "normalized_move_1d",
            "pct_vol_expansion": "vol_expansion",
            "pct_stretch_atr": "stretch_atr",
            "pct_breakout_strength": "breakout_strength",
        },
        frozenset({"return_5d"}),
    )


def add_wildcard_percentiles(
    features: Sequence[TickerFeatures],
) -> list[TickerFeatures]:
    return _add_percentiles(
        features,
        {
            "wildcard_p_volume": "relative_volume_20",
            "wildcard_p_move": "normalized_move_1d",
            "wildcard_p_vol_expansion": "vol_expansion",
            "wildcard_p_stretch": "stretch_atr",
        },
    )


def _score(*values: float | None) -> float | None:
    valid = [value for value in values if value is not None and _finite(value)]
    return mean(valid) if valid else None


def _take_top(signals: Sequence[CandidateSignal], top_k: int) -> list[CandidateSignal]:
    return sorted(
        signals,
        key=lambda signal: (
            -(signal.score if signal.score is not None else -math.inf),
            signal.ticker,
        ),
    )[:top_k]


def screen_volume_anomaly(
    features: Sequence[TickerFeatures], config: LaneConfig,
) -> list[CandidateSignal]:
    candidates = [
        CandidateSignal(
            item.ticker,
            "volume_anomaly",
            item.pct_relative_volume,
            "non_directional",
            "normal",
            f"relative volume is {item.relative_volume_20:.2f}x its 20-day median",
        )
        for item in features
        if item.relative_volume_20 is not None
        and item.relative_volume_20 >= config.volume_min_relative_volume
    ]
    return _take_top(candidates, config.volume_top_k)


def _momentum_direction(item: TickerFeatures) -> str:
    if item.breakout_direction != "none":
        return item.breakout_direction
    return "bullish" if item.return_20d > 0 else "bearish"


def screen_momentum_breakout(
    features: Sequence[TickerFeatures], config: LaneConfig,
) -> list[CandidateSignal]:
    candidates: list[CandidateSignal] = []
    for item in features:
        same_direction = (
            item.return_5d > 0 and item.return_20d > 0
        ) or (
            item.return_5d < 0 and item.return_20d < 0
        )
        momentum = (
            same_direction
            and (item.pct_abs_return_5d or 0.0) >= config.momentum_percentile
        )
        breakout = item.breakout_strength is not None and item.breakout_strength > 0
        if not (momentum or breakout):
            continue
        direction = _momentum_direction(item)
        score = _score(
            item.pct_abs_return_5d,
            item.pct_breakout_strength,
            item.pct_relative_volume,
        )
        detail = (
            f"{direction} 20-day breakout" if breakout else f"{direction} 5-day momentum"
        )
        if item.pct_abs_return_5d is not None:
            detail += f", 5-day momentum is in the {item.pct_abs_return_5d:.0%} percentile"
        if item.relative_volume_20 is not None:
            detail += f", relative volume {item.relative_volume_20:.2f}x"
        candidates.append(
            CandidateSignal(item.ticker, "momentum_breakout", score, direction, "normal", detail)
        )
    return _take_top(candidates, config.momentum_top_k)


def screen_stretched_reversal(
    features: Sequence[TickerFeatures], config: LaneConfig,
) -> list[CandidateSignal]:
    candidates = []
    for item in features:
        if (
            item.normalized_move_1d is None
            or item.stretch_atr is None
            or item.normalized_move_1d < config.stretched_min_normalized_move
            or item.stretch_atr < config.stretched_min_stretch_atr
        ):
            continue
        direction = "bearish_reversal" if item.price > item.sma20 else "bullish_reversal"
        score = _score(item.pct_normalized_move, item.pct_stretch_atr)
        candidates.append(
            CandidateSignal(
                item.ticker,
                "stretched_reversal",
                score,
                direction,
                "normal",
                f"stock moved {item.normalized_move_1d:.2f} ATR today and is {item.stretch_atr:.2f} ATR from its 20-day mean",
            )
        )
    return _take_top(candidates, config.stretched_top_k)


def screen_volatility_expansion(
    features: Sequence[TickerFeatures], config: LaneConfig,
) -> list[CandidateSignal]:
    candidates = []
    ratios = {item.ticker: item.vol_expansion for item in features}
    for item in features:
        if item.vol_expansion is None:
            continue
        if not (
            item.vol_expansion >= config.volatility_min_ratio
            or (item.pct_vol_expansion or 0.0) >= config.volatility_min_percentile
        ):
            continue
        candidates.append(
            CandidateSignal(
                item.ticker,
                "volatility_expansion",
                item.pct_vol_expansion,
                "non_directional",
                "normal",
                f"5-day realized volatility is {item.vol_expansion:.2f}x its 20-day level",
            )
        )
    return sorted(
        candidates,
        key=lambda signal: (-ratios[signal.ticker], signal.ticker),
    )[: config.volatility_top_k]


def screen_compression_breakout(
    features: Sequence[TickerFeatures], config: LaneConfig,
) -> list[CandidateSignal]:
    candidates = []
    for item in features:
        if (
            item.bb_width_percentile_60 is None
            or item.bb_width_percentile_60 > config.compression_max_percentile
            or item.breakout_strength is None
            or item.breakout_strength <= 0
            or item.relative_volume_20 is None
            or item.relative_volume_20 < config.compression_min_relative_volume
        ):
            continue
        score = _score(
            1.0 - item.bb_width_percentile_60,
            item.pct_breakout_strength,
            item.pct_relative_volume,
        )
        candidates.append(
            CandidateSignal(
                item.ticker,
                "compression_breakout",
                score,
                item.breakout_direction,
                "normal",
                f"20-day {item.breakout_direction} range breakout after volatility compression in the lowest {item.bb_width_percentile_60:.0%} of recent history, with {item.relative_volume_20:.2f}x normal volume",
            )
        )
    return _take_top(candidates, config.compression_top_k)


def extreme_percentile(percentile: float | None, floor: float = 0.80) -> float:
    if percentile is None or not _finite(percentile):
        return 0.0
    if floor >= 1.0:
        return 0.0
    return max(0.0, percentile - floor) / (1.0 - floor)


def wildcard_score(
    p_volume: float | None,
    p_move: float | None,
    p_vol_expansion: float | None,
    p_stretch: float | None,
    floor: float = 0.80,
) -> float:
    return sum(
        extreme_percentile(value, floor)
        for value in (p_volume, p_move, p_vol_expansion, p_stretch)
    )


def screen_wildcard(
    features: Sequence[TickerFeatures], config: LaneConfig,
) -> list[CandidateSignal]:
    candidates = []
    for item in features:
        percentiles = (
            item.wildcard_p_volume,
            item.wildcard_p_move,
            item.wildcard_p_vol_expansion,
            item.wildcard_p_stretch,
        )
        high_count = sum(
            value is not None and value >= config.wildcard_multi_feature_percentile
            for value in percentiles
        )
        single_extreme = any(
            value is not None and value >= config.wildcard_single_extreme_percentile
            for value in percentiles
        )
        if high_count < 2 and not single_extreme:
            continue
        raw_score = wildcard_score(*percentiles, floor=config.wildcard_extreme_floor)
        direction = item.breakout_direction if item.breakout_direction != "none" else "non_directional"
        labels = [
            f"{name} {value:.0%} percentile"
            for name, value in (
                ("volume", item.wildcard_p_volume),
                ("normalized move", item.wildcard_p_move),
                ("volatility expansion", item.wildcard_p_vol_expansion),
                ("stretch", item.wildcard_p_stretch),
            )
            if value is not None and value >= config.wildcard_multi_feature_percentile
        ]
        candidates.append(
            CandidateSignal(
                item.ticker,
                "wildcard",
                raw_score / 4.0,
                direction,
                "high",
                "relaxed-liquidity stock showing " + ", ".join(labels),
            )
        )
    return _take_top(candidates, config.wildcard_top_k)


def _community_signals(mentions: Sequence[CommunityMention]) -> list[CandidateSignal]:
    by_ticker: dict[str, list[CommunityMention]] = defaultdict(list)
    for mention in mentions:
        by_ticker[mention.ticker].append(mention)

    signals = []
    for ticker, ticker_mentions in by_ticker.items():
        details = ", ".join(
            f"{mention.source} rank #{mention.rank}"
            + (f" ({mention.mentions} mentions)" if mention.mentions is not None else "")
            for mention in ticker_mentions
        )
        signals.append(
            CandidateSignal(
                ticker,
                "community_interest",
                None,
                "non_directional",
                "normal",
                f"community interest: {details}",
                tuple(ticker_mentions),
            )
        )
    return sorted(signals, key=lambda signal: signal.ticker)


def _load_community_mentions(
    client: ApeWisdomClient | None, config: CommunityConfig,
) -> tuple[CommunityMention, ...]:
    if client is None:
        return ()
    mentions: list[CommunityMention] = []
    for source in config.sources:
        try:
            mentions.extend(client.top(source, config.top_k))
        except (ApeWisdomError, OSError) as error:
            LOGGER.warning("Community interest fetch failed for %s: %s", source, error)
    return tuple(mentions)


def screen_exploration(
    features: Sequence[TickerFeatures], selected_tickers: set[str], as_of_date: date, config: LaneConfig,
) -> list[CandidateSignal]:
    available = sorted(item.ticker for item in features if item.ticker not in selected_tickers)
    rng = random.Random(int(as_of_date.strftime("%Y%m%d")))
    sampled = rng.sample(available, min(config.exploration_top_k, len(available)))
    return [
        CandidateSignal(
            ticker,
            "exploration",
            None,
            "non_directional",
            "normal",
            "deterministic exploration sample; no predefined signal",
        )
        for ticker in sorted(sampled)
    ]


def _valid_bar(bar: Bar) -> bool:
    return (
        all(_finite(value) for value in (bar.open, bar.high, bar.low, bar.close))
        and bar.close > 0
        and bar.volume >= 0
        and bar.high >= bar.low
        and bar.low <= bar.open <= bar.high
        and bar.low <= bar.close <= bar.high
    )


def _asset_is_eligible(asset: Asset, include_etfs: bool) -> tuple[bool, str | None]:
    if asset.status != "active":
        return False, "inactive"
    if not asset.tradable:
        return False, "not_tradable"
    if asset.asset_class != "us_equity":
        return False, "not_us_equity"
    if not include_etfs and getattr(asset, "is_etf", False):
        return False, "etf_excluded"
    return True, None


def _aggregate(
    signals: Sequence[CandidateSignal],
    features_by_ticker: Mapping[str, TickerFeatures],
) -> tuple[Candidate, ...]:
    by_ticker: dict[str, list[CandidateSignal]] = defaultdict(list)
    for signal in signals:
        by_ticker[signal.ticker].append(signal)
    order_index = {category: index for index, category in enumerate(LANE_NAMES)}
    candidates: list[Candidate] = []
    for ticker, ticker_signals in by_ticker.items():
        ordered = sorted(ticker_signals, key=lambda signal: order_index[signal.category])
        categories = tuple(signal.category for signal in ordered)
        scored = [signal for signal in ordered if signal.score is not None]
        primary_signal = max(
            scored, key=lambda signal: (signal.score, -order_index[signal.category])
        ) if scored else ordered[0]
        direction_signal = max(
            ordered,
            key=lambda signal: (
                signal.score if signal.score is not None else -1.0,
                -order_index[signal.category],
            ),
        )
        candidates.append(
            Candidate(
                ticker=ticker,
                categories=categories,
                primary_category=primary_signal.category,
                category_count=len(categories),
                direction_hint=direction_signal.direction_hint,
                risk_level="high" if "wildcard" in categories else "normal",
                scores={signal.category: signal.score for signal in ordered if signal.score is not None},
                features=features_by_ticker.get(ticker),
                reasons=tuple(signal.reason for signal in ordered),
                community=tuple(
                    mention
                    for signal in ordered
                    for mention in signal.community
                ),
            )
        )
    return tuple(sorted(candidates, key=lambda candidate: candidate.ticker))


def _merge_feature_views(
    normal_features: Sequence[TickerFeatures],
    wildcard_features: Sequence[TickerFeatures],
) -> dict[str, TickerFeatures]:
    merged = {item.ticker: item for item in normal_features}
    for wildcard in wildcard_features:
        normal = merged.get(wildcard.ticker)
        merged[wildcard.ticker] = wildcard if normal is None else replace(
            normal,
            wildcard_p_volume=wildcard.wildcard_p_volume,
            wildcard_p_move=wildcard.wildcard_p_move,
            wildcard_p_vol_expansion=wildcard.wildcard_p_vol_expansion,
            wildcard_p_stretch=wildcard.wildcard_p_stretch,
        )
    return merged


class Stage1Screener:
    def __init__(
        self,
        dataset: MarketDataset,
        config: ScreeningConfig = DEFAULT_SCREENING_CONFIG,
        community_client: ApeWisdomClient | None = None,
    ) -> None:
        self.dataset = dataset
        self.config = config
        self.community_client = community_client

    def screen(self, as_of_date: date | str) -> ScreenResult:
        started = time.perf_counter()
        requested_date = _parse_as_of_date(as_of_date)
        exclusions: Counter[str] = Counter()
        base_features: dict[str, TickerFeatures] = {}
        universe_size = 0
        for ticker in sorted(self.dataset.assets):
            asset = self.dataset.assets[ticker]
            asset_ok, reason = _asset_is_eligible(asset, self.config.include_etfs)
            if not asset_ok:
                exclusions[reason or "ineligible_asset"] += 1
                continue
            universe_size += 1
            bars = [bar for bar in self.dataset.history.get(ticker, ()) if bar.date <= requested_date]
            if len(bars) < self.config.min_history_days:
                exclusions["insufficient_history"] += 1
                continue
            if any(not _valid_bar(bar) for bar in bars):
                exclusions["invalid_data"] += 1
                continue
            features = calculate_features(bars, requested_date)
            if features is None:
                exclusions["insufficient_history"] += 1
                continue
            base_features[ticker] = features

        normal_features = [
            item
            for item in base_features.values()
            if item.price >= self.config.normal.min_price
            and item.median_dollar_volume_20 >= self.config.normal.min_median_dollar_volume_20
        ]
        wildcard_features = [
            item
            for item in base_features.values()
            if item.price >= self.config.wildcard.min_price
            and item.median_dollar_volume_20 >= self.config.wildcard.min_median_dollar_volume_20
        ]
        exclusions["below_price_threshold"] += sum(
            item.price < self.config.normal.min_price for item in base_features.values()
        )
        exclusions["below_liquidity_threshold"] += sum(
            item.price >= self.config.normal.min_price
            and item.median_dollar_volume_20 < self.config.normal.min_median_dollar_volume_20
            for item in base_features.values()
        )

        normal_features = add_cross_sectional_percentiles(normal_features)
        wildcard_features = add_wildcard_percentiles(wildcard_features)
        lane_config = self.config.lane
        lane_signals = [
            screen_volume_anomaly(normal_features, lane_config),
            screen_momentum_breakout(normal_features, lane_config),
            screen_stretched_reversal(normal_features, lane_config),
            screen_volatility_expansion(normal_features, lane_config),
            screen_compression_breakout(normal_features, lane_config),
            screen_wildcard(wildcard_features, lane_config),
        ]
        community_mentions = _load_community_mentions(
            self.community_client, self.config.community
        )
        lane_signals.append(_community_signals(community_mentions))
        selected_tickers = {signal.ticker for signals in lane_signals for signal in signals}
        exploration = screen_exploration(
            normal_features, selected_tickers, requested_date, lane_config
        )
        lane_signals.append(exploration)
        all_signals = [signal for signals in lane_signals for signal in signals]
        features_by_ticker = _merge_feature_views(normal_features, wildcard_features)
        candidates = _aggregate(all_signals, features_by_ticker)
        lane_counts = {
            category: sum(signal.category == category for signal in all_signals)
            for category in LANE_NAMES
        }
        runtime = time.perf_counter() - started
        LOGGER.info(
            "Stage 1 screen as_of_date=%s universe=%d normal=%d wildcard=%d candidates=%d runtime=%.3fs",
            requested_date,
            universe_size,
            len(normal_features),
            len(wildcard_features),
            len(candidates),
            runtime,
        )
        LOGGER.info("Stage 1 lane counts=%s exclusions=%s", lane_counts, dict(exclusions))
        return ScreenResult(
            as_of_date=requested_date,
            feed=self.config.feed,
            universe_size=universe_size,
            normal_eligible=len(normal_features),
            wildcard_eligible=len(wildcard_features),
            candidates=candidates,
            lane_counts=lane_counts,
            exclusions=dict(sorted(exclusions.items())),
            runtime_seconds=runtime,
            community_interest=community_mentions,
        )


def screen(
    dataset: MarketDataset,
    as_of_date: date | str,
    config: ScreeningConfig = DEFAULT_SCREENING_CONFIG,
    community_client: ApeWisdomClient | None = None,
) -> ScreenResult:
    """Convenience API: ``screen(dataset, as_of_date)``."""

    return Stage1Screener(dataset, config, community_client).screen(as_of_date)


def write_screen_result(path: Path, result: ScreenResult) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(result.to_json(), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the deterministic Stage 1 screen")
    parser.add_argument("--db-path", type=Path, default=Path("data/market.sqlite3"))
    parser.add_argument("--as-of-date", type=date.fromisoformat)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/stage1_screen.json"),
        help="Write machine-readable JSON to this path",
    )
    parser.add_argument(
        "--print-json",
        action="store_true",
        help="Also print the JSON result to stdout",
    )
    parser.add_argument(
        "--no-community",
        action="store_true",
        help="Skip the ApeWisdom community-interest step",
    )
    parser.add_argument("--log-level", default="INFO", choices=("DEBUG", "INFO", "WARNING", "ERROR"))
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=getattr(logging, args.log_level))
    with MarketStore(args.db_path) as store:
        dataset = store.load_dataset()
        cutoff = date.today() - timedelta(days=1)
        as_of = args.as_of_date or max(
            (bar.date for bars in dataset.history.values() for bar in bars if bar.date <= cutoff),
            default=cutoff,
        )
        config = DEFAULT_SCREENING_CONFIG
        client = None if args.no_community else ApeWisdomClient(
            config.community.base_url, config.community.timeout_seconds
        )
        result = Stage1Screener(dataset, config, client).screen(as_of)
    write_screen_result(args.output, result)
    if args.print_json:
        print(result.to_json(), end="")
    print(result.summary_text(), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
