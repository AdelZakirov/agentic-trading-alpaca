# Ghost set: alpaca-stage2-20260831-GAP-buy

- Status: COMPLETE
- Real client order ID: `alpaca-stage2-20260831-GAP-buy`
- Broker order ID: `71e19ef0-330e-4f7a-ba13-2158a7a8c941`
- Ticker: GAP
- Decision time: 2026-08-31T18:01:19Z
- First fill time: 2026-08-31T18:06:28.092663151Z
- Evaluation start: 2026-08-31T18:06:28.092663151Z
- Evaluation end: 2026-09-04 regular-market close
- Checkpoints: 2026-09-01, 2026-09-02, 2026-09-03, and 2026-09-04 regular-market closes
- Holding plan: tactical post-earnings continuation trade; review no later than 2026-09-04
- Invalidation: daily close below $21.60
- Targets: $23.85–$24.00 first target; $25.20 continuation target

## Thesis and sizing

GAP's Q2 earnings beat and margin resilience cleared the binary earnings event. The current $22.54/$22.55 market is a supported retest after the breakout, with positive free cash flow, substantial cash per share, elevated short interest, and no immediate earnings print. The real trade tests a one-week bullish continuation while keeping total portfolio cash above approximately 85% and diversifying away from PCG's utility/regulatory risk.

- Instrument: GAP common stock
- Side and quantity: BUY 200 shares
- Actual fill: 200 shares at $22.55
- Initial capital deployed: $4,510.00
- Maximum loss: $4,510.00 in the theoretical total-loss case; planned price invalidation risk is approximately $190 before slippage
- Pre-trade GAP exposure: none
- Size rationale: approximately 4.5% of equity at entry; combined PCG and GAP exposure remains near 14.6% of equity and estimated post-trade cash retention is approximately 85.3%
- Exit handling: manage from live evidence under the trading and risk policies; no automatic stop was submitted

## Contemporaneous market data

- Stock source: Alpaca IEX latest quotes.
- Decision snapshot at 2026-08-31T18:01:19Z: GAP bid $22.54 / ask $22.55, bid size 800, ask size 400; PYPL bid $53.27 / ask $53.29, bid size 300, ask size 600; VISN bid $6.34 / ask $6.35, bid size 30,000, ask size 16,900.
- Post-fill snapshot at 2026-08-31T18:07:14Z: GAP bid $22.56 / ask $22.57; PCG bid $13.58 / ask $13.59.
- GAP options source: Alpaca indicative snapshots at approximately 2026-08-31T18:00Z. Sep. 11 `GAP260911C00022500` bid $0.56 / ask $0.69 and `GAP260911C00024000` bid $0.08 / ask $0.25; the executable stock market was materially cleaner.

## Real path

- Stock decision: BUY 200 shares; Alpaca confirmed `filled` for 200/200 at $22.55.
- Technical/fundamental plan: hold through 2026-09-04 unless daily close below $21.60, trim into $23.85–$24.00, and consider continuation management toward $25.20.
- Current post-fill mark: $22.56; market value $4,512.00; unrealized P/L +$2.00 at final reconciliation.

## Ghost alternatives

### NO_TRADE

- Question: Should any new exposure have been added after the shortlist scan?
- Instrument: cash / no trade
- Entry rule: remain uninvested at the real decision time
- Simulated entry: $0
- Capital at risk: $0
- Maximum loss: $0
- P/L: starts and remains $0
- Exit handling: none

### HALF_SIZE_GAP

- Question: Was 200 shares too large or too small for the GAP thesis?
- Instrument: GAP common stock
- Side and quantity: BUY 100 shares
- Entry rule: buy at the contemporaneous executable ask
- Simulated entry price: $22.55
- Simulated initial cost: $2,255.00
- Planned invalidation risk: approximately $95 before slippage at the $21.60 daily-close level
- Maximum loss: $2,255.00 in the theoretical total-loss case
- Exit handling: identical to the real GAP path

### PYPL_STOCK

- Question: Was PYPL's M&A-unwind rebound a better candidate than GAP for the same one-week risk budget?
- Instrument: PYPL common stock
- Side and quantity: BUY 90 shares
- Entry rule: buy at the contemporaneous executable ask
- Simulated entry price: $53.29
- Simulated initial cost: $4,796.10
- Planned invalidation risk: approximately $170.10 before slippage at the $51.40 daily-close level
- Target: $55.80–$57.00
- Maximum loss: $4,796.10 in the theoretical total-loss case
- Exit handling: daily-close invalidation and target management on the same common checkpoints

### VISN_STOCK

