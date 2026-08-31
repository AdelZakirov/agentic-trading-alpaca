# Ghost set: alpaca-stage2-20260831-PCG-buy

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260831-PCG-buy`
- Broker order ID: `96895785-d9f4-4134-9a2e-e063533e2203`
- Ticker: PCG
- Decision time: 2026-08-31T16:58:44Z
- First fill time: 2026-08-31T16:59:10.06429999Z
- Evaluation start: 2026-08-31T16:59:10.06429999Z
- Evaluation end: 2026-09-04 regular-market close
- Checkpoints: 2026-09-01, 2026-09-02, 2026-09-03, and 2026-09-04 regular-market closes
- Holding plan: tactical one-week mean-reversion trade; review no later than 2026-09-04
- Invalidation: daily close below $12.80, adverse credit action, material wildfire escalation, or evidence that regulatory-risk selling is continuing rather than exhausted
- Target zone: $14.70–$15.20

## Thesis and sizing

PCG fell roughly 19% after California wildfire-liability protections disappointed the market. The real trade tests whether the extreme-volume gap represents short-horizon capitulation while operating earnings and discounted valuation remain intact. Position size was limited to about 10% of equity because wildfire, regulatory, and credit risks can gap discontinuously and the moneyheap technical lane was unavailable.

## Contemporaneous market data

- Stock source: Alpaca IEX latest quote.
- PCG decision quote at 2026-08-31T16:58:44.191384951Z: bid $13.41, ask $13.42, bid size 2,100, ask size 3,800.
- Earlier alternative-definition stock quote at 2026-08-31T16:56:40.336565217Z: bid $13.39, ask $13.40.
- Option source: Alpaca indicative option snapshot.
- `PCG260911C00013500` at 2026-08-31T16:56:35.854732017Z: bid $0.47, ask $0.53, bid size 13, ask size 7, last $0.54, IV 58.46%, delta 0.4939, gamma 0.2934, theta -0.0253, vega 0.0093.

## Real path

- Instrument: PCG common stock
- Side and quantity: BUY 750 shares
- Actual fill: 750 shares at $13.42
- Initial capital deployed: $10,065.00
- Maximum loss: $10,065.00 in the theoretical total-loss case; the planned price invalidation is not a guaranteed exit price
- Pre-trade exposure: none
- Exit handling: manage from live evidence under the trading and risk policies; do not assume an automatic stop exists

## Ghost alternatives

### NO_TRADE

- Question: Should any PCG exposure have been added after the gap?
- Instrument: cash / no trade
- Entry rule: remain uninvested at the real fill time
- Simulated entry: $0
- Capital at risk: $0
- Maximum loss: $0
- P/L: starts and remains $0
- Exit handling: none

### HALF_SIZE_STOCK

- Question: Was the selected stock size too large or too small?
- Instrument: PCG common stock
- Side and quantity: BUY 375 shares
- Entry rule: buy at the executable ask observable when alternatives were defined
- Simulated entry price: $13.40
- Simulated initial cost: $5,025.00
- Maximum loss: $5,025.00 in the theoretical total-loss case
- Invalidation and exit handling: identical to the real stock path

### SEP11_13_5_CALL

- Question: Would defined-risk calls provide better one-week capital efficiency than stock?
- Instrument: 20 long `PCG260911C00013500` calls
- Side and quantity: BUY 20 contracts
- Entry rule: buy at the contemporaneous executable ask
- Simulated entry price: $0.53 per share, or $53 per contract
- Simulated premium: $1,060.00
- Maximum loss: $1,060.00 plus fees
- Initial delta-equivalent exposure: approximately 987.8 shares, using delta 0.4939
- Option assumptions: IV 58.46%, theta -0.0253, no manufactured values for assignment or future volatility
- Exit handling: use conservative bid marks at common checkpoints; close or value consistently at the common 2026-09-04 endpoint, before the 2026-09-11 expiration

## Tracking rules

At every checkpoint, use one common observation timestamp. Mark the real and half-size stock paths from the same live stock bid if still open. Mark the long-call path at its executable bid. Record P/L, percentage return, capital at risk, drawdown when available, liquidity, spread, time decay, and volatility effects. The ghost paths never reach Alpaca and never enter portfolio exposure, buying power, or risk calculations.
