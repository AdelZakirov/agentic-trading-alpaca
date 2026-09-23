# EGO pre-trade alternatives

## Identity

- decision_id: `alpaca-stage2-20260922-EGO-buy`
- creator_run_id: `922582db-61d4-4434-99a0-586fe301544f`
- decision_at: `2026-09-22T16:49:41+02:00`
- ticker: `EGO`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260922-EGO-buy`
- broker_order_id: null

## Original decision

- Thesis: first Skouries concentrate, a fresh BofA Underperform-to-Buy reversal with a $54 target, 8.24x forward P/E, and a still-intact long-term uptrend support a 1-4 week rerating; gold/copper exposure diversifies the current growth-heavy book.
- Chosen action: buy 200 EGO shares with a day limit no higher than $43.95; never chase above the bound.
- Pre-trade exposure: zero EGO; portfolio equity $102,591.20, cash $42,693.43, stock market value about $59,898, eleven stock positions, no options, no open orders.
- Size rationale: about $8,790 notional/8.6% of equity; about $690 risk to a $40.50 daily-close invalidation and $910 to the $39.40 structural stop before gaps. Post-fill long exposure would be about 67% of equity, with no leverage and improved sector diversification.
- Invalidation and horizon: daily close below $40.50 invalidates; $39.40 is structural failure. Review $45.50-$46, then $48-$48.35/$51-$54; 1-4 week horizon and immediate review on Skouries delays or a sharp gold reversal.

## Evaluation rules

- Common start: chosen and size-variant comparisons start only after a broker-confirmed EGO fill; otherwise remain unscored. The pullback alternative activates only on a $42.50-$43.10 trade followed by intraday stabilization before 2026-09-25 close. No-trade starts at the chosen fill time or, if unfilled, at 2026-09-22 close.
- Checkpoints: end of 2026-09-22, then 1, 5, 10, and 20 trading sessions after activation.
- End rule: earliest of target review execution, daily-close invalidation followed by next eligible exit, a material thesis break, or 2026-10-20 close. Mark-to-market at the common executable bid; apply the same exit rule to share alternatives.
- Exit handling: daily-close triggers are not converted into intraday stops. If the chosen order never fills, fill-anchored comparisons stay unscored.

## Initial evidence

- moneyheap fundamental at `2026-09-22T16:39:18+02:00`: strong rating; tactical $43.50-$44.50 entry, $41.20 close review, $48.50 then $51-$54 targets.
- moneyheap technical at `2026-09-22T16:39:54+02:00`: bullish pullback/range-reaccumulation; preferred $42.50-$43.10, aggressive $43.50-$43.80, close invalidation $40.50, structural $39.40, targets $45.50-$46 and $48-$48.35.
- IEX sequence: `14:45:17Z` $43.80/$43.85; `14:46:28Z` abnormal $38.21/$43.84; `14:48:01Z` $43.87/$43.91; `14:49:14Z` $43.91/$43.95. Each displayed size was 100 shares. The abnormal quote was not used alone; the later two quotes normalized.
- Missing data: IEX is a limited venue, not SIP; fills, future prices, and overnight gaps are unknown.

## Alternatives

### Half-size now

- Label/question: `half-size-now`; does reducing exposure improve risk-adjusted outcome?
- Instrument/action: EGO stock, buy 100 shares.
- Entry rule and simulated price: contemporaneous ask $43.95 at chosen-order submission time.
- Notional/max loss: $4,395 notional; about $345 to the $40.50 close invalidation and $455 to $39.40, excluding gaps.
- Exit: same invalidation, target, and end rules as chosen action.
- Pricing assumption: buy at ask, sell at bid; no fees modeled.

### Preferred pullback

- Label/question: `pullback-entry`; does waiting for the preferred technical zone improve outcome without missing the move?
- Instrument/action: EGO stock, buy 200 shares only after a $42.50-$43.10 trade and intraday stabilization.
- Entry rule and simulated price: first qualifying ask at or below $43.10 through 2026-09-25; otherwise `UNSCORABLE` as not activated.
- Notional/max loss: at $43.10, $8,620 notional; about $520 to $40.50 and $740 to $39.40, excluding gaps.
- Exit: same invalidation, target, and end rules as chosen action.
- Pricing assumption: qualifying ask, never a manufactured midpoint.

### No trade

- Label/question: `no-trade`; was adding EGO better than retaining cash?
- Instrument/action: no trade; zero notional and zero capital at risk.
- Entry rule and simulated price: starts at chosen fill time or 2026-09-22 close if the chosen order is unfilled; value remains $0 P/L.
- Exit: same common end date.

## Execution

- submitted_at: `2026-09-22T14:51:20.074123693Z`
- broker_order_id: `257f6b31-f9be-4b28-9d7c-53fea8de9112`
- broker_status: `new` at `2026-09-22T14:55:39Z`
- filled_qty: `0`
- filled_avg_price: null

## Reviewer updates

Reserved for reviewer.
