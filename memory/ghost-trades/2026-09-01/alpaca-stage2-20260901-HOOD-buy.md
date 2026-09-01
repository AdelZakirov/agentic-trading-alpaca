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

