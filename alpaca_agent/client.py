from __future__ import annotations

import json
import random
import time
from datetime import date
from email.utils import parsedate_to_datetime
from typing import Any, Iterator, Mapping
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .config import Settings


class AlpacaAPIError(RuntimeError):
    """An Alpaca request failed after retries or returned invalid JSON."""


class AlpacaClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._headers = {
            "APCA-API-KEY-ID": settings.api_key,
            "APCA-API-SECRET-KEY": settings.secret_key,
            "Accept": "application/json",
        }

    def _get_json(
        self,
        base_url: str,
        path: str,
        params: Mapping[str, str | int | None],
    ) -> Any:
        query = urlencode({key: value for key, value in params.items() if value is not None})
        url = f"{base_url}/{path.lstrip('/')}"
        if query:
            url = f"{url}?{query}"

        last_error: Exception | None = None
        for attempt in range(self.settings.max_retries + 1):
            request = Request(url, headers=self._headers, method="GET")
            try:
                with urlopen(request, timeout=self.settings.request_timeout_seconds) as response:
                    try:
                        return json.loads(response.read().decode("utf-8"))
                    except json.JSONDecodeError as error:
                        raise AlpacaAPIError(f"Invalid JSON response from {path}") from error
            except HTTPError as error:
                last_error = error
                is_transient = error.code == 429 or 500 <= error.code < 600
                if not is_transient or attempt >= self.settings.max_retries:
                    body = error.read().decode("utf-8", errors="replace")[:500]
                    raise AlpacaAPIError(
                        f"GET {path} failed with HTTP {error.code}: {body}"
                    ) from error
                self._sleep_before_retry(attempt, error.headers.get("Retry-After"))
            except (TimeoutError, URLError, OSError) as error:
                last_error = error
                if attempt >= self.settings.max_retries:
                    raise AlpacaAPIError(f"GET {path} failed: {error}") from error
                self._sleep_before_retry(attempt, None)

        raise AlpacaAPIError(f"GET {path} failed: {last_error}")

    def _sleep_before_retry(self, attempt: int, retry_after: str | None) -> None:
        delay: float | None = None
        if retry_after:
            try:
                delay = max(0.0, float(retry_after))
            except ValueError:
                try:
                    retry_at = parsedate_to_datetime(retry_after)
                    delay = max(0.0, retry_at.timestamp() - time.time())
                except (TypeError, ValueError, OverflowError):
                    delay = None
        if delay is None:
            delay = self.settings.retry_base_seconds * (2**attempt)
            delay += random.uniform(0, self.settings.retry_base_seconds)
        time.sleep(delay)

    def list_assets(self) -> list[dict[str, Any]]:
        response = self._get_json(
            self.settings.trading_endpoint,
            "/assets",
            {"status": "active", "asset_class": "us_equity"},
        )
        if not isinstance(response, list):
            raise AlpacaAPIError("The assets endpoint did not return a list")
        return response

    def get_clock(self) -> dict[str, Any]:
        response = self._get_json(self.settings.trading_endpoint, "/clock", {})
        if not isinstance(response, dict):
            raise AlpacaAPIError("The clock endpoint did not return an object")
        return response

    def fetch_snapshots(self, symbols: list[str]) -> dict[str, Any]:
        if not symbols:
            return {}
        response = self._get_json(
            self.settings.data_endpoint,
            "/stocks/snapshots",
            {"symbols": ",".join(symbols), "feed": self.settings.feed},
        )
        if not isinstance(response, dict):
            raise AlpacaAPIError("The snapshots endpoint did not return an object")
        return response

    def iter_daily_bars(
        self,
        symbols: list[str],
        start: date,
        end: date,
    ) -> Iterator[dict[str, Any]]:
        """Yield one symbol/date bar at a time, following pagination."""

        if not symbols or start > end:
            return

        page_token: str | None = None
        while True:
            response = self._get_json(
                self.settings.data_endpoint,
                "/stocks/bars",
                {
                    "symbols": ",".join(symbols),
                    "timeframe": "1Day",
                    "start": start.isoformat(),
                    "end": end.isoformat(),
                    "limit": 10000,
                    "adjustment": "raw",
                    "feed": self.settings.feed,
                    "page_token": page_token,
                },
            )
            if not isinstance(response, dict):
                raise AlpacaAPIError("The bars endpoint did not return an object")
            bars_by_symbol = response.get("bars", {})
            if not isinstance(bars_by_symbol, dict):
                raise AlpacaAPIError("The bars response has an invalid bars field")
            for symbol, bars in bars_by_symbol.items():
                if not isinstance(bars, list):
                    continue
                for bar in bars:
                    if isinstance(bar, dict):
                        yield {"symbol": symbol, **bar}
            page_token = response.get("next_page_token")
            if not page_token:
                return
