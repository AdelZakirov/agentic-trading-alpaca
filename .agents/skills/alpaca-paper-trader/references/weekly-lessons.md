# Weekly cross-case lessons review

Use lessons-learned.md and completed-reviews.md. You are a reviewer only: no broker mutations, discovery, moneyheap calls or trading-memory edits.

First inspect task status and ghost_queue status. Do not overlap another ghost reviewer or a claimed packet; wait in <=60-second increments up to 120 minutes, then report the blocker. Do not clear a claim from another task. Daily reviewer owns routine checkpoints; do not duplicate them here.

Read current lessons and the compact reviews.json registry, using Python to group records and select columns. Inventory awaiting_backfill is not evidence; report coverage separately. A first weekly run may backfill completed legacy evaluations by reading only those sources. Preserve unknown or unscorable results. If no assessed records changed since the previous weekly review and no backfill remains, stop quietly.

Compare accumulated independent decisions across time and conditions. Look for repeated strengths/weaknesses in timing, sizing, instrument choice, execution and thesis quality; test existing lessons against contrary cases. Distinguish process failures from losing but defensible decisions. Do not pool incomparable horizons, sizes or instruments using raw P&L; normalize only when supported. Group related decisions and disclose dependence, missingness and selection bias (these are selected trade decisions, not an unbiased sample of the market).

Do not scan all historical Markdown. First inspect compact records, then open original files supporting or contradicting a proposed lesson. Report both independent sample count and data coverage. No fixed winning percentage creates high confidence; many searched patterns and a small sample warrant caution. No new lesson is a valid result. Revise, merge or retire existing lessons when justified, retaining case links and contradictions.

Save the input registry snapshot and a concise report under memory/ghost-trades/weekly/YYYY-MM-DD/. Report coverage, candidate patterns, verified supporting/contradicting IDs, lesson changes, limits and next evidence needed. Atomically update memory/lessons.md only after the evidence check. Do not modify daily trading logs, ticker files or portfolio-state.md.

Notify only on meaningful lesson changes, material failures or required user action. Never imply the historical backfill has completed when entries remain awaiting_backfill.
