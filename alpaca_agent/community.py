"""Small client for ApeWisdom's deterministic ranked-interest API."""

from __future__ import annotations

import json
from dataclasses import dataclass
from collections.abc import Mapping
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


class ApeWisdomError(RuntimeError):
    """ApeWisdom could not return a valid ranked result."""


@dataclass(frozen=True, slots=True)
class CommunityMention:
    source: str
    ticker: str
    rank: int
    name: str | None
    mentions: int | None
    upvotes: int | None
    rank_24h_ago: int | None
    mentions_24h_ago: int | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "ticker": self.ticker,
            "rank": self.rank,
            "name": self.name,
            "mentions": self.mentions,
            "upvotes": self.upvotes,
            "rank_24h_ago": self.rank_24h_ago,
            "mentions_24h_ago": self.mentions_24h_ago,
        }


def _int_or_none(value: Any) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


class ApeWisdomClient:
    def __init__(self, base_url: str = "https://apewisdom.io/api/v1.0", timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def top(self, source: str, limit: int = 50) -> tuple[CommunityMention, ...]:
        url = f"{self.base_url}/filter/{quote(source, safe='')}/page/1"
        request = Request(
            url,
            headers={"Accept": "application/json", "User-Agent": "alpaca-agent/1.0"},
            method="GET",
        )
        try:
            with urlopen(request, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, OSError) as error:
            raise ApeWisdomError(f"GET {url} failed: {error}") from error
        except json.JSONDecodeError as error:
            raise ApeWisdomError(f"GET {url} returned invalid JSON") from error

        results = payload.get("results") if isinstance(payload, Mapping) else None
        if not isinstance(results, list):
            raise ApeWisdomError(f"GET {url} returned no results list")
        mentions: list[CommunityMention] = []
        for position, raw in enumerate(results[:limit], start=1):
            if not isinstance(raw, Mapping):
                continue
            ticker = str(raw.get("ticker", "")).strip().upper()
            if not ticker:
                continue
            mentions.append(
                CommunityMention(
                    source=source,
                    ticker=ticker,
                    rank=_int_or_none(raw.get("rank")) or position,
                    name=str(raw["name"]) if raw.get("name") is not None else None,
                    mentions=_int_or_none(raw.get("mentions")),
                    upvotes=_int_or_none(raw.get("upvotes")),
                    rank_24h_ago=_int_or_none(raw.get("rank_24h_ago")),
                    mentions_24h_ago=_int_or_none(raw.get("mentions_24h_ago")),
                )
            )
        return tuple(mentions)
