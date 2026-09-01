# Ghost set: alpaca-stage2-20260901-SLB-buy

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260901-SLB-buy`
- Broker order ID: `db61b37c-6fcb-4dbc-a39f-672bbc8be16c`
- Ticker: SLB
- Decision time: 2026-09-01T15:02:16.737456017Z
- First fill time: 2026-09-01T15:02:22.008309992Z
- Evaluation start: 2026-09-01T15:02:22.008309992Z
- Evaluation end: 2026-09-04 regular-market close
- Checkpoints: 2026-09-01, 2026-09-02, 2026-09-03, and 2026-09-04 regular-market closes
- Holding plan: tactical bullish pullback trade for up to five sessions
- Invalidation: break or close below $56.90, with the $57.30-$57.42 breakout shelf as the key support test
- Targets: $60.20-$60.50 first trim; $61.80-$62.50 runner

## Thesis and sizing

SLB's high-volume breakout remained technically sponsored, and the live pullback reached the researched $57.90-$58.70 entry band. The trade tests whether breakout support holds and price retests the recent high over the one-week window. Size was limited to 80 shares, approximately $4,665 notional, with planned stop risk near $114 before slippage.

- Instrument: SLB common stock
- Side and quantity: BUY 80 shares
- Actual fill: 80 shares at average $58.242124
- Initial capital deployed: approximately $4,659.37
- Maximum loss: approximately $4,659.37 in the theoretical total-loss case; planned technical stop risk is approximately $107.37 from the actual fill to $56.90 before slippage
- Pre-trade exposure: none
- Exit handling: manage from live evidence; no automatic stop order was submitted

## Contemporaneous market data

- Stock source: Alpaca IEX latest quote at 2026-09-01T15:02:16.737456017Z: bid $58.23 / ask $58.26, bid size 100 / ask size 200.
- Option source: Alpaca indicative option snapshots at approximately 2026-09-01T15:00:41Z.
- `SLB260911C00058000`: bid $1.38 / ask $1.47, bid size 45 / ask size 88, IV 32.12%, delta 0.5578, theta -0.0643.
- `SLB260911C00062000`: bid $0.27 / ask $0.37, bid size 149 / ask size 489, IV 37.21%, delta 0.1712, theta -0.0466.

## Real path

- The 80-share stock order was confirmed `filled` for 80/80 at $58.242124. The initial stock mark at the decision quote was approximately $4,658.40 at the bid.
- Stock was selected over options because the stock permits direct stop/target management without the call spread's wide short leg and theta decay.

## Ghost alternatives

### NO_TRADE

- Question: Was the bullish pullback risk worth adding to the portfolio?
- Instrument: cash / no trade
- Entry rule: retain cash at the real decision time
- Simulated entry: $0
- Capital at risk: $0
- P/L: starts and remains $0
- Exit handling: none

### HALF_SIZE_SLB

- Question: Was 80 shares too large or too small for the one-week thesis?
- Instrument: SLB common stock
- Side and quantity: BUY 40 shares at the contemporaneous $58.26 ask
- Simulated initial cost: $2,330.40
- Planned stop risk: approximately $54.40 to $56.90 before slippage
- Exit handling: identical $56.90 invalidation and $60.20-$60.50 / $61.80-$62.50 target handling

### SEP11_58_62_CALL_SPREAD

- Question: Would defined-risk leverage have improved the stock expression?
- Instrument: one Sep. 11 $58/$62 bull call debit spread
- Contracts: buy 1 `SLB260911C00058000` at the $1.47 ask and sell 1 `SLB260911C00062000` at the $0.27 bid
- Simulated executable debit: $1.20 per share, or $120.00 maximum loss before fees
- Maximum spread value: $400.00; maximum gross gain $280.00 before fees
- Greeks and IV: use the contemporaneous values above; do not manufacture missing values
- Exit/expiration handling: mark from executable bid/ask at the same checkpoints and close or value consistently at the common 2026-09-04 endpoint, before Sep. 11 expiration

## Tracking rules

Use one common market-data timestamp for the real stock path and all scoreable ghosts at each checkpoint. Mark long stock exits from the executable bid; mark the option spread from the executable side of each leg. Record open/closed status, P/L, percentage return, capital at risk, drawdown, time decay, IV, and liquidity. Ghosts never reach Alpaca and never affect portfolio totals, buying power, or risk posture.

