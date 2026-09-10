# Ghost set: alpaca-stage2-20260902-GTLB-buy

- Status: COMPLETE
- Real client order ID: `alpaca-stage2-20260902-GTLB-buy`
- Broker order ID: `16645abf-e507-4d64-a50d-27592d5b0719`
- Ticker: GTLB
- Decision time: 2026-09-02T16:19:14.637905665Z
- First fill time: 2026-09-02T16:25:25.561602747Z
- Evaluation start: 2026-09-02T16:25:25.561602747Z
- Evaluation end: 2026-09-09 regular-market close
- Checkpoints: 2026-09-02, 2026-09-03, 2026-09-04, 2026-09-08, and 2026-09-09 regular-market closes
- Holding plan: one-week post-earnings consolidation into continuation
- Invalidation: $48.40 tight failure; hard gap-support failure below $46.30
- Targets: $54-$55.55

## Thesis and real path

GTLB's earnings beat, guidance raise, high-volume gap, and analyst catch-up support continuation after a pullback into the researched shelf. The real BUY filled 150 shares at $50.80, deploying $7,620; planned loss to $48.40 is $360 before gaps/slippage.

## Contemporaneous market data

- Decision quote: $50.80/$50.85, 100/100 displayed, at `2026-09-02T16:19:14.637905665Z`.
- Sep. 11 $50 call: $2.02/$2.55; Sep. 11 $55 call: $0.43/$0.73 at the initial option comparison.

## Ghost alternatives

### NO_TRADE

- Add no GTLB exposure; zero capital and P/L.

### HALF_SIZE_STOCK

- Buy 75 shares at $50.85 ask; $3,813.75 capital and $183.75 planned loss to $48.40; identical targets and endpoint.

### SEP11_50_55_CALL_SPREAD

- Buy one `GTLB260911C00050000` at $2.55 and sell one `GTLB260911C00055000` at $0.43; $2.12 debit/$212 maximum loss, $52.12 breakeven, and $288 maximum gross profit.

### BREAKOUT_52_80

- Buy 100 shares only after an hourly close above $52.80 at the then-current ask. No entry price exists until activation; same $48.40 invalidation and endpoint.

## Initial post-fill observation

- Observed: approximately 2026-09-02T16:28:07Z; GTLB bid/ask $50.82/$50.86.
- Real path: value $7,623; P/L +$3 (+0.04%).
- `NO_TRADE`: $0.
- `HALF_SIZE_STOCK`: value $3,811.50; P/L -$2.25 (-0.06%).
- `SEP11_50_55_CALL_SPREAD`: executable value $1.39 ($2.12 long-call bid less $0.73 short-call ask); P/L -$73 (-34.43%).
- `BREAKOUT_52_80`: UNENTERED.
- Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using current Alpaca IEX stock and indicative option marks. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real GTLB stock: 150 shares at the $50.12 bid; value $7,518.00; P/L -$102.00 (-1.34%) versus the $50.80 fill.
- `NO_TRADE`: $0.
- `HALF_SIZE_STOCK`: 75 shares at $50.12; value $3,759.00; P/L -$54.75 (-1.44%) versus the $50.85 simulated entry.
- `SEP11_50_55_CALL_SPREAD`: executable value $1.20 ($1.62 long-call bid less $0.42 short-call ask); P/L -$92 (-43.40%) versus the $2.12 simulated debit.
- `BREAKOUT_52_80`: UNENTERED; no hourly close above $52.80 was observed. The $48.40 tight invalidation remains intact. Next checkpoint: 2026-09-03 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.

## 2026-09-03 close checkpoint

- Observed from Alpaca near the close. The IEX stock quote was unusably wide at $47.28/$50.90 while the official IEX close was $49.33; the stock paths use $49.33 as a disclosed non-executable close mark rather than manufacturing executable precision. Option markets were also impaired: $50 call $0.97/$1.37 and $55 call with no bid/$0.37 ask.
- Real GTLB indicative close value: 150 shares at $49.33 = $7,399.50; P/L -$220.50 (-2.89%) versus $50.80.
- `NO_TRADE`: $0.
- `HALF_SIZE_STOCK`: 75 shares at $49.33; P/L -$114.00 (-2.99%) versus $50.85.
- `SEP11_50_55_CALL_SPREAD`: UNSCORABLE at an executable close because the short leg had no bid; using $0 as the cover ask is prohibited and no value is manufactured.
- `BREAKOUT_52_80`: UNENTERED; the session high was $50.69. The official close and Alpaca account mark remained above $48.40, so the tight invalidation was not triggered. Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- Common stock mark: $49.82 executable bid near the close.
- Real path: 150 shares worth $7,473.00 and P/L -$147.00 (-1.93%). `NO_TRADE`: $0. `HALF_SIZE_STOCK`: value $3,736.50 and P/L -$77.25 (-2.03%). `BREAKOUT_52_80`: UNENTERED after the Sep. 3-4 shelf failed to close above its trigger.
- `SEP11_50_55_CALL_SPREAD`: the short leg had no 2026-09-04 trade and no synchronized executable close; UNSCORABLE rather than reusing a stale price.
- The $48.40 invalidation remained intact at this checkpoint. Next checkpoint: 2026-09-08 regular-market close.

## Real-path exit — 2026-09-08

- Fresh research confirmed distribution and the break of the $48.40 tactical invalidation. The real path sold all 150 shares at $47.42 under broker order `221a2143-357f-44eb-8ff2-0b62f7bb6ab5`, realizing approximately -$507.00 before fees versus $50.80.
- The set remains active through the 2026-09-09 endpoint; score all alternatives at the 2026-09-08 close. Separate exit comparison: [`alpaca-stage2-20260908-GTLB-sell`](../2026-09-08/alpaca-stage2-20260908-GTLB-sell.md).

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $47.15; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real path had already exited at $47.42 for $7,113.00 proceeds and P/L -$507.00. `HALF_SIZE_STOCK`: 75 shares at $47.15 = $3,536.25, P/L -$277.50. `NO_TRADE`: $0; `BREAKOUT_52_80` remained unentered.
- The option path remains formally UNSCORABLE without synchronized executable sides. The real exit led holding the full position at the official close by $40.50.
- Next checkpoint and endpoint: 2026-09-09 regular-market close.

## 2026-09-09 endpoint review

- Assessment status: `COMPLETE`. The Alpaca 2026-09-09 1Day bar closed at `$46.345`; the near-close IEX quote was abnormally wide at `$45.66/$49.19`, so the bar is a disclosed non-executable reference.
- Real path had exited all 150 shares at `$47.42`, producing `$7,113.00` and P/L `-$507.00` (`-6.65%`) versus the `$7,620` entry cost.
- `NO_TRADE`: `$0` P/L. `HALF_SIZE_STOCK`: 75 shares at the endpoint bar = `$3,475.88`, P/L `-$337.88` (`-8.86%`) versus its `$3,813.75` simulated cost. `BREAKOUT_52_80`: unentered; the trigger never occurred. The call-spread path remains `UNSCORABLE` without an executable close.
- Supported conclusion: the real exit after the documented invalidation preserved a better capital-normalized return than retaining half size through the endpoint, although no trade would have been best in absolute P/L. The comparison is partial because the close mark is a bar proxy and the option path is unavailable.
- Dimension review: thesis/forecast mixed (post-earnings continuation failed); timing/risk good at the invalidation; instrument appropriate; sizing mixed; execution good at the documented `$47.42` exit.
- Lesson change: none; this is a single invalidation episode.
