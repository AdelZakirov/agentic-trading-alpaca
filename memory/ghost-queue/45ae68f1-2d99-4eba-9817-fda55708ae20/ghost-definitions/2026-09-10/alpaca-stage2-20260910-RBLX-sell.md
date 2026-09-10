# Ghost pre-trade: RBLX target trim

## Identity

- decision_id: `alpaca-stage2-20260910-RBLX-sell`
- creator_run_id: `45ae68f1-2d99-4eba-9817-fda55708ae20`
- decision_at: `2026-09-10T16:48:23+02:00` (Europe/Amsterdam)
- ticker: `RBLX`
- status: `PENDING_SUBMISSION`
- client_order_id: `alpaca-stage2-20260910-RBLX-sell`
- broker_order_id: null

## Original decision

- Thesis: RBLX is in an emerging uptrend but is testing the $45.00-$45.75 extension zone and upper-band resistance; fresh research supports taking a partial gain while retaining a runner toward $47.50-$48.00.
- Chosen action: SELL 75 owned shares with a bounded day limit near the live bid; HOLD the remaining 75 shares.
- Pre-trade exposure: 150 shares long at $40.41 average; no option exposure.
- Size rationale: a 50% trim locks gains at the target while leaving half the position for the gap-fill extension.
- Invalidation and holding period: remaining runner has a tactical review near $43.20 and hard daily-close support at $41.40; reassess over one to three sessions.

## Evaluation rules

- Common window: compare against the chosen trim through the 2026-09-12 regular-session close.
- Start trigger: decision-time RBLX bid/ask at $45.11/$45.45.
- Checkpoints: 2026-09-10 close, 2026-09-11 close, and 2026-09-12 close, using executable bid/ask when available.
- End rule: compare realized trim proceeds plus marked runner value; no alternative order may be submitted from this file.

## Initial evidence

- Stage 1 source: `data/stage1_enriched.csv`, technical as-of 2026-09-09; 12.3% 20-day return, upper-band extension, and no active breakout flag.
- Fresh research: [`memory/research/2026-09-10/164000-RBLX-technical.md`](../../research/2026-09-10/164000-RBLX-technical.md).
- Alpaca IEX quote at 2026-09-10T14:48:12.137138646Z: bid $45.11 x 100, ask $45.45 x 100.
- Relevant missing data: no current option order selected; stock is the cleaner expression and prior option path added expiry risk.

## Alternatives

### A1 — Smaller 50-share trim

- question_tested: Does retaining two-thirds of the runner improve participation if the gap ceiling breaks?
- instrument: RBLX common stock; side SELL; quantity 50.
- entry_rule: sell 50 shares at the decision-time bid or better.
- simulated_entry_price: $45.11 bid.
- maximum_loss: no new capital risk; remaining 100-share runner retains roughly $191 of tactical risk to $43.20 before gaps.
- exit_handling: retain 100 shares toward $47.50-$48.00; review below $43.20 or $41.40.
- pricing_assumptions: hypothetical sale at contemporaneous bid.
- missing_data: future execution and path unknown.
- status: `NOT_SUBMITTED`

### A2 — Larger 100-share trim

- question_tested: Does de-risking two-thirds improve expected outcome at resistance after the sharp recovery?
- instrument: RBLX common stock; side SELL; quantity 100.
- entry_rule: sell 100 shares at the decision-time bid or better.
- simulated_entry_price: $45.11 bid.
- maximum_loss: no new capital risk; remaining 50-share runner retains roughly $96 of tactical risk to $43.20 before gaps.
- exit_handling: retain 50 shares toward $47.50-$48.00; review below $43.20 or $41.40.
- pricing_assumptions: hypothetical sale at contemporaneous bid.
- missing_data: future execution and path unknown.
- status: `NOT_SUBMITTED`

### A3 — Hold all 150 shares for the gap ceiling

- question_tested: Does momentum continuation to $47.50-$48.00 outweigh current target-zone reversal risk?
- instrument: RBLX common stock; side HOLD; quantity 150.
- entry_rule: no transaction at decision time.
- simulated_entry_price: none; no-trade alternative starts at zero P/L and zero capital at risk.
- maximum_loss: existing 150-share exposure remains; a move to $43.20 would give back approximately $287 from the decision-time bid before gaps.
- exit_handling: seek $47.50-$48.00 extension; review on a sustained break below $43.20 and exit by $41.40 daily-close failure.
- pricing_assumptions: no hypothetical fill.
- missing_data: future price path and liquidity unknown.
- status: `NOT_SUBMITTED`

## Execution

- confirmed_fills: none before handoff.
- order_ids: null
- post-decision_status: `FILLED`
- broker_order_id: `eb4eb916-a6fe-487a-a835-b087a552e051`
- broker_status: `filled`
- confirmed_fill: SELL 75/75 RBLX at $45.16; submitted 2026-09-10T14:55:12.78838921Z and filled 2026-09-10T14:55:13.556308165Z.

## Reviewer updates

Reserved for the separate ghost reviewer.
