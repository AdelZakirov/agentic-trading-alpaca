# Ghost set: alpaca-stage2-20260904-NVDA-buy

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260904-NVDA-buy`
- Broker order ID: `79fe1a38-7481-48af-94c9-635df6509a62`
- Ticker: NVDA
- Decision time: approximately 2026-09-04T14:44:00Z
- First partial fill: 2 shares at $233.19 at 2026-09-04T14:49:43.384645Z
- Final fill: 83 shares at $233.18 at 2026-09-04T14:49:44.254392722Z
- Evaluation start: 2026-09-04T14:49:43.384645Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-04, 2026-09-08, 2026-09-09, 2026-09-10, and 2026-09-11 regular-market closes
- Holding plan: same-day relative-strength trade with evidence-backed continuation retention through Sep. 11 if neither bracket exit fires
- Tactical invalidation: $231.75 stop; structural review below the $230.40 breakout; hard thesis failure below $225
- Targets: $234.75 first observation, $236-$236.75 same-day objective, then evidence-based continuation only

## Thesis and actual fill

NVDA cleared $230.40 post-payroll on strong volume, held a sequence of higher lows, and showed relative strength against QQQ. Fresh moneyheap technical work favored buying a controlled pullback rather than chasing the high.

- Instrument: NVDA common stock
- Actual action: buy 85 shares at average $233.180235
- Capital deployed: $19,820.32
- Bracket: GTC take-profit $236.50 and stop $231.75
- Planned tactical downside: approximately $121.57 before gaps/slippage
- Structural downside to $225: approximately $695.32 before gaps/slippage
- Pre-trade NVDA exposure: none

## Contemporaneous market data

- Source: Alpaca IEX stock and Alpaca option snapshots.
- Decision quote at approximately 2026-09-04T14:42:03Z: $233.76/$233.79; the order waited at $233.20 rather than chasing.
- Fill-window quote was about $233.09/$233.12 immediately before execution; post-fill quote at 2026-09-04T14:50:41Z was $233.27/$233.30.
- Sep. 11 options at the decision: $232.50 call $4.76/$4.78, delta 0.5579, theta -0.3032; $237.50 call $2.51/$2.52, delta 0.3671, theta -0.2833. Conservative vertical debit $2.27.

## Ghost alternatives fixed before submission

### NO_TRADE

- Add no NVDA exposure. Capital, risk, and P/L remain zero.

### HALF_SIZE_43

- Buy 43 shares at the same $233.20 conditional limit.
- Simulated cost: $10,027.60; planned risk to $231.75 is $62.35 before gaps/slippage.
- Use the same targets, stop, and common endpoint.

### SEP11_232_5_237_5_CALL_SPREAD

- Buy five Sep. 11 $232.50/$237.50 bull call spreads only if the stock entry trigger occurs and debit is no more than $2.27.
- Maximum loss: $1,135; maximum spread value $2,500; maximum gross profit $1,365; expiration breakeven $234.77.
- Entry status: `UNSCORABLE` until the stock trigger and a synchronized option quote occur; no option order was sent.

## Initial post-fill observation

- Real path: 85 shares at $233.180235; post-fill mark $233.27 bid, value $19,828. -$236.50 take-profit active and $231.75 paired stop held.
- `NO_TRADE`: $0.
- `HALF_SIZE_43`: simulated entry at $233.20 only because the real trigger filled; immediate mark uses the same $233.27 bid.
- `SEP11_232_5_237_5_CALL_SPREAD`: remains `UNSCORABLE` because no synchronized fill-time option quote was captured.
- Next checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 real-path stop exit

- The paired $231.75 stop activated. It sold all 85 shares at average $231.699294 at `2026-09-04T15:02:40.391488521Z`; the $236.50 take-profit was canceled by the bracket.
- Realized gross result: approximately -$125.88 versus the $233.180235 entry.
- The real path is CLOSED, but the ghost set remains ACTIVE through the common 2026-09-11 endpoint. The 2026-09-04 close checkpoint remains due at the actual close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- Real path: CLOSED at $231.699294, realized P/L about -$125.88. `NO_TRADE`: $0. `HALF_SIZE_43`: under the identical bracket stop, 43 shares exit at $231.699294 for about -$64.53 versus $233.20.
- `SEP11_232_5_237_5_CALL_SPREAD`: remained UNSCORABLE because no synchronized trigger-time entry quote had been captured; no retrospective price is manufactured.
- The stop removed risk before the $230.19 official close. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- The real stopped stock path and half-size stopped stock path remain fixed at their recorded realized losses; `NO_TRADE` remains $0.
- No synchronized executable option market was recoverable, so the option alternative remains formally UNSCORABLE. NVDA's $225.82 official daily close is disclosed only as underlying context and does not manufacture an option value.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- The real stopped stock path remains fixed at approximately -$125.88; `NO_TRADE` remains $0 and `HALF_SIZE_43` remains fixed at approximately -$64.53 under the same stop.
- NVDA's official 2026-09-09 daily close was $223.77, below the documented $225 hard-failure context, but this does not alter the already-closed real path. The option alternative remains formally UNSCORABLE because no synchronized executable option market was preserved.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- NVDA's official 1Day close was `$218.37` at the common `2026-09-10T20:00:00Z` checkpoint; the after-close quote had no ask and a `$209.47` bid, so this is a disclosed non-executable underlying proxy.
- The real stopped path remains fixed at approximately `-$125.88`; `NO_TRADE` remains `$0`; `HALF_SIZE_43` remains fixed at approximately `-$64.53` under the same stop. The option alternative remains UNSCORABLE because no synchronized executable trigger-time or close market was preserved.
- The earlier $231.75 stop and $225 structural failure are historical context only; no retrospective path change is made. Next checkpoint: 2026-09-11 regular-market close.
