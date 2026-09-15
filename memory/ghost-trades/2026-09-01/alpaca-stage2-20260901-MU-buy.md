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

## Catch-up checkpoint for 2026-09-01 close

- Observed: 2026-09-02T16:28:05Z; MU bid/ask $944.81/$945.70.
- Real MU stock: OPEN; value $11,337.72; P/L approximately +$57.76 (+0.51%).
- `NO_TRADE`: $0.
- `HALF_SIZE_MU`: value $5,668.86; P/L +$28.86 (+0.51%).
- `BREAKOUT_ENTRY_MU`: UNENTERED; sustained trade above $970 did not occur.
- No $922 invalidation or $985 target was triggered. Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using the current Alpaca IEX executable bid. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real MU stock: 12 shares at the $928.00 bid; value $11,136.00; P/L -$143.96 (-1.28%) versus the $939.996667 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_MU`: 6 shares at $928.00; P/L -$71.98 (-1.28%) versus the $940 simulated entry.
- `BREAKOUT_ENTRY_MU`: UNENTERED; no sustained trade above the $970 trigger was observed.
- The $922 invalidation and $985 target were not triggered. Next checkpoint: 2026-09-03 regular-market close.

## 2026-09-03 close checkpoint

- Observed from Alpaca IEX at `2026-09-03T19:59:59Z`; MU bid/ask was $944.00/$958.15 and the official IEX daily close was $958.325. The wide quote is disclosed and the conservative bid is used for comparison.
- Real MU: 12 shares at $944.00; value $11,328.00; P/L +$48.04 (+0.43%) versus the $939.996667 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_MU`: 6 shares at $944.00; P/L +$24.00 (+0.43%) versus $940.
- `BREAKOUT_ENTRY_MU`: UNENTERED; the regular-session high was $959.63, below the sustained $970 trigger. The account's later overnight mark is not treated as a regular-session trigger.
- The $922 invalidation and $985 target were not triggered. Next checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 real-path target reduction

- The real path reached the $985 target and later sold 6 of 12 shares at $999.03, realizing approximately $354.20 gross; six shares remain above the raised $985 profit-protection level.
- This is a real-path change, not the scheduled close checkpoint. The entry alternatives remain fixed and the 2026-09-04 close checkpoint is still due at the actual close.
- Target-sale comparison: [`alpaca-stage2-20260904-MU-sell`](../2026-09-04/alpaca-stage2-20260904-MU-sell.md).

## 2026-09-04 close checkpoint

- Common stock mark: $1,015.00 executable bid near the close.
- Real path: $5,994.18 sale proceeds plus six shares worth $6,090; total $12,084.18 and P/L about +$804.22 (+7.13%) versus original cost. `NO_TRADE`: $0. `HALF_SIZE_MU`: value $6,090 and P/L +$450 (+7.98%).
- `BREAKOUT_ENTRY_MU`: the first regular 15-minute bar closed $988.01 above $970, activating the ghost. The next quote was abnormally wide with a $999.88 ask; using that conservative entry and the $1,005 target gives a disclosed +$30.72 result on six shares. Quote quality makes this comparison low confidence.
- The real path reached and reduced at its target. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $1,000.27; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real path after the prior six-share sale: $5,994.18 proceeds plus six shares at $1,000.27 = $11,995.80, P/L +$715.84 versus $11,279.96 initial cost. `HALF_SIZE_STOCK`: six shares worth $6,001.62, P/L +$361.62. `NO_TRADE`: $0.
- The conditional breakout path's earlier low-confidence +$30.72 target result remains fixed. The retained runner remained above the $985 review.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $1,027.70 (high $1,042.38, low $992.47); this is a non-executable proxy because the near-close quote was abnormally wide at $1,000/$1,035.
- Real path after the prior six-share sale: $5,994.18 proceeds plus six shares at $1,027.70 = $12,160.38, P/L +$880.42 versus the $11,279.96 initial cost. `HALF_SIZE_MU`: six shares at $1,027.70 = $6,166.20, P/L +$526.20. `NO_TRADE`: $0.
- The retained runner stayed above the $985 review and the $1,005-$1,012 continuation objective was exceeded. The earlier conditional breakout result remains fixed; no new lesson is supported by this proxy checkpoint.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: MU close `$980.47`; the after-close quote was wide at `$927.31/$1,027.38`, so the bar is a disclosed non-executable proxy.
- Real path after the six-share target sale: `$5,994.18` proceeds plus six shares worth `$5,882.82` = `$11,877.00`, P/L `+$597.04` versus the `$11,279.96` entry cost. `HALF_SIZE_MU`: six shares worth `$5,882.82`, P/L `+$242.82`; `NO_TRADE`: `$0`. The earlier conditional breakout result remains fixed at its low-confidence `+$30.72` observation.
- The retained runner closed below its raised `$985` review level. The 15-minute `$984.18` close at `15:15Z` and later sub-$985 closes confirm the related profit-protection review trigger; no retrospective broker action is attributed to this ghost set. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: MU close `$975.12`; this is a disclosed non-executable proxy because no synchronized closing quote was preserved.
- Real path: `$5,994.18` proceeds plus six shares worth `$5,850.72` = `$11,844.90`, P/L `+$564.94` versus the `$11,279.96` entry cost. `HALF_SIZE_MU`: six shares worth `$5,850.72`, P/L `+$210.72`; `NO_TRADE`: `$0`. The conditional breakout result remains fixed at its earlier low-confidence `+$30.72` observation.
- The profit-protection review stayed active below `$985`; no retrospective execution is added. The real path led the half-size alternative by `$354.22`. Comparison complete; no lesson change.
