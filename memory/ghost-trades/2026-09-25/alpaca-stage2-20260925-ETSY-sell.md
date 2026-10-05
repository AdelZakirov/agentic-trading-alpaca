# ETSY exit decision — original definitions

## Identity

- decision_id: `alpaca-stage2-20260925-ETSY-sell`
- creator_run_id: `a2d14c54-69dc-496d-8d5e-c0ec996c75bd`
- decision_at: `2026-09-25T16:35:13+02:00`
- ticker: ETSY
- Status: COMPLETE
- client_order_id: `alpaca-stage2-20260925-ETSY-sell`
- broker_order_id: `dafc8a72-300e-4962-98be-8315f1bace27`

## Original decision

Long 75 ETSY at broker average $72.71, with no open order. Sep 24 broker last-day close $68.98 crossed the predeclared $69.20 daily-close invalidation; the Arete Buy-to-Neutral downgrade weakens the original analyst-supported reversal thesis. Sep 25 rebound to about $70.33 does not by itself renew the 1–4 week thesis. Chosen action: sell all 75 by regular-session DAY limit, initially $70.20 or better, to remove about $5.3k of consumer/high-beta exposure. This is a risk-reducing exit, not a short. No new ETSY options; their IV, theta and bearish directional risk do not repair the expired stock thesis. Re-entry requires a new current catalyst and sustained reclaim above the broken area, separately researched.

## Evaluation rules

Common comparison starts only after the real sale is broker-confirmed filled. Observe at Sep 28 and Oct 2 regular-session closes, ending Oct 2 close or earlier on a verified corporate event that renders the original comparison inapplicable. Mark shares at broker-reported prices; alternatives that retain shares follow their rules below and may gap through any review level. Do not infer or fabricate fills. If the real order does not fill, leave fill-anchored comparisons inactive. No re-entry for the real sale during the comparison window.

## Initial evidence

- Alpaca paper Sep 25 10:34:52 ET: market open, 75 shares available, lastday_price $68.98, current_price $70.33, no open orders.
- Alpaca IEX Sep 25 10:34:38 ET: bid $70.29 x200, ask $70.53 x100. IEX is a single exchange; a limit protects the execution floor. Intended initial sale limit $70.20, $0.09 below displayed bid as a bounded allowance, not an assumed fill.
- Quote validation before submission: IEX Sep 25 10:36:48 $67.49/$70.92 briefly widened; 10:37:14 $69.41/$70.64; 10:37:52 $70.55/$70.92; 10:39:38 $70.51/$70.92; 10:39:50 $67.49/$70.92; 10:40:45 $67.50/$70.92. All displayed bids/asks had positive sizes, but IEX was dislocated and the bid unreliable. Delayed SIP at 10:25:34 ET was $70.06/$70.08, too stale for a current fill assumption. Broker mark at 10:40 was $70.58. A $70.20 sale limit bounded downside slippage; no market order was used.
- Historical Sep 24 composite close $68.98 and Arete downgrade corroborated by public price/news sources; exact URLs in the Sep 25 trading log. [Current moneyheap technical](../../research/2026-09-25/163550-ETSY-technical.md) finds a downtrend, heavy-volume Sep 24 breakdown and a weak bounce; the user's explicit authorization allowed the local service request after an initial approval rejection.

## Alternatives

1. `HOLD_ALL`: Test whether the Sep 25 rebound quickly repairs the breakdown. No trade now; retain 75 shares, zero incremental cash, and roughly $5,274.75 current exposure. If another daily close is below $69.20, sell at next regular-session executable bid; otherwise mark through Oct 2 close. Entry price is the real sale's confirmed execution benchmark, not today's guessed fill. Maximum loss is share value subject to gaps; no guaranteed stop. Missing data: future closing and exit quotes.
2. `SELL_40_KEEP_35`: Test a partial de-risk. Hypothetical sell 40 shares at contemporaneous IEX bid $70.29, about $2,811.60 proceeds, and retain 35 shares, about $2,460 of market exposure. On another daily close below $69.20, sell remaining 35 at next regular-session executable bid; otherwise mark them through Oct 2 close. The partial-sale assumption is an indicative single-exchange bid, not a broker fill. Maximum retained-share loss is the invested share value; gaps remain possible. Missing data: future closing and exit quotes.

