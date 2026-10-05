# DT partial profit decision — original definition

## Identity

- decision_id: `alpaca-stage2-20260923-DT-sell`
- creator_run_id: `1812f603-ccb6-4fa1-a316-29318838cace`
- decision_at: 2026-09-23T17:42:27+02:00
- ticker: DT
- status: ACTIVE
- client_order_id: `alpaca-stage2-20260923-DT-sell`
- broker_order_id: null

## Original decision

Existing paper position: 100 long DT shares at $55.00, no open order. The $58.50 first review is activated. Current broker IEX bid/ask $58.97/$59.09 (200/100 displayed) at 2026-09-23T15:42:26.958899411Z. Moneyheap technical research [DT technical](../../research/2026-09-23/174108-DT-technical.md) finds a rising trend but RSI 72.29 and a price above the upper Bollinger band. Chosen action: sell 50 owned shares with a DAY limit at $58.95, retain 50 toward $62–$64. This reduces technology overlap while retaining upside. Approximate gross realized gain if filled at limit: $197.50 before fees. Review the runner after a daily close below $55.80; $51.80 remains the original structural invalidation. Planned runner horizon: through 2026-10-16 or earlier target/thesis break. This is a profit trim, not a new short.

## Evaluation rules

Anchor alternatives at the broker quote above; start comparisons only after a confirmed chosen fill and at its actual fill time. Observe the first subsequent daily close, 2026-09-25 close, 2026-09-30 close, and final 2026-10-07 close, or earlier if DT reaches $62/$64 or closes below $55.80. Mark unobservable checkpoints UNSCORABLE. For held-share alternatives, mark 50 incremental shares at the same broker bid and apply any actually observed corporate actions; do not pretend a standing stop would fill at its trigger. Exit a hypothetical position only at a contemporaneous executable bid after its predeclared trigger. No ghost order goes to Alpaca.

## Initial evidence

- Alpaca paper clock: regular session open at 2026-09-23T11:42:20-04:00.
- Paper account: equity $102,208.70, cash $45,737.38, active/unblocked; DT qty/available 100/100; zero open orders.
- Alpaca IEX DT bid $58.97 x200 and ask $59.09 x100 at 2026-09-23T15:42:26.958899411Z. Indicative equity midpoint is not treated as an executable sale.
- Research: [DT technical](../../research/2026-09-23/174108-DT-technical.md); prior plan [DT position](../../positions/DT.md).
- Other market venues, taxes and future liquidity are unknown; gross comparisons exclude fees.

## Alternatives fixed before order submission

1. **hold_all** — Test whether momentum continuation beats taking the first profit. Retain all 100 owned shares, with 50 shares incremental to the chosen runner. No order now, incremental shadow mark $58.97 bid; new cash received $0 and 50 shares remain at risk. Review on daily close below $55.80, $62 first next target, $64 final target or final 2026-10-07 close. Approximate incremental 50-share loss to $55.80 is $158.50; gap to $51.80 is $358.50; no fixed maximum stock loss beyond paid cost. No fabricated fill.
2. **sell_all** — Test full de-risking of tech overlap. Sell 100 owned shares now at observed bid $58.97 as a conservative hypothetical sale; the incremental 50 over chosen action would receive $2,948.50, with no remaining DT exposure. Opportunity cost at $62/$64 on those 50 shares is $151.50/$251.50 from the quote anchor. Actual future executable sale price is unknown; reviewer should use the decision-time bid only for this hypothetical immediate action.
3. **wait_for_60** — Test a higher first trim trigger. Retain 100 shares now and sell 50 only if executable DT bid reaches $60.00 by 2026-09-25 regular close; otherwise keep the additional 50 until the common final date or the $55.80 close review. Simulated price is not prefilled; use observed bid at trigger, otherwise score as HOLD. This risks missing the existing $58.50 review and a reversal; maximum stock loss is not fixed.

## Execution

- Submission: pending.
- Confirmed broker fill: null.

## Reviewer updates

Reserved for the separate reviewer after handoff.

## Execution update before handoff

