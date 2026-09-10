#!/usr/bin/env python3
"""Small dependency-free dashboard server for the paper-trading agent.

Markdown remains the source of truth. This module only extracts the parts the
dashboard needs at request time, so a new log or reconciliation is visible on
the next refresh without a separate build step.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
from dataclasses import replace
from datetime import datetime, time as datetime_time, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
DASHBOARD_DIR = ROOT / "dashboard"
NEW_YORK = ZoneInfo("America/New_York")
AMSTERDAM = ZoneInfo("Europe/Amsterdam")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def section(text: str, heading: str) -> str:
    """Return the body below a markdown heading until the next heading."""
    pattern = rf"(?ms)^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^#{{1,3}}\s+|\Z)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


def bullets(text: str) -> list[str]:
    return [
        re.sub(r"^[-*]\s+", "", line).strip()
        for line in text.splitlines()
        if re.match(r"^[-*]\s+", line)
    ]


def split_table_row(line: str) -> list[str]:
    line = line.strip().strip("|")
    return [cell.strip() for cell in line.split("|")]


def markdown_tables(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    tables: list[dict[str, str]] = []
    index = 0
    while index < len(lines):
        if not lines[index].lstrip().startswith("|"):
            index += 1
            continue
        headers = split_table_row(lines[index])
        if index + 1 >= len(lines) or not lines[index + 1].lstrip().startswith("|"):
            index += 1
            continue
        index += 2  # header and separator
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            values = split_table_row(lines[index])
            if len(values) == len(headers):
                tables.append(dict(zip(headers, values)))
            index += 1
    return tables


def first_sentence(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    match = re.match(r"(.+?[.!?])(?:\s|$)", value)
    return match.group(1) if match else value


def number(value: str | None) -> float | None:
    if not value:
        return None
    match = re.search(r"[-+]?\$?([\d,]+(?:\.\d+)?)", value)
    if not match:
        return None
    parsed = float(match.group(1).replace(",", ""))
    return -parsed if value.strip().startswith("-") else parsed


def date_label(value: str) -> str:
    try:
        return datetime.strptime(value, "%Y-%m-%d").strftime("%d %b %Y")
    except ValueError:
        return value


def money(value: object, *, signed: bool = False) -> str:
    try:
        amount = float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return "—"
    prefix = "-" if amount < 0 else "+" if signed and amount > 0 else ""
    return f"{prefix}${abs(amount):,.2f}"


def api_number(value: object) -> float | None:
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def format_timestamp(value: object, zone: ZoneInfo = AMSTERDAM) -> str:
    if not isinstance(value, str) or not value:
        return "—"
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        local = parsed.astimezone(zone)
        return local.strftime("%d %b %Y, %H:%M %Z")
    except ValueError:
        return value


def option_contract_label(symbol: str) -> tuple[str, str]:
    match = re.match(r"^(?P<underlying>[A-Z0-9]+)(?P<date>\d{6})(?P<kind>[CP])(?P<strike>\d{8})$", symbol)
    if not match:
        return symbol or "—", "Option"
    try:
        expiry = datetime.strptime(match.group("date"), "%y%m%d")
        expiry_label = expiry.strftime("%b %d").replace(" 0", " ")
    except ValueError:
        expiry_label = match.group("date")
    strike = int(match.group("strike")) / 1000
    kind = "call" if match.group("kind") == "C" else "put"
    strike_label = f"${strike:,.0f}" if strike.is_integer() else f"${strike:,.3f}".rstrip("0").rstrip(".")
    return match.group("underlying"), f"Option · {expiry_label} {strike_label} {kind}"


def portfolio_data() -> dict:
    path = ROOT / "memory/portfolio-state.md"
    text = read_text(path)
    values: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^-\s+([^:]+):\s*(.+)$", line)
        if match:
            values[match.group(1).strip()] = match.group(2).strip()

    positions = []
    for row in markdown_tables(section(text, "Positions and open orders")):
        pnl = row.get("Unrealized P/L", "")
        positions.append(
            {
                "ticker": row.get("Ticker", "—"),
                "instrument": row.get("Instrument", "—"),
                "side": row.get("Side", "—"),
                "quantity": row.get("Quantity", "—"),
                "entry": row.get("Average entry", "—"),
                "price": row.get("Current price", "—"),
                "marketValue": row.get("Market value", "—"),
                "pnl": pnl,
                "pnlValue": number(pnl),
                "positive": pnl.strip().startswith("+") or (number(pnl) or 0) > 0,
            }
        )

    decision_lines = bullets(section(text, "Latest decisions"))
    decisions = []
    for line in decision_lines:
        ticker_match = re.match(r"([A-Z0-9]+)\s+", line)
        ticker = ticker_match.group(1) if ticker_match else "—"
        action_match = re.search(r"\b(BUY|SELL|HOLD)\b", line)
        action = action_match.group(1) if action_match else "NOTE"
        decisions.append(
            {
                "ticker": ticker,
                "action": action,
                "text": line,
                "short": first_sentence(line),
            }
        )

    stock_count = len({position["ticker"] for position in positions if position["instrument"] == "Stock"})
    option_underlyings = {position["ticker"] for position in positions if position["instrument"] == "Option"}
    position_summary = f"{stock_count} stocks" + (f" + {len(option_underlyings)} option spreads" if option_underlyings else "")

    order_line = next(
        (line.strip() for line in section(text, "Positions and open orders").splitlines() if line.strip().startswith("Open order:")),
        "",
    )
    order_detail = "No open orders are documented."
    if order_line:
        order_text = re.sub(r"^Open order:\s*", "", order_line)
        order_text = order_text.split(", replacement broker order", 1)[0].rstrip(".")
        status_match = re.search(r"status `([^`]+)`, filled ([^.]*)", order_line)
        status_text = f"; status {status_match.group(1)}, filled {status_match.group(2)}" if status_match else ""
        order_detail = order_text + status_text + "."

    equity = values.get("Equity / portfolio value", values.get("Equity", "—"))
    return {
        "values": values,
        "equity": equity,
        "cash": values.get("Cash", "—"),
        "longValue": values.get("Long market value", "—"),
        "return": values.get("Return since initial $100,000", "—"),
        "positionsLabel": values.get("Positions", "—"),
        "positionSummary": position_summary,
        "positionRows": len(positions),
        "openOrders": values.get("Open orders", "—"),
        "ghostCount": values.get("Active ghost sets", "—"),
        "generated": values.get("Generated", "—"),
        "positions": positions,
        "decisions": decisions,
        "openOrderDetail": order_detail,
        "riskPosture": bullets(section(text, "Risk posture")),
        "warnings": bullets(section(text, "Links and warnings"))[-1:] or [],
        "source": "memory/portfolio-state.md",
        "sourceLabel": "Memory snapshot",
        "live": False,
        "syncError": None,
        "accountStatus": "—",
        "tradingBlocked": False,
        "buyingPower": "—",
        "optionsBuyingPower": "—",
        "shortValue": values.get("Short option-leg market value", "—"),
        "lastAccountRefresh": values.get("Last Alpaca account refresh", values.get("Generated", "—")),
        "session": {
            "isOpen": None,
            "label": "Session unavailable",
            "timestamp": "",
            "timestampLabel": "—",
            "nextCloseLabel": "—",
            "nextOpenLabel": "—",
            "timezone": "America/New_York",
        },
        "executions": [],
        "executionCountToday": 0,
        "todayOrderCount": 0,
    }


def trading_day_start_iso(trading_date: str) -> str:
    start = datetime.strptime(trading_date, "%Y-%m-%d").replace(tzinfo=NEW_YORK)
    return start.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def execution_data(activities: list[dict]) -> list[dict]:
    executions = []
    for activity in sorted(activities, key=lambda item: item.get("transaction_time", ""), reverse=True):
        symbol = str(activity.get("symbol", ""))
        if re.match(r"^[A-Z0-9]+\d{6}[CP]\d{8}$", symbol):
            ticker, contract = option_contract_label(symbol)
        else:
            ticker, contract = symbol or "—", ""
        executions.append(
            {
                "ticker": ticker,
                "contract": contract,
                "symbol": symbol,
                "side": str(activity.get("side", "")).upper(),
                "quantity": str(activity.get("qty", "—")),
                "price": money(activity.get("price")),
                "status": "Partial fill" if activity.get("type") == "partial_fill" else "Filled",
                "timestamp": activity.get("transaction_time", ""),
                "timestampLabel": format_timestamp(activity.get("transaction_time"), NEW_YORK),
                "orderId": activity.get("order_id", ""),
            }
        )
    return executions


def live_portfolio_data(base: dict) -> dict:
    """Overlay the Markdown snapshot with the read-only Alpaca paper account."""
    try:
        # Import lazily so the local Markdown dashboard still works without credentials.
        import sys

        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from alpaca_agent.client import AlpacaClient
        from alpaca_agent.config import Settings

        settings = Settings.from_env(ROOT / ".env")
        if os.getenv("ALPACA_PAPER_TRADE", "").lower() != "true":
            raise RuntimeError("paper trading is not enabled")
        if settings.trading_endpoint != "https://paper-api.alpaca.markets/v2":
            raise RuntimeError("the configured Alpaca endpoint is not the paper endpoint")
        settings = replace(settings, request_timeout_seconds=min(settings.request_timeout_seconds, 8), max_retries=1)
        client = AlpacaClient(settings)
        clock = client.get_clock()
        account = client.get_account()
        positions = client.get_positions()
        timestamp = str(clock.get("timestamp", ""))
        try:
            trading_date = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).astimezone(NEW_YORK).date().isoformat()
        except ValueError:
            trading_date = datetime.now(NEW_YORK).date().isoformat()
        orders = client.get_orders(status="all", after=trading_day_start_iso(trading_date))
        activities = client.get_account_activities(date_value=trading_date)
    except Exception as error:  # pragma: no cover - exercised by unavailable credentials/network
        base["syncError"] = str(error)
        return base

    live_positions = []
    for item in positions:
        symbol = str(item.get("symbol", ""))
        is_option = item.get("asset_class") == "us_option" or bool(re.match(r"^[A-Z0-9]+\d{6}[CP]\d{8}$", symbol))
        if is_option:
            ticker, instrument = option_contract_label(symbol)
        else:
            ticker, instrument = symbol or "—", "Stock"
        pnl_value = api_number(item.get("unrealized_pl"))
        pnl_percent = api_number(item.get("unrealized_plpc"))
        pnl = money(pnl_value, signed=True)
        if pnl_percent is not None and pnl != "—":
            pnl += f" ({pnl_percent * 100:.3f}%)"
        quantity = api_number(item.get("qty"))
        live_positions.append(
            {
                "ticker": ticker,
                "instrument": instrument,
                "side": str(item.get("side", "—")).title(),
                "quantity": f"{abs(quantity):g}" if quantity is not None else "—",
                "entry": money(item.get("avg_entry_price")),
                "price": money(item.get("current_price")),
                "marketValue": money(item.get("market_value")),
                "pnl": pnl,
                "pnlValue": pnl_value,
                "positive": (pnl_value or 0) >= 0,
                "symbol": symbol,
            }
        )

    stocks = {item["ticker"] for item in live_positions if item["instrument"] == "Stock"}
    option_underlyings = {item["ticker"] for item in live_positions if item["instrument"].startswith("Option")}
    position_summary = f"{len(stocks)} stocks" + (f" + {len(option_underlyings)} option spreads" if option_underlyings else "")
    terminal_statuses = {"filled", "canceled", "expired", "rejected", "replaced", "done_for_day"}
    open_orders = [order for order in orders if str(order.get("status", "")).lower() not in terminal_statuses]
    if open_orders:
        order_detail = "; ".join(
            f"{order.get('symbol') or 'Multi-leg order'} · {str(order.get('side') or order.get('order_class') or 'order').replace('_', ' ')} · {order.get('status', 'open')}"
            for order in open_orders
        )
    else:
        order_detail = "No open orders in Alpaca."
    equity_value = api_number(account.get("equity", account.get("portfolio_value")))
    return_value = (equity_value or 0) - 100000
    next_close = clock.get("next_close", "")
    next_open = clock.get("next_open", "")
    live = dict(base)
    live.update(
        {
            "values": account,
            "equity": money(equity_value),
            "cash": money(account.get("cash")),
            "longValue": money(account.get("long_market_value")),
            "shortValue": money(account.get("short_market_value")),
            "return": f"{money(return_value, signed=True)} ({return_value / 1000:.3f}%)",
            "positionsLabel": f"{len(stocks)} stock positions plus {len(live_positions) - len(stocks)} option legs",
            "positionSummary": position_summary,
            "positionRows": len(live_positions),
            "openOrders": str(len(open_orders)),
            "positions": live_positions,
            "openOrderDetail": order_detail,
            "generated": format_timestamp(timestamp),
            "sourceLabel": "Live Alpaca paper account",
            "live": True,
            "syncError": None,
            "accountStatus": str(account.get("status", "—")),
            "tradingBlocked": bool(account.get("trading_blocked")),
            "buyingPower": money(account.get("buying_power")),
            "optionsBuyingPower": money(account.get("options_buying_power")),
            "lastAccountRefresh": format_timestamp(timestamp),
            "session": {
                "isOpen": bool(clock.get("is_open")),
                "label": "Market open" if clock.get("is_open") else "Market closed",
                "timestamp": timestamp,
                "timestampLabel": format_timestamp(timestamp, NEW_YORK),
                "nextCloseLabel": format_timestamp(next_close, NEW_YORK),
                "nextOpenLabel": format_timestamp(next_open, NEW_YORK),
                "timezone": "America/New_York",
            },
            "executions": execution_data(activities),
            "executionCountToday": len(activities),
            "todayOrderCount": len(orders),
        }
    )
    return live


def summary_data(portfolio: dict) -> dict:
    summary_paths = sorted((ROOT / "memory/logs").glob("*-summary.md"), reverse=True)
    summary_path = summary_paths[0] if summary_paths else ROOT / "memory/logs/latest.md"
    text = read_text(summary_path)
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", summary_path.name)
    summary_date = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")
    material = bullets(section(text, "Material actions"))
    buys = [line for line in material if line.lower().startswith("bought ")]
    submitted = [line for line in material if line.lower().startswith("submitted ")]
    pnl_by_ticker: dict[str, float] = {}
    for position in portfolio["positions"]:
        if position["pnlValue"] is not None:
            pnl_by_ticker[position["ticker"]] = pnl_by_ticker.get(position["ticker"], 0) + position["pnlValue"]
    p_and_l = sorted(pnl_by_ticker.items(), key=lambda item: item[1])
    drag = p_and_l[0] if p_and_l else None
    help_item = p_and_l[-1] if p_and_l else None
    risk = bullets(section(text, "Portfolio risk and follow-up"))
    risk_line = next((line for line in risk if line.startswith("Main risks:")), "")

    buy_details = []
    bought_tickers = []
    for line in buys:
        match = re.match(r"Bought\s+(.+?)(?:\.\s+Thesis:|;|$)", line, flags=re.I)
        buy_details.append(match.group(1).rstrip(".") if match else re.sub(r"^Bought\s+", "", line, flags=re.I))
        ticker_match = re.search(r"\b([A-Z]{2,5})\s+shares", line)
        if ticker_match:
            bought_tickers.append(ticker_match.group(1))
    buy_text = " and ".join(buy_details)
    sold_lines = [line for line in material if re.search(r"\b(Sold|Closed)\b", line, flags=re.I)]
    sale_details = []
    for line in sold_lines:
        ticker_match = re.match(r"([A-Z0-9]+)\s+", line)
        ticker = ticker_match.group(1) if ticker_match else "the position"
        action_match = re.search(r"\b(Sold|Closed)\s+(.+?)(?:\s+under broker order|;|$)", line, flags=re.I)
        if action_match:
            verb = action_match.group(1).lower()
            detail = action_match.group(2).strip()
            sale_details.append(f"{verb} {ticker} {detail}")
    action_text = ""
    if sale_details:
        action_text = " " + ". ".join(detail[0].upper() + detail[1:] for detail in sale_details) + "."
    submitted_text = ""
    if submitted and not sold_lines:
        submitted_text = " I also submitted an order that stayed open and unfilled, so it is not a position."
    movement = ""
    if drag and help_item:
        movement = f" {help_item[0]} helped most at {money(help_item[1], signed=True)}, while {drag[0]} was the main drag at {money(drag[1], signed=True)}."
    risk_text = ""
    if risk_line:
        risk_text = " I’m keeping an eye on " + re.sub(r"^Main risks:\s*", "", risk_line).rstrip(".") + "."

    existing = [
        position["ticker"]
        for position in portfolio["positions"]
        if position["instrument"] == "Stock" and position["ticker"] not in bought_tickers
    ]
    held_text = ""
    if existing:
        held_verb = "kept the remaining" if sold_lines else "left the existing"
        held_text = " I " + held_verb + " " + ", ".join(existing[:-1]) + (f" and {existing[-1]}" if len(existing) > 1 else existing[0]) + " positions in place."

    account_state = "is currently at" if portfolio.get("live") and portfolio.get("session", {}).get("isOpen") else "ended at"
    voice = (
        "Today was busy but fairly controlled. "
        + (f"I bought {buy_text}." if buy_text else "I didn’t find anything convincing enough to buy, so I mostly stayed put.")
        + action_text
        + held_text
        + submitted_text
        + f" The account {account_state} {portfolio['equity']}, "
        + f"with the overall return at {portfolio['return'].split('(')[0].strip()}."
        + movement
        + risk_text
    )
    return {
        "date": summary_date,
        "voice": voice,
        "material": material,
        "source": summary_path.relative_to(ROOT).as_posix(),
        "updated": next((line.replace("Updated:", "").strip() for line in text.splitlines() if line.startswith("- Updated:")), ""),
    }


def shortlist_data() -> dict:
    path = ROOT / "data/stage1_shortlist.md"
    text = read_text(path)
    headings = {
        "community": "Community attention — top 10",
        "expert": "Expert attention — top 10",
        "technical": "Technical RRF — top 20",
    }
    categories = {}
    for key, heading in headings.items():
        rows = markdown_tables(section(text, heading))
        categories[key] = rows
    metadata = {}
    for line in text.splitlines():
        match = re.match(r"^-\s+([^:]+):\s*(.+)$", line)
        if match:
            metadata[match.group(1)] = match.group(2)
    return {"categories": categories, "metadata": metadata, "source": "data/stage1_shortlist.md"}


def research_data() -> list[dict]:
    items = []
    for path in sorted((ROOT / "memory/research").glob("**/*.md"), reverse=True):
        match = re.search(r"-(?P<ticker>[A-Z0-9]+)-(?P<kind>fundamental|technical|technical-reconciliation|technical-followup)\.md$", path.name)
        if not match:
            continue
        relative = path.relative_to(ROOT).as_posix()
        content = read_text(path)
        title = next((line.lstrip("# ").strip() for line in content.splitlines() if line.startswith("#")), path.stem)
        items.append(
            {
                "ticker": match.group("ticker"),
                "kind": match.group("kind").replace("-", " "),
                "title": title,
                "date": path.parent.name,
                "path": relative,
                "preview": first_sentence(next((line for line in content.splitlines() if line and not line.startswith("#") and not line.startswith("-")), "Research note")),
            }
        )
    return items


def ghosts_data() -> dict:
    path = ROOT / "memory/ghost-trades/index.md"
    text = read_text(path)
    return {"rows": markdown_tables(text), "source": "memory/ghost-trades/index.md"}


def logs_data() -> list[dict]:
    items = []
    for path in sorted((ROOT / "memory/logs").glob("*.md"), reverse=True):
        if path.name.endswith("-summary.md"):
            continue
        content = read_text(path)
        date = path.stem
        headings = re.findall(r"^##\s+(.+)$", content, flags=re.MULTILINE)
        preview = first_sentence(next((line for line in content.splitlines() if line.startswith("- ")), "No activity recorded."))
        items.append(
            {
                "date": date,
                "label": date_label(date),
                "headings": headings[:4],
                "preview": preview,
                "path": path.relative_to(ROOT).as_posix(),
            }
        )
    return items


def lessons_data() -> dict:
    path = ROOT / "memory/lessons.md"
    text = read_text(path)
    return {"html": simple_markdown_to_html(text), "empty": "No durable lessons yet." in text, "source": "memory/lessons.md"}


def dashboard_payload() -> dict:
    portfolio = live_portfolio_data(portfolio_data())
    summary = summary_data(portfolio)
    shortlist = shortlist_data()
    return {
        "generatedAt": datetime.now().astimezone().isoformat(timespec="minutes"),
        "portfolio": portfolio,
        "summary": summary,
        "shortlist": shortlist,
        "research": research_data(),
        "ghosts": ghosts_data(),
        "lessons": lessons_data(),
        "logs": logs_data(),
    }


def inline_markdown(value: str) -> str:
    escaped = html.escape(value, quote=True)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def simple_markdown_to_html(text: str) -> str:
    """Render the small Markdown subset used by the memory files."""
    output: list[str] = []
    lines = text.splitlines()
    in_list = False
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            if in_list:
                output.append("</ul>")
                in_list = False
            index += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            if in_list:
                output.append("</ul>")
                in_list = False
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
        elif line.startswith("- ") or line.startswith("* "):
            if not in_list:
                output.append("<ul>")
                in_list = True
            output.append(f"<li>{inline_markdown(line[2:])}</li>")
        elif line.startswith("|") and index + 1 < len(lines) and lines[index + 1].startswith("|"):
            rows = []
            headers = split_table_row(line)
            index += 2
            while index < len(lines) and lines[index].startswith("|"):
                rows.append(split_table_row(lines[index]))
                index += 1
            output.append("<table><thead><tr>" + "".join(f"<th>{inline_markdown(c)}</th>" for c in headers) + "</tr></thead><tbody>")
            for row in rows:
                output.append("<tr>" + "".join(f"<td>{inline_markdown(c)}</td>" for c in row) + "</tr>")
            output.append("</tbody></table>")
            continue
        else:
            if in_list:
                output.append("</ul>")
                in_list = False
            output.append(f"<p>{inline_markdown(line)}</p>")
        index += 1
    if in_list:
        output.append("</ul>")
    return "\n".join(output)


def document_page(relative_path: str) -> str:
    safe_path = safe_path_from_relative(relative_path)
    if safe_path is None or safe_path.suffix.lower() not in {".md", ".json"}:
        return ""
    content = read_text(safe_path)
    title = safe_path.stem.replace("-", " ").replace("_", " ").title()
    body = simple_markdown_to_html(content) if safe_path.suffix.lower() == ".md" else f"<pre>{html.escape(content)}</pre>"
    return f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · Machine Earning</title><link rel="stylesheet" href="/style.css"></head>
<body class="document-page"><main class="document-shell"><a class="back-link" href="/">← Back to dashboard</a><p class="eyebrow">Source document</p><h1>{html.escape(title)}</h1><p class="document-path">{html.escape(safe_path.relative_to(ROOT).as_posix())}</p><article class="document-content">{body}</article></main></body></html>"""


