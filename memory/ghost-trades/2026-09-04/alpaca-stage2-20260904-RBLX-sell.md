# Ghost set: alpaca-stage2-20260904-RBLX-sell

- Status: ACTIVE
- Real client order ID: `alpaca-stage2-20260904-RBLX-sell`
- Broker order ID: `fafaa3af-44bd-4252-88d2-2123a4fd81cf`
- Ticker: RBLX
- Decision/order time: 2026-09-04T14:48:57.399878Z
- First partial fill: 50 shares at average $42.52 at 2026-09-04T15:04:16.056345Z
- Final fill: 100/100 shares at average $42.515 at 2026-09-04T15:04:24.623578Z
- Evaluation start: 2026-09-04T15:04:16.056345Z
- Evaluation end: 2026-09-11 regular-market close
- Checkpoints: 2026-09-04 and 2026-09-08 through 2026-09-11 regular-market closes
- Holding plan: realize 40% at first resistance and retain 150 shares toward $45-$46
- Runner support: $41.40; secondary intraday review below $42.00 on a 15-minute close

## Thesis and actual fill

RBLX reclaimed the $42.50 first objective after an earlier target touch and retracement. The bounded sale converted the defined target into a realized reduction while preserving a 150-share runner.

- Pre-trade exposure: 250 RBLX shares at average $40.41
- Actual action: sell 100 shares at average $42.515; retain 150 shares
- Realized gross result: approximately +$210.50 versus average cost
- Retained capital at the fill price: approximately $6,377.25
- Size rationale: the fresh technical review recommended a 100-share trim at $42.50-$43.00 and a 150-share runner toward $45-$46

## Contemporaneous market data

- Source: Alpaca IEX execution and the fresh moneyheap technical artifact [`163936-RBLX-technical.md`](../../research/2026-09-04/163936-RBLX-technical.md).
- The research observed an intraday rise from $41.41 through $42.625, tight consolidation near $42.30-$42.35, resistance at $42.50-$43.28, and key runner support at $41.40-$41.50.
- The real day limit required $42.50 or better; it filled only after that objective trigger was executable.

## Ghost alternatives fixed before submission

### HOLD_250

- Retain all 250 shares under the same $41.40 support and $45-$46 extension plan.

### EXIT_ALL_250_AT_TRIGGER

- Sell all 250 shares at the same $42.515 executable trigger and retain no RBLX exposure.

### NO_RECLAIM_NO_SALE

- Sell nothing unless $42.50 becomes executable. The objective trigger did activate, so this path now retains 250 shares for the common comparison window.

## Tracking rules

Compare every path from the same 250-share pre-trade exposure. Include sale proceeds and mark retained shares at the conservative executable bid. Use the same chronological window and objective triggers. Ghosts never reach Alpaca or affect portfolio state.

## Initial post-fill state

- Real path: 100 shares sold at $42.515 and 150 remain open.
- `HOLD_250`: 250 shares remain.
- `EXIT_ALL_250_AT_TRIGGER`: simulated sale of 250 at $42.515 and no shares remain.
- `NO_RECLAIM_NO_SALE`: 250 shares remain after the trigger; it tests the consequence of ignoring the reclaimed target.
- Next checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 close checkpoint

- Common stock mark: $43.29 executable bid near the close.
- Real path: $4,251.50 proceeds plus 150 shares worth $6,493.50 = $10,745.00. `HOLD_250` and `NO_RECLAIM_NO_SALE`: $10,822.50, leading real by $77.50. `EXIT_ALL_250_AT_TRIGGER`: $10,628.75, trailing real by $116.25.
- The 40% trim was the middle outcome: it captured gains while retaining participation. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $44.83; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real 100-share reduction: $4,251.50 proceeds plus 150 shares worth $6,724.50 = $10,976.00. `HOLD_250` and `NO_RECLAIM_NO_SALE`: $11,207.50, leading real by $231.50. `EXIT_ALL_250_AT_TRIGGER`: $10,628.75, trailing real by $347.25.
- Partial reduction remained between the full-retention and full-exit paths while preserving the 150-share runner.
- Next checkpoint: 2026-09-09 regular-market close.

## 2026-09-09 close checkpoint

- Alpaca's official 2026-09-09 daily bar closed at $44.52 (high $45.04, low $43.51); this is a non-executable proxy because the near-close quote was abnormally wide at $42.27/$47.01.
- Real 100-share reduction: $4,251.50 proceeds plus 150 shares at $44.52 = $10,929.50. `HOLD_250` and `NO_RECLAIM_NO_SALE`: $11,130.00, leading real by $200.50. `EXIT_ALL_250_AT_TRIGGER`: $10,628.75, trailing real by $300.75.
- The $41.40 runner support was not breached by the close. Partial reduction remained between full retention and full exit; no new lesson is supported.
- Next checkpoint: 2026-09-10 regular-market close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: RBLX close `$44.85`; the after-close quote was wide at `$42.58/$47.41`, so the bar is a disclosed non-executable proxy.
- Real path: `$4,251.50` proceeds plus 150 shares worth `$6,727.50` = `$10,979.00`, P/L `+$876.50` versus the `$10,102.50` original cost. `HOLD_250` and `NO_RECLAIM_NO_SALE`: `$11,212.50`, P/L `+$1,110.00`; `EXIT_ALL_250_AT_TRIGGER`: fixed `$10,628.75`, P/L `+$526.25`.
- Full retention led the real trim by `$233.50`, while the real trim led the full exit by `$350.25`. The `$41.40` runner support remained intact. Next checkpoint: 2026-09-11 regular-market close.

## 2026-09-11 close checkpoint and endpoint

- Observed at `2026-09-11T20:00:00Z` from the Alpaca IEX official 1Day bar: RBLX close `$45.495`; this is a disclosed non-executable proxy.
- Real path: `$4,251.50` proceeds plus 150 shares worth `$6,824.25` = `$11,075.75`, P/L `+$973.25` versus the `$10,102.50` original cost. `HOLD_250` and `NO_RECLAIM_NO_SALE`: `$11,373.75`, P/L `+$1,271.25`; `EXIT_ALL_250_AT_TRIGGER`: fixed `$10,628.75`, P/L `+$526.25`.
- Full retention led the real trim by `$298.00`; the real trim led full exit by `$447.00`. Runner support remained intact. Comparison complete; no lesson change.
