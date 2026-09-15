# Ghost set: alpaca-stage2-20260908-GTLB-sell

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260908-GTLB-sell`
- Broker order ID: `221a2143-357f-44eb-8ff2-0b62f7bb6ab5`
- Ticker: GTLB
- Decision time: approximately 2026-09-08T14:42:00Z
- Fill time: 2026-09-08 regular session
- Evaluation start: actual fill time
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-08 through 2026-09-11 regular-market closes
- Holding plan tested: full exit after tactical support failed versus retaining exposure into the gap-fill zone

## Thesis and real path

Fresh moneyheap research classified the post-earnings shelf break as short-term distribution and an active gap-fill. The prior $48.40 tactical invalidation failed; $48.90-$49.80 became resistance and $44.50-$46.65 became the next credible stabilization area.

- Pre-trade exposure: 150 GTLB shares at $50.80 average.
- Actual action: sell all 150 shares at $47.42.
- Actual proceeds: $7,113.00 before fees.
- Realized P/L: approximately -$507.00 before fees.
- Size rationale: remove all broken-thesis exposure rather than preserve an arbitrary residual.

## Contemporaneous market data

- Initial preflight at `2026-09-08T14:42:41.784739126Z` was abnormal at $45.34/$47.43.
- Two later quotes normalized: $47.41/$47.45 and $47.41/$47.46 with positive displayed size; these supported a bounded limit order.
- Fresh research: [`163732-GTLB-technical.md`](../../research/2026-09-08/163732-GTLB-technical.md).

## Ghost alternatives fixed before submission

### HOLD_FULL

- Retain all 150 shares through 2026-09-11 close, exiting earlier only on a daily close below $44.46.
- Reference baseline: $47.41 executable bid.

### HALF_EXIT

- Sell 75 shares at $47.41 and retain 75 under the same $44.46 failure and endpoint.
- Simulated sale proceeds: $3,555.75.

### REAL_FULL_EXIT

- Actual sale of all 150 shares at $47.42; proceeds $7,113.00.

## Tracking rules

Use one common quote timestamp at every checkpoint, include proceeds for exited paths, and mark retained shares at the conservative executable bid. Ghosts never reach Alpaca or affect portfolio state.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $47.15; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- `REAL_FULL_EXIT`: $7,113.00 actual proceeds. `HOLD_FULL`: 150 shares worth $7,072.50, trailing real by $40.50. `HALF_EXIT`: $3,555.75 proceeds plus 75 shares worth $3,536.25 = $7,092.00, trailing real by $21.00.
- The real full exit led both retained-exposure paths at the first scheduled close.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $46.345; this is a non-executable proxy because the near-close quote was abnormally wide at $45.66/$49.19.
- `REAL_FULL_EXIT`: $7,113.00 actual proceeds. `HOLD_FULL`: 150 shares at $46.345 = $6,951.75, trailing real by $161.25. `HALF_EXIT`: $3,555.75 proceeds plus 75 shares at $46.345 = $7,031.63, trailing real by $81.38.
- The $44.46 failure level was not breached by the close; the real full exit continued to lead both retained-exposure paths. Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: GTLB close `$47.285`; the after-close quote was wide at `$44.97/$49.40`, so the bar is a disclosed non-executable proxy.
- `REAL_FULL_EXIT` remains fixed at `$7,113.00`. `HOLD_FULL`: 150 shares at the close proxy = `$7,092.75`, trailing real by `$20.25`; `HALF_EXIT`: `$3,555.75` proceeds plus 75 shares worth `$3,546.38` = `$7,102.13`, trailing real by `$10.88`.
- The `$44.46` failure level was not breached by the close; the real full exit still leads both retained-exposure paths. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: GTLB close `$46.99`; this is a disclosed non-executable proxy.
- `REAL_FULL_EXIT` remains fixed at `$7,113.00`, or `+$1.50` versus the `$7,111.50` decision-time reference. `HOLD_FULL`: 150 shares worth `$7,048.50`, or `-$63.00`; `HALF_EXIT`: `$3,555.75` proceeds plus 75 shares worth `$3,524.25` = `$7,080.00`, or `-$31.50`.
- The real full exit led `HOLD_FULL` by `$64.50` and `HALF_EXIT` by `$33.00`. The `$44.46` failure level was not breached by the close. Comparison complete; no lesson change.
