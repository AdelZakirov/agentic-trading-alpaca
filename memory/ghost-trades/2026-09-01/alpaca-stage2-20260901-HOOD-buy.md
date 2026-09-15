# Ghost set: alpaca-stage2-20260901-HOOD-buy

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260901-HOOD-buy`
- Broker order ID: `1bd84d34-24c6-4d66-857b-85cecdeaed71`
- Ticker: HOOD
- Decision time: 2026-09-01T16:53:47.866688788Z
- First fill time: 2026-09-01T16:53:50.588860122Z
- Evaluation start: 2026-09-01T16:53:50.588860122Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-01 through 2026-09-04 and 2026-09-08 through 2026-09-11 regular-market closes
- Holding plan: tactical bullish fundamental/technical trade for roughly one to two weeks
- Review level: daily close below $101
- Hard invalidation: $98.80
- Targets: $111.50-$112.45 first objective; $117.50-$121 extension

## Thesis and sizing

HOOD's revenue/margin momentum and emerging uptrend remained constructive after the underlying spread normalized across a full quote sequence. Size is 75 shares, $7,826.10 capital at the fill, with approximately $251.10 risk to the $101 review and $416.10 to hard invalidation before gaps/slippage.

- Instrument: HOOD common stock
- Side and quantity: BUY 75 shares
- Actual fill: 75 shares at average $104.348
- Initial capital deployed: $7,826.10
- Maximum loss: $7,826.10 in a theoretical total-loss case; planned hard-invalidation risk approximately $416.10
- Pre-trade HOOD exposure: none
- Exit handling: manage from live evidence; no automatic stop order was submitted

## Contemporaneous market data

- Stock source: Alpaca IEX latest quote at `2026-09-01T16:53:47.866688788Z`: bid $104.32 / ask $104.39, bid size 100 / ask size 100.
- Quote-validation sequence: $104.35/$104.56 at `16:49:24Z`, $104.27/$104.33 at `16:50:53Z`, and $104.30/$104.38 at `16:52:14Z`, all with positive displayed size.
- Option source: Alpaca indicative snapshots around `2026-09-01T16:49:59Z`–`16:50:04Z`.
- `HOOD260911C00107000`: bid $2.96 / ask $3.13, IV 59.67%, delta 0.4259, theta -0.2063.
- `HOOD260911C00115000`: bid $1.03 / ask $1.16, IV 62.58%, delta 0.1923, theta -0.1497.

## Real path

- The 75-share limit order was confirmed `filled` for 75/75 at average $104.348.
- Stock was selected because it permits direct management at $101/$98.80 without the call spread's theta and Sep. 11 expiry cliff.

## Ghost alternatives

### NO_TRADE

- Question: Was adding HOOD exposure better than retaining cash?
- Instrument: cash / no trade
- Simulated entry and capital at risk: $0
- P/L: starts and remains $0
- Exit handling: none

### HALF_SIZE_HOOD

- Question: Was 75 shares too large for the setup and correlated-growth portfolio risk?
- Instrument: HOOD common stock
- Side and quantity: BUY 37 shares at the contemporaneous $104.39 ask
- Simulated initial cost: $3,862.43
- Planned risk: approximately $125.43 to $101 and $206.83 to $98.80 before gaps/slippage
- Exit handling: identical review, invalidation, and target plan to the real trade

### SEP11_107_115_CALL_SPREAD

- Question: Would defined-risk leverage outperform stock for the same bullish thesis?
- Instrument: one Sep. 11 $107/$115 bull call debit spread
- Contracts: buy 1 `HOOD260911C00107000` at $3.13 ask and sell 1 `HOOD260911C00115000` at $1.03 bid
- Simulated executable debit and maximum loss: $2.10 per share, or $210 before fees
- Breakeven: $109.10; maximum spread value $800; maximum gross profit $590 before fees
- Exit/expiration handling: conservative executable marks at common checkpoints and final expiry handling on Sep. 11

## Tracking rules

Use one market-data timestamp for all scoreable paths at every checkpoint. Mark long stock at the executable bid and the spread from executable leg sides. Ghosts never reach Alpaca or affect portfolio state.

## Catch-up checkpoint for 2026-09-01 close

- Observed: approximately 2026-09-02T16:28:07Z; HOOD bid/ask $106.01/$106.09.
- Real HOOD stock: OPEN; value $7,950.75; P/L +$124.65 (+1.59%).
- `NO_TRADE`: $0.
- `HALF_SIZE_HOOD`: value $3,922.37; P/L +$59.94 (+1.55%).
- `SEP11_107_115_CALL_SPREAD`: executable value $2.23 ($3.41 long-call bid less $1.18 short-call ask); P/L +$13 (+6.19%) versus $2.10 entry.
- No $101 review or $98.80 invalidation was triggered. Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using the current Alpaca IEX executable bid, before the later HOOD management reduction. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real HOOD stock: 75 shares at the $122.55 bid; value $9,191.25; P/L +$1,365.15 (+17.44%) versus the $104.348 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_HOOD`: 37 shares at $122.55; value $4,534.35; P/L +$671.92 (+17.40%) versus the $104.39 simulated entry.
- `SEP11_107_115_CALL_SPREAD`: executable value $6.37 ($15.74 long-call bid less $9.37 short-call ask); P/L +$427 (+203.33%) versus the $2.10 simulated debit.
- The real stock had exceeded the documented $117.50-$121 extension target at this observation. After this checkpoint, the real path sold 25 shares at $121.984; the residual is 50 shares. Next checkpoint: 2026-09-03 regular-market close.

