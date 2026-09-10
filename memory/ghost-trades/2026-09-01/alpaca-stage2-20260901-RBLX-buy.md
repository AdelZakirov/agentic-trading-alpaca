# Ghost set: alpaca-stage2-20260901-RBLX-buy

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260901-RBLX-buy`
- Broker order ID: `50e20244-c806-4b7f-a0a3-2c11114c24eb`
- Ticker: RBLX
- Decision time: 2026-09-01T16:53:27.438441684Z
- First fill time: 2026-09-01T16:53:30.128337357Z
- Evaluation start: 2026-09-01T16:53:30.128337357Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-01 through 2026-09-04 and 2026-09-08 through 2026-09-11 regular-market closes
- Holding plan: tactical bullish breakout-retest trade for roughly one to two weeks
- Invalidation: loss or daily close below $38.90
- Targets: $42.50-$43.00 first objective; $45.00-$45.75 extension

## Thesis and sizing

The RBLX breakout retest held support and live liquidity normalized. The trade tests whether the retest can resolve into a continuation leg. Size is 250 shares, approximately $10,102.50 capital at the actual fill, with about $377.50 planned loss to $38.90 before gaps/slippage.

- Instrument: RBLX common stock
- Side and quantity: BUY 250 shares
- Actual fill: 250 shares at average $40.41
- Initial capital deployed: $10,102.50
- Maximum loss: $10,102.50 in a theoretical total-loss case; planned technical risk approximately $377.50
- Pre-trade RBLX exposure: none
- Exit handling: manage from live evidence; no automatic stop order was submitted

## Contemporaneous market data

- Stock source: Alpaca IEX latest quote at `2026-09-01T16:53:27.438441684Z`: bid $40.39 / ask $40.41, bid size 100 / ask size 100.
- Option source: Alpaca indicative snapshots around `2026-09-01T16:49:36Z`–`16:49:58Z`.
- `RBLX260918C00040000`: bid $2.11 / ask $2.37, IV 57.63%, delta 0.5627, theta -0.0603.
- `RBLX260918C00045000`: bid $0.58 / ask $0.71, IV 60.12%, delta 0.2262, theta -0.0472.

## Real path

- The 250-share limit order was confirmed `filled` for 250/250 at $40.41.
- Stock was selected because support-based management is cleaner than accepting IV, theta, and the Sep. 18 expiry constraint.

## Ghost alternatives

### NO_TRADE

- Question: Was adding RBLX exposure better than retaining cash?
- Instrument: cash / no trade
- Simulated entry and capital at risk: $0
- P/L: starts and remains $0
- Exit handling: none

### HALF_SIZE_RBLX

- Question: Was 250 shares too large for the setup and correlated-growth portfolio risk?
- Instrument: RBLX common stock
- Side and quantity: BUY 125 shares at the contemporaneous $40.41 ask
- Simulated initial cost: $5,051.25
- Planned stop risk: approximately $188.75 to $38.90 before gaps/slippage
- Exit handling: identical invalidation and target plan to the real trade

### SEP18_40_45_CALL_SPREAD

- Question: Would defined-risk leverage outperform stock for the same bullish thesis?
- Instrument: one Sep. 18 $40/$45 bull call debit spread
- Contracts: buy 1 `RBLX260918C00040000` at $2.37 ask and sell 1 `RBLX260918C00045000` at $0.58 bid
- Simulated executable debit and maximum loss: $1.79 per share, or $179 before fees
- Breakeven: $41.79; maximum spread value $500; maximum gross profit $321 before fees
- Exit/expiration handling: conservative executable marks at common checkpoints; close or value at the common endpoint before Sep. 18 expiration

## Tracking rules

Use one market-data timestamp for all scoreable paths at every checkpoint. Mark long stock at the executable bid and the spread from executable leg sides. Ghosts never reach Alpaca or affect portfolio state.

## Catch-up checkpoint for 2026-09-01 close

- Observed: approximately 2026-09-02T16:28:06Z. IEX stock quote was abnormally wide at $39.38/$41.46, so conservative bid marks are retained with an explicit quote-quality warning.
- Real RBLX stock: OPEN; value $9,845 at bid; P/L -$257.50 (-2.55%).
- `NO_TRADE`: $0.
- `HALF_SIZE_RBLX`: value $4,922.50; P/L -$128.75 (-2.55%).
- `SEP18_40_45_CALL_SPREAD`: executable value $1.16 ($1.67 long-call bid less $0.51 short-call ask); P/L -$63 (-35.20%) versus $1.79 entry.
- The $38.90 invalidation was not triggered by available trade/position evidence. Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using the current Alpaca IEX executable bid. The stock quote remained wide at $41.79/$42.35, so the conservative bid is used with an explicit liquidity warning; the scheduled 2026-09-02 close was unavailable.
- Real RBLX stock: 250 shares at the $41.79 bid; value $10,447.50; P/L +$345.00 (+3.42%) versus the $40.41 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_RBLX`: 125 shares at $41.79; P/L +$172.50 (+3.42%) versus the $40.41 simulated entry.
- `SEP18_40_45_CALL_SPREAD`: executable value $2.01 ($3.03 long-call bid less $1.02 short-call ask); P/L +$22 (+12.29%) versus the $1.79 simulated debit.
- The $38.90 invalidation was not triggered. Next checkpoint: 2026-09-03 regular-market close.