- Question: Was the higher-upside special-dividend dislocation a better candidate than GAP despite greater structural risk?
- Instrument: VISN common stock
- Side and quantity: BUY 500 shares
- Entry rule: buy at the contemporaneous executable ask
- Simulated entry price: $6.35
- Simulated initial cost: $3,175.00
- Planned invalidation risk: approximately $225.00 before slippage at the $5.90 daily-close level
- Target: $7.20–$7.50
- Maximum loss: $3,175.00 in the theoretical total-loss case
- Exit handling: daily-close invalidation and target management on the same common checkpoints; options were excluded because special-distribution contract adjustments impair comparability and liquidity

## Tracking rules

At every checkpoint, use one common observation timestamp for the real path and all scoreable ghosts. Mark long stock exits from the same live bid and entry from the documented contemporaneous ask. Record open/closed status, current or exit value, dollar and percentage P/L, capital at risk, drawdown, liquidity, and any triggered invalidation or target. The no-trade path remains at zero; ghost paths never reach Alpaca and never affect portfolio exposure, buying power, or risk calculations.

- Pricing assumptions: conservative executable marks; no fees or slippage modeled unless later documented.
- Missing data: no missing entry quote data; future checkpoint data is not yet available.
- Lesson review: deferred until the common evaluation window completes.

## Catch-up checkpoint for 2026-09-01 close

- Observed: approximately 2026-09-02T16:28:04Z. The scheduled prior-close checkpoint was missed; all paths use this disclosed catch-up observation.
- Real GAP: OPEN, $22.25 executable bid; value $4,450; P/L -$60 (-1.33%).
- `NO_TRADE`: $0.
- `HALF_SIZE_GAP`: value $2,225; P/L -$30 (-1.33%).
- `PYPL_STOCK`: $54.10 bid; value $4,869; P/L +$72.90 (+1.52%).
- `VISN_STOCK`: $6.33 bid; value $3,165; P/L -$10 (-0.31%).
- No invalidation or target was triggered at the observation. Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using the current Alpaca IEX executable bid. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real GAP: OPEN, 200 shares at the $22.22 bid; value $4,444; P/L -$66 (-1.46%) versus the $22.55 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_GAP`: 100 shares at $22.22; P/L -$33 (-1.46%) versus the $22.55 simulated ask entry.
- `PYPL_STOCK`: 90 shares at the $54.19 bid; value $4,877.10; P/L +$81.00 (+1.69%) versus the $53.29 simulated entry.
- `VISN_STOCK`: 500 shares at the $6.45 bid; value $3,225.00; P/L +$50.00 (+1.57%) versus the $6.35 simulated entry.
- No GAP invalidation or target was triggered. Next checkpoint: 2026-09-03 regular-market close.

## 2026-09-03 close checkpoint

- Observed from Alpaca IEX at approximately `2026-09-03T19:59:59Z`; all stock paths use the contemporaneous executable bid.
- Real GAP: OPEN, 200 shares at $22.31; value $4,462; P/L -$48 (-1.06%) versus the $22.55 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_GAP`: 100 shares at $22.31; P/L -$24 (-1.06%).
- `PYPL_STOCK`: 90 shares at $56.81; value $5,112.90; P/L +$316.80 (+6.61%).
- `VISN_STOCK`: 500 shares at $6.37; value $3,185; P/L +$10 (+0.31%).
- No GAP invalidation or target was triggered. Next checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 close completion

- Observed from Alpaca IEX at `2026-09-04T19:59:59.999695116Z`: GAP $22.41/$22.43 and PYPL $54.93/$54.95. VISN had no usable close quote; its official IEX close was $6.395 and is used only as a disclosed non-executable proxy.
- Real GAP: 200 shares at $22.41; value $4,482 and P/L -$28 (-0.62%). `HALF_SIZE_GAP`: P/L -$14 (-0.62%). `NO_TRADE`: $0.
- `PYPL_STOCK`: 90 shares at $54.93; value $4,943.70 and P/L +$147.60 (+3.08%). `VISN_STOCK`: proxy value $3,197.50 and proxy P/L +$22.50 (+0.71%); formally UNSCORABLE at an executable endpoint.
- Outcome: PYPL clearly outperformed GAP; no-trade modestly outperformed GAP; the full and half GAP sizes had the same percentage result and neither invalidation nor target fired.
- Decision review: earnings thesis and stock selection were plausible but opportunity ranking was mixed; timing did not capture follow-through; size and execution were disciplined; no option-selection issue was tested. One modest underperformance does not justify a durable lesson change.
