# Ghost pre-trade: GAP exit

## Identity

- decision_id: `alpaca-stage2-20260910-GAP-sell`
- creator_run_id: `45ae68f1-2d99-4eba-9817-fda55708ae20`
- decision_at: `2026-09-10T16:48:23+02:00` (Europe/Amsterdam)
- ticker: `GAP`
- status: `ACTIVE`
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

### Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`.
- Evaluation start: `2026-09-10T14:52:17.032248Z`, when the full exit completed; the common comparison window remains through the `2026-09-11` regular-session close.
- Paper endpoint confirmed: `https://paper-api.alpaca.markets/v2`, with `ALPACA_PAPER_TRADE=true`.
- Broker order `68a32472-ea45-4601-b634-6c60d8bb6456` is `filled`, `SELL 200/200`, average `$20.83`, limit `$20.82`. Account activity shows a 2-share partial fill at `2026-09-10T14:52:16.788281Z` followed by 198 shares at `2026-09-10T14:52:17.032248Z`; no quantity or price discrepancy.
- No checkpoint mark is recorded yet. Next checkpoint: `2026-09-10` regular-session close.

## 2026-09-10 close checkpoint

- Observed at the common close timestamp `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: close `$20.905`; the after-close quote was wide at `$19.55/$22.02`, so the bar is a disclosed non-executable proxy.
- Real exit proceeds remain fixed at `$4,166.00` from the confirmed 200-share sale at `$20.83`. A1 (hold through the next close) marks at `$4,181.00`, leading the real exit by `$15.00` at this checkpoint.
- A2 (wait for a micro-bounce exit) was not activated; the daily high reached `$21.26`, but no executable bid in the predeclared `$21.05-$21.20` zone was preserved. A3 (tight `$20.75` stop) saw the bar low at `$20.72`, confirming the price trigger but not an exact hypothetical stop fill, so its outcome remains UNSCORABLE.
- The `$21.60` invalidation remained below the close; no hindsight change is made. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: GAP close `$21.51`; this is a disclosed non-executable proxy.
- Real exit proceeds remain fixed at `$4,166.00`, or `+$8.00` versus the `$4,158.00` decision-time reference. `A1_HOLD_THROUGH_CLOSE`: `$4,302.00`, or `+$144.00` and `$136.00` ahead of the real exit.
- `A2_WAIT_MICRO_BOUNCE` remains UNSCORABLE because no executable bid in the predeclared `$21.05-$21.20` zone was preserved; `A3_TIGHT_STOP` remains UNSCORABLE because the hypothetical stop execution was not observable. The `$21.60` invalidation remained above the close. Comparison complete; no lesson change.
