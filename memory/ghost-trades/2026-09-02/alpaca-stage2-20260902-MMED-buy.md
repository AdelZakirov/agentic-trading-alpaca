# Ghost set: alpaca-stage2-20260902-MMED-buy

- Status: ACTIVE
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
- Next checkpoint: 2026-09-02 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.
