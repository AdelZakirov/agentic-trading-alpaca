# MSFT partial profit decision — original definitions

## Identity

- decision_id: `alpaca-stage2-20260925-MSFT-sell`
- creator_run_id: `a2d14c54-69dc-496d-8d5e-c0ec996c75bd`
- decision_at: `2026-09-25T16:48:49+02:00`
- ticker: MSFT
- Status: COMPLETE
- client_order_id: `alpaca-stage2-20260925-MSFT-sell`
- broker_order_id: `a302bcd8-feb9-4477-a412-561c1638bf44`

## Original decision

Broker holds 20 MSFT at $497.4715 average, no open orders. Its predeclared $510–$514 partial profit review has activated with Sep 25 mark $513.85. [Current moneyheap technical](../../research/2026-09-25/164744-MSFT-technical.md) sees a bullish trend, yet price is near upper-band/range supply. Chosen action: sell 10 of 20 at a bounded DAY limit near the executable bid, retaining 10 for $528–$535 if trend extends. This crystallizes roughly half of the unrealized gain and reduces overlapping MSFT/MU/SPY growth risk without changing the remaining close-based $485.50 review rule. Remaining horizon 1–4 weeks; reassess after a close above $518 or below $485.50, and before late-October earnings. No option order: a derivative would add unnecessary tech-factor leverage/theta or cap retained upside.

## Evaluation rules

Comparison starts only on confirmed real fill. Observe Sep 28 and Oct 2 regular-session closes, ending Oct 2 close or earlier if a verified corporate event makes comparison invalid. Mark held shares at broker prices. Apply the same original $485.50 daily-close review rule to every still-held share; if breached, model next-session bounded exit at executable bid. Do not assume stops guarantee an execution price. If the real order is unfilled, fill-anchored alternatives remain inactive.

## Initial evidence

- Alpaca paper Sep 25 10:48:28 ET: regular market open, 20 MSFT available, mark $513.85, no open orders; account equity $101,626.68, cash $54,787.88.
- Alpaca IEX Sep 25 10:48:37 ET: bid $513.74 x120, ask $514.84 x80; $1.10 spread is wide for an ordinary liquid name. Additional quote validation is required before submission. No fill is assumed.
- Follow-up IEX quotes: 10:49:53 ET bid $515.04 x40, ask $515.77 x80; 10:50:58 ET bid $514.42 x40, ask $514.75 x40. The spread narrowed from $1.10 to $0.33 over 2m21s and displayed sizes stayed positive. Intended sale limit $514.25, $0.17 below latest bid; no fill assumed.
- Final preflight at 10:51:44 ET showed bid $515.17 x120, ask $515.77 x80, and 20 shares still available. The limit is revised before submission to $515.00, $0.17 below the current bid; the $514.25 earlier bound was never submitted.
- [Moneyheap technical](../../research/2026-09-25/164744-MSFT-technical.md): improving bullish momentum but price at upper band/range resistance; a tactical half trim at $513–$514 is plausible. Brokerage quote remains execution authority.

## Alternatives

1. `HOLD_ALL`: Test whether preserving all 20 shares captures more upside from the strong trend. No trade now; retain roughly $10,277 stock exposure. Mark through Oct 2 close; use the common close-based $485.50 review and next-session bounded exit if triggered. The comparison baseline is real confirmed trim fill, never an assumed price. Maximum possible share loss is market value; gaps can defeat review levels. Future marks/exit quote missing.
2. `SELL_ALL`: Test full de-risking at activated range resistance. Hypothetically sell all 20 at contemporaneous IEX bid $513.74, about $10,274.80 proceeds and no further MSFT price exposure. Remain out through Oct 2. The bid is indicative single-exchange pricing, not a broker fill. Maximum future loss after sale is zero price exposure, while upside is forgone. Missing data: actual hypothetical execution and future marks.

## Execution

- Submitted DAY limit SELL 10 at $515.00, broker `a302bcd8-feb9-4477-a412-561c1638bf44`.
- Broker order status `filled`: 10/10 at $515.15, 2026-09-25T14:52:04.459590485Z. Exact order-specific FILL activity 10@$515.15. Follow-up paper cash $59,939.38 and MSFT position 10 remaining at broker average $497.4715; no open MSFT order.

## Reviewer updates

### Confirmed fill and comparison start — 2026-09-25

- Project alpaca_paper order a302bcd8-feb9-4477-a412-561c1638bf44 is filled 10/10 at $515.15 at 2026-09-25T14:52:04.459590Z; one order-specific FILL activity confirms 10 shares. The comparison starts at this confirmed fill.
- At the 2026-09-28T16:37:43Z broker snapshot, 10 MSFT shares remained at average $497.473, with no open orders.
- Status: ACTIVE. First common checkpoint remains 2026-09-28 close; evaluation end remains 2026-10-02 close.

## 2026-09-28 first close checkpoint

- The Alpaca IEX daily bar closed at `$509.36` (high `$513.29`, low `$502.38`); the near-close quote at `2026-09-28T19:59:59.075863279Z` was `$509.31` bid x40 / `$515.40` ask x80. The spread was wide and IEX-only, but bid depth covered the 20-share alternatives.
- Gross P/L versus `$497.4715` basis: the real path (10 sold at `$515.15`, 10 marked at `$509.31`) `+$295.17`; HOLD_ALL 20 at `$509.31` `+$236.77`; SELL_ALL 20 at the original `$513.74` bid `+$325.37`. No `$485.50` close invalidation or `$528` target review triggered.
- Partial-quality checkpoint due to the wide single-venue mark; no lesson change. Next checkpoint: `2026-10-02` close.

## October 2 terminal checkpoint and completed review

- Common mark: the last coherent near-close IEX quote was `$517.11 x80` bid / `$522.00 x80` ask at `2026-10-02T19:59:55.001928Z`, five seconds before the bell. The final quote widened to `$493.32/$523.00`; that dislocated record is rejected. The selected bid covers 20 shares but is wide (about `$4.89`) and single-venue. The IEX daily bar closed `$517.32`.
- Gross P/L from the `$497.4715` basis: real (10 sold at `$515.15`, 10 marked at `$517.11`) = `+$373.17`; HOLD_ALL 20 = `+$392.77`; SELL_ALL 20 at its original `$513.74` bid = `+$325.37`. Full hold exceeds the real partial trim by `$19.60`; the real trim exceeds full sale by `$47.80`. The `$485.50` close invalidation and `$528` target were not reached.
- Assessment completed 2026-10-03; set status `COMPLETE`. The terminal return modestly favors holding all shares, while the actual trim reduced concentration and retained 10 shares. The narrow, wide-book difference is not a durable lesson.

### Decision-quality assessment

- Thesis / research: worked — the bullish trend persisted, although the original supply concern remained plausible.
- Forecast: worked — price rose from the trim fill through the endpoint.
- Instrument / strategy: mixed — stock matched the thesis; a half trim balanced exposure, but full hold returned slightly more.
- Strike / expiration: not applicable — no option was selected.
- Timing: mixed — the `$515.15` sale captured profit, while the retained shares advanced to the endpoint.
- Sizing / risk: mixed — half-size reduction limited exposure but modestly lagged full hold in this short window.
- Execution: worked — 10/10 shares filled at `$515.15`, confirmed by the order-specific FILL activity.
