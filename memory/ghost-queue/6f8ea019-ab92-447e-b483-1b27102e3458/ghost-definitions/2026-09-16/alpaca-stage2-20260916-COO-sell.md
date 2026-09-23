# Ghost alternatives: COO spread close

## Identity

- decision_id: `alpaca-stage2-20260916-COO-sell`
- creator_run_id: `6f8ea019-ab92-447e-b483-1b27102e3458`
- decision_at: `2026-09-16T16:58:31+02:00`
- ticker: `COO`
- status: `FILLED`
- client_order_id: `alpaca-stage2-20260916-COO-sell`
- broker_order_id: `341117e2-7c5b-467e-82e3-b3fb5903936d`

## Original decision

- Thesis: the September 18 long 55 put / short 50 put spread has not reached its $50-$51 downside target, has only two sessions to expiry, and now carries dominant theta, pin, exercise, and short-leg assignment risk.
- Chosen action: close the full one-lot spread as a paired multi-leg limit order for at least $0.64 net credit.
- Pre-trade exposure: long 1 `COO260918P00055000` at $2.00 and short 1 `COO260918P00050000` at $0.05; original net debit and defined maximum loss $195.
- Size rationale: close the entire one-lot structure; partial legging would create unsupported naked/assignment risk.
- Invalidation and holding period: this is an expiry-risk exit, not a renewed bearish trade. If the paired close does not execute in the bounded management window, re-read both legs and the underlying before one justified replacement or retain for explicit recovery.

## Evaluation rules

- Common observation start: confirmed fill timestamp of the chosen close; if unfilled, use `2026-09-16T15:15:00-04:00` as the comparison start.
- Checkpoints: September 17 close; September 18 at 15:30 ET; October 16 close only for the roll alternative.
- End rule: value all spread alternatives from conservative executable sides; use intrinsic value only if no valid quote exists at expiration.
- Exit handling: paired legs only. Never assume exercise, assignment, or a fill from a submitted order.

## Initial evidence

- Alpaca IEX underlying quote at `2026-09-16T14:58:31.600937545Z`: bid $54.61 x100, ask $54.65 x100.
- Indicative long 55 put quote at `2026-09-16T14:56:38.779305181Z`: bid $0.67 x69, ask $0.93 x38; IV 0.3787; delta -0.5830; theta -0.1460.
- Indicative short 50 put quote at `2026-09-16T14:46:15.155588912Z`: bid $0.00 x0, ask $0.03 x67; IV and Greeks unavailable.
- Conservative paired liquidation credit: $0.67 long-leg bid minus $0.03 short-leg ask = $0.64, or $64 before fees. Indicative, not firm OPRA pricing or a guaranteed fill.
- Both contracts are active and tradable; expiration is 2026-09-18. Open interest: 471 at the 55 strike and 1,277 at the 50 strike.

## Alternatives

### A. Hold one more session, then close September 17

- Question tested: did one additional day of bearish exposure improve recovery enough to compensate for theta and expiry risk?
- Instrument: existing Sep 18 55/50 put debit spread; no new order today.
- Entry rule and simulated price: retain at the contemporaneous conservative liquidation value of $0.64.
- Maximum loss: original spread maximum loss remains $195; from the $0.64 observation mark, another $64 can decay away while downside can add up to $436 of spread value.
- Exit: paired close at the September 17 15:45 ET executable credit, or intrinsic value if quotes are unavailable.
- Pricing assumptions: long bid minus short ask. Missing firm OPRA pricing is explicitly retained.

### B. Hold through expiration

- Question tested: did preserving the full final two-day convexity outperform removing assignment and pin risk?
- Instrument: existing Sep 18 55/50 put debit spread.
- Entry rule and simulated price: no trade; baseline conservative liquidation value $0.64.
- Maximum loss: original $195 debit; final spread value ranges from $0 to $500 before fees.
- Exit: intrinsic value at September 18 15:30 ET and expiration; assignment/exercise operational costs remain a qualitative penalty.
- Pricing assumptions: no fabricated fill. This alternative is scoreable from intrinsic value and underlying price.

### C. Roll to October 16 55/50 put spread

- Question tested: would buying more time preserve the bearish thesis better than closing it?
- Instrument: close Sep 18 spread and open one Oct 16 55/50 put debit spread.
- Entry rule: execute only if the October spread had a conservative debit no greater than $1.60 and COO remained below $55.60.
- Simulated entry price: `UNSCORABLE`; the October chain was not refreshed because no renewed thesis justified another month of risk.
- Maximum loss: `UNSCORABLE` without a contemporaneous executable debit.
- Exit: close by October 14 or at a $50-$51 underlying target; no expiration hold.
- Missing data: October leg quotes, IV, Greeks, and sizes.

## Execution

- submitted_at: `2026-09-16T14:59:37.605359666Z`
- original_broker_order_id: `7005ae93-4364-43b6-b2aa-f601c950fb47`
- original_status: `replaced`
- replacement_client_order_id: `alpaca-stage2-20260916-COO-sell-r1`
- broker_order_id: `341117e2-7c5b-467e-82e3-b3fb5903936d`
- status: `filled`
- filled_at: `2026-09-16T15:03:59.886421657Z`
- filled_qty: `1`
- filled_avg_price: `-0.60` net credit, or $60 gross before fees
- reconciliation: both COO option positions absent after fill; account cash increased by $59.95. No leg remains open.

## Reviewer updates

