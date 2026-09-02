# SLB — OPEN

## Current Alpaca state

- Instrument: common stock
- Side: long
- Quantity: 80 shares
- Average entry: $58.242124
- Cost basis: $4,659.36992
- Latest reconciled stock price: $58.01
- Latest stock market value: $4,640.80
- Latest stock unrealized P/L: -$18.57 (-0.399%)
- Option position: long 1 `SLB260911C00058000` at $1.25 and short 1 `SLB260911C00062000` at $0.17; atomic net fill $1.08 on broker order `204e01a8-2c35-47f0-a042-3c88581e2364`
- Latest option position marks: long market value $126, short market value -$28; Alpaca leg P/L net -$10. Conservative executable checkpoint spread mark $0.95 and P/L -$13.
- Open orders: none
- Reconciled: 2026-09-02 18:38 Europe/Amsterdam

## Current plan

- Thesis: high-volume bullish breakout sponsorship held through a pullback into the $57.90-$58.70 entry band; the one-week setup seeks a retest of the recent high.
- Confidence: moderate.
- Holding period: tactical through 2026-09-04 unless invalidated earlier.
- Targets: $60.20-$60.50 first trim; $61.80-$62.50 runner.
- Invalidation: break or close below $56.90, with the $57.30-$57.42 breakout shelf as the key support test.
- Size rationale: approximately $4,665 notional, about 4.7% of equity at entry; planned stop risk approximately $107 before slippage while retaining over 90% cash.
- Stock decision: BUY 80 shares executed and filled 80/80 at $58.242124.
- Option decision: HOLD one filled Sep. 11 $58/$62 call debit spread. Manage tactically through the 2026-09-04 review and avoid expiration/assignment without a fresh decision.
- Review triggers: $57.30-$57.42 support, $56.90 invalidation, $60.20-$60.50, $61.80-$62.50, commodity/EIA news, and the 2026-09-04 close.

## Relevant evidence

- Shortlist: [`../../data/stage1_shortlist.md`](../../data/stage1_shortlist.md)
- Technical research: [`../research/2026-09-01/165312-SLB-technical.md`](../research/2026-09-01/165312-SLB-technical.md)
- Active ghost set: [`../ghost-trades/2026-09-01/alpaca-stage2-20260901-SLB-buy.md`](../ghost-trades/2026-09-01/alpaca-stage2-20260901-SLB-buy.md)
- Daily log: [`../logs/2026-09-01.md`](../logs/2026-09-01.md)

## History

### 2026-09-01

- Initiated 80-share long position through client order `alpaca-stage2-20260901-SLB-buy`.
- Broker order `db61b37c-6fcb-4dbc-a39f-672bbc8be16c` filled 80 shares at average $58.242124 at `2026-09-01T15:02:22.008309992Z`.
- No option order submitted.
- Later submitted atomic Sep. 11 $58/$62 call-spread order `9a13c4ca-3604-4c90-bd47-8d8e4f951e2f` at $1.05 debit under client ID `alpaca-stage2-20260901-SLB-option-buy`; it filled 0/1 and was replaced once.
- Replacement order `204e01a8-2c35-47f0-a042-3c88581e2364` is `new`, filled 0/1, at a $1.08 debit as of 19:56 Europe/Amsterdam. It is not yet a position, and no ghost set exists until a fill is confirmed.

### 2026-09-02

- Alpaca confirmed replacement order `204e01a8-2c35-47f0-a042-3c88581e2364` filled 1/1 at a $1.08 net debit at `2026-09-01T18:02:12.483149Z`; the two option legs are now a live spread position.
- Stock HOLD and option HOLD. SLB is $58.055, above $56.90 invalidation and below the $60.20-$60.50 first target. No open order.
- Created [`../ghost-trades/2026-09-01/alpaca-stage2-20260901-SLB-option-buy.md`](../ghost-trades/2026-09-01/alpaca-stage2-20260901-SLB-option-buy.md) for the late-confirmed spread fill.
