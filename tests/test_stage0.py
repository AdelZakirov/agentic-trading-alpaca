from datetime import date
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Iterator

from alpaca_agent.stage0 import chunks, parse_bar
from alpaca_agent.config import Settings
from alpaca_agent.stage0 import Stage0Fetcher
from alpaca_agent.store import MarketStore


class Stage0Tests(unittest.TestCase):
    def test_chunks_respects_configured_batch_size(self) -> None:
        self.assertEqual(
            list(chunks(["A", "B", "C", "D", "E"], 2)),
            [["A", "B"], ["C", "D"], ["E"]],
        )

    def test_parse_bar_validates_and_normalizes_bar(self) -> None:
        bar = parse_bar(
            {
                "symbol": "aapl",
                "t": "2026-08-24T00:00:00Z",
                "o": "100",
                "h": "110",
                "l": "95",
                "c": "105",
                "v": "1234",
            }
        )
        self.assertEqual(bar.symbol, "AAPL")
        self.assertEqual(bar.date, date(2026, 8, 24))
        self.assertEqual(bar.close, 105.0)
        self.assertEqual(bar.volume, 1234)

    def test_parse_bar_rejects_bad_data(self) -> None:
        raw = {
            "symbol": "AAPL",
            "t": "2026-08-24T00:00:00Z",
            "o": "100",
            "h": "110",
            "l": "95",
            "c": "105",
            "v": "1234",
        }
        for field, value in (("c", "0"), ("h", "90"), ("v", "-1"), ("t", "not-a-date")):
            with self.subTest(field=field):
                invalid = {**raw, field: value}
                with self.assertRaises((TypeError, ValueError, KeyError)):
                    parse_bar(invalid)

    def test_fetcher_filters_assets_and_persists_local_dataset(self) -> None:
        class FakeClient:
            def list_assets(self) -> list[dict[str, Any]]:
                return [
                    {
                        "symbol": "AAPL",
                        "exchange": "NASDAQ",
                        "class": "us_equity",
                        "status": "active",
                        "tradable": True,
                        "shortable": True,
                        "fractionable": True,
                    },
                    {
                        "symbol": "MSFT",
                        "exchange": "NASDAQ",
                        "class": "us_equity",
                        "status": "inactive",
                        "tradable": True,
                    },
                    {
                        "symbol": "TSLA",
                        "exchange": "NASDAQ",
                        "class": "us_equity",
                        "status": "active",
                        "tradable": True,
                    },
                ]

            def fetch_snapshots(self, symbols: list[str]) -> dict[str, Any]:
                return {
                    "AAPL": {
                        "latestTrade": {"p": 105.0, "t": "2026-08-24T20:00:00Z"},
                        "dailyBar": {"o": 100.0, "h": 110.0, "l": 95.0, "c": 105.0, "v": 1000},
                    }
                }

            def iter_daily_bars(
                self, symbols: list[str], start: date, end: date
            ) -> Iterator[dict[str, Any]]:
                yield {
                    "symbol": "AAPL",
                    "t": "2026-08-24T00:00:00Z",
                    "o": 100,
                    "h": 110,
                    "l": 95,
                    "c": 105,
                    "v": 1000,
                }

        settings = Settings(
            api_key="test",
            secret_key="test",
            trading_endpoint="https://paper.example/v2",
            data_endpoint="https://data.example/v2",
            feed="iex",
            batch_size=100,
            history_days=1,
            request_timeout_seconds=1,
            max_retries=0,
            retry_base_seconds=0,
            db_path=Path("unused.sqlite3"),
            manifest_path=Path("unused.json"),
        )
        with TemporaryDirectory() as temp_dir:
            with MarketStore(Path(temp_dir) / "market.sqlite3") as store:
                summary = Stage0Fetcher(settings, FakeClient(), store).run()
                dataset = store.load_dataset()

                self.assertEqual(summary.symbols_requested, 2)
                self.assertEqual(summary.symbols_loaded, 1)
                self.assertEqual(set(dataset.assets), {"AAPL", "TSLA"})
                self.assertEqual(len(dataset.history["AAPL"]), 1)
                self.assertIn("TSLA", {error.symbol for error in summary.errors})
