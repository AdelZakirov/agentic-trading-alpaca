# Ghost set: alpaca-stage2-20260909-HOOD-sell

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260909-HOOD-sell`
- Broker order ID: `8a4bde5d-4e10-4458-a51d-f3c3248f6b02`
- Ticker: HOOD
- Decision time: approximately 2026-09-09T16:17:00Z
- Fill time: `2026-09-09T16:21:09.569022042Z`
- Evaluation start: `2026-09-09T16:21:09.569022042Z`
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-09, 2026-09-10, and 2026-09-11 regular-market closes
- Holding plan tested: 40% review trim versus full retention, half reduction, or full exit

## Thesis and actual fill

HOOD's 2026-09-08 daily close at $117.37 activated its documented $117.50 residual profit review. Moneyheap technical research favored trimming 33%-50% after the failed $125.25 extension, while fundamentals supported retaining a smaller core rather than abandoning a profitable long-term thesis.

- Pre-trade exposure: 50 shares at $104.342 average.
- Actual action: sell 20 shares at $116.85; proceeds $2,337.00 before fees.
- Residual: 30 shares at the broker's unchanged $104.342 average.
- Residual review: structural close failure around $112.50-$113.20; reclaim target $120-$121.40.

## Contemporaneous market data

- Preflight normalized IEX quote: $116.87/$116.94 at `2026-09-09T16:17:00Z`.
- Final pre-fill quote: $116.85/$116.93 at `2026-09-09T16:21:08.584230237Z`.
- The bounded $116.85 day limit filled in full without replacement.

## Ghost alternatives fixed before submission

### HOLD_50

- Retain all 50 shares through the common endpoint under the same review levels.

### SELL_HALF_25

- Sell 25 shares at the $116.87 preflight bid and retain 25 under the same review levels; simulated proceeds $2,921.75.

### SELL_ALL_50

- Sell all 50 shares at the $116.87 preflight bid; simulated proceeds $5,843.50.

### REAL_SELL_20

- Actual sale of 20 at $116.85, retaining 30 shares.

## Initial observation

- Common pre-trade reference: 50 shares at $116.87 = $5,843.50.
- `REAL_SELL_20`: $2,337.00 proceeds plus 30 shares at the $116.84 post-fill bid = $5,842.20, incremental -$1.30.
- `HOLD_50`: 50 shares at $116.84 = $5,842.00, incremental -$1.50.
- `SELL_HALF_25`: $2,921.75 proceeds plus 25 shares at $116.84 = $5,842.75, incremental -$0.75.
- `SELL_ALL_50`: $5,843.50 fixed proceeds, incremental $0.
- Initial differences are execution noise, not decision quality. Ghosts never reach Alpaca or affect portfolio state.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $115.29; this is a non-executable proxy because the near-close quote was abnormally wide at $115.25/$120.99. The common pre-trade reference remains $5,843.50.
- `REAL_SELL_20`: $2,337.00 proceeds plus 30 shares at $115.29 = $5,795.70, incremental P/L -$47.80. `HOLD_50`: $5,764.50, -$79.00. `SELL_HALF_25`: $2,921.75 proceeds plus 25 shares at $115.29 = $5,804.00, -$39.50. `SELL_ALL_50`: $5,843.50, $0.
- The half reduction led the real path by $8.30, while full exit led it by $47.80. The $112.50-$113.20 structural review remained active; no new lesson is supported.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: HOOD close `$113.33`; the after-close quote was wide at `$109.17/$120.65`, so the bar is a disclosed non-executable proxy.
- `REAL_SELL_20`: `$2,337.00` proceeds plus 30 shares worth `$3,399.90` = `$5,736.90`, incremental P/L `-$106.60` versus the `$5,843.50` pre-trade reference. `HOLD_50`: `$5,666.50` (`-$177.00`); `SELL_HALF_25`: `$5,755.00` (`-$88.50`); `SELL_ALL_50`: `$5,843.50` (`$0`).
- The fixed half-trim led the real path by `$18.10`, while full exit led it by `$106.60`. The residual review remained active and the structural band was not decisively broken. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: HOOD close `$112.59`; this is a disclosed non-executable proxy.
- `REAL_SELL_20`: `$2,337.00` proceeds plus 30 shares worth `$3,377.70` = `$5,714.70`, incremental P/L `-$128.80`. `HOLD_50`: `$5,629.50` (`-$214.00`); `SELL_HALF_25`: `$5,736.50` (`-$107.00`); `SELL_ALL_50`: `$5,843.50` (`$0`).
- The fixed half-trim led the real path by `$21.80`, while full exit led it by `$128.80`. The close sits inside the `$112.50-$113.20` structural review band. Comparison complete; no lesson change.
