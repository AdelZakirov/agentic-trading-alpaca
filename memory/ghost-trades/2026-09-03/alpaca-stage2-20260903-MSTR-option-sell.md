# Ghost set: alpaca-stage2-20260903-MSTR-option-sell

- Status: COMPLETE
- Real client order ID: `alpaca-stage2-20260903-MSTR-option-sell`
- Broker order ID: `3e31adb7-2eea-4569-8469-3e391b737c19`
- Ticker: MSTR
- Decision time: approximately 2026-09-03T16:29:42Z
- Fill time: `2026-09-03T16:35:33.782484589Z`
- Evaluation start: `2026-09-03T16:35:33.782484589Z`
- Evaluation end: 2026-09-09 regular-market close
- Checkpoints: 2026-09-03, 2026-09-04, 2026-09-08, and 2026-09-09 regular-market closes
- Holding plan: compare target-based trimming against holding or fully closing through the original MSTR review endpoint
- Invalidation: retained spread uses the original $117.50 underlying invalidation
- Runner target: $148-$150 underlying

## Thesis and actual fill

MSTR reached the documented $137.50-$139.80 second target zone. The real path closed one of two Sep. 11 $125/$135 bull call spreads and retained one runner.

- Pre-trade exposure: two spreads entered at a $2.62 debit each, $524 total original risk
- Actual closing order: sell one long `MSTR260911C00125000` and buy to close one short `MSTR260911C00135000`
- Actual leg fills: long call sold at $16.00; short call covered at $9.10
- Actual net credit: $6.90, or $690 proceeds
- Realized gross profit on the closed spread: $428 versus its $262 allocated debit
- Residual: one Sep. 11 $125/$135 bull call spread
- Size rationale: lock a target gain while retaining defined-risk extension participation; the proceeds exceed the original total debit for both spreads

## Contemporaneous market data

- Source: Alpaca IEX stock snapshot and Alpaca indicative option snapshots.
- At approximately `2026-09-03T16:29:42Z`, MSTR latest trade was $139.315. The $125 call was $15.18/$15.85, IV 71.57%, delta 0.8608, theta -0.2148; the $135 call was $8.28/$8.42, IV 72.57%, delta 0.6384, theta -0.3585. Conservative executable closing credit was $6.76.
- Immediate preflight at `2026-09-03T16:35:30Z` showed latest trade $140.12; the stock quote was wide at $140.10/$145.32. Both option contracts were active and tradable. The $125 call was $16.12 bid and the $135 call $9.04 ask, giving a $7.08 conservative executable credit.
- Option execution was acceptable despite the wide IEX stock quote because the order reduced risk, both option legs had positive current markets, and the target was already reached.

## Ghost alternatives fixed before submission

### HOLD_TWO_SPREADS

- Question: Would full participation outperform target discipline?
- Instrument: retain both Sep. 11 $125/$135 spreads
- Simulated value at decision: two spreads at $6.76 conservative executable value = $1,352
- Exit handling: original invalidation and 2026-09-09 endpoint

### CLOSE_BOTH_SPREADS

- Question: Would full profit capture be superior?
- Instrument: close both spreads at the contemporaneous $6.76 conservative executable credit
- Simulated proceeds: $1,352; simulated gross profit $828 versus $524 original debit
- Exit handling: no residual MSTR exposure

### REAL_CLOSE_ONE_SPREAD

- Question: Does a 50% target trim best balance realized gain and extension upside?
- Instrument: actual close of one spread for $6.90, retaining one spread
- Actual proceeds: $690
- Exit handling: retained spread uses the original invalidation and 2026-09-09 endpoint

## Initial post-fill observation

- Pre-trade package reference: $1,352 using two spreads at the $6.76 conservative executable value.
- Real path: $690 actual proceeds plus one retained spread marked at $6.90 immediately after fill = $1,380; incremental value +$28 and cumulative package P/L +$856 versus $524 original debit.
- `HOLD_TWO_SPREADS`: $1,352 at the decision mark; incremental value $0.
- `CLOSE_BOTH_SPREADS`: $1,352 simulated proceeds; incremental value $0.
- The immediate difference is execution, not completed decision quality. Next checkpoint: 2026-09-03 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-03 close checkpoint

- Observed from Alpaca at approximately `2026-09-03T19:59:59Z`: Sep. 11 $125 call $20.31/$21.10 and $135 call $12.13/$12.86; conservative executable spread value $7.45.
- Real path: $690 actual proceeds plus one retained spread at $745 = $1,435, or +$83 versus the $1,352 pre-trade package reference.
- `HOLD_TWO_SPREADS`: two spreads at $7.45 = $1,490, or +$138 versus reference.
- `CLOSE_BOTH_SPREADS`: $1,352 simulated proceeds, incremental P/L $0.
- Holding both leads the real path by $55 at this checkpoint; the real path still preserves a locked package profit and leads closing both by $83. The $148-$150 runner target and $117.50 invalidation were not triggered. Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- No synchronized executable close was recoverable; last-trade bars imply an $8.40 spread reference and are treated as non-executable proxies.
- Proxy comparison versus the $1,352 decision reference: real path $690 proceeds + $840 retained = $1,530, +$178; `HOLD_TWO_SPREADS` $1,680, +$328; `CLOSE_BOTH_SPREADS` $1,352, $0.
- Holding both led the real partial trim by $150 at the proxy, while the real trim led closing both by $178 and locked capital. Formal executable ranking remains UNSCORABLE. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- No synchronized executable option close was preserved. Official contract close prices were $12.56 and $5.13, implying a disclosed non-executable spread reference of $7.43; underlying MSTR officially closed at $136.53.
- Proxy comparison versus the $1,352 decision reference: real path $690 proceeds plus $743 retained = $1,433, +$81; `HOLD_TWO_SPREADS` $1,486, +$134; `CLOSE_BOTH_SPREADS` $1,352, $0.
- Holding both led the real trim by $53 at the proxy; the real trim led closing both by $81 while retaining less expiry risk. Formal executable ranking remains UNSCORABLE.
- The retained runner was subsequently closed on 2026-09-09 for a $6.35 credit; that action does not alter this checkpoint.
- Next checkpoint and endpoint: 2026-09-09 regular-market close.

## 2026-09-09 endpoint review

- Assessment status: `COMPLETE`. Paper API records confirm the real target trim filled for `$6.90` and the retained spread later closed in the separate 2026-09-09 management decision for `$6.35`. The real package therefore produced `$1,325` total proceeds and `+$801` gross P/L versus the `$524` original debit.
- `CLOSE_BOTH_SPREADS`: fixed decision-time reference proceeds `$1,352`, or `+$828` gross P/L, beating the real partial-trim path by `$27`. `HOLD_TWO_SPREADS`: `UNSCORABLE` because no synchronized executable option endpoint market was preserved.
- Supported conclusion: taking the partial target trim locked substantial profit and avoided expiry risk, but the fixed full-close alternative would have produced slightly more proceeds. The hold-versus-trim question remains formally unscorable; the endpoint is partial and the later runner close is correlated with the separate MSTR management decision.
- Dimension review: thesis/research good in identifying expiry and pin risk; forecast mixed because the extension target was not reached; instrument appropriate; timing good for risk reduction; sizing mixed because full close led at the fixed reference; execution good with both multi-leg fills confirmed.
- Lesson change: none; this case is correlated with the MSTR entry and later runner-close decisions.
