# Ghost pre-trade: RBLX partial trim

## Identity

- decision_id: `alpaca-stage2-20260914-RBLX-sell`
- creator_run_id: `f69753d6-76b4-4255-b370-bdb39af6070f`
- decision_at: `2026-09-14T12:28:32-04:00` (America/New_York)
- ticker: `RBLX`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260914-RBLX-sell`
- broker_order_id: null

## Original decision

RBLX is a 75-share long position entered at $40.41 with a broker quote of $50.40 bid / $50.45 ask and unrealized profit of about $752. The fresh technical research identifies a +25% advance, RSI 73.84, price outside the upper Bollinger Band, and a July gap-fill resistance zone around $50.90-$51.05. Sell 25 shares into strength to lock part of the gain while retaining 50 shares for a possible continuation toward $53.50-$55.00. Do not add. The size reduces concentration and leaves participation if the trend extends.

- chosen action: submit a day limit sell for 25 shares at $50.50
- pre-trade exposure: 75 shares long; no RBLX open orders
- invalidation / review: a daily close below $46.80 triggers runner review; a daily close below $44.50 breaks the structural trend
- holding period: trim now if the limit fills; review the remaining 50 shares over the next 1-10 trading days or at $53.50-$55.00

## Evaluation rules

- common window: from the confirmed fill timestamp through 5 trading days, or earlier if a daily-close trigger occurs
- checkpoints: first regular-session close; daily close below $46.80; daily close below $44.50; touch of $53.50-$55.00; end of the fifth trading day
- end rule: compare realized trim P/L plus marked remaining shares against each alternative using the same broker evidence; do not invent fills
- exit handling: hypothetical alternatives use the same daily-close rules and no unplanned intraday exits

## Initial evidence

- Alpaca clock: market open, `2026-09-14T12:28:32-04:00`
- Alpaca account: equity $101,520.34; cash $85,921.43; buying power $367,734.66
- RBLX position: 75 shares, average entry $40.41, market value $3,783, unrealized P/L $752.25
- delayed-SIP quote: bid $50.40, ask $50.45, bid size 500, quote time `2026-09-14T16:13:41.962833339Z`
- research: `memory/research/2026-09-14/182721-RBLX-technical.md`; technical evidence is current research, not a broker fill
- missing data: no live OPRA or alternative execution feed required; delayed-SIP quote is the execution input

## Alternatives

### A — Chosen bounded trim

- label: `chosen-25-share-trim`
- question tested: can partial profit-taking reduce overbought reversal risk while retaining upside?
- instrument: RBLX stock, sell 25 shares
- entry rule: sell limit at $50.50 during the regular session
- simulated entry price: $50.50 limit; conservative contemporaneous bid was $50.40
- maximum loss: not applicable to the sale; retains 50 shares of upside/downside exposure
- exit / handling: remaining 50 shares follow the daily-close rules above
- pricing assumptions: limit may remain unfilled; only broker `filled` status establishes execution

### B — Immediate bid trim

- label: `immediate-25-share-bid`
- question tested: is immediate de-risking better than waiting for the research trim band?
- instrument: RBLX stock, sell 25 shares
- entry rule: hypothetical sell at the contemporaneous bid
- simulated entry price: $50.40 bid
- maximum loss: not applicable to the sale; retains 50 shares
- exit / handling: same daily-close rules as chosen action
- pricing assumptions: conservative bid-side hypothetical; no invented fill

### C — Larger de-risking trim

- label: `immediate-50-share-bid`
- question tested: does a larger reduction improve risk-adjusted outcome at gap-fill resistance?
- instrument: RBLX stock, sell 50 shares
- entry rule: hypothetical sell at the contemporaneous bid
- simulated entry price: $50.40 bid
- maximum loss: not applicable to the sale; retains 25 shares
- exit / handling: same daily-close rules as chosen action
- pricing assumptions: conservative bid-side hypothetical; no invented fill

### D — No trade / hold full position

- label: `hold-75`
- question tested: does momentum continuation outweigh the overbought gap-fill risk?
- instrument: no trade; hold 75 shares
- entry rule: no order and zero new capital at risk
- simulated entry price: null
- maximum loss: no new loss; existing 75-share exposure remains
- exit / handling: same daily-close rules; review the resistance zone at $50.90-$51.05
- pricing assumptions: starts at zero incremental P/L and zero incremental capital at risk

## Execution

- confirmed fill: 25 shares at $50.50
- broker_order_id: `76114a4e-bd9f-486b-95e9-ea3582305a9b`
- broker status: `filled`
- submitted_at: `2026-09-14T16:29:48.706953586Z`
- filled_at: `2026-09-14T16:30:51.373919121Z`
- post-fill position: 50 shares long; 50 shares available
- post-fill account evidence: equity $101,537.72; cash $87,183.93; buying power $366,886.31

## Reviewer updates

Reserved for the ghost reviewer.
