# Ghost set: alpaca-stage2-20260901-SLB-buy

- Status: COMPLETE
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

## Catch-up checkpoint for 2026-09-01 close

- Observed: approximately 2026-09-02T16:28:06Z. The scheduled prior-close checkpoint was missed; current executable marks are used consistently.
- Real SLB stock: OPEN, $58.05 bid; value $4,644; P/L approximately -$15.37 (-0.33%).
- `NO_TRADE`: $0.
- `HALF_SIZE_SLB`: value $2,322; P/L -$8.40 (-0.36%).
- `SEP11_58_62_CALL_SPREAD`: executable value $0.95 ($1.25 long-call bid less $0.30 short-call ask); P/L -$25 (-20.83%) versus $1.20 entry. Long IV/delta/theta 34.29%/0.5244/-0.0721; short 37.17%/0.1397/-0.0426.
- No $56.90 invalidation or $60.20 target was triggered. Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using the current Alpaca IEX executable bid and focused indicative option marks. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real SLB stock: 80 shares at the $58.72 bid; value $4,697.60; P/L +$38.23 (+0.82%) versus the $58.242124 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_SLB`: 40 shares at $58.72; P/L +$18.40 (+0.79%) versus the $58.26 simulated entry.
- `SEP11_58_62_CALL_SPREAD`: executable value $1.25 ($1.51 long-call bid less $0.26 short-call ask); P/L +$5 (+4.17%) versus the $1.20 simulated debit.
- No $56.90 invalidation or $60.20 target was triggered. Next checkpoint: 2026-09-03 regular-market close.

## 2026-09-03 close checkpoint

- Observed from Alpaca at approximately `2026-09-03T19:59:59Z`: SLB $57.41/$57.43; Sep. 11 $58 call $0.79/$1.02; Sep. 11 $62 call $0.10/$0.14.
- Real SLB stock: OPEN, 80 shares at $57.41; value $4,592.80; P/L -$66.57 (-1.43%) versus the $58.242124 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_SLB`: 40 shares at $57.41; P/L -$34.00 (-1.46%).
- `SEP11_58_62_CALL_SPREAD`: executable value $0.65 ($0.79 long-call bid less $0.14 short-call ask); P/L -$55 (-45.83%) versus the $1.20 simulated debit.
- The $56.90 invalidation and $60.20 target were not triggered. Next and final checkpoint: 2026-09-04 regular-market close.

## Real-path exit — 2026-09-04

- The 2026-09-04 session opened below $56.90 and failed to reclaim $57.05. The real path sold all 80 shares at an average $56.62 at `2026-09-04T14:47:37.047510754Z`.
- Realized P/L was approximately -$129.77 before fees versus the $58.242124 entry. The common evaluation still completes at the 2026-09-04 close, when the alternatives will be marked consistently.
- Separate exit-decision comparison: [`../2026-09-04/alpaca-stage2-20260904-SLB-sell.md`](../2026-09-04/alpaca-stage2-20260904-SLB-sell.md).

## 2026-09-04 close completion

- Endpoint quote: SLB $57.50/$57.52 at `2026-09-04T19:59:59.996801485Z`.
- Real stock: CLOSED at $56.62; realized P/L about -$129.77 (-2.79%). `NO_TRADE`: $0. `HALF_SIZE_SLB`: under the identical invalidation, 40 shares exit at $56.62 for -$65.60 (-2.81%).
- `SEP11_58_62_CALL_SPREAD`: no synchronized executable close was recoverable. Last-trade-bar references were $0.72 for the $58 call and a stale $0.10 for the $62 call, so the endpoint is UNSCORABLE rather than manufacturing a spread value.
- Outcome: no-trade beat the bullish entry; reducing size only scaled the same losing thesis. The breakout shelf failed within the planned window.
- Decision review: thesis/research was reasonable but forecast failed; stock was cleaner than the wide option alternative; entry timing was early; size and execution were disciplined. No new durable lesson beyond existing invalidation and option-overlap guidance.
