from __future__ import annotations

import argparse
import fcntl
import json
from datetime import date, datetime, time
from pathlib import Path
from typing import Any, Mapping
from zoneinfo import ZoneInfo

from .client import AlpacaClient
from .config import Settings
from .shortlist import main as shortlist_main
from .stage0 import main as stage0_main
from .stage1 import main as stage1_main


NEW_YORK = ZoneInfo("America/New_York")
RUN_AFTER = time(10, 0)
DEFAULT_STATE_PATH = Path("data/daily_shortlist_state.json")
DEFAULT_LOCK_PATH = Path("data/daily_shortlist.lock")


def load_last_completed(path: Path) -> date | None:
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    value = payload.get("last_completed_date")
    return date.fromisoformat(value) if value else None


def is_due(
    clock: Mapping[str, Any], last_completed: date | None
) -> tuple[bool, date, str]:
    raw_timestamp = clock.get("timestamp")
    if not isinstance(raw_timestamp, str):
        raise ValueError("Alpaca clock has no timestamp")
    timestamp = datetime.fromisoformat(raw_timestamp.replace("Z", "+00:00"))
    if timestamp.tzinfo is None:
        raise ValueError("Alpaca clock timestamp has no timezone")

    market_now = timestamp.astimezone(NEW_YORK)
    market_date = market_now.date()
    if clock.get("is_open") is not True:
        return False, market_date, "market is closed"
    if market_now.time().replace(tzinfo=None) < RUN_AFTER:
        return False, market_date, "waiting until 10:00 America/New_York"
    if last_completed == market_date:
        return False, market_date, "already completed for this market date"
    return True, market_date, "due"


def run_pipeline() -> None:
    steps = (
        ("stage0", stage0_main, ["--quiet"]),
        ("stage1", stage1_main, []),
        ("shortlist", shortlist_main, []),
    )
    for name, step, arguments in steps:
        print(f"Starting {name}", flush=True)
        exit_code = step(arguments)
        if exit_code != 0:
            raise RuntimeError(f"{name} failed with exit code {exit_code}")
        print(f"Finished {name}", flush=True)


def save_completion(path: Path, completed_date: date) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "last_completed_date": completed_date.isoformat(),
        "completed_at": datetime.now(NEW_YORK).isoformat(),
        "shortlist": "data/stage1_shortlist.md",
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def run(force: bool, check_only: bool, state_path: Path, lock_path: Path) -> int:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("w", encoding="utf-8") as lock_file:
        try:
            fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Daily shortlist is already running")
            return 0

        if force:
            completed_date = datetime.now(NEW_YORK).date()
        else:
            settings = Settings.from_env()
            clock = AlpacaClient(settings).get_clock()
            due, completed_date, reason = is_due(
                clock, load_last_completed(state_path)
            )
            if not due:
                print(f"Skipped: {reason}")
                return 0

        if check_only:
            print(f"Due: {completed_date.isoformat()}")
            return 0

        run_pipeline()
        save_completion(state_path, completed_date)
        print(f"Daily shortlist completed for {completed_date}")
        return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the deterministic Stage 0 → Stage 1 → shortlist pipeline"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Run now without checking market time or the last completed date",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Report whether the pipeline is due without running any stages",
    )
    parser.add_argument("--state-path", type=Path, default=DEFAULT_STATE_PATH)
    parser.add_argument("--lock-path", type=Path, default=DEFAULT_LOCK_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return run(args.force, args.check_only, args.state_path, args.lock_path)


if __name__ == "__main__":
    raise SystemExit(main())
