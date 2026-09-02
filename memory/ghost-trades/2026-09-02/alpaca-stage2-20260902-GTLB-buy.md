# Ghost set: alpaca-stage2-20260902-GTLB-buy

- Status: ACTIVE
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
- Next checkpoint: 2026-09-02 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.
