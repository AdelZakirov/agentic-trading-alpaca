# Alpaca Trading Agent

## What this is

This repository contains an agentic trading workflow for Alpaca paper trading. It
builds a local market-data dataset, screens candidates, and can use
[moneyheap.ai](https://moneyheap.ai)
for fundamental and technical research before supporting risk-managed automated
paper orders with durable trade memory. It never places live trades.

**Stage 0 — Market data.** Collects all Alpaca assets, IEX snapshots, and completed
daily bars, validates them, and maintains a local SQLite dataset for later runs.

**Stage 1 — Candidate discovery.** Screens the market with deterministic signals,
combines the results with community and expert attention, and produces a focused
investigation shortlist.

**Stage 2 — Paper trading.** Researches shortlisted candidates with moneyheap.ai,
applies portfolio and risk checks, chooses BUY, SELL, or HOLD, and tracks real
paper trades alongside simulated ghost alternatives so later cycles can learn
from the comparison.

## Full workflow

```mermaid
flowchart TB
    market["Alpaca market data"] --> stage0["Stage 0<br/>Collect and validate"]
    stage0 --> stage1["Stage 1<br/>Screen candidates"]
    signals["Community and expert signals"] --> stage1
    stage1 --> shortlist["Investigation shortlist"]
    shortlist --> research["moneyheap.ai research"]
    research --> decision["Stage 2<br/>Risk and trade decision"]
    memory[("Trade memory and lessons")] --> decision
    decision --> action{"BUY · SELL · HOLD"}
    action -->|BUY or SELL| alpaca["Alpaca paper account"]
    action -->|BUY or SELL alternatives| ghost["Ghost trades<br/>simulation only"]
    action -->|HOLD| memory
    alpaca --> memory
    ghost --> memory
    memory -. next cycle .-> decision

    classDef source fill:#EEF2FF,stroke:#6366F1,color:#111827;
    classDef step fill:#F5F3FF,stroke:#7C3AED,color:#111827;
    classDef state fill:#ECFDF5,stroke:#059669,color:#111827;
    class market,signals source;
    class stage0,stage1,shortlist,research,decision,ghost step;
    class memory,alpaca state;
```

Stage 0 builds a local whole-market dataset from Alpaca's US-equity asset list,
IEX snapshots, and IEX daily bars. The cache is SQLite so later runs update only
bars newer than each symbol's latest cached bar.

## Setup

Create a local `.env` from `.env.example`; `.env` and other environment-specific
files are ignored by Git. Set the Alpaca credentials in your local file before
running the agent.

The implementation uses only the Python standard library:

```bash
python3 -m alpaca_agent
```

Useful configuration variables are in `.env.example`. In particular,
`ALPACA_BATCH_SIZE` defaults to 100 and `ALPACA_HISTORY_DAYS` defaults to 120,
which provides a buffer above Stage 1's 100 completed daily bars.

The command writes:

- `data/market.sqlite3`: `assets`, `snapshots`, `bars`, `fetch_errors`, and metadata tables.
- `data/stage0_manifest.json`: counts, feed, table names, and errors from the run.

Run with temporary paths when testing:

```bash
python3 -m alpaca_agent --db-path /tmp/alpaca-market.sqlite3 \
  --manifest-path /tmp/alpaca-stage0.json
```

For a bounded bootstrap or smoke test, limit the universe:

```bash
python3 -m alpaca_agent --max-symbols 100
```

Run the dependency-free test suite with:

```bash
python3 -m unittest discover -v
```

## Local data interface for Stage 1

Screening code should use `MarketStore.load_dataset()` and not the Alpaca client:

```python
from pathlib import Path

from alpaca_agent import MarketStore

with MarketStore(Path("data/market.sqlite3")) as store:
    dataset = store.load_dataset()
    bars_for_aapl = dataset.history.get("AAPL", ())
    current_aapl = dataset.snapshots.get("AAPL")
```

`dataset.assets`, `dataset.snapshots`, and `dataset.history` are the stable local
representations that Stage 1 can consume.

## Stage 1 deterministic screen

Stage 1 uses only completed daily IEX bars and includes a separate ApeWisdom
community-interest step. It fetches the top 50 results from both the
`all-stocks` and `options` feeds, then deduplicates them in the candidate list.

Run the historical-safe screen with:

```bash
python3 -m alpaca_agent.stage1 \
  --db-path data/market.sqlite3 \
  --as-of-date 2026-08-24
```

The program writes machine-readable JSON to `data/stage1_screen.json` by
default and logs only a compact lane summary to stderr. Use `--output` to
change the path, `--no-community` to skip ApeWisdom, or `--print-json` to also
print the JSON to stdout.
The Python API is:

```python
from datetime import date
from pathlib import Path

from alpaca_agent.community import ApeWisdomClient
from alpaca_agent import MarketStore, Stage1Screener
from alpaca_agent.stage1 import DEFAULT_SCREENING_CONFIG

with MarketStore(Path("data/market.sqlite3")) as store:
    config = DEFAULT_SCREENING_CONFIG
    result = Stage1Screener(
        store.load_dataset(),
        config,
        ApeWisdomClient(config.community.base_url, config.community.timeout_seconds),
    ).screen(date(2026, 8, 24))
```

## Stage 1 investigation shortlist

Build a Markdown shortlist for downstream investigation agents:

```bash
python3 -m alpaca_agent.shortlist
```

The command reads `data/stage1_screen.json` and `data/stage1_experts.json` and
writes `data/stage1_shortlist.md`. It selects the top 10 unique community
tickers by their best rank across community feeds, the first 10 expert
candidates in expert-source order, and the top 20 technical candidates by
Reciprocal Rank Fusion with `k=10`. Technical category ranks use descending
category score with ticker order as the tie-breaker. Scoreless categories such
as `exploration` and the community category are excluded from technical RRF.

Input and output paths, selection sizes, and RRF `k` can be changed with the
`--screen`, `--experts`, `--output`, `--community-top-k`, `--expert-top-k`,
`--rrf-top-k`, and `--rrf-k` options.

Results are multi-label and reproducible for identical bars, configuration, and
screening date. The exploration lane uses the date as its deterministic seed.
Community rankings are a current ApeWisdom snapshot; use `--no-community` for
market-only historical runs or inject a fixed client response for replay.

## Stage 2 autonomous paper trader

The project skill at `.agents/skills/alpaca-paper-trader` runs Stage 2 from the
latest `data/stage1_shortlist.md`. It may research tickers through moneyheap,
makes separate stock and option decisions, applies the risk policy, and submits
valid Alpaca paper orders without human approval.

Moneyheap persistence is handled by `python3 -m alpaca_agent.moneyheap`: pass one
request JSON object on stdin. It makes the request once, saves the exact response
to a sibling JSON artifact, and writes one rendered Markdown artifact under
`memory/research/`. A local write failure is retried locally and never recovered
by issuing another successful research request.

Each filled trade also starts a small set of realistic ghost alternatives that
are evaluated over the same market-data window without ever reaching Alpaca or
affecting the portfolio. Completed real-versus-ghost comparisons can update the
short, durable principles in `memory/lessons.md`; those principles inform later
decisions as learned priors rather than hard rules.

Invoke it as `$alpaca-paper-trader`. Its durable state is stored in `memory/`.
The skill contains instructions and references only; it adds no Stage 2 script.

## Daily autonomous pipeline

`alpaca_agent.daily_shortlist` runs Stage 0, Stage 1, and the shortlist builder.
Codex owns the weekday schedule: a Luna automation invokes expert-attention
discovery and then runs this deterministic pipeline at 16:00 Europe/Amsterdam.
It runs only when Alpaca reports that the market is open, New York time is at
least 10:00, and that market date has not already completed. A separate Sol
automation runs Stage 2 at 16:30 only after verifying the current market day's
completion marker and fresh Stage 1 artifacts. A management-only pre-close
automation starts at 20:30 Europe/Amsterdam and uses the Alpaca clock to enter
the 15:15–15:50 New York window. It may hold, reduce, close, cancel, or replace
existing exposure and orders, but it cannot open or enlarge a position.

Check whether a run is due without changing any data:

```bash
python3 -m alpaca_agent.daily_shortlist --check-only
```

Run it manually with:

```bash
python3 -m alpaca_agent.daily_shortlist --force
```

The completion marker is `data/daily_shortlist_state.json`. The legacy macOS
LaunchAgent in `automation/` is retained only as a reference and must remain
unloaded while the Codex automations are active.

## Data-quality and feed behavior

- Assets are filtered to `active`, `tradable`, `us_equity` records from `/v2/assets`.
- Snapshots and bars are requested in configurable batches, with `feed=iex`.
- HTTP 429, 5xx, timeout, and network failures are retried with exponential backoff and jitter.
- A failed batch is recorded and does not abort later batches.
- Missing symbols and invalid bars are recorded in `fetch_errors`.
- Bars require positive close, `high >= low`, OHLC values inside the high/low range,
  non-negative volume, and a parseable date.
- Historical requests end at the previous New York calendar day so Stage 1 does
  not accidentally use an in-progress daily candle.
- IEX volumes are only IEX volumes; they must not be interpreted as consolidated
  US-market volume.
