# Ghost set: alpaca-stage2-20260903-HOOD-sell

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260903-HOOD-sell`
- Broker order ID: `e3f20537-6ef6-4571-a3e1-5b6620c88737`
- Ticker: HOOD
- Decision time: approximately 2026-09-03T14:39:38Z
- Fill time: `2026-09-03T14:39:58.821160929Z`
- Evaluation start: `2026-09-03T14:39:58.821160929Z`
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-03, 2026-09-04, 2026-09-08, 2026-09-09, 2026-09-10, and 2026-09-11 regular-market closes
- Holding plan: compare partial profit-taking choices through the original HOOD horizon
- Invalidation/review: residual real stock reviews on a daily close below $117.50; original hard thesis invalidation remains $98.80

## Thesis and actual fill

HOOD exceeded the documented $117.50-$121 extension target. The real path sold 25 of 75 shares at $121.984 and retained 50 shares, balancing target discipline with continued upside participation.

- Pre-trade exposure: 75 HOOD shares at $104.348 average
- Actual sale: 25 shares at $121.984; proceeds $3,049.60
- Residual: 50 shares
- Size rationale: reduce one-third after a target overrun without fully abandoning a strong momentum day

## Contemporaneous market data

- Source: Alpaca IEX.
- Immediate preflight quote at approximately `2026-09-03T14:39:38Z`: about $121.75 bid / $121.84 ask.
- Immediate post-fill quote at approximately `2026-09-03T14:41:15Z`: about $121.84 bid / $121.96 ask.
- The earlier decision record used an approximate $122.55/$122.61 observation; execution used the later refreshed quote and a bounded day limit.

## Ghost alternatives fixed before submission

### HOLD_FULL_HOOD

- Question: Would retaining all 75 shares outperform target-based de-risking?
- Instrument: 75 HOOD shares, no sale
- Simulated entry: retain at the common pre-trade reference; no new capital
- Exit handling: original horizon and thesis rules

### SELL_HALF_HOOD

- Question: Would a larger 37-share reduction improve risk-adjusted outcome?
- Instrument: sell 37 shares at the contemporaneous $121.75 bid and retain 38 shares
- Simulated sale proceeds: $4,504.75
- Exit handling: retained shares follow the same horizon and review rules

### REAL_SELL_25_HOOD

- Question: Does a one-third reduction best balance locked gains and participation?
- Instrument: actual sale of 25 shares, retaining 50
- Actual sale proceeds: $3,049.60
- Exit handling: retained shares follow the same horizon and review rules

## Initial post-fill observation

- Common pre-trade reference value: 75 shares at $121.75 bid = $9,131.25.
- Real path: $3,049.60 actual proceeds plus 50 shares at the $121.84 post-fill bid = $9,141.60, incremental value +$10.35.
- `HOLD_FULL_HOOD`: 75 shares at $121.84 = $9,138.00, incremental value +$6.75.
- `SELL_HALF_HOOD`: $4,504.75 simulated proceeds plus 38 shares at $121.84 = $9,134.67, incremental value +$3.42.
- These small initial differences reflect execution and the immediate quote move, not completed decision quality. Next checkpoint: 2026-09-03 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-03 close checkpoint

- Observed from Alpaca IEX at approximately `2026-09-03T19:59:59Z`; HOOD's conservative executable bid was $120.01.
- Real path: $3,049.60 actual proceeds plus 50 shares at $120.01 = $9,050.10, or -$81.15 versus the $9,131.25 pre-trade reference.
- `HOLD_FULL_HOOD`: 75 shares at $120.01 = $9,000.75, or -$130.50 versus reference.
- `SELL_HALF_HOOD`: $4,504.75 simulated proceeds plus 38 shares at $120.01 = $9,065.13, or -$66.12 versus reference.
- The larger half reduction leads the real path by $15.03 and holding all shares trails it by $49.35 at this early checkpoint. The $117.50 residual review did not trigger. Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- Common stock mark: $122.06 executable bid near the close; pre-trade reference remained $9,131.25.
- Real path: $3,049.60 proceeds plus 50 shares worth $6,103.00 = $9,152.60, +$21.35. `HOLD_FULL_HOOD`: $9,154.50, +$23.25. `SELL_HALF_HOOD`: $4,504.75 proceeds plus 38 shares worth $4,638.28 = $9,143.03, +$11.78.
- Full retention led the real path by $1.90; the real one-third trim led the larger trim by $9.57. The $117.50 review did not trigger. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $117.37; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved. The common pre-trade reference remains $9,131.25.
- Real path: $3,049.60 proceeds plus 50 shares at $117.37 = $8,918.10, incremental P/L -$213.15. `HOLD_FULL_HOOD`: $8,802.75, -$328.50. `SELL_HALF_HOOD`: $4,504.75 proceeds plus 38 shares worth $4,460.06 = $8,964.81, -$166.44.
- The larger trim led the real path by $46.71; the real path led full retention by $115.35. The $117.37 daily close activated the residual review.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $115.29; this is a non-executable proxy because the near-close quote was abnormally wide at $115.25/$120.99. The common pre-trade reference remains $9,131.25.
- Real path, including the separate 2026-09-09 20-share management trim: $3,049.60 + $2,337.00 proceeds plus 30 shares at $115.29 = $8,845.30, incremental P/L -$285.95. `HOLD_FULL_HOOD`: $8,646.75, -$484.50. `SELL_HALF_HOOD`: $4,504.75 proceeds plus 38 shares at $115.29 = $8,885.77, -$245.48.
- The fixed larger-trim alternative led the real path by $40.47; the real path led full retention by $198.55 after the later management trim. The $117.50 residual review remained active; the $98.80 hard invalidation was not reached.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: HOOD close `$113.33`; the after-close quote was wide at `$109.17/$120.65`, so the bar is a disclosed non-executable proxy.
- Real path, including the separate 20-share 2026-09-09 management trim: `$3,049.60 + $2,337.00` proceeds plus 30 shares worth `$3,399.90` = `$8,786.50`, incremental P/L `-$344.75` versus the `$9,131.25` pre-trade reference. `HOLD_FULL_HOOD`: `$8,499.75` (`-$631.50`); `SELL_HALF_HOOD`: `$8,811.29` (`-$319.96`).
- The larger fixed half-trim led the real path by `$24.79`; the real path led full retention by `$286.75`. The `$117.50` residual review remained active, while the `$98.80` hard invalidation and `$112.50-$113.20` structural close failure were not confirmed. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: HOOD close `$112.59`; this is a disclosed non-executable proxy because no synchronized closing quote was preserved.
- Real path, including the separate later 20-share management trim: `$3,049.60 + $2,337.00` proceeds plus 30 shares worth `$3,377.70` = `$8,764.30`, incremental P/L `-$366.95` versus the `$9,131.25` pre-trade reference. `HOLD_FULL_HOOD`: `$8,444.25` (`-$687.00`); `SELL_HALF_HOOD`: `$8,783.17` (`-$348.08`).
- The fixed half-trim led the real path by `$18.87`, while the real path led full retention by `$320.05`. The close sits inside the structural review band; no hard invalidation was reached. Comparison complete; no lesson change.
