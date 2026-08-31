from __future__ import annotations

from dataclasses import replace
from datetime import date, timedelta
from statistics import pstdev
import unittest
from unittest.mock import patch

from alpaca_agent.community import ApeWisdomClient, CommunityMention
from alpaca_agent.models import Asset, Bar, MarketDataset
from alpaca_agent.stage1 import (
    LaneConfig,
    ScreeningConfig,
    average_true_range,
    bollinger_width,
    calculate_features,
    percentile_rank,
    screen_compression_breakout,
    screen_volume_anomaly,
    screen_wildcard,
    wildcard_score,
    Stage1Screener,
)


def make_bars(
    symbol: str,
    closes: list[float],
    volumes: list[int] | None = None,
    start: date = date(2026, 1, 1),
) -> list[Bar]:
    volumes = volumes or [100_000] * len(closes)
    bars = []
    for index, (close, volume) in enumerate(zip(closes, volumes)):
        previous = closes[index - 1] if index else close
        high = max(close, previous) + 0.5
        low = min(close, previous) - 0.5
        bars.append(
            Bar(
                symbol=symbol,
                date=start + timedelta(days=index),
                open=previous,
                high=high,
                low=low,
                close=close,
                volume=volume,
            )
        )
    return bars


class Stage1FeatureTests(unittest.TestCase):
    def test_apewisdom_client_parses_ranked_results(self) -> None:
        class FakeResponse:
            def __enter__(self) -> "FakeResponse":
                return self

            def __exit__(self, *_: object) -> None:
                pass

            def read(self) -> bytes:
                return b'{"results":[{"rank":1,"ticker":"aapl","name":"Apple","mentions":12,"upvotes":34}]}'

        with patch("alpaca_agent.community.urlopen", return_value=FakeResponse()) as opener:
            result = ApeWisdomClient("https://example.test").top("all-stocks", 1)

        self.assertEqual(result[0].ticker, "AAPL")
        self.assertEqual(result[0].mentions, 12)
        self.assertEqual(opener.call_args.args[0].full_url, "https://example.test/filter/all-stocks/page/1")

    def test_features_exclude_current_bar_from_baselines(self) -> None:
        closes = [100.0] * 24 + [110.0]
        bars = make_bars("TEST", closes, [100] * 24 + [250])
        features = calculate_features(bars)
        self.assertIsNotNone(features)
        assert features is not None

        self.assertAlmostEqual(features.return_1d, 0.10)
        self.assertAlmostEqual(features.return_5d, 0.10)
        self.assertAlmostEqual(features.return_20d, 0.10)
        self.assertAlmostEqual(features.relative_volume_20 or 0.0, 2.5)
        self.assertAlmostEqual(features.median_dollar_volume_20, 10_000.0)
        self.assertAlmostEqual(features.sma20, 100.0)
        self.assertAlmostEqual(features.previous_20d_high, 100.5)
        self.assertGreater(features.breakout_strength or 0.0, 0.0)

        future = make_bars(
            "TEST",
            closes + [50.0],
            [100] * 24 + [250, 1_000],
        )
        historical = calculate_features(future, bars[-1].date)
        self.assertEqual(features.to_dict(), historical.to_dict() if historical else None)

    def test_atr_and_bollinger_helpers(self) -> None:
        bars = make_bars("TEST", [100.0] * 30)
        self.assertAlmostEqual(average_true_range(bars) or 0.0, 1.0)
        closes = list(range(1, 21))
        expected = 4 * pstdev(closes) / 10.5
        self.assertAlmostEqual(bollinger_width(closes), expected)
        self.assertEqual(percentile_rank(3.0, [1.0, 2.0, 3.0, 4.0]), 0.75)

    def test_wildcard_score_and_lane_qualification(self) -> None:
        bars = make_bars("TEST", [100.0] * 100)
        features = calculate_features(bars)
        self.assertIsNotNone(features)
        assert features is not None
        wildcard = replace(
            features,
            wildcard_p_volume=0.95,
            wildcard_p_move=0.91,
            wildcard_p_vol_expansion=0.50,
            wildcard_p_stretch=0.50,
        )
        self.assertAlmostEqual(wildcard_score(0.80, 0.90, 1.0, 0.70), 1.5)
        signals = screen_wildcard([wildcard], LaneConfig())
        self.assertEqual([signal.ticker for signal in signals], ["TEST"])

        volume = replace(features, relative_volume_20=2.0, pct_relative_volume=1.0)
        self.assertEqual(len(screen_volume_anomaly([volume], LaneConfig())), 1)

        compressed = replace(
            features,
            bb_width_percentile_60=0.10,
            breakout_strength=1.0,
            breakout_direction="bullish",
            relative_volume_20=2.0,
            pct_breakout_strength=1.0,
            pct_relative_volume=1.0,
        )
        self.assertEqual(
            len(screen_compression_breakout([compressed], LaneConfig())), 1
        )


