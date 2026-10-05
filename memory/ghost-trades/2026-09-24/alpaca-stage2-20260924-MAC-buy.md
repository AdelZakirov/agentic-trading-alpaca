# MAC pre-trade alternatives

## Identity

- decision_id: `alpaca-stage2-20260924-MAC-buy`
- creator_run_id: `733d7e3c-d69d-4b97-b5cf-9f43744a627b`
- decision_at: `2026-09-24T17:44:05+02:00`
- ticker: MAC
- status: `ACTIVE`
- client_order_id: `alpaca-stage2-20260924-MAC-buy`
- broker_order_id: 2e57b1fc-5371-4a51-a7e3-538b2c1c0d4c

## Original decision

BUY 200 MAC shares with a DAY limit no higher than $22.62. Sep 24 JPMorgan Neutral-to-Overweight/$26 upgrade, a $22–$23 trading base, improving reported leasing and FFO, and a 14.9% short float support a 1–4 week tactical long. Confidence moderate; analyst targets are context, not short-horizon forecasts. The balance sheet is leveraged, so no add without renewed evidence. Before entry the account has 11 long stocks, no MAC, no options or open orders, about $100,883 equity and $48,686 cash. At $22.62, notional $4,524 (4.5% of equity); a daily close below $21.50 triggers bounded exit review, about $224 below cost before gaps. A 10% overnight gap would cost about $452 (0.45% equity). Review by Sep 28, first profit review $24–$24.50, then $25.50–$26; final review Oct 22. No option order: shares have no theta or strike cap and keep the risk transparent.

## Evaluation rules

Common observation window starts only after a broker-confirmed real fill and ends Oct 22, 2026 or on an earlier thesis exit. Compare executable bid marks at next trading-day close, five trading days, and weekly thereafter. A daily close below $21.50 calls for next-session bounded sale in each filled scenario; $24–$24.50 and $25.50–$26 activate profit-review decisions, not automatic assumed fills. No-trade has zero P/L and capital at risk. If the real order never fills, this definition remains an unfilled decision; do not anchor hypothetical fills to an unobserved trade.

## Initial evidence

