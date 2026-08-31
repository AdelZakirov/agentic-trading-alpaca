from __future__ import annotations

from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from alpaca_agent.daily_shortlist import (
    is_due,
    load_last_completed,
    run,
    run_pipeline,
    save_completion,
)


class DailyShortlistTests(unittest.TestCase):
    def test_due_thirty_minutes_after_open(self) -> None:
        due, market_date, reason = is_due(
            {"is_open": True, "timestamp": "2026-08-31T10:00:00-04:00"},
            None,
        )
        self.assertTrue(due)
        self.assertEqual(market_date, date(2026, 8, 31))
        self.assertEqual(reason, "due")

    def test_not_due_before_time_closed_or_already_completed(self) -> None:
        before = {"is_open": True, "timestamp": "2026-08-31T09:59:59-04:00"}
        closed = {"is_open": False, "timestamp": "2026-08-31T10:00:00-04:00"}
        ready = {"is_open": True, "timestamp": "2026-08-31T10:00:00-04:00"}

        self.assertFalse(is_due(before, None)[0])
        self.assertFalse(is_due(closed, None)[0])
        self.assertFalse(is_due(ready, date(2026, 8, 31))[0])

    def test_check_only_does_not_run_pipeline_or_save_completion(self) -> None:
        clock = {"is_open": True, "timestamp": "2026-08-31T10:00:00-04:00"}
        with TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            with (
                patch("alpaca_agent.daily_shortlist.Settings.from_env"),
                patch("alpaca_agent.daily_shortlist.AlpacaClient") as client_class,
                patch("alpaca_agent.daily_shortlist.run_pipeline") as pipeline,
            ):
                client_class.return_value.get_clock.return_value = clock
                result = run(
                    False,
                    True,
                    temp_path / "state.json",
                    temp_path / "lock",
                )

        self.assertEqual(result, 0)
        pipeline.assert_not_called()

    def test_completion_state_round_trip(self) -> None:
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "state.json"
            save_completion(path, date(2026, 8, 31))
            self.assertEqual(load_last_completed(path), date(2026, 8, 31))

    def test_pipeline_runs_all_steps_in_order(self) -> None:
        calls: list[str] = []

        def step(name: str):
            def run(_argv: list[str]) -> int:
                calls.append(name)
                return 0
            return run

        with (
            patch("alpaca_agent.daily_shortlist.stage0_main", step("stage0")),
            patch("alpaca_agent.daily_shortlist.stage1_main", step("stage1")),
            patch("alpaca_agent.daily_shortlist.shortlist_main", step("shortlist")),
        ):
            run_pipeline()

        self.assertEqual(calls, ["stage0", "stage1", "shortlist"])


if __name__ == "__main__":
    unittest.main()
