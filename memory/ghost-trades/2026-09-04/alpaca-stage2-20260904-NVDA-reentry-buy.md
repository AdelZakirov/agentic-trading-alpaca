# Ghost set: alpaca-stage2-20260904-NVDA-reentry-buy

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260904-NVDA-reentry-buy`
- Broker order ID: `2b09aab7-20be-4260-ad14-db4749573cc0`
- Ticker: NVDA
- Decision time: approximately 2026-09-04T15:50:25Z
- First and final fill time: 2026-09-04T15:51:33.430281999Z
- Evaluation start: 2026-09-04T15:51:33.430281999Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-04 and 2026-09-08 through 2026-09-11 regular-market closes
- Holding plan: support-retest entry with same-day first target and continuation only while the breakout structure remains intact
- Tactical/structural stop: $229.75
- Hard thesis failure: below $224.75-$225
- Targets: $234.75, then a fresh decision for $238.50-$240 and $245

## Thesis and actual fill

The morning breakout to $234.75 retraced on contracting 15-minute volume into $231.30-$231.60 while completed 15-minute closes remained above $231.28. Fresh moneyheap research classified the action as support stabilization, not a failed breakout. The re-entry fixes the first trade's construction error by placing the stop below the $229.80-$230.40 breakout floor.

- Instrument: NVDA common stock
- Actual action: buy 125 shares at average $231.16
- Initial capital deployed: $28,895.00
- Bracket: $234.75 take-profit and $229.75 stop
- Planned downside from actual fill: approximately $176.25 before gaps/slippage
- Planned upside to target: approximately $448.75
- Pre-trade NVDA exposure: none; the earlier 85-share trade was already closed
- Size rationale: an initial support tranche with less than $250 planned downside, not a full risk-budget allocation

## Contemporaneous market data

- Alpaca IEX stock quote at `2026-09-04T15:50:16.068307885Z`: $231.43 bid / $231.45 ask, bid size 100 / ask size 500; last trade $231.44.
- Focused Sep. 11 indicative option quotes at about 15:49Z: $230 call $4.76/$4.87, IV 31.76%, delta 0.5692, theta -0.2982; $240 call $1.12/$1.18, IV 31.31%, delta 0.2103, theta -0.2114.
- Fresh research: [`174819-NVDA-technical.md`](../../research/2026-09-04/174819-NVDA-technical.md).

## Ghost alternatives fixed before submission

### NO_REENTRY

- Add no NVDA exposure after the first stop. Capital and P/L remain zero.

### HALF_SIZE_62

- Buy 62 shares at the same entry timing and $231.60 cap with the same $234.75 target and $229.75 stop.
- Simulated fill: $231.16, matching the real order's executable timing.
- Planned downside: approximately $87.42; planned upside: approximately $222.58.

### WAIT_CONFIRM_233

- Buy 125 shares only after a completed 15-minute close above $233 with more than 200,000 shares of 15-minute volume.
- Entry remains UNENTERED until the objective trigger; price at the then-current executable ask.
- Use the same common endpoint and $229.75 structural stop unless the trigger-time evidence requires a tighter non-hindsight adjustment.

### SEP11_230_240_CALL_SPREAD

- Buy two Sep. 11 $230/$240 bull call spreads at the contemporaneous conservative $3.75 debit.
- Maximum loss: $750; maximum gross profit: $1,250; expiration breakeven: $233.75.
- Exit by Sep. 10 or earlier on a 50% premium loss or underlying below $225. Mark from executable option sides.

## Initial post-fill state

- Real path: OPEN, 125 shares at $231.16. At `2026-09-04T15:52:04.503741302Z`, executable bid/ask was $231.05/$231.07; conservative P/L about -$13.75. The $234.75 target was `new` and the paired $229.75 stop was `held`.
- `NO_REENTRY`: $0.
- `HALF_SIZE_62`: OPEN at simulated $231.16; conservative P/L about -$6.82 at the same bid.
- `WAIT_CONFIRM_233`: UNENTERED.
- `SEP11_230_240_CALL_SPREAD`: simulated entry at $3.75; score at the regular close with synchronized executable quotes.
- Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-04 stop and close checkpoint

- Alpaca later confirmed the $229.75 stop sold all 125 shares at $229.645839 at `2026-09-04T19:30:19.026092Z`; the paired target canceled. Realized gross P/L was approximately -$189.27 versus $231.16.
- `NO_TRADE`: $0. `WAIT_CONFIRM_233`: UNENTERED because the required post-decision 15-minute close/volume confirmation did not occur. `SEP11_230_240_CALL_SPREAD`: no synchronized executable close was recovered and is UNSCORABLE.
- The wider structure-based stop still failed on the same day; no NVDA exposure remained at the $230.19 official close. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- The real re-entry and its half-size analogue remain fixed at their recorded stop outcomes; `NO_TRADE` remains $0.
- `WAIT_CONFIRM_233` remains UNENTERED/UNSCORABLE because no qualifying executable confirmation and fill were preserved. The call-spread path also remains UNSCORABLE. NVDA's $225.82 official daily close is disclosed only as context.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- The real re-entry remains fixed at its recorded stop outcome of approximately -$189.27; `NO_TRADE` remains $0. `HALF_SIZE_62` remains a fixed same-entry analogue with approximately half the realized loss.
- NVDA's official 2026-09-09 daily close was $223.77, below the documented $224.75-$225 hard-failure area, but no retrospective path change is made. `WAIT_CONFIRM_233` and `SEP11_230_240_CALL_SPREAD` remain UNSCORABLE/unentered under their fixed rules.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- NVDA's official 1Day close was `$218.37` at the common `2026-09-10T20:00:00Z` checkpoint; the after-close quote had no ask and a `$209.47` bid, so this is a disclosed non-executable underlying proxy.
- The real re-entry remains fixed at approximately `-$189.27`; `NO_REENTRY` remains `$0`; `HALF_SIZE_62` remains fixed at approximately `-$93.88`. `WAIT_CONFIRM_233` remained unentered and the call-spread path remains UNSCORABLE under its fixed rules.
- The `$224.75-$225` hard-failure context is historical only because the real path had already stopped. No retrospective path change is made. Next checkpoint: 2026-09-11 regular-market close.
