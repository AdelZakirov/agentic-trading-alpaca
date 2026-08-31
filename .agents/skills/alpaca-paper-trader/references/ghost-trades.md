# Ghost trades

Ghost trades are counterfactual records attached to a real filled trade, including an entry, add, reduction, close, or roll. They are never submitted to Alpaca and never affect the portfolio.

## Choose the alternatives

Before submitting a real order, define two to four realistic alternatives that were genuinely considered. Record the definitions and quote snapshot in the daily log before calling the order endpoint. If the order is still unfilled at final reconciliation, leave that record tied to its client order ID. If it fills later, copy those original definitions into its ghost file; if it never fills, do not create a ghost set. Do not invent alternatives after seeing later prices.

Each ghost must answer one specific question about the real decision by changing a meaningful choice, such as:

- stock instead of options, or options instead of stock;
- a different option structure, strike, or expiration;
- a different position size;
- different entry timing when the alternative has an objective trigger;
- no trade.

Prefer changing one decision at a time so the comparison remains interpretable. Do not add random variants or several nearly identical contracts. Include no trade when the main question concerns whether exposure should have been added at all.

## Record the set

Create one file per real client order using the path in `memory-contract.md` when its first fill is confirmed. Mark it `ACTIVE` until the common evaluation period is complete, then `COMPLETE`. For a partially filled order, update the real path with later fills while keeping one ghost set and the original alternatives.

Record:

- the real client order ID, broker order ID, ticker, thesis, decision time, fill time, actual fill quantity and price, pre-trade position or exposure, holding period, invalidation, and size rationale;
- one common evaluation start, end, and checkpoint schedule for the real trade and every ghost;
- the contemporaneous market-data source, timestamp, underlying quote, and each relevant option quote, Greek, and implied-volatility value that is available;
- for each ghost: a stable label, the question it tests, rationale, instrument or no-trade choice, side, quantity or notional, option structure and contracts when applicable, entry rule, simulated entry price, maximum loss when knowable, and exit or expiration handling;
- pricing assumptions and missing data.

Use data that was observable at the real decision. Price a hypothetical buy at the contemporaneous ask and a hypothetical sale at the bid unless a more realistic conservative fill is documented. Price multi-leg structures from the executable side of each leg. A no-trade ghost starts and remains at zero P&L and zero capital at risk.

If reliable contemporaneous data needed to price an alternative is unavailable, keep the question but mark that ghost `UNSCORABLE`; do not manufacture a price.

## Track consistently

All paths use the same chronological evaluation window and market observations. Instrument-specific exits, invalidations, exercises, assignments, or expirations may occur inside that window, but do not move the common end date after observing outcomes.

At each scheduled checkpoint and at completion, use one market-data timestamp for the real trade and all scoreable ghosts. Record, when meaningful:

- open, closed, expired, or no-trade status;
- current or exit value;
- dollar and percentage P&L;
- capital at risk and maximum loss when knowable;
- material drawdown, time decay, volatility, liquidity, and spread effects;
- triggered exit, invalidation, exercise, assignment, or expiration events.

Use conservative executable marks: bid to exit a long position and ask to cover a short position, with multi-leg marks composed from the executable side of each leg. Use the actual real fill and actual real exit when available. For reductions and closes, measure every path from the same pre-trade exposure and include the value of sale proceeds so retaining versus selling is comparable. Keep assumptions identical across alternatives where they are comparable, and document unavoidable differences.

Do not place broker orders, reserve cash, change portfolio statistics, or alter risk posture because of a ghost. The risk figures in the ghost file describe only the hypothetical comparison.

## Complete the comparison

At the common evaluation end, compare the real trade and ghosts on decision quality as well as outcome. Identify which alternative did better or worse, why, and which original choice the result tests. Normalize for capital or maximum loss where raw P&L would otherwise make different sizes misleading.

Review the dimensions in `lessons-learned.md`. Link the completed set from the ticker file and daily log, then update durable lessons only when the evidence is generalizable.
