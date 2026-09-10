# Ghost set: alpaca-stage2-20260902-MMED-sell

- Status: COMPLETE
- Real client order ID: `alpaca-stage2-20260902-MMED-sell`
- Broker order ID: `1da8e90f-4200-469f-a714-b1182e85e614`
- Ticker: MMED
- Decision time: 2026-09-02T19:18:24.553235161Z
- First fill time: 2026-09-02T19:20:04.027779537Z
- Evaluation start: 2026-09-02T19:20:04.027779537Z
- Evaluation end: 2026-09-09 regular-market close
- Checkpoints: 2026-09-02, 2026-09-03, 2026-09-04, 2026-09-08, and 2026-09-09 regular-market closes
- Holding plan: compare half reduction against retaining or fully exiting the original MMED continuation exposure through the original endpoint
- Trigger for the decision: reported 2026-09-02 lock-up expiry and associated overnight supply/gap risk

## Decision and sizing

MMED's earnings/squeeze continuation thesis remained valid above the $22.40 review and $21.80 hard invalidation, but the reported lock-up expiry created a material discontinuous supply risk. The real decision reduced the 250-share position by half while retaining continuation participation.

- Instrument: MMED common stock
- Real side and quantity: SELL 125 shares
- Actual fill: 125 shares at $23.57
- Limit: $23.55 day limit; extended hours disabled
- Pre-trade exposure: 250 shares at $23.76 average
- Sale proceeds: $2,946.25 before fees
- Retained real exposure after fill: 125 shares at $23.76 average
- Planned residual risk to $21.80: approximately $245 before gaps/slippage

## Contemporaneous market data

- Source: Alpaca IEX latest stock quote.
- Preflight quote at 2026-09-02T19:18:24.103936461Z: bid $23.55 / ask $23.67, displayed size 200/200.
- Current first-observation quote at 2026-09-02T19:21:23.576737134Z: bid $23.55 / ask $23.60, displayed size 100/300.
- Current event evidence: [MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/MMED/) reports the lock-up period expiring on 2026-09-02.

## Real path

- Alpaca confirmed the bounded sell `filled` 125/125 at $23.57. No replacement was needed and no open orders remain.
- At the first observation, the remaining 125 shares were marked at the $23.55 bid. Sale proceeds plus retained value were $5,890.00, versus $5,887.50 for the 250-share pre-trade reference at the same bid: incremental P/L +$2.50 (+0.04%) before fees.
- Real path remains OPEN with 125 shares.

## Ghost alternatives

### HOLD_FULL

- Question: Was the immediate lock-up risk manageable without reducing the position?
- Instrument: retain 250 MMED shares
- Entry/reference mark: $23.55 bid at the decision snapshot
- Capital at risk at reference: $5,887.50; planned hard-invalidation risk from the $21.80 level was approximately $487.50
- First-observation value: $5,887.50; incremental P/L: $0
- Exit handling: retain through the common endpoint, subject to the existing $22.40 review/$21.80 hard invalidation and supply-event risk

### SELL_FULL

- Question: Would complete de-risking be better than preserving continuation optionality?
- Instrument: sell 250 MMED shares
- Entry rule: sell at the contemporaneous $23.55 bid
- Simulated proceeds: $5,887.50
- First-observation value and incremental P/L: $5,887.50 and $0
- Exit handling: no retained MMED exposure through the common endpoint

## Initial observation

- Observed: 2026-09-02T19:21:23Z, using the same current executable bid for retained shares and both counterfactuals.
- The real path modestly outperformed both alternatives because the fill improved to $23.57, but this is an execution observation, not a completed decision-quality evaluation.
- No common endpoint was reached; next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using the current Alpaca IEX executable bid. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real path: 125 retained shares at $23.54 plus $2,946.25 sale proceeds; total value $5,888.75; incremental P/L +$1.25 versus the $5,887.50 pre-trade reference.
- `HOLD_FULL`: 250 shares at $23.54; value $5,885.00; incremental P/L -$2.50 versus the pre-trade reference.
- `SELL_FULL`: $5,887.50 sale proceeds; incremental P/L $0.
- The half reduction currently outperforms retaining the full position by $3.75 and trails a full exit by $1.25; no common endpoint was reached. Next checkpoint: 2026-09-03 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-03 close checkpoint

- Observed from Alpaca IEX at `2026-09-03T19:59:59Z`; MMED bid/ask was $23.81/$23.98.
- Real half-reduction path: $2,946.25 actual sale proceeds plus 125 shares at $23.81; total value $5,922.50; incremental P/L +$35.00 versus the $5,887.50 decision reference.
- `HOLD_FULL`: 250 shares at $23.81; value $5,952.50; incremental P/L +$65.00.
- `SELL_FULL`: $5,887.50 simulated sale proceeds; incremental P/L $0.
- The real path trails retaining all shares by $30 and leads a full exit by $35 at this checkpoint. No common endpoint or invalidation was reached. Next checkpoint: 2026-09-04 regular-market close.

Ghosts never reach Alpaca or affect portfolio state, exposure, buying power, or risk limits.

## 2026-09-04 close checkpoint

- Common stock mark: $23.26 executable bid near the close.
- Real half reduction: $2,946.25 proceeds plus 125 shares worth $2,907.50; total $5,853.75, incremental P/L -$33.75 versus the $5,887.50 decision reference. `HOLD_FULL`: $5,815.00, -$72.50. `SELL_FULL`: $5,887.50, $0.
- The half reduction led holding all by $38.75 and trailed selling all by $33.75. No invalidation occurred. Next checkpoint: 2026-09-08 regular-market close.

## 2026-09-08 close checkpoint

- Alpaca's 2026-09-08 daily bar closed at $23.31; this is an official-bar, non-executable reference because a synchronized closing quote was not preserved.
- Real half reduction: $2,946.25 proceeds plus 125 shares at $23.31 = $5,860.00, incremental P/L -$27.50 versus the $5,887.50 decision reference. `HOLD_FULL`: $5,827.50, -$60.00. `SELL_FULL`: $5,887.50, $0.
- The real path led holding all by $32.50 and trailed selling all by $27.50. No invalidation occurred.
- Next checkpoint and endpoint: 2026-09-09 regular-market close.

## 2026-09-09 endpoint review

- Assessment status: `COMPLETE`. The Alpaca 2026-09-09 1Day bar closed at `$22.76`; the near-close IEX quote was abnormally wide at `$19.44/$25.79`, so the bar is a disclosed non-executable reference.
- Real half-reduction path: `$2,946.25` proceeds plus 125 shares at `$22.76` = `$5,791.25`, incremental P/L `-$96.25` (`-1.64%`) versus the `$5,887.50` pre-trade reference.
- `HOLD_FULL`: 250 shares at `$22.76` = `$5,690.00`, incremental P/L `-$197.50` (`-3.35%`). `SELL_FULL`: fixed simulated proceeds `$5,887.50`, incremental P/L `$0`.
- Supported conclusion: reducing half materially beat retaining all shares by `$101.25`, while a full exit was better by `$96.25` at this endpoint. The evidence supports the risk-control mechanism but not a universal preference for half versus full exit; the stock mark is only a bar proxy.
- Dimension review: thesis/forecast mixed; timing good relative to the lock-up risk; instrument appropriate; sizing/risk effective; execution good with the bounded 125-share sale filling at `$23.57`.
- Lesson change: none; one concentration-reduction episode is insufficient to alter active lessons.
