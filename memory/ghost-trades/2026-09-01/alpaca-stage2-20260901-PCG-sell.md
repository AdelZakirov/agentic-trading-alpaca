# Ghost set: alpaca-stage2-20260901-PCG-sell

- Status: COMPLETE
- Real client order ID: `alpaca-stage2-20260901-PCG-sell`
- Broker order ID: `40ebd237-635b-4d47-bdd5-5bbb3c5ba58f`
- Ticker: PCG
- Decision time: 2026-09-01T14:48:44.4363165Z
- First fill time: 2026-09-01T14:49:51.361275348Z
- Evaluation start: 2026-09-01T14:49:51.361275348Z
- Evaluation end: 2026-09-04 regular-market close
- Checkpoints: 2026-09-01, 2026-09-02, 2026-09-03, and 2026-09-04 regular-market closes
- Holding plan: immediate full de-risking after a bearish continuation break; no re-entry in flat drift
- Invalidation of the sell thesis: a higher-low plus close above $13.70 or a daily close above $14.00 with momentum recovery

## Thesis and sizing

PCG's synchronized utility/wildfire-liability breakdown, extreme distribution volume, and strong bearish trend made the existing long's continuation risk outweigh an unconfirmed oversold bounce. The real trade closed the full 750-share position to remove discontinuous downside exposure. Pre-trade position was 750 shares at average $13.42; planned capital released was approximately $9,900 at the contemporaneous bid.

- Instrument: PCG common stock
- Side and quantity: SELL 750 shares
- Actual fill: 750 shares at $13.20
- Realized P/L versus $13.42 average entry: approximately -$165.00 before fees
- Maximum avoided loss: the former stock position's theoretical total-loss exposure was $9,900 at the pre-trade mark; the comparison is about decision quality, not a guaranteed avoided loss
- Exit handling: real path is closed; no automatic stop or further order was submitted

## Contemporaneous market data

- Source: Alpaca IEX latest quote.
- PCG quote at 2026-09-01T14:48:44.4363165Z: bid $13.20 / ask $13.21, bid size 2,200 / ask size 4,800.
- No option ghost was defined because the real decision reduced exposure, fresh technical research flagged inflated post-breakdown IV, and an option would not improve the risk-reduction objective.

## Ghost alternatives

### HOLD_FULL

- Question: Was immediate full de-risking too early versus retaining the entire position through the common window?
- Instrument: PCG common stock
- Side and quantity: retain 750 shares; no broker order
- Entry/reference mark: $13.20 bid / $13.21 ask at the decision snapshot; use the same pre-trade exposure and conservative bid marks at checkpoints
- Capital at risk: 750 shares marked from the $13.20 bid, approximately $9,900
- Maximum loss: theoretical total-loss exposure of approximately $9,900 from the reference mark
- Exit handling: retain through 2026-09-04 unless the documented $13.00 clean-break or $13.70-$14.20 relief management would have triggered an exit

### HALF_SELL

- Question: Would reducing half preserve better rebound optionality while limiting continuation risk?
- Instrument: PCG common stock
- Side and quantity: sell 375 shares at the contemporaneous $13.20 bid and retain 375 shares
- Simulated sale proceeds: $4,950.00 before fees
- Retained exposure reference: 375 shares marked from $13.20, approximately $4,950 capital at risk
- Exit handling: retained shares use the same $13.00 clean-break, $13.70-$14.20 relief, and 2026-09-04 common-window rules

## Tracking rules

Use one common market-data timestamp for the real closed path and both scoreable alternatives at each checkpoint. Price retained stock from the executable bid; compare total wealth including the real sale proceeds and the alternative's retained exposure. Record continuation drawdown, any reclaim, liquidity, and the effect of the avoided PCG gap risk. Ghosts never reach Alpaca and never affect portfolio totals, buying power, or risk posture.

## Catch-up checkpoint for 2026-09-01 close

- Observed: 2026-09-02T16:28:06Z; PCG bid/ask $13.04/$13.06 with positive size. This is a disclosed late checkpoint.
- Real full exit: CLOSED at $13.20; incremental P/L from the decision reference is $0 and realized trade P/L versus the original $13.42 entry remains -$165.
- `HOLD_FULL`: retained-value change -$120 at the $13.04 bid versus the $13.20 decision reference.
- `HALF_SELL`: retained-half change -$60; sold-half proceeds unchanged.
- The real full exit leads both retention alternatives at this mark. Sell-thesis invalidation above $13.70/$14.00 was not active. Next checkpoint: 2026-09-03 regular-market close.

## Catch-up checkpoint for 2026-09-02 close

- Observed: approximately 2026-09-03T14:37:57Z using the current Alpaca IEX executable bid. The scheduled 2026-09-02 close was unavailable, so this is a disclosed catch-up mark.
- Real full exit: CLOSED at the $13.20 fill; decision-reference value remains $9,900.
- `HOLD_FULL`: 750 shares at the $13.57 bid; retained value $10,177.50; incremental P/L +$277.50 versus the $13.20 decision reference.
- `HALF_SELL`: 375 shares at the $13.57 bid plus $4,950.00 sale proceeds; total value $10,038.75; incremental P/L +$138.75 versus the full-position decision reference.
- The real full exit trails both retention alternatives at this catch-up mark, but the sell-thesis invalidation above $13.70/$14.00 was not active. Next checkpoint: 2026-09-03 regular-market close.

## 2026-09-03 close checkpoint

- Observed from Alpaca IEX at `2026-09-03T19:59:59Z`; PCG bid/ask was $13.95/$13.96.
- Real full exit: CLOSED at $13.20; decision-reference value remains $9,900.
- `HOLD_FULL`: 750 shares at $13.95; value $10,462.50; incremental P/L +$562.50 versus the decision reference.
- `HALF_SELL`: $4,950 sale proceeds plus 375 shares at $13.95; total value $10,181.25; incremental P/L +$281.25.
- The $13.955 close followed a higher low and exceeded $13.70, activating the documented sell-thesis invalidation/reclaim condition. Both retention counterfactuals are treated as closed at the $13.95 checkpoint bid for subsequent comparison; the real account remains flat. Next and final checkpoint: 2026-09-04 regular-market close.

## 2026-09-04 close completion

- The retention alternatives were already closed at the documented 2026-09-03 $13.95 reclaim; the 2026-09-04 $14.31/$14.33 close quote does not retrospectively alter those exits.
- Real full exit: $9,900 decision-reference value, incremental P/L $0. `HOLD_FULL`: $10,462.50 final comparison value, +$562.50. `HALF_SELL`: $10,181.25, +$281.25.
- Outcome: full retention through the reclaim beat the real exit by $562.50 and half retention by $281.25. The full sell reduced discontinuous wildfire risk, but it was mistimed relative to the original close-based thesis and the documented reclaim condition.
- Decision review: research identified real tail risk; forecast of immediate continuation was wrong; full-stock exit was an appropriate risk instrument but too aggressive; sizing/execution were clean. This is the same PCG episode as the entry set and counts as one generalizable evidence case, not two independent cases.