## 2026-09-03 close checkpoint

- Observed from Alpaca at approximately `2026-09-03T19:59:55Z`: RBLX IEX was unusually wide at $40.15/$43.88; Sep. 18 $40 call $2.52/$2.90 and $45 call $0.64/$0.84. Conservative executable sides are used with a liquidity warning.
- Real RBLX: 250 shares at $40.15; value $10,037.50; P/L -$65 (-0.64%) versus $40.41.
- `NO_TRADE`: $0.
- `HALF_SIZE_RBLX`: 125 shares at $40.15; P/L -$32.50 (-0.64%).
- `SEP18_40_45_CALL_SPREAD`: executable value $1.68 ($2.52 long-call bid less $0.84 short-call ask); P/L -$11 (-6.15%) versus the $1.79 debit.
- The regular-session high of $43.24 touched the $42.50-$43.00 first objective, but the close retraced to $41.465 and no real reduction occurred. The $38.90 invalidation remained intact. Next checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 real-path target reduction

- A fresh $42.50 reclaim activated the target plan. The real path sold 100 of 250 shares at average $42.515, realizing approximately $210.50 gross; 150 shares remain toward $45-$46 with $41.40 tactical support.
- This is a real-path change, not the scheduled close checkpoint. The entry alternatives remain fixed and the 2026-09-04 close checkpoint is still due at the actual close.
- Target-sale comparison: [`alpaca-stage2-20260904-RBLX-sell`](../2026-09-04/alpaca-stage2-20260904-RBLX-sell.md).

## 2026-09-04 close checkpoint

- Common stock mark: $43.29 executable bid at `2026-09-04T19:59:51.110903517Z`.
- Real path: $4,251.50 sale proceeds plus 150 shares worth $6,493.50; total $10,745.00 and P/L +$642.50 (+6.36%) versus initial cost. `NO_TRADE`: $0. `HALF_SIZE_RBLX`: value $5,411.25 and P/L +$360.00 (+7.13%).
- `SEP18_40_45_CALL_SPREAD`: 2026-09-04 last-trade bars imply a $2.65 reference spread value, but no synchronized executable sides were recovered; formally UNSCORABLE at this checkpoint.
- The real target reduction preserved a 150-share runner. No $38.90 invalidation fired. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $44.83; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real path: $4,251.50 prior proceeds plus 150 shares at $44.83 = $10,976.00, P/L +$873.50 versus $10,102.50 initial cost. `HALF_SIZE_STOCK`: $5,603.75, P/L +$552.50. `NO_TRADE`: $0.
- The option alternative remains formally UNSCORABLE without synchronized executable sides. RBLX remained above $41.40 and near, but below, the $45-$45.75 target zone at the close.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $44.52 (high $45.04, low $43.51); this is a non-executable proxy because no synchronized closing quote was preserved.
- Real path: $4,251.50 prior proceeds plus 150 shares at $44.52 = $10,929.50, P/L +$827.00 versus the $10,102.50 initial cost. `HALF_SIZE_RBLX`: 125 shares at $44.52 = $5,565.00, P/L +$513.75. `NO_TRADE`: $0.
- The $41.40 runner support and $38.90 invalidation were not breached by the close. The $45-$45.75 extension was touched intraday at the bar high but not confirmed as a closing outcome; the option path remains UNSCORABLE without executable leg sides.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at the common close timestamp `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: RBLX close `$44.85`; the after-close quote was wide at `$42.58/$47.41`, so the bar is a disclosed non-executable proxy.
- Real path after the earlier 100-share reduction: `$4,251.50` proceeds plus 150 shares worth `$6,727.50` = `$10,979.00`, P/L `+$876.50` versus the `$10,102.50` entry cost. `HALF_SIZE_RBLX`: `$5,606.25` value, P/L `+$555.00`; `NO_TRADE`: `$0`.
- The runner remained above `$41.40` and below the `$45.00-$45.75` extension. The option alternative remains UNSCORABLE without synchronized executable close sides. Next checkpoint: 2026-09-11 regular-market close.
