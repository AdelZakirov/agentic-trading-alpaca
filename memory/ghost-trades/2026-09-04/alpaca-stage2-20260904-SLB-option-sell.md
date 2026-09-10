# Ghost set: alpaca-stage2-20260904-SLB-option-sell

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260904-SLB-option-sell`
- Broker order ID: `a2636576-7a05-4aae-b48a-dc1fb65049d3`
- Ticker: SLB
- Decision time: approximately 2026-09-04T14:44:00Z
- Fill time: 2026-09-04T14:48:15.710180388Z
- Evaluation start: 2026-09-04T14:48:15.710180388Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-04, 2026-09-08, 2026-09-09, 2026-09-10, and 2026-09-11 regular-market closes
- Holding plan tested: immediate capital salvage after the tactical thesis failed with five sessions remaining to expiry

## Thesis and actual fill

With SLB near $56.60, both Sep. 11 $58/$62 calls were out of the money and the underlying had broken the tactical invalidation. Fresh technical evidence favored closing before accelerated theta decay.

- Pre-trade exposure: long one `SLB260911C00058000` at $1.25 and short one `SLB260911C00062000` at $0.17; original net debit $1.08
- Actual action: atomically sell the $58 call and buy to close the $62 call
- Limit: minimum $0.25 credit, encoded as `-0.25`
- Actual fills: $58 call sold at $0.44; $62 call covered at $0.15
- Actual net credit: $0.29, or $29 proceeds
- Realized spread P/L: -$79 before fees

## Contemporaneous market data

- Source: Alpaca option snapshots and IEX underlying quote.
- Earlier decision snapshot: $58 call $0.48/$0.49, delta about 0.31 and theta about -0.064; $62 call $0.03/$0.13, delta about 0.06 and theta about -0.027. Conservative closing credit was $0.35.
- Fresh preflight prices produced a $0.25 conservative credit. Both contracts were confirmed active and tradable before submission.

## Ghost alternatives fixed before submission

### HOLD_SPREAD

- Retain the spread through the Sep. 11 expiry-management window.
- Capital remaining at risk from original cost: $108 less any later closing proceeds.
- Mark from executable $58-call bid minus $62-call ask at common checkpoints.

### WAIT_BREAK_56_25

- Close only if the underlying breaks the 2026-09-04 session low of $56.25.
- The alternative remains conditional until the objective trigger occurs or the common endpoint arrives.

### CLOSE_AT_TODAY_CLOSE

- Defer the same risk reduction until the 2026-09-04 regular-market close.
- Price at the conservative executable multi-leg credit at that checkpoint.

## Initial post-fill observation

- Real path: CLOSED for a $0.29 credit; realized spread P/L -$79 before fees.
- `HOLD_SPREAD`: initial comparison value uses the same $0.29 actual exit observation only as a contemporaneous mark; no later outcome is inferred.
- `WAIT_BREAK_56_25` and `CLOSE_AT_TODAY_CLOSE`: remain conditional.
- Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- Real path remains CLOSED for a $0.29 credit and -$79 realized P/L.
- No synchronized executable close quote was recoverable for both legs. The $58 call last-trade bar closed $0.72 while the $62 call had no 2026-09-04 trade; `HOLD_SPREAD` and `CLOSE_AT_TODAY_CLOSE` are UNSCORABLE rather than using a stale short-leg price.
- The underlying low was $56.25 but did not decisively break below it, so `WAIT_BREAK_56_25` did not activate and remained exposed; its close value is also UNSCORABLE. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- No synchronized executable market was recoverable for both option legs, so all open option counterfactuals remain formally UNSCORABLE. The real spread exit remains fixed at the recorded $79 loss and is not re-marked.
- Underlying SLB's official daily close was $57.11, a disclosed context mark only; it cannot substitute for executable option sides.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- No synchronized executable market was recoverable for both option legs. `HOLD_SPREAD`, `WAIT_BREAK_56_25`, and `CLOSE_AT_TODAY_CLOSE` therefore remain formally UNSCORABLE; the real path stays fixed at a $79 realized loss.
- Underlying SLB's official daily close was $57.06, disclosed only as context and not substituted for the missing option sides. No new lesson is supported.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- The real spread exit remains fixed at a `$0.29` credit and realized `-$79` before fees. No synchronized executable close was available for both option legs through the configured Alpaca OPRA route, so `HOLD_SPREAD`, the activated `WAIT_BREAK_56_25`, and `CLOSE_AT_TODAY_CLOSE` remain UNSCORABLE; no stale or non-executable option mark is substituted.
- SLB's official 1Day close was `$56.005` at the common `2026-09-10T20:00:00Z` checkpoint, and the regular-session low of `$55.15` confirms that the `$56.25` break trigger activated. This underlying bar is context only and does not manufacture an option P/L. Next checkpoint: 2026-09-11 regular-market close.
