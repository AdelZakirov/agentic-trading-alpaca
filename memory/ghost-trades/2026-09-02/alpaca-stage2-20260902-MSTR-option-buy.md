# Ghost set: alpaca-stage2-20260902-MSTR-option-buy

- Status: COMPLETE
- Real logical client order ID: `alpaca-stage2-20260902-MSTR-option-buy`
- Original broker order ID: `81fa7e82-6798-47a1-86b4-e41af3f31692` (`replaced`, 0/2)
- Filled replacement broker order ID: `c7592541-fa86-48f3-bacb-160d2e45b232`
- Replacement client order ID: `2baa0d9b-ba7d-4230-9c5d-42090a26f00e`
- Ticker: MSTR
- Decision time: 2026-09-02T16:19:19Z
- First fill time: 2026-09-02T16:48:46.446501335Z
- Evaluation start: 2026-09-02T16:48:46.446501335Z
- Evaluation end: 2026-09-09 regular-market close
- Checkpoints: 2026-09-02, 2026-09-03, 2026-09-04, 2026-09-08, and 2026-09-09 regular-market closes
- Holding plan: tactical bull-flag continuation through 2026-09-09 unless invalidated earlier; avoid expiration/assignment without a fresh decision
- Invalidation: underlying below $117.50
- Targets: $133, then $137.50-$139.80, with $148-$150 extension

## Thesis and sizing

MSTR's bullish flag continuation setup was expressed through defined-risk spreads because the stock adds uncapped 24/7 Bitcoin gap exposure alongside HOOD and MU. The real order filled both spreads after one permitted replacement. Actual leg fills were two long Sep. 11 $125 calls at $4.10 and two short Sep. 11 $135 calls at $1.48, for a $2.62 net debit per spread.

- Instrument: two Sep. 11 $125/$135 bull call debit spreads
- Actual capital at risk: $524 before fees
- Maximum spread value: $2,000; maximum gross profit: $1,476 before fees
- Pre-trade MSTR exposure: none
- Exit handling: manage from executable multi-leg marks under the trading policy; no automatic stop or expiration action

## Contemporaneous market data

- Source: Alpaca IEX for stock and Alpaca indicative option snapshots.
- Decision underlying quote was temporarily wide near $122.54; stock alternative was marked `UNSCORABLE` rather than manufacturing an entry.
- Decision options: Sep. 11 $125 call $4.13/$4.39, IV 66.65%, delta 0.4613, theta -0.2891; Sep. 11 $135 call $1.52/$1.64, IV 70.06%, delta 0.2157, theta -0.2225.
- Initial order was a $2.60 day limit and was replaced once at $2.66 after a full refresh. No further chase was permitted.

## Real path

- The replacement was confirmed `filled` 2/2. At the 2026-09-02T19:21:39Z-19:21:40Z observation, the long $125 call was $3.78/$4.11 and the short $135 call was $1.48/$1.52.
- Conservative executable spread value: $2.26; real-path P/L: -$72 (-13.74%) versus the $2.62 actual debit for two spreads.
- Underlying IEX quote remained abnormally wide at $122.36/$129.72, but the bid remained above the $117.50 invalidation and within the researched demand area. Real path remains OPEN and is HOLD.

## Ghost alternatives

### NO_TRADE

- Question: Did crypto-beta exposure deserve inclusion at all?
- Instrument: cash / no trade
- Simulated entry and capital at risk: $0
- P/L: $0
- Exit handling: none

### MSTR_50_STOCK

- Question: Would outright stock provide better upside flexibility than the vertical?
- Instrument: MSTR common stock, 50 shares
- Entry rule: buy at the contemporaneous executable ask only if a reliable quote is available
- Simulated entry: `UNSCORABLE` because the decision-time stock market was abnormally wide
- Maximum loss: unbounded overnight stock risk; no capital or P/L is manufactured
- Exit handling: same $117.50 invalidation and common endpoint if later scoreable

### TWO_LONG_125_CALLS

- Question: Would uncapped call upside outperform the vertical despite higher premium and theta?
- Instrument: two long `MSTR260911C00125000` calls
- Entry rule: buy at the contemporaneous $4.39 ask
- Simulated premium and maximum loss: $878 before fees
- Current executable value: $3.78 bid x 2 x 100 = $756; P/L: -$122 (-13.90%)
- Expiration breakeven: $129.39; exit or value at the common endpoint before expiration

### ONE_125_135_SPREAD

- Question: Was one spread sufficient for the thesis and correlation risk?
- Instrument: one Sep. 11 $125/$135 bull call debit spread
- Entry rule: same initial $2.60 debit assumption as the real order
- Simulated maximum loss: $260; maximum gross profit: $740
- Current executable value: $2.26; P/L: -$34 (-13.08%)
- Exit or value at the common endpoint before expiration

## Initial observation

- Observed: 2026-09-02T19:21:39Z-19:21:40Z, disclosed as the first post-fill observation because the fill occurred after the prior cycle's reconciliation.
- Stock alternative remains `UNSCORABLE`; no historical quote is manufactured. Option alternatives use the same current executable sides as the real path.
- No invalidation, target, exercise, assignment, or completion event occurred. Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:38:20Z using current Alpaca IEX stock and indicative option marks. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real path: two Sep. 11 $125/$135 call spreads at an executable value of $5.91 each ($12.38 long-call bid less $6.47 short-call ask); total value $1,182; P/L +$658 (+125.57%) versus the $524 actual debit.
- `NO_TRADE`: $0.
- `MSTR_50_STOCK`: `UNSCORABLE`; the stock market remained unusually wide at $129.62/$136.50, so no stock entry or P/L is manufactured.
- `TWO_LONG_125_CALLS`: two $125 calls at the $12.38 bid; value $2,476; P/L +$1,598 (+182.00%) versus the $878 simulated premium.
- `ONE_125_135_SPREAD`: one spread at $5.91; value $591; P/L +$331 (+127.31%) versus the $260 simulated debit.
- The underlying last trade was above the $133 first target but below the $137.50-$139.80 next zone; the $117.50 invalidation, exercise, assignment, and completion were not triggered. Next checkpoint: 2026-09-03 regular-market close.

