# Ghost alternatives: CHYM starter

## Identity

- decision_id: `alpaca-stage2-20260916-CHYM-buy`
- creator_run_id: `6f8ea019-ab92-447e-b483-1b27102e3458`
- decision_at: `2026-09-16T17:00:52+02:00`
- ticker: `CHYM`
- status: `COMPLETE`
- client_order_id: `alpaca-stage2-20260916-CHYM-buy`
- broker_order_id: `4115f7d1-12d2-4c8c-ae3c-6ed621580651`

## Original decision

- Thesis: Chime combines 26.8% revenue growth, positive free cash flow, net cash, a fresh Buy upgrade tied to the Stride Bank acquisition, and a constructive low-volume pullback that is holding the rising 20-day EMA. A small starter captures event upside while preserving capacity for post-Fed confirmation.
- Chosen action: buy 100 CHYM shares with a $32.47 limit, $35.45 take-profit, and $30.95 catastrophic stop in a GTC bracket.
- Pre-trade exposure: zero CHYM shares or orders. Existing fintech exposure is 15 HOOD shares.
- Size rationale: 100 shares are about $3,247 or 3.2% of equity. Risk to the $30.95 stop is about $152; 15% gap stress is about $487. This keeps estimated aggregate event stress, including the pending META bracket, below the temporary approximately $6,000 guardrail. A 200-share starter would exceed it.
- Invalidation and holding period: daily close below $31.40 triggers thesis review; $30.95 is the wider catastrophic broker stop. Initial target $35.45. Holding period 1-4 weeks with review after the Federal Reserve reaction, on any bracket fill, and no later than 2026-10-14 without renewal.

## Evaluation rules

- Common observation start: confirmed fill timestamp of the chosen order. If unfilled, use the first executable CHYM quote after `2026-09-16T15:15:00-04:00`.
- Checkpoints: September 16 close, September 17 close, five trading sessions, and October 14 close.
- End rule: first target, stop, documented invalidation exit, or October 14 close, whichever comes first.
- Exit handling: use confirmed broker fills for the chosen order. Ghost stock buys use contemporaneous ask; sales use contemporaneous bid. A no-trade ghost remains zero P/L and zero capital at risk.

## Initial evidence

- Alpaca IEX quote at `2026-09-16T15:00:51.828253422Z`: bid $32.46 x500, ask $32.47 x500; spread $0.01.
- Asset status: active and tradable on NASDAQ.
- moneyheap fundamental research: strong rating; 26.8% revenue growth, $437.65M FCF, net cash, Stride Bank acquisition catalyst, tactical entry $32.40-$32.80, daily-close invalidation below $30.00.
- moneyheap technical research: bullish high-base consolidation; 20-day EMA $32.45, ADX 46.51, contracting pullback volume, starter zone $32.40-$32.70, daily-close invalidation $31.40, targets $34.50-$35.00 and $35.45-$37.00.
- Data limitation: quote is IEX rather than consolidated SIP. Spread and displayed size are executable evidence for bounded paper-order analysis, not a fill guarantee.

## Alternatives

### A. No pre-Fed trade

- Question tested: did avoiding all event exposure outperform the small starter?
- Instrument: no trade.
- Entry rule and simulated price: none; P/L starts at $0 with $0 capital at risk.
- Maximum loss: $0.
- Exit: observation ends October 14 close.
- Rationale: most researched candidates require post-Fed confirmation, and even CHYM can whipsaw around the announcement.

### B. Buy 200 shares now

- Question tested: did the stronger fundamental/technical alignment justify twice the starter size?
- Instrument: CHYM stock, buy 200 shares.
- Entry rule and simulated price: contemporaneous ask $32.47; simulated notional $6,494.
- Maximum planned loss: about $304 to the $30.95 catastrophic stop; 15% gap stress about $974.
- Exit: same $35.45 target, $31.40 close review, $30.95 catastrophic stop, and October 14 end rule.
- Rationale for rejection: combined event stress would exceed the temporary portfolio guardrail once pending META and existing growth exposure are counted.

### C. Wait for post-Fed confirmation, then buy 100 shares