- Alpaca IEX MAC quote `2026-09-24T15:43:45.337605641Z`: bid $22.59 x 800, ask $22.60 x 300, 1-cent spread. This is a single-exchange current quote, not consolidated liquidity.
- Alpaca delayed SIP at `2026-09-24T15:23:50.975412854Z`: bid $22.56 x 400, ask $22.57 x 300. It is 15-minute delayed.
- Alpaca IEX daily bars through intraday Sep 24: Sep 23 $22.56–$22.85, close $22.68; Sep 24 low $22.48 and high $22.85 as observed before this decision.
- Stage 1 Sep 24 expert file and [moneyheap fundamental](../../research/2026-09-24/174145-MAC-fundamental.md); company [Q2 release](https://investing.macerich.com/news-releases/news-release-details/macerich-reports-second-quarter-2026-earnings-results). Moneyheap's precise upgrade date conflicts with Stage 1, so use Stage 1 event date and broker prices.

## Alternatives

1. **NO_TRADE** — Test whether new exposure improves P/L after an analyst upgrade without a breakout. Instrument: none; side/quantity/entry/exit: none; simulated capital and P/L $0; maximum loss $0; no pricing data needed.
2. **HALF_SIZE** — Test whether 100 cash shares preserve most upside with less downside. BUY 100 MAC at contemporaneous ask $22.60, simulated notional $2,260; review/exit at the same close-below-$21.50 rule and profit bands as the real action. Gap loss is uncapped; $110 is only the difference to the review level, not a guaranteed maximum loss. Simulated fill is an ask assumption, not a broker fill.
3. **WAIT_FOR_BREAKOUT** — Test whether paying for confirmation improves return. BUY 200 cash shares only after a daily close above Sep 23 high $22.85 and next-session positive executable quote; the future entry price is unknown and this alternative is `UNSCORABLE` until the trigger and contemporaneous ask are recorded by the reviewer. Same invalidation, targets, and Oct 22 end rule; gap loss is uncapped. No cash reservation.

## Execution

- Submitted order: null
- Confirmed fills: null

## Reviewer updates

Reserved for ghost reviewer after handoff.

## Trader execution addendum before handoff

- Alpaca broker order `2e57b1fc-5371-4a51-a7e3-538b2c1c0d4c` submitted 2026-09-24T15:45:21Z; DAY limit $22.62 for 200 shares.
- Broker status `filled` 200/200 at $22.60 at 2026-09-24T15:45:23.312243412Z. FILL activities: 127 shares at 15:45:22.263599Z and 73 shares at 15:45:23.312243Z, both $22.60. Alpaca position shows 200 shares at $22.60; no open MAC order.

### Reviewer activation and broker reconciliation — 2026-09-24

- Lifecycle state: `ACTIVE`. Project `alpaca_paper` order lookup confirms broker order `2e57b1fc-5371-4a51-a7e3-538b2c1c0d4c`, client ID `alpaca-stage2-20260924-MAC-buy`, filled 200/200 at $22.60. Order-specific FILL activities are 127 shares at 15:45:22.263599Z and 73 at 15:45:23.312243Z, both at $22.60. Current broker position is 200/200 available at $22.60 average.
- Common comparison starts with the first confirmed fill at `2026-09-24T15:45:22.263599Z`; later fill is included in the real path. The original no-trade, half-size and breakout alternatives remain unchanged. No post-fill checkpoint is due yet; first observation is Sep 24 close.

## 2026-09-24 close checkpoint

- Common observation: Alpaca IEX 1Day bar closed at $22.645. The final regular-session IEX quote at 2026-09-24T19:59:59.999091488Z was $22.64 bid x400 / $22.65 ask x200; it is a single-exchange mark.
- Real 200-share path at the confirmed $22.60 average is +$8.00 gross (+0.18%). HALF_SIZE, 100 shares at the original $22.60 ask assumption, is +$4.00. NO_TRADE is $0.00. WAIT_FOR_BREAKOUT remains unentered: the Sep 24 close did not exceed the Sep 23 high of $22.85, so no next-session entry quote is assigned.
- The $21.50 close invalidation and profit-review bands were not reached. No new lesson is supported. Next checkpoint: Sep 25 regular-session close.

## 2026-09-25 close checkpoint

- Common mark: Alpaca IEX quote at 2026-09-25T19:59:59.991257434Z was $22.65 bid x100 / $22.66 ask x200; the IEX daily bar closed at $22.66. The bid size covers only half the 200-share position on this single feed, so the comparison mark is partial.
- Real 200-share path from $22.60: +$10.00 gross at the bid; HALF_SIZE 100 shares: +$5.00; NO_TRADE: $0.00. WAIT_FOR_BREAKOUT remains unentered: the Sep 23 close was $22.68 and Sep 25 high $22.75, neither above the predeclared $22.85 trigger.
- No invalidation or profit-review band was reached. Interim result; no lesson change. Next checkpoint: 2026-10-01 close.

### 2026-10-01 close checkpoint

- Common observation: Alpaca paper IEX 1Day bar closed at `$22.56` (high `$22.645`, low `$22.035`). The near-close IEX quote at `2026-10-01T19:59:59.998710479Z` was `$22.55` bid x200 / `$22.57` ask x100; the bid size covers the real 200-share position. Single-exchange mark quality is partial.
- Gross P/L: real 200 shares from `$22.60` `-$10.00`; HALF_SIZE 100 shares `-$5.00`; NO_TRADE `$0.00`. WAIT_FOR_BREAKOUT remains unentered because the daily high stayed below `$22.85`; no entry price is assigned.
- The `$21.50` close invalidation and profit-review bands were not reached. No lesson change. Next checkpoint: October 8 close; final review remains October 22.
