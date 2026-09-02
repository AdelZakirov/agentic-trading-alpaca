# Ghost set: alpaca-stage2-20260901-PCG-sell

- Status: ACTIVE
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
- The real full exit leads both retention alternatives at this mark. Sell-thesis invalidation above $13.70/$14.00 was not active. Next checkpoint: 2026-09-02 regular-market close.
