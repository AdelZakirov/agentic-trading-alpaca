# DT partial profit decision — original definition

## Identity

- decision_id: `alpaca-stage2-20260923-DT-sell`
- creator_run_id: `1812f603-ccb6-4fa1-a316-29318838cace`
- decision_at: 2026-09-23T17:42:27+02:00
- ticker: DT
- status: WAITING_FOR_FILL
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