- Submitted DAY limit SELL 50 DT at $58.95; broker order `fc7c25c7-c034-4f05-9475-9980cb398491`.
- Broker status FILLED 50/50 at average $58.97 on 2026-09-23T15:46:56.776606304Z. Two FILL activities, 44 and 6 shares, both $58.97, reconcile to 50. Remaining DT position 50/50 available. Gross realized gain versus $55 basis: $198.50 before fees.

## Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`; comparison starts at the confirmed chosen fill, `2026-09-23T15:46:56.776606304Z` (50 shares at `$58.97`). Read-only `alpaca_paper` order lookup and order-specific FILL activities confirm the 44-share and 6-share executions; the current paper position confirms 50 DT shares remain available.
- The original alternatives and checkpoints are adopted unchanged. No post-fill mark is recorded yet; the first subsequent daily close is Sep 23. Next checkpoint: Sep 23 regular-session close.

### 2026-09-23 first-close checkpoint

- Project `alpaca_paper` historical IEX quote at `2026-09-23T19:59:50.006867112Z` was DT `$58.51` bid x100 / `$58.54` ask x100; the IEX daily bar closed at `$58.505`, with high `$59.30`. The last close update was dislocated (`$55.86/$58.85`), so this is a timestamped near-close observation, not an exact closing bid; checkpoint quality is partial. The `$60` wait trigger was not observed by this checkpoint.
- At the common bid, selected path is `+$374` (realized `$198.50` plus 50 shares from `$55`), hold_all `+$351`, sell_all `+$397`, and wait_for_60 remains held at `+$351`. No target or invalidation was reached. Next checkpoint: Sep 25 close.

## 2026-09-25 close checkpoint

- Common mark: Alpaca IEX quote at 2026-09-25T19:59:59.838704630Z was $55.79 bid x100 / $60.94 ask x100; the daily bar closed at $57.95. The unusually wide IEX spread makes this a partial-quality conservative mark. The $55.80 daily-close review did not trigger; the bar close was above it, and the $62/$64 targets were not reached.
- Outcomes from the original 100 shares at $55.00: selected trim path realized $198.50 on 50 at $58.97 and marked the remaining 50 at $55.79, total +$238.00. hold_all: +$79.00. sell_all at the predeclared decision-time $58.97 bid: +$397.00. wait_for_60 never reached $60 by Sep 25 and remained held, +$79.00.
- The higher $60 trim condition was not activated; the selected $58.50 review captured proceeds while leaving a 50-share runner. No lesson change at this interim checkpoint. Next checkpoint: 2026-09-30 close.

## 2026-09-30 close checkpoint

- Read-only Alpaca paper reconciliation reconfirmed the original 50-share sale at `$58.97` from order `fc7c25c7-c034-4f05-9475-9980cb398491`; its two order-specific FILL activities total 50 shares. Current paper position remains 50 DT shares at `$55.00` average.
- The Sep 30 IEX daily bar closed `$57.72` (high `$58.595`, low `$57.65`). The last coherent pre-close quote was `$57.71 x100 / $57.95 x100` at `19:59:58.166866598Z`; later IEX books widened/dislocated and the first post-close quote is excluded. Mark quality is partial.
- From the original 100 shares at `$55.00`, the real trim path is `+$334.00` (`+$198.50` realized plus 50 at the `$57.71` bid); hold_all is `+$271.00`; sell_all at the predeclared `$58.97` decision bid is `+$397.00`; wait_for_60 remained held after no qualifying bid through Sep 25 and is also `+$271.00`. No daily close was below `$55.80`; Sep 25-30 daily highs stayed below `$62`.
- Comparison remains ACTIVE through the Oct 7 endpoint. Next checkpoint: Oct 7 close; between-checkpoint triggers remain a daily close below `$55.80` or an executable target bid at `$62/$64`. No lesson change.

### 2026-09-30 close checkpoint

- Existing checkpoint already records the Sep 30 catch-up at the stable near-close IEX bid `$57.71` and marks it partial quality. Routing is now aligned with that saved evidence; next checkpoint remains October 7 close.