class Stage1PipelineTests(unittest.TestCase):
    def test_community_interest_fetches_both_feeds_and_merges_tickers(self) -> None:
        class FakeCommunityClient:
            def __init__(self) -> None:
                self.calls: list[tuple[str, int]] = []

            def top(self, source: str, limit: int) -> tuple[CommunityMention, ...]:
                self.calls.append((source, limit))
                return {
                    "all-stocks": (
                        CommunityMention("all-stocks", "VOLUME", 1, "Volume Co", 12, 20, 2, 8),
                        CommunityMention("all-stocks", "COMM", 2, "Community Co", 10, 18, 4, 6),
                    ),
                    "options": (
                        CommunityMention("options", "COMM", 1, "Community Co", 15, 22, 3, 9),
                        CommunityMention("options", "OPTS", 2, "Options Co", 9, 11, 5, 5),
                    ),
                }[source]

        bars = make_bars("VOLUME", [100.0] * 100)
        assets = {
            "VOLUME": Asset("VOLUME", "NASDAQ", "active", "us_equity", True, True, True),
        }
        client = FakeCommunityClient()
        result = Stage1Screener(
            MarketDataset(assets, {}, {"VOLUME": bars}),
            ScreeningConfig(min_history_days=80),
            client,
        ).screen(bars[-1].date)

        self.assertEqual(client.calls, [("all-stocks", 50), ("options", 50)])
        self.assertEqual(len(result.community_interest), 4)
        self.assertEqual(result.lane_counts["community_interest"], 3)
        candidates = {candidate.ticker: candidate for candidate in result.candidates}
        self.assertIn("community_interest", candidates["VOLUME"].categories)
        self.assertIsNone(candidates["COMM"].features)
        self.assertEqual(
            [item["source"] for item in result.to_dict()["community_interest"]],
            ["all-stocks", "all-stocks", "options", "options"],
        )

    def test_screen_is_multilabel_and_exploration_is_reproducible(self) -> None:
        common = [100.0] * 100
        boring = make_bars("BORING", common)
        volume = make_bars("VOLUME", common, [100_000] * 99 + [300_000])
        momentum = make_bars(
            "MOMENTUM",
            [100.0] * 95 + [102.0, 106.0, 112.0, 120.0, 130.0],
            [100_000] * 95 + [150_000] * 5,
        )
        wildcard = make_bars(
            "WILD",
            [2.5] * 99 + [3.5],
            [250_000] * 99 + [1_000_000],
        )
        assets = {
            symbol: Asset(symbol, "NASDAQ", "active", "us_equity", True, True, True)
            for symbol in ("BORING", "VOLUME", "MOMENTUM", "WILD")
        }
        dataset = MarketDataset(
            assets=assets,
            snapshots={},
            history={
                "BORING": boring,
                "VOLUME": volume,
                "MOMENTUM": momentum,
                "WILD": wildcard,
            },
        )
        config = ScreeningConfig(min_history_days=80)
        as_of = boring[-1].date
        first = Stage1Screener(dataset, config).screen(as_of)
        second = Stage1Screener(dataset, config).screen(as_of)

        self.assertEqual(first.to_dict(), second.to_dict())
        self.assertGreaterEqual(first.lane_counts["volume_anomaly"], 1)
        self.assertGreaterEqual(first.lane_counts["momentum_breakout"], 1)
        self.assertGreaterEqual(first.lane_counts["wildcard"], 1)
        candidate_map = {candidate.ticker: candidate for candidate in first.candidates}
        self.assertIn("MOMENTUM", candidate_map)
        self.assertIn("volume_anomaly", candidate_map["VOLUME"].categories)
        self.assertIn("exploration", candidate_map["BORING"].categories)
        self.assertEqual(first.normal_eligible, 3)
        self.assertEqual(first.wildcard_eligible, 4)

    def test_invalid_data_is_excluded_without_crashing(self) -> None:
        bars = make_bars("BAD", [100.0] * 100)
        bars[50] = replace(bars[50], close=0.0)
        asset = Asset("BAD", "NASDAQ", "active", "us_equity", True, True, True)
        dataset = MarketDataset({"BAD": asset}, {}, {"BAD": bars})
        result = Stage1Screener(dataset).screen(bars[-1].date)
        self.assertEqual(result.candidate_count, 0)
        self.assertEqual(result.exclusions["invalid_data"], 1)


if __name__ == "__main__":
    unittest.main()
