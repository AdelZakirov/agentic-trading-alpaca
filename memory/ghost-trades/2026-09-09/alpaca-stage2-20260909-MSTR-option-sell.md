# Ghost set: alpaca-stage2-20260909-MSTR-option-sell

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260909-MSTR-option-sell`
- Broker order ID: `7bc99118-4b22-42f8-94eb-3e7902a50527`
- Ticker: MSTR
- Decision time: approximately 2026-09-09T16:17:00Z
- Fill time: `2026-09-09T16:20:17.597138468Z`
- Evaluation start: `2026-09-09T16:20:17.597138468Z`
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-09, 2026-09-10, and 2026-09-11 regular-market closes
- Holding plan tested: close the expiring runner versus holding through expiry or rolling one week

## Thesis and actual fill

Moneyheap technical and fundamental research both favored closing the final Sep. 11 $125/$135 bull call spread. The macro trend remained constructive, but front-week momentum had turned choppy, underlying price was near the short $135 strike, and pin/assignment risk dominated the remaining two-session opportunity.

- Actual action: sell to close one `MSTR260911C00125000` and buy to close one `MSTR260911C00135000` atomically.
- Actual leg fills: long $125 call sold at $9.95; short $135 call covered at $3.60.
- Actual net credit: $6.35, or $635 proceeds before fees.
- Allocated entry debit: $2.62, or $262; realized gross profit on this spread: $373.
- Combined two-spread campaign: first spread realized $428 gross and the runner realized $373 gross, for approximately $801 gross before fees.
- Residual MSTR exposure: none.

## Contemporaneous market data and execution

- The latest valid OPRA observation before execution was approximately $10.33/$10.64 for the $125 call and $3.69/$3.79 for the $135 call, a conservative $6.54 closing credit. A subsequent OPRA route returned `403`; the broker's combined position mark was about $6.30.
- The bounded multi-leg day limit required at least a $6.20 credit and filled immediately at $6.35. No replacement was used.
- Underlying MSTR traded near $134.40-$134.54 around reconciliation, below the day's $141.87 high and near the short strike.

## Ghost alternatives fixed before submission

### HOLD_TO_EXPIRY

- Retain the Sep. 11 $125/$135 spread through the 2026-09-11 close/expiry settlement, including assignment/exercise handling.
- Reference value at execution: $6.35 based on the actual simultaneous leg fills.

### ROLL_SEP18_135_145

- Close the current spread and buy one Sep. 18 $135/$145 bull call spread at the contemporaneous researched $4.28 conservative debit.
- New maximum loss $428; expiration breakeven $139.28; maximum gross profit $572.
- At inception, $207 of net proceeds plus the new spread's $428 cost preserves a $635 reference package value.

### REAL_CLOSE_NOW

- Actual full close for $635 proceeds and no remaining expiry or assignment risk.

## Initial observation

- `REAL_CLOSE_NOW`: $635 fixed proceeds.
- `HOLD_TO_EXPIRY`: $635 reference value at the simultaneous execution prices.
- `ROLL_SEP18_135_145`: $207 net proceeds plus a newly opened spread at its $428 cost, total $635 reference value.
- Initial values are equal by construction; subsequent checkpoints test whether avoiding expiry risk outweighed foregone continuation. Ghosts never reach Alpaca or affect portfolio state.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- `REAL_CLOSE_NOW` remains fixed at $635 proceeds. No synchronized executable market was recoverable for the Sep. 11 $125/$135 spread or the Sep. 18 $135/$145 roll at the common close, so `HOLD_TO_EXPIRY` and `ROLL_SEP18_135_145` remain formally UNSCORABLE rather than using stale or non-synchronized option marks.
- MSTR's official underlying daily close was $132.64, disclosed only as context and not substituted for option values. No new lesson is supported.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- `REAL_CLOSE_NOW` remains fixed at `$635` proceeds. No synchronized executable close was available for the Sep. 11 `$125/$135` spread or the Sep. 18 `$135/$145` roll through the configured Alpaca OPRA route, so `HOLD_TO_EXPIRY` and `ROLL_SEP18_135_145` remain UNSCORABLE.
- MSTR's official 1Day underlying close was `$128.62` at the common `2026-09-10T20:00:00Z` checkpoint, disclosed only as context and not substituted for option values. No new lesson is supported. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- `REAL_CLOSE_NOW` remains fixed at `$635` proceeds. No synchronized executable historical market was available for the Sep. 11 `$125/$135` spread or the Sep. 18 `$135/$145` roll, so `HOLD_TO_EXPIRY` and `ROLL_SEP18_135_145` remain UNSCORABLE.
- MSTR's official 1Day underlying close was `$130.96`, disclosed only as context and not substituted for option values. Comparison complete with partial data; no lesson change.
