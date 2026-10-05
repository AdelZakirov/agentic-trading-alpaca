# CCK exit decision — original definitions

## Identity

- decision_id: `alpaca-stage2-20260925-CCK-sell`
- creator_run_id: `a2d14c54-69dc-496d-8d5e-c0ec996c75bd`
- decision_at: `2026-09-25T16:37:23+02:00`
- ticker: CCK
- Status: COMPLETE
- client_order_id: `alpaca-stage2-20260925-CCK-sell`
- broker_order_id: `a8242f71-57f3-4964-80c0-5219652b0a92`

## Original decision

Long 50 CCK at broker average $109.67, no open orders. Sep 24 full-market close $105.70 crossed the predeclared $106 daily-close review level, and today’s modest rebound has not restored the $107.19 200-day moving average. [Current moneyheap technical](../../research/2026-09-25/163626-CCK-technical.md) identifies stronger downside momentum and a low-volume bounce. Chosen action: sell all 50 with a regular-session DAY limit near the current bid, removing about $5.3k of cyclical/rate-sensitive stock risk. A new long requires a fresh base/reclaim and thesis. No added option position: a bearish derivative would create a new thesis and option risk rather than simply removing this exposure.

## Evaluation rules

Common comparison starts only after a real broker-confirmed fill. Observe Sep 28 and Oct 2 regular-session closes, ending at Oct 2 close or earlier if a verified corporate event invalidates comparability. Mark retained shares at broker prices and use executable bid for any simulated exit. No real-sale re-entry within this window. If the real order does not fill, leave fill-anchored comparisons inactive.

## Initial evidence

- Alpaca Sep 25 10:34 ET paper account held 50 available CCK; Sep 24 last close reported $105.70 by public historical price and IEX $105.71. No open orders.
- Alpaca IEX Sep 25 10:37:14 ET bid $106.49 x100, ask $106.77 x100. IEX is one exchange; a fresh preflight quote is required before the real order.
- [Moneyheap technical](../../research/2026-09-25/163626-CCK-technical.md): 50-day moving average slopes lower, negative momentum has strengthened, $107.19 200-day average has been lost; the current bounce lacks reversal confirmation.

## Alternatives

1. `HOLD_ALL`: Test whether the $106 review breach was a false breakdown. No trade now; retain 50 shares (roughly $5,325 exposure) and mark at Sep 28/Oct 2 closes. Sell at next regular-session executable bid if another daily close is below $106, or at Oct 2 close otherwise. Entry comparison price is the actual real-sale fill, never a guessed fill. Shares could gap to zero; review is no guaranteed stop. Future prices/exit quote missing.
2. `SELL_25_KEEP_25`: Test partial de-risk. Hypothetically sell 25 at contemporaneous IEX bid $106.49, about $2,662.25 proceeds, retaining 25 shares. Exit remaining 25 at next regular-session executable bid after another daily close below $106, or at Oct 2 close. Maximum retained-share loss is the share value and may gap; hypothetical bid is indicative, not a confirmed broker fill. Future prices/exit quote missing.

## Execution

- Submitted DAY limit SELL 50 at $106.42, broker `a8242f71-57f3-4964-80c0-5219652b0a92`.
- Broker order status `filled`: 50/50 at $106.51, 2026-09-25T14:39:09.670531701Z. Exact order-specific FILL activity quantities 28+16+4+1+1=50, all $106.51. Follow-up broker account cash $49,491.38 and CCK position absent; no open CCK order.

## Reviewer updates

### Confirmed fill and comparison start — 2026-09-25

- Project alpaca_paper order a8242f71-57f3-4964-80c0-5219652b0a92 is filled 50/50 at $106.51 at 2026-09-25T14:39:09.670532Z; five order-specific FILL activities sum to 50 at that price. The comparison starts at this confirmed fill.
- At the 2026-09-28T16:37:43Z broker snapshot, CCK was absent from current positions and there were no open orders. No share re-entry is recorded.
- Status: ACTIVE. First common checkpoint remains 2026-09-28 close; evaluation end remains 2026-10-02 close.

## 2026-09-28 first close checkpoint

- The Alpaca IEX daily bar closed at `$107.50` (high `$108.24`, low `$106.93`), so the `$106` close-based exit rule did not trigger. The near-close IEX book was dislocated (for example `$101.42` bid x100 / `$114.36` ask x100 at `2026-09-28T19:59:43.738460218Z`, followed by still wider quotes); there is no reliable executable closing bid.
- The real 50-share sale remains fixed at `-$158` gross versus `$109.67` basis. HOLD_ALL is `UNSCORABLE` at this checkpoint; SELL_25_KEEP_25 has a known first-half hypothetical loss of `$79.50` at `$106.49`, but its remaining 25-share mark is `UNSCORABLE`. No closing P/L is inferred from the daily bar.
- Partial-quality checkpoint; no lesson change. Next checkpoint: `2026-10-02` close.

## October 2 terminal checkpoint and completed review

- Alpaca IEX daily bar closed `$106.02`, just above the `$106` daily-close exit trigger. The last coherent near-close IEX quote was `$106.09 x100` bid / `$106.19 x100` ask at `2026-10-02T19:59:15.642297Z`; later quotes became dislocated. The displayed bid covered all 50 retained shares; this is a partial-quality, single-venue mark 44 seconds before the bell.
- Gross P/L from the `$109.67` basis: real sale 50 at `$106.51` = `-$158`; HOLD_ALL at `$106.09` = `-$179`; SELL_25_KEEP_25 (25 at the original `$106.49` bid and 25 at `$106.09`) = `-$169`. No re-entry occurred. The real sale led by `$21` and `$11`, respectively.
- Assessment completed 2026-10-03; set status `COMPLETE`. The small differences are consistent with removing risk after a close-based breakdown, but one IEX-only case does not change the durable lessons.

### Decision-quality assessment

- Thesis / research: mixed — the breakdown and weak bounce supported de-risking, while the endpoint stayed close to the review level.
- Forecast: mixed — downside continued only modestly after the sale; this short comparison does not validate a broad bearish call.
- Instrument / strategy: worked — a full stock exit removed cyclical exposure without adding a new short thesis.
- Strike / expiration: not applicable — no option was selected.
- Timing: worked — the fill at `$106.51` preceded the alternative endpoint bid at `$106.09`.
- Sizing / risk: worked — the full sale removed the remaining 50-share exposure; the partial path retained some downside.
- Execution: worked — 50/50 shares filled at `$106.51`, confirmed by five order-specific FILL activities.
