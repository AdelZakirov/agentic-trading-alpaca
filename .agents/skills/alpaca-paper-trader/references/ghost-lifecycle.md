# Filled ghost-set lifecycle

Owned exclusively by the separate ghost reviewer. Read when a real order first fills, its real path changes, or a ghost checkpoint/completion is due. The trading agent uses ghost-pretrade.md and publishes confirmed execution facts through ghost_queue; it does not read or execute this lifecycle.

Ghost trades never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits. Their risk figures describe only the hypothetical comparison.

## Adopt the definition and activate after a fill

For new packets, adopt the original file listed in handoff.json `ghost_files`; do not create a second file or rename it to the fill date. The trader created it before submission and ownership transferred on finish. Preserve original definitions, evidence and evaluation rules; append reviewer tracking separately. Use the packet snapshot to verify the initial definition when needed. If a source file is missing, restore it from that snapshot. A differing source may contain legitimate earlier reviewer updates: never blindly overwrite it; reconcile by decision ID and original sections.

Keep `WAITING_FOR_FILL` until a real fill is confirmed; then record actual evaluation start under the predeclared rule and mark `ACTIVE`, later `COMPLETE` when the common window ends. A cancelled/rejected order with no fill is `NO_FILL`, not a completed investment outcome. Keep `NOT_SUBMITTED` studies separate from filled-trade statistics; evaluate only if their own observation window and baseline were specified before outcomes.

Legacy packets without a ghost_files manifest may contain pre-submission definitions in the trading log. Reuse existing files by original order/decision ID first; create a missing legacy file only from that contemporaneous evidence, never invented alternatives.
For a partial fill, update the real path with later fills while keeping one ghost set and the original alternatives.

Record:

- real client and broker order IDs, ticker, thesis, decision and fill times, actual fill quantity and price, pre-trade exposure, holding period, invalidation, and size rationale;
- one common evaluation start, end, and checkpoint schedule;
- the contemporaneous market-data source, timestamp, underlying quote, and available option quotes, Greeks, and implied volatility;
- every pre-trade ghost definition, pricing assumption, and missing-data note.

## Track consistently

Use the same chronological window and market observations for the real path and all ghosts. Instrument-specific exits, invalidations, exercises, assignments, or expirations may occur inside it, but never move the common end after observing outcomes.

At each checkpoint and completion, use one market-data timestamp for every scoreable path. Record when meaningful:

- open, closed, expired, or no-trade status;
- current or exit value;
- dollar and percentage P/L;
- capital at risk and maximum loss when knowable;
- material drawdown, time decay, volatility, liquidity, and spread effects;
- triggered exit, invalidation, exercise, assignment, or expiration events.

Use conservative executable marks: bid to exit a long and ask to cover a short, with multi-leg marks composed from executable sides. Use actual real fills and exits when available. For reductions and closes, measure all paths from the same pre-trade exposure and include sale proceeds so retaining versus selling is comparable. Keep comparable assumptions identical and document unavoidable differences.

## Complete the comparison

At the common end, compare decision quality as well as outcome. Identify which alternative did better or worse, why, and which original choice the result tests. Normalize for capital or maximum loss when raw P/L would make different sizes misleading.

Before the decision-quality review or any durable lesson update, read [lessons-learned.md](lessons-learned.md) completely. Keep links in the ghost file and reviewer-state.md; never edit trading logs or ticker files. Upsert its compact assessment using completed-reviews.md before archiving. Update `memory/lessons.md` only when the evidence is generalizable.

## Maintain the routing index

After creating or changing a ghost file, update its row in `memory/ghost-trades/index.md`. Record the real-path state, evaluation end, last completed checkpoint, next checkpoint, any still-pending objective trigger that needs attention between checkpoints, status, and update time. Remove a trigger after it activates or becomes impossible; keep completed-but-unreviewed sets in the working index until assessment is persisted, then move their routing rows to archive-index.md with no next checkpoint. Preserve full files and stable lesson links. Do not copy ghost definitions, quote history, or P/L detail into the index.
