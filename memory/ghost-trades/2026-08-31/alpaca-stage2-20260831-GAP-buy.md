# Ghost set: alpaca-stage2-20260831-GAP-buy

- Status: ACTIVE
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
