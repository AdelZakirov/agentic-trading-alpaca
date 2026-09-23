# ARQT entry alternatives

## Identity

- decision_id: `alpaca-stage2-20260917-ARQT-buy`
- creator_run_id: `0f174d8e-9089-4bd4-8018-b349778a8ea2`
- decision_at: `2026-09-17T16:43:34+02:00`
- ticker: `ARQT`
- status: `WAITING_FOR_FILL`
- client_order_id: `alpaca-stage2-20260917-ARQT-buy`
- broker_order_id: `50df6ebd-cbbb-40c0-8ca9-a2c426026369`

## Original decision

- Thesis: rapid ZORYVE-led revenue growth, positive free cash flow, strong estimate revisions and high short interest support a 1-4 week rebound, but the September 16 gap should not be chased. A pullback to $24.50 offers a defined entry below the current ask.
- Chosen action: buy 200 shares with a $24.50 day limit; no options.
- Pre-trade exposure: zero ARQT shares and no ARQT order.
- Size rationale: $4,900 notional is about 4.8% of pre-trade equity; risk to a $22.40 daily-close invalidation is about $420 or 0.41% of equity before gap/slippage. Concurrent HOOD exit and MU trim keep aggregate long exposure near its prior level.
- Invalidation: daily close below $22.40 or material deterioration in ZORYVE prescription/formulary evidence.
- Holding period: 1-4 weeks; first target $27.50, second $30.00-$31.50; review by 2026-10-15.

## Evaluation rules

- Common start: confirmed real fill. If the day limit does not fill, retain status `NOT_SUBMITTED` for comparison and observe from the 2026-09-17 close.
- Checkpoints: next daily close after start, five trading days, ten trading days, and 2026-10-15 close.
- End rule: exit at the first target/review rule reached, otherwise mark at the final executable bid.
- Exit handling: daily close below $22.40 exits at next-session executable bid; at $27.50 compare trimming half versus holding; $30.00-$31.50 ends the study.

## Initial evidence

- Alpaca IEX quotes: $24.76/$25.17 at 2026-09-17T14:40:09Z; $24.80/$25.17 at 14:42:19Z; $24.65/$24.81 at 14:42:52Z. September 17 intraday low $24.505.
- moneyheap fundamental research saved at `memory/research/2026-09-17/163928-ARQT-fundamental.md`.
- Indicative 2026-10-16 calls: 22.5 strike $1.28/$4.93; 25 strike $0/$4.14; 27.5 strike $0.22/$1.23; 30 strike $0/$0.72. Option quotes are too wide or one-sided for an executable paper order.
- Missing data: consolidated SIP and firm OPRA quotes unavailable.

## Alternatives

### A. No trade
- question: Does avoiding the post-gap pullback outperform the selected entry?
- rationale: the stock may need more time to stabilize after its high-volume move.
- instrument: no trade; side: none; quantity: 0.
- entry rule / simulated price: none; zero capital and zero P/L.
- maximum loss: $0.
- exit handling: observe ARQT through the common window.
- pricing assumptions: none.

### B. Half-size pullback entry
- question: Does 100 shares offer better risk-adjusted performance than 200?
- rationale: reduce biotechnology gap risk while testing the same thesis.
- instrument: ARQT stock; side: buy; quantity: 100.
- entry rule / simulated price: $24.50 limit on 2026-09-17.
- maximum loss: about $210 to the $22.40 close invalidation, excluding gaps.
- exit handling: same targets and common rules.
- pricing assumptions: simulated fill only if observable price reaches $24.50.

### C. Breakout-confirmation entry
- question: Is paying up after confirmation superior to buying the pullback?
- rationale: require a daily close above $26.10 on above-average volume.
- instrument: ARQT stock; side: buy; quantity: 200.
- entry rule / simulated price: next-session ask after a qualifying close above $26.10.
- maximum loss: unknown until entry; invalidation would be the breakout pivot or $22.40, whichever current evidence supports.
- exit handling: common targets and end date.
- pricing assumptions: `UNSCORABLE` until the trigger and next-session quote exist.

### D. October bull call spread
- question: Can defined-risk options improve the payoff versus stock?
- rationale: cap loss while retaining upside toward $27.50-$30.
- instrument: one 2026-10-16 25/27.5 call spread; side: buy vertical; quantity: 1.
- entry rule / simulated price: conservative indicative debit uses long 25 ask $4.14 minus short 27.5 bid $0.22 = $3.92.
- maximum loss / payoff: the indicative debit exceeds the $2.50 spread width, so the snapshot is economically unusable.
- exit handling: expiry or 75% of maximum gain if a valid quote later exists.
- pricing assumptions: indicative feed only; zero bid and wide spreads make this alternative `UNSCORABLE`.

## Execution

- submitted_at: `2026-09-17T14:47:47.545450Z`
- broker_order_id: `50df6ebd-cbbb-40c0-8ca9-a2c426026369`
- status: `NEW`
- filled_qty: 0/200
- filled_avg_price: null

## Reviewer updates

### 2026-09-17 activation reconciliation

- Read-only reconciliation through the project `alpaca_paper` server confirmed broker order `50df6ebd-cbbb-40c0-8ca9-a2c426026369` is `filled`, `BUY 200/200` ARQT at average `$24.50`. The fills were recorded as 196 shares, 2 shares, and 2 shares at `$24.50`; the current broker position is 200 shares long.
- Reviewer status is now `ACTIVE`; the common evaluation start is the final confirmed fill at `2026-09-17T17:07:03.784769Z`, and the original alternatives and pricing rules remain unchanged. The account clock was still in the regular session at the review time, so no close mark is recorded. Next checkpoint: `2026-09-17` regular-market close.

## 2026-09-17 close checkpoint

- The September 17 Alpaca IEX 1Day bar closed at `$26.49` (high `$26.61`, low `$24.36`). Near-close IEX bids were dislocated at `$22.68` against asks from `$26.48` to `$29.57`, so the bar close is retained as a disclosed non-executable proxy.
- No `$22.40` daily-close invalidation or `$27.50` target touch occurred. Gross P/L from the `$24.50` entry: chosen 200-share path `+$398.00`; half-size 100-share path `+$199.00`; no trade `$0.00`. The breakout-confirmation alternative remains `UNSCORABLE`: the close exceeded `$26.10`, but the required above-average-volume confirmation and next-session executable ask are not yet established. The October call-spread alternative remains `UNSCORABLE` under its indicative, economically unusable quote.
- This is an interim, partial-quality checkpoint and supports no lesson change. Next checkpoint: 2026-09-24 regular-session close.

## 2026-09-22 real-path update

- Alpaca paper order `cf80b4ec-00d4-4bae-b3ee-15a2a4671906` and its four FILL activities confirm that 100 shares were sold at $27.95 on 2026-09-22, for $2,795 gross proceeds. The remaining broker position is 100 shares at the original $24.50 average entry, fully available.
- This records a real-path reduction for subsequent common-window accounting; it is not a new mark or a checkpoint. Include the sale proceeds when comparing retained shares with the original alternatives. Next scheduled checkpoint remains 2026-09-24 close.
