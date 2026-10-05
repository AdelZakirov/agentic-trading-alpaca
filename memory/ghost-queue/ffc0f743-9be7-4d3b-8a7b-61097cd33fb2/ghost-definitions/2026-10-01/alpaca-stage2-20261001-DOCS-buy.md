# DOCS entry alternatives — original definition

## Identity

- decision_id: `alpaca-stage2-20261001-DOCS-buy`
- creator_run_id: `ffc0f743-9be7-4d3b-8a7b-61097cd33fb2`
- decision_at: `2026-10-01T20:31:58.809642+02:00`
- ticker: `DOCS`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20261001-DOCS-buy`
- broker_order_id: null

## Original decision

Buy 150 DOCS cash shares with a DAY limit no higher than $28.38. Thesis: September 30 completed IEX bar closed $28.34 after a break above the $27.30 base on 367,236 IEX shares, and current October 1 IEX book at 14:30:48 ET was $28.33 bid/$28.36 ask, 400/200 displayed. The stock is near the breakout rather than an extended chase. Doximity's primary fiscal Q1 revenue grew 7% and fiscal Q2 revenue guide is $170M–$171M, but quarterly free cash flow fell 34%; confidence moderate, not a fundamental acceleration claim. Size uses about $4,254 at the observed ask and preserves cash funding. A daily close below $26.80 invalidates the breakout and triggers next-session bounded exit review; at $28.36, nominal review-price loss is $234 and an illustrative 20% gap is $851; full capital $4,254 remains at risk. Holding plan: 1–4 weeks, review October 2 and October 8, first observed executable target $31.50–$32.00, exit or explicit renewal by October 29 before estimated early-November earnings. Existing healthcare exposure makes the smaller, nonbinary software position preferable to the UTHR/LQDA legal-event chase.

## Evaluation rules

The real path and executable ghost buys start only after a broker-confirmed real fill; no fill means no fill-anchored P/L. Observe at October 2, October 8 and October 15 regular-session closes, and finish by October 29 at 15:45 ET unless a declared daily-close invalidation or executable $31.50 target is seen sooner. On a completed daily close below $26.80, compare next regular-session bids for an exit. On an observed bid at or above $31.50, compare selling half and reassessing the runner. Use the same price/time basis on every path. No-trade remains $0 P/L and $0 capital at risk. If the real order is not filled, the unsubmitted observation window is October 1 decision time through October 15 regular close using the quoted asks below only as initial hypotheses; do not manufacture fills.

## Initial evidence

- Alpaca paper IEX DOCS 2026-10-01T18:30:48.109828485Z: bid $28.33 size 400, ask $28.36 size 200. A prior 14:30:20 ET IEX quote was $28.35/$28.36, 300/100. Delayed SIP at 14:15:21 ET was $28.26/$28.29 and is not a current execution quote.
- Alpaca paper IEX BP 2026-10-01T18:30:50.33389532Z: bid $44.51 size 200, ask $44.52 size 1100.
- September 30 completed DOCS IEX close $28.34; October 1 bar is incomplete. [Doximity primary release](https://investors.doximity.com/news/news-details/2026/Doximity-Announces-Fiscal-2027-First-Quarter-Financial-Results/default.aspx), [fundamental research](../../research/2026-10-01/200609-DOCS-fundamental.md), [technical research](../../research/2026-10-01/200641-DOCS-technical.md), [coverage](../../research/2026-10-01/shortlist-coverage.csv).

## Alternatives

1. **No new trade.** Question: does holding current cash outperform adding the DOCS breakout risk? Instrument: none; side/quantity: none. Entry rule: remain in cash at the decision time. Simulated entry: $0. Maximum loss: $0; capital at risk: $0. Exit/end: same evaluation window. Pricing assumption: zero return on idle cash for this comparison; actual account cash yield is unknown. Missing data: future deposit interest is not modeled.
2. **Smaller DOCS stock entry.** Question: does halving new idiosyncratic risk improve the outcome? Instrument: DOCS stock, buy 75 shares. Entry rule: contemporaneous buy at IEX ask $28.36 if the real decision executes, otherwise no simulated fill. Simulated ask cost $2,127; full stock capital at risk $2,127; nominal loss to $26.80 review price $117, illustrative 20% gap $425.40. Same invalidation, target, review dates and exit handling as real path. Missing data: later fill quality and spreads, to be observed rather than assumed.
3. **BP instead of DOCS.** Question: does the fresh energy upgrade with lower software correlation outperform the technical breakout? Instrument: BP stock, buy 95 shares. Entry rule: contemporaneous IEX ask $44.52; simulated ask cost $4,229.40. Full capital at risk $4,229.40; daily close below $42.50 triggers next-session bid exit review, and first observed bid $48.00 triggers profit review by October 29. The $42.50 review price implies about $191.90 nominal loss; a 20% gap implies about $845.88. Exposed to Brent/refining and dividend-adjustment risk. Missing data: future crude and dividend-adjusted path; no later price invented. [BP research](../../research/2026-10-01/200434-BP-fundamental.md).

## Execution

No broker submission or fill is asserted at definition time. Broker IDs, statuses, and confirmed fill details will be appended before handoff if observed.

## Reviewer updates

Reserved for the separate ghost reviewer after immutable handoff.

## Execution facts before handoff

- Alpaca paper broker order `36e082c8-885a-45f5-ae64-8038912fdd92` was submitted at 2026-10-01T18:32:59.862305897Z as a 150-share DAY limit BUY at $28.36.
- The broker status is `filled`: 150 shares at $28.34, filled at 2026-10-01T18:33:00.377189775Z. Matching FILL activity `20261001143300377::41df91f8-9ae5-4184-a38f-eb7a22ae0af5` is tied to the same order and quantity.
- Immediate post-fill reconciliation: DOCS long 150, average entry $28.34, available 150; zero open orders; broker cash $53,040.97 and equity $100,665.67. Cash debit $4,251 equals 150 × $28.34. The initial definition and comparison rules above were not changed.
