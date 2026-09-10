# Ghost set: alpaca-stage2-20260902-MMED-buy

- Status: COMPLETE
- Real client order ID: `alpaca-stage2-20260902-MMED-buy`
- Broker order ID: `6df8ca70-8023-41ea-85db-f3513ac7b239`
- Ticker: MMED
- Decision time: 2026-09-02T16:19:10.792573581Z
- First fill time: 2026-09-02T16:22:09.499780108Z
- Evaluation start: 2026-09-02T16:22:09.499780108Z
- Evaluation end: 2026-09-09 regular-market close
- Checkpoints: 2026-09-02, 2026-09-03, 2026-09-04, 2026-09-08, and 2026-09-09 regular-market closes
- Holding plan: one-week earnings/squeeze continuation
- Review/invalidation: daily close below $22.40; hard failure below $21.80 or material secondary/lockup supply filing
- Targets: $25-$26.50

## Thesis and real path

MiniMed's Q1 beat, raised guidance, tight public float, and high short interest support continuation after a high-volume breakout. Early-September lockup supply risk makes the position intentionally bounded. The real BUY filled 250 shares at $23.76, deploying $5,940; planned loss to $21.80 is $490 before gaps/slippage.

## Contemporaneous market data

- Decision quote: $23.77/$23.84, 100/100 displayed, at `2026-09-02T16:19:10.792573581Z`.
- Submitted limit: $23.90; actual fill: $23.76.

## Ghost alternatives

### NO_TRADE

- Add no MMED exposure; zero capital and P/L.

### HALF_SIZE_STOCK

- Buy 125 shares at $23.84 ask; $2,980 capital and $255 planned loss to $21.80; identical targets and exit rules.

### PULLBACK_22_75

- Buy 250 shares only if the ask reaches $22.75 while the thesis remains valid. No entry price exists until activation; same hard invalidation and endpoint.

## Initial post-fill observation

- Observed: 2026-09-02T16:27:58.803836314Z; MMED bid/ask $23.72/$23.76.
- Real path: value $5,930; P/L -$10 (-0.17%).
- `NO_TRADE`: $0.
- `HALF_SIZE_STOCK`: value $2,965; P/L -$15 (-0.50%).
- `PULLBACK_22_75`: UNENTERED.
- Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using the current Alpaca IEX executable bid. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real path after the later bounded half reduction: 125 shares at the $23.54 bid plus $2,946.25 sale proceeds; total value $5,888.75; P/L -$51.25 (-0.86%) versus the original $5,940 capital.
- `NO_TRADE`: $0.
- `HALF_SIZE_STOCK`: 125 shares at $23.54; value $2,942.50; P/L -$37.50 (-1.26%) versus the $23.84 simulated entry.
- `PULLBACK_22_75`: UNENTERED; the current ask was $26.91 and never reached the $22.75 objective trigger in the observed data.
- The real path includes the separate 125-share reduction; no hard invalidation or target was triggered for the retained position. Next checkpoint: 2026-09-03 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.

## 2026-09-03 close checkpoint

- Observed from Alpaca IEX at `2026-09-03T19:59:59Z`; MMED bid/ask was $23.81/$23.98.
- Real path after the half reduction: $2,946.25 sale proceeds plus 125 shares at $23.81, total value $5,922.50; P/L -$17.50 (-0.29%) versus the original $5,940.
- `NO_TRADE`: $0.
- `HALF_SIZE_STOCK`: 125 shares at $23.81; value $2,976.25; P/L -$3.75 (-0.13%) versus the $23.84 simulated entry.
- `PULLBACK_22_75`: UNENTERED; the regular-session low was $23.235 and the ask never reached the $22.75 trigger in observed data.
- No $22.40 review, $21.80 hard invalidation, or target was triggered. Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- Common stock mark: $23.26 executable bid near the close.
- Real path after the half reduction: $2,946.25 proceeds plus 125 shares worth $2,907.50; total $5,853.75 and P/L -$86.25 (-1.45%) versus $5,940. `NO_TRADE`: $0. `HALF_SIZE_STOCK`: value $2,907.50 and P/L -$72.50 (-2.43%). `PULLBACK_22_75`: UNENTERED; the session did not reach the trigger.
- The $22.40/$21.80 invalidations and $25 target remained inactive. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $23.31; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real path after the half reduction: $2,946.25 proceeds plus 125 shares at $23.31 = $5,860.00, P/L -$80.00 versus $5,940. `HALF_SIZE_STOCK`: $2,913.75, P/L -$66.25 versus the $2,980 simulated entry. `NO_TRADE`: $0.
- `PULLBACK_22_75` remains UNSCORABLE/unentered because the daily low touching $22.75 does not prove that the required executable ask reached the trigger. No invalidation occurred.
- Next checkpoint and endpoint: 2026-09-09 regular-market close.

## 2026-09-09 endpoint review

- Assessment status: `COMPLETE`. The Alpaca 2026-09-09 1Day bar closed at `$22.76`; the near-close IEX quote was abnormally wide at `$19.44/$25.79`, so the bar is a disclosed non-executable reference rather than an exact liquidation mark.
- Real path after the separate 125-share reduction: `$2,946.25` sale proceeds plus 125 shares at `$22.76` = `$5,791.25`, P/L `-$148.75` (`-2.50%`) versus the original `$5,940` cost.
- `NO_TRADE`: `$0` P/L. `HALF_SIZE_STOCK`: 125 shares at `$22.76` = `$2,845`, P/L `-$135.00` (`-4.53%`) versus its `$2,980` simulated cost.
- `PULLBACK_22_75`: unentered and `UNSCORABLE`; no contemporaneous executable ask established the trigger. The stock-path comparison is partial because endpoint marks are official-bar proxies.
- Supported conclusion: the original full-size entry was worse than no trade and, on a capital-normalized basis, the half-size alternative; the thesis did not produce the intended continuation over this window. The later reduction limited loss, but this one decision does not warrant a new durable lesson.
- Dimension review: thesis/forecast mixed (credible company setup, weak short-window follow-through); timing weak; instrument appropriate; sizing/risk mixed because the initial position still required a later reduction; execution good (full fill at `$23.76`).
- Lesson change: none.
