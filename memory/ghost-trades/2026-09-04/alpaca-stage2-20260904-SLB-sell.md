# Ghost set: alpaca-stage2-20260904-SLB-sell

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260904-SLB-sell`
- Broker order ID: `27449aaa-eb9b-4276-8bbc-d781b20f3cda`
- Ticker: SLB
- Decision time: approximately 2026-09-04T14:44:00Z
- Fill sequence: 13, 40, 25, and 2 shares; fully filled at 2026-09-04T14:47:37.047510754Z
- Evaluation start: 2026-09-04T14:47:37.047510754Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-04, 2026-09-08, 2026-09-09, 2026-09-10, and 2026-09-11 regular-market closes
- Holding plan tested: immediate tactical exit after the documented invalidation and final review endpoint failed

## Thesis and actual fill

SLB gapped below the documented $56.90 invalidation, traded as low as $56.25, and failed to reclaim $57.05 before execution. Fresh moneyheap technical work classified the tactical setup as failed even though the intermediate trend remained intact.

- Pre-trade exposure: 80 SLB shares at $58.242124 average
- Actual action: sell all 80 shares
- Limit: $56.59; actual average fill: $56.62
- Actual proceeds: $4,529.60 before fees
- Realized P/L: approximately -$129.77 before fees
- Size rationale: remove the full tactical exposure at its planned endpoint instead of widening the invalidation after the fact

## Contemporaneous market data

- Source: Alpaca IEX.
- Preflight at approximately 2026-09-04T14:47Z: SLB about $56.59/$56.60, below the $56.90 invalidation and $57.05 reclaim level.
- Session context at the decision: open $56.89, high $57.05, low $56.25. Sector peers were also weak.

## Ghost alternatives fixed before submission

### HOLD_80_TO_CLOSE

- Retain all 80 shares through the 2026-09-04 close, then continue only if the original thesis is freshly restored.
- Reference: 80 shares at the contemporaneous $56.59 executable bid.
- Exit handling: common checkpoints and the original tactical levels.

### SELL_HALF_40

- Sell 40 shares at the contemporaneous executable bid and retain 40.
- Simulated sale proceeds: $2,263.60 at $56.59.
- Exit handling: retained shares use the same levels and common endpoint.

### WAIT_RECLAIM_57_05

- Delay the sale only if a 15-minute close above $57.05 occurs; otherwise exit at the next conservative executable bid.
- Entry/reference value: `UNSCORABLE` until the objective condition occurs or fails.

## Initial post-fill observation

- Real path: CLOSED at $56.62; proceeds $4,529.60 and realized trade P/L approximately -$129.77.
- `HOLD_80_TO_CLOSE`: initial reference value $4,527.20 at $56.59; no post-fill checkpoint is manufactured.
- `SELL_HALF_40`: initial combined reference $4,527.20 before later marks.
- `WAIT_RECLAIM_57_05`: remains conditional; no reclaim had occurred at the fill.
- Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- Common close quote: $57.50/$57.52 at `2026-09-04T19:59:59.996801485Z`.
- Real path: $4,529.60 proceeds. `HOLD_80_TO_CLOSE`: $4,600 value, $72.80 above its $4,527.20 decision reference and $70.40 above the real path. `SELL_HALF_40`: $2,263.60 proceeds plus $2,300 retained = $4,563.60, $34 above the real path.
- A later 15-minute reclaim above $57.05 occurred, so `WAIT_RECLAIM_57_05` retained the 80 shares and matches the $4,600 close value for this checkpoint.
- Immediate exit reduced gap risk but trailed every retention alternative after the same-day recovery. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $57.11; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real path: $4,529.60 actual proceeds. `HOLD_80` and the activated `WAIT_RECLAIM_57_05`: 80 shares worth $4,568.80, leading real by $39.20. `SELL_HALF_40`: $2,263.60 proceeds plus 40 shares worth $2,284.40 = $4,548.00, leading real by $18.40.
- The relief move favored retention at this checkpoint; the real exit still removed event/commodity exposure as intended.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $57.06; the near-close IEX quote was tight at $57.05/$57.07, but the official bar is retained as the common reference for this checkpoint.
- Real path remains fixed at $4,529.60. `HOLD_80_TO_CLOSE`: 80 shares at $57.06 = $4,564.80, leading real by $35.20. `SELL_HALF_40`: $2,263.60 proceeds plus 40 shares at $57.06 = $4,546.00, leading real by $16.40. The activated `WAIT_RECLAIM_57_05` matches the full-retention value.
- Retention still led the immediate exit at this checkpoint; no new lesson is supported. Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: SLB close `$56.005`; the after-close quote was wide at `$53.02/$58.13`, so the bar is a disclosed non-executable proxy.
- Real path remains fixed at `$4,529.60` proceeds. `HOLD_80_TO_CLOSE`: 80 shares at the close proxy = `$4,480.40`, trailing real by `$49.20`; `SELL_HALF_40`: `$2,263.60` proceeds plus 40 shares worth `$2,240.20` = `$4,503.80`, trailing real by `$25.80`. The previously activated `WAIT_RECLAIM_57_05` matches full retention.
- The immediate exit still leads the retention paths at this checkpoint. No new lesson is supported. Next checkpoint: 2026-09-11 regular-market close.
