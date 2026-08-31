from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def load_dotenv(path: Path = Path(".env")) -> None:
    """Load the small subset of dotenv syntax needed by this project.

    This keeps the first version dependency-free. Existing environment values
    win over values in ``.env`` so deployment environments remain authoritative.
    """

    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def _env_int(name: str, default: int, minimum: int = 1) -> int:
    raw = os.getenv(name)
    if raw is None:
        return default
    value = int(raw)
    if value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return value


def _env_float(name: str, default: float, minimum: float = 0.0) -> float:
    raw = os.getenv(name)
    if raw is None:
        return default
    value = float(raw)
    if value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return value


@dataclass(frozen=True, slots=True)
class Settings:
    api_key: str
    secret_key: str
    trading_endpoint: str
    data_endpoint: str
    feed: str
    batch_size: int
    history_days: int
    request_timeout_seconds: int
    max_retries: int
    retry_base_seconds: float
    db_path: Path
    manifest_path: Path

    @classmethod
    def from_env(cls, dotenv_path: Path = Path(".env")) -> "Settings":
        load_dotenv(dotenv_path)
        api_key = os.getenv("ALPACA_API_KEY", "").strip()
        secret_key = os.getenv("ALPACA_SECRET_KEY", "").strip()
        if not api_key or not secret_key:
            raise ValueError(
                "ALPACA_API_KEY and ALPACA_SECRET_KEY are required; "
                "copy .env.example to .env and fill them in"
            )

        return cls(
            api_key=api_key,
            secret_key=secret_key,
            trading_endpoint=os.getenv(
                "ALPACA_ENDPOINT", "https://paper-api.alpaca.markets/v2"
            ).rstrip("/"),
            data_endpoint=os.getenv(
                "ALPACA_DATA_ENDPOINT", "https://data.alpaca.markets/v2"
            ).rstrip("/"),
            feed=os.getenv("ALPACA_FEED", "iex").strip().lower(),
            batch_size=_env_int("ALPACA_BATCH_SIZE", 100),
            history_days=_env_int("ALPACA_HISTORY_DAYS", 120),
            request_timeout_seconds=_env_int("ALPACA_REQUEST_TIMEOUT_SECONDS", 30),
            max_retries=_env_int("ALPACA_MAX_RETRIES", 5, minimum=0),
            retry_base_seconds=_env_float("ALPACA_RETRY_BASE_SECONDS", 1.0),
            db_path=Path(os.getenv("ALPACA_DB_PATH", "data/market.sqlite3")),
            manifest_path=Path(
                os.getenv("ALPACA_MANIFEST_PATH", "data/stage0_manifest.json")
            ),
        )

