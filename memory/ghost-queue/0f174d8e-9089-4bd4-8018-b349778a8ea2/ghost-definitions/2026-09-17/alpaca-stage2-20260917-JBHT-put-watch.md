# JBHT bearish watch alternatives

## Identity

- decision_id: `alpaca-stage2-20260917-JBHT-put-watch`
- creator_run_id: `0f174d8e-9089-4bd4-8018-b349778a8ea2`
- decision_at: `2026-09-17T16:52:06+02:00`
- ticker: `JBHT`
- status: `NOT_SUBMITTED`
- client_order_id: null
- broker_order_id: null

## Original decision

- Thesis: management warned that Q3 earnings may decline 5%-10% sequentially, creating a high-volume bearish break while a roughly 23.7x forward multiple still leaves estimate-cut risk. The stock has not yet confirmed continuation with a daily close below $235.
- Chosen action: no stock or option order now; watch for a sustained daily close below $235 before considering one 2026-10-16 240/220 put debit spread.
- Pre-trade exposure: zero JBHT stock or options and no order.
- Size rationale: the indicative spread would risk about $841, roughly 0.83% of current equity, but opening before confirmation would expose the account to an oversold rebound and IV normalization.
- Invalidation: daily close above $248 invalidates the immediate bearish setup.
- Holding period: observation through 2026-10-16 expiration; downside reviews at $220 and $200.

## Evaluation rules

- Common start: 2026-09-17 close for the no-trade decision; triggered alternatives start at the next indicative quote after a qualifying close.
- Checkpoints: next close, five trading days, ten trading days, and 2026-10-16.
- End rule: close option alternatives at conservative indicative executable sides at target, invalidation, or expiry.
- Exit handling: bearish alternatives exit on a daily close above $248; take-profit review at $220 and $200 underlying.

## Initial evidence

- Alpaca IEX underlying quote: $237.87/$238.71 at 2026-09-17T14:52:06Z.
- moneyheap fundamental research: `memory/research/2026-09-17/165119-JBHT-fundamental.md`.
- Indicative 2026-10-16 puts at 2026-09-17T14:51Z: 240 $10.78/$11.93, 230 $6.25/$7.88, 220 $3.52/$4.92, 210 $1.87/$2.23. Quotes are indicative, not firm OPRA prices.
- Missing data: no firm OPRA feed; no daily-close confirmation below $235 yet.

## Alternatives

### A. Immediate long 240 put
- question: Does uncapped downside outperform waiting for confirmation?
- rationale: preserves gains below $220 but pays high IV and theta.
- instrument: JBHT 2026-10-16 240 put; side: buy; quantity: 1.
- entry rule / simulated price: immediate indicative ask $11.93.
- maximum loss: $1,193; expiry breakeven $228.07.
- exit handling: close at target, invalidation, or expiry using the indicative bid.
- pricing assumptions: conservative indicative ask/bid; not a guaranteed fill.

### B. Immediate 240/220 put spread
- question: Does defined-risk bearish exposure outperform no trade before confirmation?
- rationale: caps IV/theta cost while matching the first $218-$220 downside target.
- instrument: long 240 put, short 220 put, 2026-10-16; quantity: 1 spread.
- entry rule / simulated price: conservative debit $11.93 - $3.52 = $8.41.
- maximum loss: $841; maximum profit $1,159; expiry breakeven $231.59.
- exit handling: common rules; assignment/exercise handled by closing before expiry when feasible.
- pricing assumptions: indicative executable sides, not firm quotes.

### C. Confirmed 240/220 put spread
- question: Is paying after a daily close below $235 worth the lower false-break risk?
- rationale: require the breakdown to persist before adding bearish exposure.
- instrument: same 2026-10-16 240/220 put spread; quantity: 1.
- entry rule / simulated price: next-session conservative indicative debit after a qualifying close below $235.
- maximum loss: unknown until trigger; must remain below 1% of then-current equity.
- exit handling: common rules.
- pricing assumptions: `UNSCORABLE` until trigger and fresh quotes exist.

### D. No trade
- question: Does avoiding a post-gap option entry outperform bearish structures?
- rationale: the stock may mean-revert above $248 and option IV may contract.
- instrument: no trade; side: none; quantity: 0.
- entry rule / simulated price: none; zero capital and zero P/L.
- maximum loss: $0.
- exit handling: observe through the common window.
- pricing assumptions: none.

## Execution

- submitted_at: null
- broker_order_id: null
- status: `NOT_SUBMITTED`
- filled_qty: null
- filled_avg_price: null

## Reviewer updates

