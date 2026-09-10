# Ghost set: alpaca-stage2-20260904-SMMT-buy

- Status: COMPLETE
- Real client order ID: `alpaca-stage2-20260904-SMMT-buy`
- Broker order ID: `e634e654-c0a9-42b2-af74-afca476fbcef`
- Ticker: SMMT
- Decision time: approximately 2026-09-04T16:39:30Z
- First and final fill time: 2026-09-04T16:53:19.756747435Z
- Evaluation start: 2026-09-04T16:53:19.756747435Z
- Evaluation end: 2026-09-04 regular-market close
- Checkpoints: initial post-fill and 2026-09-04 regular-market close
- Holding plan: approximately 45 minutes to two hours, with no intended overnight hold without a fresh close decision
- Stop: $17.18
- Target: $17.70

## Thesis and actual fill

SMMT's multi-day accumulation trend remained constructive, but buying the session high was rejected. The real order waited for a retest of the $17.30-$17.33 five-minute pivot, using a bracket to bound a late-session continuation attempt.

- Instrument: SMMT common stock
- Actual action: buy 1,000 shares at $17.33
- Initial capital deployed: $17,330
- Bracket: $17.70 take-profit and $17.18 stop
- Planned downside: approximately $150 before gaps/slippage
- Planned upside to target: approximately $370
- Pre-trade SMMT exposure: none
- Size rationale: a tightly stopped incremental position with about 0.15% of account equity planned risk, not a use-cash target

## Contemporaneous market data

- Alpaca IEX stock quote at `2026-09-04T16:39:20.151909871Z`: $17.47 bid / $17.48 ask, 100 / 100 displayed; last trade $17.475. The completed 12:35-12:40 ET five-minute bar closed $17.445 on 1,863 shares.
- Focused Sep. 11 indicative option quotes around the decision: $17 call $0.72/$1.02 and $18 call $0.32/$0.48, making a conservative $0.70 debit for the $17/$18 call spread. Open interest was 2 and absent, respectively.
- Fresh research: [`183729-SMMT-technical.md`](../../research/2026-09-04/183729-SMMT-technical.md).

## Ghost alternatives fixed before submission

### NO_TRADE

- Add no SMMT exposure. Capital and P/L remain zero.

### HALF_SIZE_PULLBACK

- Buy 500 shares at $17.33 with the same $17.70 target and $17.18 stop.
- Simulated fill: $17.33, matching the real order's executable timing.
- Planned downside: $75; planned upside: $185.

### CONFIRMED_BREAKOUT

- Buy 1,000 shares only after a completed five-minute close above $17.46 on at least 7,500 IEX shares.
- Entry remains UNENTERED until the objective trigger and is priced at the then-current executable ask.
- Stop $17.32 and target $17.75 after entry.

### SEP11_17_18_CALL_SPREAD

- Buy two Sep. 11 $17/$18 bull call spreads at the contemporaneous conservative $0.70 debit.
- Maximum loss: $140; maximum gross expiration profit: $60; breakeven: $17.70.
- Close at the common evaluation end using conservative executable sides; no overnight extension.

## Initial post-fill state

- Real path: OPEN, 1,000 shares at $17.33. At `2026-09-04T17:25:00Z`, the executable stock quote was $17.36/$17.38; conservative P/L was approximately +$30. The $17.70 target was `new` and the $17.18 stop was `held`.
- `NO_TRADE`: $0.
- `HALF_SIZE_PULLBACK`: OPEN at simulated $17.33; conservative P/L approximately +$15 at the same $17.36 bid.
- `CONFIRMED_BREAKOUT`: UNENTERED. No completed five-minute bar through 13:20 ET both closed above $17.46 and traded at least 7,500 IEX shares; the highest-volume relevant bar closed $17.44 on 6,670 shares.
- `SEP11_17_18_CALL_SPREAD`: simulated entry at $0.70. At about `2026-09-04T17:25:43Z`, the conservative executable value was $0.25 ($17-call bid $0.77 less $18-call ask $0.52), for approximately -$90 on two spreads. The wide execution penalty is material.
- Next checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 close completion

- The `CONFIRMED_BREAKOUT` trigger activated when the 15:25-15:30 ET five-minute bar closed $17.515 on 7,600 IEX shares. The next executable quote was $17.52/$17.54, so the ghost enters 1,000 shares at $17.54 with $17.32 stop and $17.75 target.
- The last normal close quote was $17.60/$17.61 at `2026-09-04T19:59:54.329974884Z`; the later $17.31/$18.20 quote was rejected as abnormal.
- Real pullback path: 1,000 shares at $17.33 marked at $17.60, P/L +$270 (+1.56%). `HALF_SIZE_PULLBACK`: +$135 (+1.56%). `NO_TRADE`: $0. `CONFIRMED_BREAKOUT`: +$60 (+0.34%) at the same close bid; neither $17.32 stop nor $17.75 target activated after entry.
- `SEP11_17_18_CALL_SPREAD`: no historical synchronized executable close was recoverable; formally UNSCORABLE rather than extrapolating the earlier wide quotes.
- Outcome: the real pullback entry decisively beat waiting for confirmation and no-trade over the planned intraday window. Full size beat half only by scaling the same return.
- Decision review: thesis, forecast, stock selection, pullback timing, and size were good; options were correctly rejected. Execution quality was mixed because the day-only exits expired at the close and no close reconciliation occurred, leaving an unintended overnight position despite the stated plan.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.