## Execution

- Submitted DAY limit SELL 75 at $70.20, broker `dafc8a72-300e-4962-98be-8315f1bace27`.
- Broker order status `filled`: 75/75 at $70.62, 2026-09-25T14:41:05.290196642Z. Exact order-specific FILL activity quantities 13+62=75, both $70.62. Follow-up paper cash $54,787.88 and ETSY position absent; no open ETSY order.

## Reviewer updates

### Confirmed fill and comparison start — 2026-09-25

- Project alpaca_paper order dafc8a72-300e-4962-98be-8315f1bace27 is filled 75/75 at $70.62 at 2026-09-25T14:41:05.290197Z; two order-specific FILL activities sum to 75 at that price. The comparison starts at this confirmed fill.
- At the 2026-09-28T16:37:43Z broker snapshot, ETSY was absent from current positions and there were no open orders. No share re-entry is recorded.
- Status: ACTIVE. First common checkpoint remains 2026-09-28 close; evaluation end remains 2026-10-02 close.

## 2026-09-28 close invalidation and next-session exits — 2026-09-29

- The Alpaca IEX daily bar closed at `$68.95` (high `$69.46`, low `$66.26`), below the predeclared `$69.20` close review. At the Sep 29 open, the first reasonable IEX book after the dislocated opening quotes was `$68.84` bid x100 / `$69.45` ask x100 at `2026-09-29T13:30:41.479459391Z`; later quotes kept the bid near `$68.85`. The displayed bid covers 75 shares, though this remains an IEX-only simulated exit.
- Gross P/L versus `$72.71` basis: real sale 75 at `$70.62`, `-$156.75`; HOLD_ALL 75 exited at `$68.84`, `-$290.25`; SELL_40_KEEP_35, 40 at the original `$70.29` bid and 35 at `$68.84`, `-$232.25`. The actual exit led HOLD_ALL by `$133.50` and the partial exit by `$75.50`. No re-entry is assumed.
- Both retained-share alternatives exited under their original close-based rule. The declared comparison horizon remains `2026-10-02` close; their P/L is frozen after the Sep 29 exits. Partial-quality checkpoint; no lesson change. Next checkpoint: `2026-10-02` close.

## October 2 terminal checkpoint and completed review

- The original paths were already frozen after their declared September 29 exits; no re-entry is assumed. The October 2 IEX daily bar closed `$72.73`, and the last tight near-close IEX book was `$72.66 x100` bid / `$72.77 x100` ask at `2026-10-02T19:59:50.483097Z`. The market's rebound does not rewrite the original exit rules.
- Gross P/L from the `$72.71` basis remains: real sale 75 at `$70.62` = `-$156.75`; HOLD_ALL exited 75 at `$68.84` = `-$290.25`; SELL_40_KEEP_35 = `-$232.25`. The actual exit led by `$133.50` and `$75.50`; these simulated next-session marks are IEX-only.
- Assessment completed 2026-10-03; set status `COMPLETE`. The result supports the actual exit under the stated event and breakdown evidence, while the October 2 recovery shows the forgone upside of the frozen no-re-entry paths.

### Decision-quality assessment

- Thesis / research: worked — the downgrade and heavy-volume breakdown weakened the original reversal case.
- Forecast: mixed — the next-session weakness validated the exit, but price recovered by the terminal date after paths were frozen.
- Instrument / strategy: worked — the stock exit reduced risk without adding a bearish derivative thesis.
- Strike / expiration: not applicable — no option was selected.
- Timing: worked — the actual fill at `$70.62` exceeded the alternatives' predeclared later exit at `$68.84`.
- Sizing / risk: worked — full exit removed the position; the partial-retention path still lost more.
- Execution: worked — 75/75 shares filled at `$70.62`, confirmed by two order-specific FILL activities.