- Question tested: was confirmation worth paying a potentially higher entry price?
- Instrument: CHYM stock, buy 100 shares.
- Entry rule: after the Federal Reserve announcement, buy at the first executable ask no higher than $33.50 if $32.40 support holds, or after a daily close above $33.50. Do not trigger after a daily close below $31.40.
- Simulated entry price: determined by the objective trigger; currently `UNSCORABLE` because the event has not occurred.
- Maximum planned loss: entry minus $30.95, multiplied by 100 shares; unknown until trigger.
- Exit: $35.45 first target, then $36.50 stretch target; October 14 end rule.
- Missing data: post-event quote, volume, and closing confirmation.

## Execution

- submitted_at: `2026-09-16T15:01:59.118761549Z`
- broker_order_id: `4115f7d1-12d2-4c8c-ae3c-6ed621580651`
- status: `filled`
- filled_at: `2026-09-16T15:02:11.417917936Z`
- filled_qty: `100`
- filled_avg_price: `$32.47`
- take_profit_leg: `c5ec5afc-5629-4814-b966-428ae113bcee`, 100 shares at $35.45 GTC, status `new`
- stop_leg: `dd12a114-1c25-46b7-bbe3-1181ac2b246f`, 100 shares stop $30.95 GTC, status `held`
- reconciliation: broker position long 100 CHYM at $32.47; quantity available 0 because bracket exits reserve the shares.

## Reviewer updates

### Reviewer activation and broker reconciliation

- Reviewer status: `COMPLETE`; evaluation started at the confirmed CHYM fill `2026-09-16T15:02:11.417917936Z` and ended at the confirmed catastrophic stop.
- Read-only reconciliation through the project `alpaca_paper` server confirmed the parent order `4115f7d1-12d2-4c8c-ae3c-6ed621580651` is `filled`, `100/100`, at `$32.47`. The `$35.45` target leg is `NEW`; the `$30.95` stop leg is `HELD`.
- Account activities agree with the stock fill. The current paper position is long 100 CHYM at a `$32.47` average entry with zero quantity available because the bracket exits reserve the shares.
- No market-close checkpoint is scored in this run because the handoff occurred during the regular session. Next checkpoint: the 2026-09-16 regular-market close, then 2026-09-17 close and five trading sessions.
- No durable lesson change is supported at activation; the post-Fed confirmation alternative remains `UNSCORABLE` until its objective trigger is observed.

### Completion at catastrophic stop — 2026-09-16

- Independent paper-MCP reconciliation confirmed the parent `4115f7d1-12d2-4c8c-ae3c-6ed621580651` remained filled for 100 shares at `$32.47`; its `$35.45` target `c5ec5afc-5629-4814-b966-428ae113bcee` was canceled and its `$30.95` stop `dd12a114-1c25-46b7-bbe3-1181ac2b246f` filled 100 shares at `$30.94` at `2026-09-16T19:14:04.824143Z`. The real path therefore ended before the official close with gross realized P/L `-$153.00`.
- The common stop observation is supported by the Alpaca IEX 1-minute bars around the fill (`19:13Z` close `$30.98`; `19:14Z` low `$30.92`; `19:15Z` close `$30.94`). A no-pre-Fed-trade alternative finished at `$0.00`. The 200-share immediate-entry alternative is scored at `-$306.00` using the confirmed `$30.94` stop execution as a common-exit proxy; it is not an inferred broker fill. The post-Fed confirmation alternative remains `UNSCORABLE`: no contemporaneous executable ask/volume record establishes whether its support-based trigger activated before the later close invalidation.
- Decision review: thesis/research mixed (the catalyst and technical setup were real, but event-path risk dominated); forecast mixed (the expected starter held briefly and then failed); instrument/strategy mixed (stock avoided option decay, while the entry still carried Fed whipsaw risk); strike/expiration not applicable; timing could improve by waiting for event confirmation; sizing/risk worked well because the 100-share starter limited the loss versus the 200-share counterfactual; execution worked well because the bracket filled and canceled the target automatically, with only one cent of stop slippage.
- Conclusion: the bounded starter lost `$153`, but it lost `$153` less than the larger immediate alternative and `$153` more than no trade. The evidence supports the predeclared sizing discipline in this single event case, not a broad new rule. Data quality is `partial`; no durable lesson change.
- Assessment complete. No further CHYM checkpoint is due; the original definition and this completion record remain the audit source.
