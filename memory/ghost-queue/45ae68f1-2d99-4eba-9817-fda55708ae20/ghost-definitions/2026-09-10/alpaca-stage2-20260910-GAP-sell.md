# Ghost pre-trade: GAP exit

## Identity

- decision_id: `alpaca-stage2-20260910-GAP-sell`
- creator_run_id: `45ae68f1-2d99-4eba-9817-fda55708ae20`
- decision_at: `2026-09-10T16:48:23+02:00` (Europe/Amsterdam)
- ticker: `GAP`
- status: `PENDING_SUBMISSION`
- client_order_id: `alpaca-stage2-20260910-GAP-sell`
- broker_order_id: null

## Original decision

- Thesis: the documented $21.60 daily-close invalidation was confirmed by the 2026-09-09 close at $21.365; fresh moneyheap technical research identifies a breakdown regime and continuation risk toward $20.40 and below.
- Chosen action: SELL 200 owned shares with a bounded day limit near the live bid.
- Pre-trade exposure: 200 shares long at $22.55 average; no option exposure.
- Size rationale: full exit removes a confirmed invalidated setup and approximately $120-$260 of additional downside risk if gap-fill support fails.
- Invalidation and holding period: exit now; no overnight holding plan after the confirmed daily-close failure.

## Evaluation rules

- Common window: compare against the chosen exit through the 2026-09-11 regular-session close.
- Start trigger: decision-time GAP bid/ask at $20.79/$20.80.
- Checkpoints: 2026-09-10 close and 2026-09-11 close, using executable bid/ask when available.
- End rule: compare exit proceeds and avoided drawdown; a delayed alternative remains hypothetical and does not authorize a later order.

## Initial evidence

- Stage 1 technical source: `data/stage1_enriched.csv`, technical as-of 2026-09-09; shortlist includes GAP only through the prior community/technical screen context.
- Fresh research: [`memory/research/2026-09-10/163849-GAP-technical.md`](../../research/2026-09-10/163849-GAP-technical.md).
- Alpaca IEX quote at 2026-09-10T14:48:23.010067271Z: bid $20.79 x 1,300, ask $20.80 x 300.
- Relevant missing data: no current option structure was selected; options would add complexity to an already invalidated stock thesis.

## Alternatives

### A1 — Hold through the next close

- question_tested: Does preserving the original daily-close time basis after the confirmed breach improve proceeds?
- instrument: GAP common stock; side HOLD; quantity 200.
- entry_rule: no transaction at decision time.
- simulated_entry_price: none; no-trade alternative starts at zero P/L and zero capital at risk.
- maximum_loss: unbounded beyond the existing position; current exposure remains 200 shares.
- exit_handling: reassess at the 2026-09-10 close, then exit only if evidence changes.
- pricing_assumptions: no hypothetical fill.
- missing_data: future close and execution path unknown.
- status: `NOT_SUBMITTED`

### A2 — Wait for a micro-bounce exit

- question_tested: Does waiting for the moneyheap-suggested $21.05-$21.20 bounce improve sale price without unacceptable continuation risk?
- instrument: GAP common stock; side SELL; quantity 200.
- entry_rule: sell on a verified bid in the $21.05-$21.20 bounce zone, otherwise remain exposed.
- simulated_entry_price: `UNSCORABLE` because the decision-time bid was $20.79 and the future bounce was not observable.
- maximum_loss: additional downside remains unbounded beyond the existing position until exit.
- exit_handling: one-session window; no chase above the documented exit zone.
- pricing_assumptions: hypothetical sale only if a future executable bid reaches the zone.
- missing_data: future bid, spread, and bounce probability unavailable.
- status: `NOT_SUBMITTED`

### A3 — Use a tight $20.75 stop instead of exiting

- question_tested: Can the gap-fill support at $20.80 hold for a tactical rebound while capping further damage?
- instrument: GAP common stock; side HOLD with hypothetical stop; quantity 200.
- entry_rule: retain shares at decision time and sell only after a verified print below $20.75.
- simulated_entry_price: none; no-trade alternative starts at zero P/L and zero capital at risk.
- maximum_loss: additional loss from $20.79 toward the stop is approximately $8 before slippage, with gap risk beyond the stop.
- exit_handling: stop within the next regular session; no overnight carry after a stop trigger.
- pricing_assumptions: stop execution is hypothetical and may gap through.
- missing_data: future stop execution and gap behavior unavailable.
- status: `NOT_SUBMITTED`

## Execution

- confirmed_fills: none before handoff.
- order_ids: null
- post-decision_status: `FILLED`
- broker_order_id: `68a32472-ea45-4601-b634-6c60d8bb6456`
- broker_status: `filled`
- confirmed_fill: SELL 200/200 GAP at $20.83; submitted 2026-09-10T14:52:16.179688536Z and filled 2026-09-10T14:52:17.032247579Z.

## Reviewer updates

Reserved for the separate ghost reviewer.
