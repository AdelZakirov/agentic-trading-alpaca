# Filled ghost-set lifecycle

Read this reference when a real order first fills, when a partially filled real order changes, or when an active ghost checkpoint or completion is due.

Ghost trades never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits. Their risk figures describe only the hypothetical comparison.

## Create the set after a fill

Create one file per real client order at `memory/ghost-trades/YYYY-MM-DD/{REAL_CLIENT_ORDER_ID}.md`, where the date is the real trade's first fill date. Copy the alternatives and contemporaneous observations recorded before submission; never redefine them with hindsight. Mark the set `ACTIVE` until its common evaluation period ends, then `COMPLETE`.

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

Before the decision-quality review or any durable lesson update, read [lessons-learned.md](lessons-learned.md) completely. Link the completed set from the ticker file and daily log. Update `memory/lessons.md` only when the evidence is generalizable.

## Maintain the routing index

After creating or changing a ghost file, update its row in `memory/ghost-trades/index.md`. Record the real-path state, evaluation end, last completed checkpoint, next checkpoint, any still-pending objective trigger that needs attention between checkpoints, status, and update time. Remove a trigger after it activates or becomes impossible; mark `COMPLETE` sets with no next checkpoint. Do not copy ghost definitions, quote history, or P/L detail into the index.
