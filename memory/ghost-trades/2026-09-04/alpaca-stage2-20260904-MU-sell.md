# Ghost set: alpaca-stage2-20260904-MU-sell

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260904-MU-sell`
- Broker order ID: `532d2916-4f78-4293-9367-8c1692216aea`
- Ticker: MU
- Decision/order time: 2026-09-04T14:48:21.559468Z
- First and final fill time: 2026-09-04T14:55:14.204296Z
- Evaluation start: 2026-09-04T14:55:14.204296Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-04 and 2026-09-08 through 2026-09-11 regular-market closes
- Holding plan: realize half after the first target and retain six shares toward $1,008-$1,012
- Profit-protection trigger: 15-minute close below $985

## Thesis and actual fill

MU cleared the documented $985 target and reached $1,003.52 after a strong opening impulse. The real path reduced target/giveback risk without abandoning the bullish continuation thesis.

- Pre-trade exposure: 12 MU shares at average $939.996667
- Actual action: sell 6 shares at average $999.03; retain 6 shares
- Realized gross result: approximately +$354.20 versus average cost
- Retained capital at the fill price: approximately $5,994.18
- Size rationale: the fresh technical review recommended trimming four to six shares into $1,000-$1,008 while retaining a runner

## Contemporaneous market data

- Source: Alpaca IEX execution and the fresh moneyheap technical artifact [`163854-MU-technical.md`](../../research/2026-09-04/163854-MU-technical.md).
- The research observed a $1,003.52 session high, a $994.70-$996.50 VWAP/EMA support zone, and $985 as the profit-protection floor.
- The IEX quote was intermittently wide, so the real order used a bounded $999 day limit and did not chase a midpoint.

## Ghost alternatives fixed before submission

### HOLD_12

- Retain all 12 shares under the same $985 support and $1,008-$1,012 next-target plan.

### SELL_4

- Sell 4 shares at the same bounded trigger and retain 8 under the same management plan.

### SELL_ALL_12

- Sell all 12 shares at the same bounded trigger and retain no MU exposure.

## Tracking rules

Compare every path from the same 12-share pre-trade exposure. Include sale proceeds and mark retained shares at the conservative executable bid. Use the same chronological window and objective triggers. Ghosts never reach Alpaca or affect portfolio state.

## Initial post-fill state

- Real path: six shares sold at $999.03 and six remain open.
- `HOLD_12`: 12 shares remain.
- `SELL_4`: simulated sale of 4 at $999.03 and 8 shares remain.
- `SELL_ALL_12`: simulated sale of 12 at $999.03 and no shares remain.
- Next checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 close checkpoint

- Common stock mark: $1,015.00 executable bid near the close.
- Real path: $5,994.18 proceeds plus six shares worth $6,090 = $12,084.18. `HOLD_12`: $12,180, leading real by $95.82. `SELL_4`: $3,996.12 proceeds plus eight shares worth $8,120 = $12,116.12, leading real by $31.94. `SELL_ALL_12`: $11,988.36, trailing real by $95.82.
- The partial trim locked profit while retention benefited from continued upside. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $1,000.27; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real six-share reduction: $5,994.18 proceeds plus six shares worth $6,001.62 = $11,995.80. `HOLD_12`: $12,003.24, leading real by $7.44. `SELL_4`: $3,996.12 proceeds plus eight shares worth $8,002.16 = $11,998.28, leading real by $2.48. `SELL_ALL`: $11,988.36, trailing real by $7.44.
- Full retention narrowly led at this checkpoint, while the real reduction preserved most participation with lower nominal exposure.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $1,027.70; this is a non-executable proxy because the near-close quote was abnormally wide at $1,000/$1,035.
- Real six-share reduction: $5,994.18 proceeds plus six shares at $1,027.70 = $12,160.38. `HOLD_12`: 12 shares at $1,027.70 = $12,332.40, leading real by $172.02. `SELL_4`: $3,996.12 proceeds plus eight shares at $1,027.70 = $12,217.72, leading real by $57.34. `SELL_ALL_12`: $11,988.36, trailing real by $172.02.
- The 9/9 close stayed above the $985 profit-protection trigger. Full retention led at this checkpoint, while the real trim retained lower exposure; no new lesson is supported.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: MU close `$980.47`; the after-close quote was wide at `$927.31/$1,027.38`, so the bar is a disclosed non-executable proxy.
- Real path: `$5,994.18` sale proceeds plus six retained shares worth `$5,882.82` = `$11,877.00`, P/L `+$597.04` versus the `$11,279.96` original exposure. `HOLD_12`: `$11,765.64`, P/L `+$485.68`; `SELL_4`: `$11,839.88`, P/L `+$559.92`; `SELL_ALL_12`: fixed `$11,988.36`, P/L `+$708.40`.
- The full exit led the real trim by `$111.36`; the real trim led `HOLD_12` by `$111.36` and `SELL_4` by `$37.12`. A 15-minute close below `$985` occurred at `15:15Z` (`$984.18`), so `MU_985_SUPPORT` activated; no hindsight execution is added. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: MU close `$975.12`; this is a disclosed non-executable proxy.
- Real path: `$5,994.18` proceeds plus six shares worth `$5,850.72` = `$11,844.90`, P/L `+$564.94` versus the `$11,279.96` pre-trade exposure. `HOLD_12`: `$11,701.44`, P/L `+$421.48`; `SELL_4`: `$11,797.08`, P/L `+$517.12`; `SELL_ALL_12`: fixed `$11,988.36`, P/L `+$708.40`.
- `SELL_ALL_12` led the real trim by `$143.46`; the real trim led `HOLD_12` by `$143.46` and `SELL_4` by `$47.82`. `MU_985_SUPPORT` remained activated, with no hindsight execution. Comparison complete; no lesson change.