## Real-path target reduction — 2026-09-03

- At `2026-09-03T16:35:33.782484589Z`, after MSTR traded around $140.12 inside/above the documented $137.50-$139.80 second target zone, the real path closed one of two Sep. 11 $125/$135 spreads for a $6.90 net credit. The long $125 call sold at $16.00 and the short $135 call was covered at $9.10.
- One spread remains. The closed spread realized $428 gross profit versus its $262 allocated entry debit. The $690 proceeds exceed the original $524 aggregate debit for both spreads, so the combined package has locked at least $166 gross profit even if the retained spread later expires worthless.
- At the immediate post-fill broker marks, the retained spread was worth $690 and the total package value including sale proceeds was $1,380, or +$856 (+163.36%) versus the $524 original aggregate debit.
- Existing ghost alternatives remain unchanged and will be scored at the common 2026-09-03 close checkpoint. The retained runner keeps the $148-$150 extension objective, $117.50 underlying invalidation, and 2026-09-09 common endpoint.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-03 close checkpoint

- Observed from Alpaca at approximately `2026-09-03T19:59:59Z`: MSTR $143.44/$144.86; Sep. 11 $125 call $20.31/$21.10 and $135 call $12.13/$12.86. The conservative executable spread value was $7.45.
- Real path after the one-spread target trim: $690 actual sale proceeds plus one retained spread worth $745; total package value $1,435; P/L +$911 (+173.85%) versus the $524 original debit.
- `NO_TRADE`: $0.
- `MSTR_50_STOCK`: remains `UNSCORABLE`; the decision-time entry was never defined and no historical price is manufactured.
- `TWO_LONG_125_CALLS`: executable value $4,062 at the $20.31 bid; P/L +$3,184 (+362.64%) versus $878 premium.
- `ONE_125_135_SPREAD`: executable value $745; P/L +$485 (+186.54%) versus the $260 simulated debit.
- The underlying closed above the prior second target but below the $148-$150 runner target; the $117.50 invalidation remained intact. Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- No synchronized executable option close was recoverable. The Sep. 11 $125 and $135 calls' last-trade bars closed $18.53 and $10.13, implying a disclosed non-executable spread reference of $8.40.
- At that proxy: real path equals $690 proceeds plus $840 retained value = $1,530, P/L +$1,006 (+191.98%); `TWO_LONG_125_CALLS` proxy value $3,706 and P/L +$2,828; `ONE_125_135_SPREAD` proxy value $840 and P/L +$580. `NO_TRADE`: $0; stock path remains UNSCORABLE.
- Because these are last-trade proxies, option paths are formally UNSCORABLE for executable checkpoint ranking. Underlying closed $142.64, above invalidation and below the $148-$150 runner target. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- No synchronized executable option close was preserved. Official contract close prices were $12.56 for the $125 call and $5.13 for the $135 call, implying a disclosed non-executable spread reference of $7.43; MSTR's underlying official close was $136.53.
- At that proxy, the real path was $690 prior proceeds plus $743 retained value = $1,433, P/L +$909 versus the original $524 debit. `TWO_LONG_125_CALLS`: $2,512, P/L +$1,634. `ONE_125_135_SPREAD`: $743, P/L +$483. `NO_TRADE`: $0; the stock path remains UNSCORABLE.
- All option paths remain formally UNSCORABLE for executable ranking because these are official closes, not synchronized two-sided markets.
- The runner remained above invalidation but below its $148-$150 target. It was subsequently closed on 2026-09-09 for a $6.35 credit; that action does not alter this checkpoint.
- Next checkpoint and endpoint: 2026-09-09 regular-market close.

## 2026-09-09 endpoint review

- Assessment status: `COMPLETE`. Paper API reconciliation confirms the replacement entry filled two spreads at `$2.62` each, the first spread later closed for `$6.90`, and the retained spread closed in the separate 2026-09-09 MSTR management decision for `$6.35`. Total proceeds were `$1,325`; gross P/L was `+$801` versus the `$524` original debit.
- `NO_TRADE`: `$0` P/L. `MSTR_50_STOCK`: `UNSCORABLE` from inception because the decision-time stock market was abnormally wide. `TWO_LONG_125_CALLS` and `ONE_125_135_SPREAD`: `UNSCORABLE` at the endpoint because no synchronized executable option close was preserved; official/last-trade option values are not substituted.
- Supported conclusion: the defined-risk spread captured a large positive outcome and beat no trade, but the endpoint evidence cannot rank it against the uncapped calls or stock path. The target reduction and later expiry-risk exit were effective real-path management, though the later close is correlated evidence rather than an independent decision case.
- Dimension review: thesis/forecast good on continuation but not on the runner target; instrument good for bounded crypto-beta risk; timing good; sizing acceptable but not fully testable against alternatives; execution mixed-good because one permitted replacement filled and both later exits were filled as intended.
- Data quality: `partial`; option and stock alternatives remain unavailable or unscorable at the common endpoint.
- Lesson change: none; existing option-payoff guidance already covers the capped-spread tradeoff.
