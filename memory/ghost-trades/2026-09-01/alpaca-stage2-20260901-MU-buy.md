# Ghost set: alpaca-stage2-20260901-MU-buy

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260901-MU-buy`
- Broker order ID: `5b38c8ed-64d1-4efe-ac7d-b68c5a4dc97d`
- Ticker: MU
- Decision time: 2026-09-01T16:53:31.397109491Z
- First fill time: 2026-09-01T17:23:58.05634105Z
- Evaluation start: 2026-09-01T17:23:58.05634105Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-01 through 2026-09-04 and 2026-09-08 through 2026-09-11 regular-market closes
- Holding plan: bullish pullback trade for roughly one to two weeks
- Tight invalidation: loss or daily close below $922
- Structural thesis failure: $900.50
- Targets: $985, then $1,005-$1,012

## Thesis and sizing

MU's strong fundamental case and technical support plan justified a bounded pullback entry at $940 without chasing. The order rested until the market reached the researched zone. Size is 12 shares, approximately $11,279.96 at the actual fill, with planned risk of about $215.96 to $922 before gaps/slippage.

- Instrument: MU common stock
- Side and quantity: BUY 12 shares
- Actual fill: 12 shares at average $939.996667
- Initial capital deployed: approximately $11,279.96
- Maximum loss: approximately $11,279.96 in the theoretical total-loss case; planned tight-invalidation risk approximately $215.96
- Pre-trade MU exposure: none
- Exit handling: manage from live evidence; no automatic stop order was submitted

## Contemporaneous market data

- Original decision quote: Alpaca IEX bid $941.20 / ask $943.38, bid size 40 / ask size 40, at `2026-09-01T16:53:31.397109491Z`.
- Real entry rule: day limit $940; the order filled only after the market reached that bound.
- Fill: 12 shares at average $939.996667 at `2026-09-01T17:23:58.05634105Z`.
- Relevant option comparison at the original decision: the Sep. 18 $940/$1,010 call spread had a conservative debit near $27.38, or $2,738 maximum loss for one contract, and was rejected as too large for the intended thesis risk.

## Real path

- The 12-share limit order was confirmed `filled` for 12/12 at $939.996667.
- Stock was selected because the $940 pullback limit and $922 invalidation provided substantially cleaner and smaller risk than the available call spread.

## Ghost alternatives

### NO_TRADE

- Question: Was adding MU exposure at pullback support better than retaining cash?
- Instrument: cash / no trade
- Simulated entry and capital at risk: $0
- P/L: starts and remains $0
- Exit handling: none

### HALF_SIZE_MU

- Question: Was 12 shares too large for the setup and correlated-growth portfolio risk?
- Instrument: MU common stock
- Side and quantity: BUY 6 shares at the same $940 executable limit
- Simulated initial cost: $5,640
- Planned risk: $108 to the $922 tight invalidation before gaps/slippage
- Exit handling: identical invalidation and target plan to the real trade

### BREAKOUT_ENTRY_MU

- Question: Would waiting for trend confirmation outperform buying pullback support?
- Instrument: MU common stock
- Side and quantity: BUY 6 shares only after a sustained trade above $970
- Entry status at the real fill: not triggered
- Simulated entry: use the conservative executable ask when and if the objective trigger occurs; do not manufacture a price before then
- Invalidation after trigger: $945 failure level
- Exit handling: same common evaluation endpoint and $1,005-$1,012 target area; mark UNSCORABLE if the trigger never occurs

## Tracking rules

Use one common market-data timestamp for every scoreable path at each checkpoint. Mark long stock at the executable bid. The breakout alternative remains unentered until its objective trigger. Ghosts never reach Alpaca or affect portfolio state.

