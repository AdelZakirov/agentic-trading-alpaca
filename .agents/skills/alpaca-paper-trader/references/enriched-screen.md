# Local enriched shortlist

Normal Stage 2, before deep-research selection, use the local table instead of the screencheck API:

```bash
python3 -m alpaca_agent.enriched_screen
```

Use a Python environment with the project's screening extra installed (`python -m pip install -e ".[screening]"`). The helper copies existing Stage 1 technical values, recovers missing tickers from ALPACA_DB_PATH (default data/market.sqlite3) using the same Stage1Screener and full eligible universe, and retrieves Yahoo info/calendar/0q estimates and revisions with two workers, 45-second per-ticker deadlines and a one-hour cache. It does not rank, filter or trade. Progress prints the output directory under data/enriched-screen/.

After the helper completes, read data/stage1_enriched.csv plus data/stage1_enriched_fields.json; data/stage1_enriched.json contains equivalent records. These stable files sit beside the shortlist; dated copies remain in data/enriched-screen/. Before reuse, require stage1_enriched_manifest.json shortlist_sha256 to match the current shortlist and use the dated archive to establish freshness. A failed/interrupted build may leave the previous stable table; do not use it as a successful current run. One row per unique shortlist ticker, including names missing from Stage 1. `from` includes every nomination source; `reason_shortlist` preserves original Reason/Reasons cells, or Source details for community, without paraphrase. Array values align with shortlist_details. Original inputs and Yahoo responses are saved alongside the table.

Missing data is not a bearish signal: inspect yahoo_status, technical_status, missing_fields and yahoo_errors. Technical dates and Yahoo prices differ; never substitute this table for current Alpaca execution checks. Yahoo 0q estimates are not guaranteed to correspond to the next earnings announcement. Estimated earnings ranges remain ranges. Analyst targets are not short-horizon return forecasts. Preserve source-specific event context from shortlist_details.

Account for every ticker in the decision ledger. This table is equal first-pass evidence, not proof of equal deep research; full moneyheap research is still required for advanced candidates. Do not call screencheck as an additional mandatory step. Management-only mode skips this table.


## Yahoo network access and recovery

Yahoo/yfinance retrieval is an authorized read-only external request. Use the project environment with screening dependencies (prefer `./.venv/bin/python` when available). If the execution environment restricts external networking, request the tool's permitted external access for Yahoo/yfinance (`sandbox_permissions="require_escalated"` where supported); do not infer that Yahoo is down from a sandbox DNS failure. This authorization does not bypass tool approval enforcement.

After building, inspect aggregated yahoo_status and yahoo_errors in pandas. A written table and exit code zero do not establish successful Yahoo retrieval. If Yahoo requests failed with DNS/network-access errors and the build was not already run with permitted external access, retry the read-only builder once with that access:

`./.venv/bin/python -m alpaca_agent.enriched_screen --cache-ttl 0`

Use the selected project interpreter if its path differs. The zero cache TTL forces a fresh diagnostic retrieval. Recheck the resulting status counts and shortlist hash. If access is rejected or the retry still fails, stop retrying, report the concrete failure and affected/total ticker counts, and label screening as incomplete. Keep missing fields unknown; never describe an untested ticker as inferior because of the outage. Do not claim a Yahoo service outage without evidence beyond the local failure.

## Candidate selection from the table

Read every row before fixing the research funnel. Preserve original shortlist order during the first pass; do not stop at the first attractive ticker. If the table output is truncated, read the remaining rows explicitly.

For each unique ticker, record one disposition in the daily coverage ledger: `research`, `watch`, `reject`, or `insufficient_evidence`. Include the actual field values/dates supporting the decision, the material uncertainty, and either the question for deep research or the condition for reconsideration. Reconcile the ledger's ticker set and count with the table before claiming complete coverage.

Compare combinations of signals rather than a single number: technical structure and volume, event timing, estimate revisions, valuation/quality context, and existing exposure. Explain conflicts. Compare valuation and balance-sheet metrics in sector/instrument context; ETF nulls are not financial weakness. Analyst target upside is not a forecast for the trading horizon. Missing data and source membership must not automatically lower priority.

An unresearched ticker cannot be rejected merely because its catalyst or technical packet is incomplete. Identify a concrete blocker or retain it as insufficient_evidence. Before stopping, inspect the strongest remaining alternatives and explain why their unresolved questions do or do not justify further research. If time or credit budget ends, state that limitation rather than asserting those names were proven inferior.

Table screening is not full company research. Use full moneyheap analysis for advanced candidates, and current Alpaca prices, positions and execution checks before action. No forced source quotas, trades or unsupported numerical attractiveness scores.


## Reading the table efficiently

- Load one table into pandas with `pd.read_csv("data/stage1_enriched.csv")` or `pd.read_json("data/stage1_enriched.json")`; do not dump the raw file or read both copies. Read the field dictionary once.
- Do not treat head() or truncated output as reviewing the full table. Inspect every ticker.
- Select columns appropriate to the question while keeping the complete dataset available for follow-up inspection. Show shared Yahoo failures as one aggregate summary, not repeated yahoo_errors/missing_fields objects in every row. Inspect ticker-specific gaps only when relevant.
- Use explicit row batches when needed to cover all tickers without truncated output; do not repeatedly print the full table in CSV, JSON and wide text forms. For follow-up questions print only newly needed columns/rows.
- Before finishing, compare the decision ledger's ticker set with the table: every unique ticker must have exactly one disposition, with no missing or extra tickers.
