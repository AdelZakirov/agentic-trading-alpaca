# CADL exit alternatives

## Identity
- decision_id: alpaca-stage2-20261002-CADL-sell
- creator_run_id: 2c215101-4a65-42a2-b094-f832bb6de4ac
- decision_at: 2026-10-02T13:23:17.719214362-04:00
- ticker: CADL
- status: ACTIVE
- client_order_id: alpaca-stage2-20261002-CADL-sell
- broker_order_id: ebd6974e-da7a-4df2-8210-6005c65f29d8

## Original decision
SELL all 400 owned shares. October 1 completed IEX close $10.16 breached the previously declared $10.40 daily-close exit-review rule. October 2 remains below that threshold. Fresh moneyheap technical evidence shows sub-50 RSI, negative MACD and distribution; no confirmed reclaim. The year-end BLA remains a longer catalyst and does not justify renewing the failed tactical setup. Pre-trade exposure: 400 shares at $11.44 average, $4,576 basis. Moderate-high confidence in reduction; future return uncertain. No new put or hedge: this is an invalidated long exit, without a separately validated bearish event/payoff edge.

Chosen execution: SELL 400 DAY limit at $10.20, extended_hours=false. Reference bid $10.21, max initial concession $0.01/share ($4); absolute lower execution bound $10.18 after a fresh reassessment, at most one replacement. No market order. Owned quantity confirmed; no other open CADL order; intended client ID returned explicit broker 404/not found.

## Evaluation rules
Filled comparison starts only at reviewer-confirmed actual fill; before then no fabricated realized P/L. Compare changes in portfolio P/L relative to retaining all 400 shares at contemporaneous reference $10.21. Common checkpoints: October 2 close, October 5 close, October 8 close (end). Final marks require trustworthy executable bid; missing marks UNSCORABLE. Any alternative exit is next regular-session executable bid after its declared completed-close trigger, and stays frozen afterward. No automatic re-entry. Dividend/corporate actions included if any. Actual full exit has zero future CADL exposure.

## Initial evidence
- Alpaca paper MCP clock: 2026-10-02T13:23:17.719214362-04:00, regular market open.
- Quote source: IEX; observed 2026-10-02T17:23:16.432052185Z; bid/ask $10.21/$10.23; displayed sizes 300/500; spread $0.02.
- Completed October 1 bar: open10.42/high10.49/low10.16/close10.16, volume43317. October 2 partial bar is not a completed close.
- [Fresh research](../../research/2026-10-02/192155-CADL-technical.md).
- Options quotes not requested: no selected options alternative or separately established bearish thesis.

## Alternatives
### A — Hold all 400 through short recovery window
Question: does accepting continued failed-setup risk outperform exiting now?
Genuinely considered, rejected for unconfirmed reclaim and biotech downside. Stock long, 400 shares retained; no new buy, reference existing exposure at $10.21 bid ($4,084). This is an explicitly separate renewal scenario after the original threshold has already activated, not a rewrite of the original trade rule. Exit next session after completed close below $9.80, or at October 8 close checkpoint; no re-entry. Gross adverse move from reference to9.80 is $164, but full $4,084 reference value remains at risk and gaps are uncapped. Pricing at executable bid on exit; no slippage/fees assumed yet; missing mark UNSCORABLE.

### B — Sell 200 and retain 200
Question: does a partial exit retain sufficient catalyst participation to justify remaining risk?
Stock sell200 at contemporaneous bid $10.21, retain200 at same $10.21 reference; no hypothetical new buy. Simulated sale proceeds $2,042; full retained reference capital $2,042 at risk. Remaining200 exit next session if completed close below9.80 or at October8 final checkpoint. Same separate renewal scenario as A, half remaining exposure. Rejected because original tactical setup failed and no credible reclaim currently supports renewed carry. Use conservative executable bids; missing marks UNSCORABLE.

## Execution
No submitted order or confirmed fill at definition time. Actual IDs/fills will be appended before handoff.

## Reviewer updates


## Execution facts appended before handoff
Broker order ebd6974e-da7a-4df2-8210-6005c65f29d8, client alpaca-stage2-20261002-CADL-sell: filled400 at10.20 at2026-10-02T17:25:34.822560247Z. Order-specific FILL activities123+277 at10.20 match400. Proceeds4080; basis4576; gross realized P/L -496 before fees. Post-fill positions omit CADL, zero open orders, broker cash57120.96. Original hypotheses unchanged.

### 2026-10-03 reviewer activation and October 2 close checkpoint

- The manifest source SHA-256 matches its immutable packet snapshot. Read-only Alpaca paper order `ebd6974e-da7a-4df2-8210-6005c65f29d8` is `filled`, SELL 400/400 at `$10.20` at `2026-10-02T17:25:34.822560Z`; matching order-specific FILL activities of 123 and 277 total 400. Current positions omit CADL. Lifecycle state is `ACTIVE`; common start is the confirmed fill.
- Historical IEX near-close quote `2026-10-02T19:59:32.295925Z` was `$10.18 x400` bid / `$10.20 x1000` ask. The daily bar ended `$10.195`; its close is not substituted for an executable mark. The `$9.80` close rule and any re-entry trigger were not reached.
- On the predeclared `$10.21` common decision reference, the real sale at `$10.20` is `-$4`; HOLD_ALL at the near-close `$10.18` bid is `-$12`; SELL_200_KEEP_200 (sell 200 at the defined `$10.21` reference and mark the remaining 200 at `$10.18`) is `-$6`. The real sale leads those alternatives by `$8` and `$2` at this checkpoint. IEX displayed depth covered all retained quantities, but the mark is single-venue and 28 seconds before the bell; treat quality as partial and do not infer a final lesson from the narrow differences.
- Gross realized P/L from the original `$11.44` basis remains `-$496` before fees. Next checkpoint: October 5 close; declared comparison end: October 8 close. No lesson change.
