# Ghost pre-trade: ESI pullback long

## Identity

- decision_id: `alpaca-stage2-20260914-ESI-buy`
- creator_run_id: `f69753d6-76b4-4255-b370-bdb39af6070f`
- decision_at: `2026-09-14T12:31:31-04:00` (America/New_York)
- ticker: `ESI`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260914-ESI-buy`
- broker_order_id: null

## Original decision

ESI has a fresh Goldman Sachs Buy reinstatement at $44, strong reported growth and a 15.3x forward P/E, while the broker quote is $32.14 bid / $32.16 ask after a 20-day pullback. The trade is a tactical oversold rebound, not a long-term endorsement: leverage and the break below the 200-day average require a bounded entry and a daily-close invalidation. Buy 75 shares at the current ask to target a move back toward $34.50-$37.00 while keeping portfolio risk small and avoiding a second simultaneous electronics-distributor entry.

- chosen action: submit a day limit buy for 75 shares at $32.16
- pre-trade exposure: no ESI position or open ESI order
- size rationale: approximately $2,412 notional; about $132 risk to the $30.40 daily-close invalidation before slippage, with sector overlap to existing MU recognized
- invalidation: daily close below $30.40
- targets: $34.50 first, $36.00-$37.00 second, $42.00-$44.00 only after a new review
- holding period: 5-10 trading days, or earlier on invalidation or target review

## Evaluation rules

- common window: from confirmed fill through 10 trading days, or until the daily-close invalidation
- checkpoints: first regular-session close; daily close below $30.40; touch of $34.50; touch of $36.00-$37.00; end of the tenth trading day
- end rule: compare realized or marked P/L against alternatives using the same broker evidence; do not invent fills
- exit handling: no unplanned intraday stop; preserve the daily-close time basis unless a new material thesis change is documented

## Initial evidence

- Alpaca clock: market open, `2026-09-14T12:31:31-04:00`
- Alpaca account: equity $101,528.46; cash $87,183.93; buying power $369,272.39
- ESI position/order check: no position and no open order
- delayed-SIP quote: bid $32.14, ask $32.16, bid size 200, ask size 100, quote time `2026-09-14T16:16:39.757625747Z`
- research: `memory/research/2026-09-14/182522-ESI-fundamental.md`
- local evidence: 2026-09-11 technical bar; 20-day return -11.97%, relative volume 1.49x; expert source recorded Goldman Buy / $44 on Sep. 11
- missing data: no ESI option structure was selected; stock liquidity and defined daily-close risk were the chosen instrument basis

## Alternatives

### A — Chosen 75-share stock entry

- label: `chosen-75-share-stock`
- question tested: does a bounded stock entry capture the oversold rebound without taking option premium/decay risk?
- instrument: ESI stock, buy 75 shares
- entry rule: day limit at $32.16 or better
- simulated entry price: $32.16 ask
- maximum loss: approximately $132 to the $30.40 invalidation before slippage; no hard broker stop submitted
- exit / handling: daily-close invalidation and target checkpoints above
- pricing assumptions: ask-side hypothetical; only broker `filled` status establishes execution

### B — Smaller stock entry

- label: `smaller-40-share-stock`
- question tested: does reducing size improve downside control while preserving the same thesis?
- instrument: ESI stock, buy 40 shares
- entry rule: same $32.16-or-better limit
- simulated entry price: $32.16 ask
- maximum loss: approximately $70 to the invalidation before slippage
- exit / handling: same daily-close rules and targets
- pricing assumptions: ask-side hypothetical; no invented fill

### C — Correlated AVT alternative

- label: `watch-AVT-entry`
- question tested: is the stronger value/revision setup in AVT preferable to ESI's oversold reversal?
- instrument: AVT stock, buy 20 shares only in the researched $93.00-$94.50 range
- entry rule: conditional entry after stabilization; no ESI capital reserved
- simulated entry price: $94.15 ask observed in the same session
- maximum loss: approximately $105 to the $88.90 invalidation before slippage
- exit / handling: 5-10 trading-day review; no order submitted
- pricing assumptions: ask-side hypothetical; status `NOT_SUBMITTED`

### D — No trade

- label: `no-trade`
- question tested: does leverage and the break below longer moving averages outweigh the analyst catalyst?
- instrument: no trade; retain cash
- entry rule: no order and zero new capital at risk
- simulated entry price: null
- maximum loss: zero incremental loss
- exit / handling: reconsider only on a daily close back above the moving-average band or a new catalyst
- pricing assumptions: starts at zero P/L and zero capital at risk

## Execution

- confirmed fill: null
- broker_order_id: `3b2caccb-8451-473f-ab70-f955bbccd657`
- broker status: `new` (unfilled at final reconciliation)
- submitted_at: `2026-09-14T16:32:36.090440174Z`
- final observed quote: $32.14 bid / $32.17 ask at `2026-09-14T16:18:15.530814993Z`; limit remained $32.16

## Reviewer updates

Reserved for the ghost reviewer.