def safe_path_from_relative(relative_path: str) -> Path | None:
    try:
        candidate = (ROOT / unquote(relative_path)).resolve()
        candidate.relative_to(ROOT.resolve())
    except (OSError, ValueError):
        return None
    if candidate.name.startswith("."):
        return None
    return candidate


class DashboardHandler(BaseHTTPRequestHandler):
    def send_bytes(self, data: bytes, content_type: str, status: HTTPStatus = HTTPStatus.OK) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/api/dashboard":
            self.send_bytes(json.dumps(dashboard_payload()).encode("utf-8"), "application/json; charset=utf-8")
            return
        if parsed.path == "/document":
            params = parse_qs(parsed.query)
            page = document_page(params.get("path", [""])[0])
            if not page:
                self.send_bytes(b"Document not found", "text/plain; charset=utf-8", HTTPStatus.NOT_FOUND)
            else:
                self.send_bytes(page.encode("utf-8"), "text/html; charset=utf-8")
            return
        relative = "index.html" if parsed.path in {"", "/"} else parsed.path.lstrip("/")
        path = (DASHBOARD_DIR / relative).resolve()
        try:
            path.relative_to(DASHBOARD_DIR.resolve())
        except ValueError:
            self.send_bytes(b"Not found", "text/plain; charset=utf-8", HTTPStatus.NOT_FOUND)
            return
        if not path.is_file():
            self.send_bytes(b"Not found", "text/plain; charset=utf-8", HTTPStatus.NOT_FOUND)
            return
        content_type = {".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".png": "image/png"}.get(path.suffix, "application/octet-stream")
        self.send_bytes(path.read_bytes(), f"{content_type}; charset=utf-8")

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the Alpaca paper-trading dashboard")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), DashboardHandler)
    print(f"Dashboard running at http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
