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

