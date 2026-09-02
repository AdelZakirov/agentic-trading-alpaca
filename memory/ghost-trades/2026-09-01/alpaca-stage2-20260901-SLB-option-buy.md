# Ghost set: alpaca-stage2-20260901-SLB-option-buy

- Status: ACTIVE
- Logical real client order ID: `alpaca-stage2-20260901-SLB-option-buy`
- Original broker order ID: `9a13c4ca-3604-4c90-bd47-8d8e4f951e2f`
- Filled replacement broker order ID: `204e01a8-2c35-47f0-a042-3c88581e2364`
- Replacement client order ID: `03b9f521-5c47-4f76-922c-219fd3c369ee`
- Ticker: SLB
- Decision time: 2026-09-01T17:48:55Z
- First fill time: 2026-09-01T18:02:12.483149Z
- Evaluation start: 2026-09-01T18:02:12.483149Z
- Evaluation end: 2026-09-04 regular-market close
- Checkpoints: 2026-09-01, 2026-09-02, 2026-09-03, and 2026-09-04 regular-market closes
- Holding plan: tactical through 2026-09-04; avoid expiration/assignment without a fresh decision
- Invalidation: underlying loss/close below $56.90 or decisive failure of $57.30 support
- Targets: $60.20-$60.50, then $61.80-$62.50

## Thesis and real path

The real trade adds small defined-risk leverage to an active SLB breakout-pullback thesis. One Sep. 11 $58/$62 bull call debit spread filled atomically at $1.08, with the long $58 call at $1.25 and short $62 call at $0.17. Maximum loss is $108; maximum spread value is $400; maximum gross profit is $292; expiration breakeven is $59.08. Existing pre-trade exposure was 80 SLB shares.

## Contemporaneous market data

- SLB stock: $57.83/$57.84 at `2026-09-01T17:48:55Z`.
- `SLB260911C00058000`: $1.19/$1.27, IV 33.63%, delta 0.4972, theta -0.0669.
- `SLB260911C00062000`: $0.15/$0.27, IV 35.47%, delta 0.1272, theta -0.0361.
- Conservative pre-order executable debit: $1.12. The initial $1.05 order was replaced once and filled at $1.08.

## Ghost alternatives

### NO_TRADE

- Add no option; retain only existing SLB stock. Zero incremental capital, risk, and P/L.

### SEP11_58_LONG_CALL

- Buy one `SLB260911C00058000` at the contemporaneous $1.27 ask; $127 maximum loss and $59.27 expiration breakeven. Exit at conservative bid marks through the common endpoint.

### ADD_20_SLB_STOCK

- Buy 20 SLB shares at the contemporaneous $57.84 ask; $1,156.80 capital and about $18.80 planned loss to $56.90 before gaps/slippage. Use the same underlying invalidation, targets, and common endpoint.

## Catch-up checkpoint for 2026-09-01 close

- Observed: approximately 2026-09-02T16:28:06Z; exact prior-close option marks were unavailable.
- Real spread: executable value $0.95 ($1.25 long-call bid less $0.30 short-call ask); P/L -$13 (-12.04%) versus $1.08 fill.
- `NO_TRADE`: $0.
- `SEP11_58_LONG_CALL`: $1.25 bid; P/L -$2 (-1.57%).
- `ADD_20_SLB_STOCK`: $58.05 bid; P/L +$4.20 (+0.36%).
- Next checkpoint: 2026-09-02 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.