## Real-path target reduction — 2026-09-03

- At `2026-09-03T14:39:58.821160929Z`, the real path sold 25 of 75 shares at $121.984 after exceeding the $117.50-$121 extension target. Sale proceeds were $3,049.60; 50 shares remain.
- Initial post-fill observation at approximately `2026-09-03T14:41:15Z`: retained 50 shares at the $121.84 executable bid were worth $6,092.00. Sale proceeds plus retained value were $9,141.60, for cumulative real-path P/L of +$1,315.50 (+16.81%) versus the original $7,826.10 cost.
- The option and half-size alternatives were not redefined after the management action and remain scheduled for the common 2026-09-03 close checkpoint. The residual real stock now uses $117.50 as a profit-protection review level; the original $98.80 thesis invalidation remains the hard failure level.

## 2026-09-03 close checkpoint

- Observed from Alpaca at approximately `2026-09-03T19:59:59Z`: HOOD executable IEX bid $120.01; Sep. 11 $107 call $17.69/$18.33 and $115 call $10.97/$11.54.
- Real HOOD path: $3,049.60 realized sale proceeds plus 50 shares at $120.01, total value $9,050.10; cumulative P/L +$1,224.00 (+15.64%) versus the original $7,826.10 cost.
- `NO_TRADE`: $0.
- `HALF_SIZE_HOOD`: 37 shares at $120.01; value $4,440.37; P/L +$577.94 (+14.96%).
- `SEP11_107_115_CALL_SPREAD`: executable value $6.15 ($17.69 long-call bid less $11.54 short-call ask); P/L +$405 (+192.86%) versus the $2.10 debit.
- The daily close remained above the $117.50 residual profit-review level. Next checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 close checkpoint

- Common stock mark: $122.06 executable bid near the close.
- Real path: $3,049.60 sale proceeds plus 50 shares worth $6,103.00; total $9,152.60 and cumulative P/L +$1,326.50 (+16.95%). `NO_TRADE`: $0. `HALF_SIZE_HOOD`: 37 shares worth $4,516.22 and P/L +$653.79 (+16.93%).
- `SEP11_107_115_CALL_SPREAD`: last-trade bars imply a $7.23 reference value, but no synchronized executable sides were recovered; formally UNSCORABLE at this checkpoint.
- The $117.50 residual review remained intact. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $117.37; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real path after the prior 25-share sale: $3,049.60 proceeds plus 50 shares at $117.37 = $8,918.10, P/L +$1,092.00 versus the original $7,826.10 cost. `HALF_SIZE_STOCK`: 37 shares at $117.37 = $4,342.69, P/L +$480.26. `NO_TRADE`: $0.
- The option alternative remains formally UNSCORABLE without synchronized executable option sides. The $117.37 daily close activated the residual profit-review rule.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $115.29 (high $121.38, low $115.105); this is a non-executable proxy because the near-close quote was abnormally wide at $115.25/$120.99.
- Real path, including the separate 2026-09-09 20-share management trim: $3,049.60 + $2,337.00 prior proceeds plus 30 shares at $115.29 = $8,845.30, P/L +$1,019.20 versus the $7,826.10 initial cost. `HALF_SIZE_HOOD`: 37 shares at $115.29 = $4,265.73, P/L +$403.30. `NO_TRADE`: $0.
- The $117.50 residual review remained active; the $101 review and $98.80 hard invalidation were not reached. The option alternative remains UNSCORABLE without synchronized executable option sides.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: HOOD close `$113.33`; the after-close quote was wide at `$109.17/$120.65`, so the bar is a disclosed non-executable proxy.
- Real path, including the separate 25-share and 20-share management trims: `$3,049.60 + $2,337.00` proceeds plus 30 shares worth `$3,399.90` = `$8,786.50`, P/L `+$960.40` versus the `$7,826.10` entry cost. `HALF_SIZE_HOOD`: 37 shares worth `$4,193.21`, P/L `+$330.78`; `NO_TRADE`: `$0`.
- The residual close stayed above the `$112.50-$113.20` structural review band; the $101 review and $98.80 hard invalidation were not reached. The option path remains UNSCORABLE without synchronized executable close sides. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: HOOD close `$112.59`; this is a disclosed non-executable proxy because no synchronized closing quote was preserved.
- Real path: `$3,049.60 + $2,337.00` proceeds plus 30 shares worth `$3,377.70` = `$8,764.30`, P/L `+$938.20` versus the `$7,826.10` entry cost. `HALF_SIZE_HOOD`: 37 shares worth `$4,165.83`, P/L `+$303.40`; `NO_TRADE`: `$0`.
- The real path led the half-size alternative by `$634.80`. The close sits inside the documented `$112.50-$113.20` structural review band; the $101 review and $98.80 hard invalidation were not reached. The option path remains UNSCORABLE. Comparison complete; no lesson change.
