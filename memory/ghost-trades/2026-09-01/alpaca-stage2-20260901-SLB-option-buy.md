# Ghost set: alpaca-stage2-20260901-SLB-option-buy

- Status: COMPLETE
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
- Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:38:20Z using current Alpaca IEX stock and indicative option marks. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real spread: executable value $1.25 ($1.51 long-call bid less $0.26 short-call ask); P/L +$17 (+15.74%) versus the $1.08 actual debit.
- `NO_TRADE`: $0.
- `SEP11_58_LONG_CALL`: $1.51 bid; P/L +$24 (+18.90%) versus the $1.27 simulated ask entry.
- `ADD_20_SLB_STOCK`: 20 shares at the $58.72 bid; P/L +$17.60 (+1.52%) versus the $57.84 simulated entry.
- The underlying remained above the $56.90 invalidation and below the $60.20-$60.50 first target. Next checkpoint: 2026-09-03 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.

## 2026-09-03 close checkpoint

- Observed from Alpaca at approximately `2026-09-03T19:59:59Z`: SLB $57.41/$57.43; Sep. 11 $58 call $0.79/$1.02; Sep. 11 $62 call $0.10/$0.14.
- Real spread: executable value $0.65; P/L -$43 (-39.81%) versus the $1.08 fill.
- `NO_TRADE`: $0.
- `SEP11_58_LONG_CALL`: $0.79 bid; P/L -$48 (-37.80%) versus the $1.27 simulated ask entry.
- `ADD_20_SLB_STOCK`: 20 shares at $57.41; P/L -$8.60 (-0.74%) versus $57.84.
- The underlying remained above $56.90 and below $60.20. Next and final checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio totals, exposure, buying power, or risk limits.

## Real-path exit — 2026-09-04

- After the underlying broke the tactical invalidation, the real path closed the Sep. 11 $58/$62 spread atomically at `2026-09-04T14:48:15.710180388Z`.
- The $58 call sold at $0.44 and the $62 call was covered at $0.15, producing a $0.29 net credit and a -$79 realized result versus the $1.08 debit before fees.
- The common evaluation still completes at the 2026-09-04 close. Separate exit-decision comparison: [`../2026-09-04/alpaca-stage2-20260904-SLB-option-sell.md`](../2026-09-04/alpaca-stage2-20260904-SLB-option-sell.md).

## 2026-09-04 close completion

- Real spread: CLOSED for $0.29 credit; realized P/L -$79 (-73.15%) versus the $1.08 debit. `NO_TRADE`: $0.
- `SEP11_58_LONG_CALL`: the $58 call's 2026-09-04 last-trade bar closed at $0.72, a non-executable proxy P/L of -$55; formally UNSCORABLE at the endpoint without a synchronized bid.
- `ADD_20_SLB_STOCK`: identical invalidation implies an exit at $56.62; P/L -$24.40 (-2.11%) versus $57.84.
- Outcome: no-trade was best; the small stock add lost less in both dollars and percentage than the real spread. Defined maximum loss did not compensate for theta, spread cost, and duplication of the existing stock thesis.
- Decision review: underlying thesis failed; strategy/overlap selection was weak; strikes and short expiry amplified the loss; sizing capped dollars and execution was bounded. This supports the existing option-payoff/overlap lesson without increasing its evidence count beyond the completed SLB decision set.
