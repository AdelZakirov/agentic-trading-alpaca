# Ghost pre-trade: ESI pullback long

## Identity

- decision_id: `alpaca-stage2-20260914-ESI-buy`
- creator_run_id: `f69753d6-76b4-4255-b370-bdb39af6070f`
- decision_at: `2026-09-14T12:31:31-04:00` (America/New_York)
- ticker: `ESI`
- status: `ACTIVE`
- client_order_id: `alpaca-stage2-20260914-ESI-buy`
- broker_order_id: null

## Original decision

ESI has a fresh Goldman Sachs Buy reinstatement at $44, strong reported growth and a 15.3x forward P/E, while the broker quote is $32.14 bid / $32.16 ask after a 20-day pullback. The trade is a tactical oversold rebound, not a long-term endorsement: leverage and the break below the 200-day average require a bounded entry and a daily-close invalidation. Buy 75 shares at the current ask to target a move back toward $34.50-$37.00 while keeping portfolio risk small and avoiding a second simultaneous electronics-distributor entry.

- chosen action: submit a day limit buy for 75 shares at $32.16
- pre-trade exposure: no ESI position or open ESI order
- size rationale: approximately $2,412 notional; about $132 risk to the $30.40 daily-close invalidation before slippage, with sector overlap to existing MU recognized
- invalidation: daily close below $30.40
- targets: $34.50 first, $36.00-$37.00 second, $42.00-$44.00 only after a new review
- holding period: 5-10 trading days, or earlier on invalidation or target review

## Evaluation rules

- common window: from confirmed fill through 10 trading days, or until the daily-close invalidation
- checkpoints: first regular-session close; daily close below $30.40; touch of $34.50; touch of $36.00-$37.00; end of the tenth trading day
- end rule: compare realized or marked P/L against alternatives using the same broker evidence; do not invent fills
- exit handling: no unplanned intraday stop; preserve the daily-close time basis unless a new material thesis change is documented

## Initial evidence

- Alpaca clock: market open, `2026-09-14T12:31:31-04:00`
- Alpaca account: equity $101,528.46; cash $87,183.93; buying power $369,272.39
- ESI position/order check: no position and no open order
- delayed-SIP quote: bid $32.14, ask $32.16, bid size 200, ask size 100, quote time `2026-09-14T16:16:39.757625747Z`
- research: `memory/research/2026-09-14/182522-ESI-fundamental.md`
- local evidence: 2026-09-11 technical bar; 20-day return -11.97%, relative volume 1.49x; expert source recorded Goldman Buy / $44 on Sep. 11
- missing data: no ESI option structure was selected; stock liquidity and defined daily-close risk were the chosen instrument basis

## Alternatives

### A — Chosen 75-share stock entry

- label: `chosen-75-share-stock`
- question tested: does a bounded stock entry capture the oversold rebound without taking option premium/decay risk?
- instrument: ESI stock, buy 75 shares
- entry rule: day limit at $32.16 or better
- simulated entry price: $32.16 ask
- maximum loss: approximately $132 to the $30.40 invalidation before slippage; no hard broker stop submitted
- exit / handling: daily-close invalidation and target checkpoints above
- pricing assumptions: ask-side hypothetical; only broker `filled` status establishes execution

### B — Smaller stock entry

- label: `smaller-40-share-stock`
- question tested: does reducing size improve downside control while preserving the same thesis?
- instrument: ESI stock, buy 40 shares
- entry rule: same $32.16-or-better limit
- simulated entry price: $32.16 ask
- maximum loss: approximately $70 to the invalidation before slippage
- exit / handling: same daily-close rules and targets
- pricing assumptions: ask-side hypothetical; no invented fill

### C — Correlated AVT alternative

- label: `watch-AVT-entry`
- question tested: is the stronger value/revision setup in AVT preferable to ESI's oversold reversal?
- instrument: AVT stock, buy 20 shares only in the researched $93.00-$94.50 range
- entry rule: conditional entry after stabilization; no ESI capital reserved
- simulated entry price: $94.15 ask observed in the same session
- maximum loss: approximately $105 to the $88.90 invalidation before slippage
- exit / handling: 5-10 trading-day review; no order submitted
- pricing assumptions: ask-side hypothetical; status `NOT_SUBMITTED`

### D — No trade

- label: `no-trade`
- question tested: does leverage and the break below longer moving averages outweigh the analyst catalyst?
- instrument: no trade; retain cash
- entry rule: no order and zero new capital at risk
- simulated entry price: null
- maximum loss: zero incremental loss
- exit / handling: reconsider only on a daily close back above the moving-average band or a new catalyst
- pricing assumptions: starts at zero P/L and zero capital at risk

## Execution

- confirmed fill: null
- broker_order_id: `3b2caccb-8451-473f-ab70-f955bbccd657`
- broker status: `new` (unfilled at final reconciliation)
- submitted_at: `2026-09-14T16:32:36.090440174Z`
- final observed quote: $32.14 bid / $32.17 ask at `2026-09-14T16:18:15.530814993Z`; limit remained $32.16

## Reviewer updates

### First close checkpoint — 2026-09-14

- Reviewer status: `ACTIVE`; confirmed evaluation start is the actual fill at `2026-09-14T17:14:02.809764Z`; common end remains the close of the tenth trading session, `2026-09-25T20:00:00Z`, unless the original invalidation or target rule ends it earlier.
- Broker reconciliation: `get_account_activities` recorded four fills totaling 75 shares at `$32.16`, and `get_order_by_id` confirmed order `3b2caccb-8451-473f-ab70-f955bbccd657` status `filled`, `filled_qty=75`, and `filled_avg_price=$32.16`. The broker position is 75 shares long. No fill was inferred from order status alone.
- Common observation: first regular-session close, delayed-SIP quote at `2026-09-14T20:00:00.013130007Z`; bid `$32.12`, ask `$32.13`, displayed sizes 100/16,700. The post-fill IEX 1-minute series reached a high of `$32.33` and a low of `$31.89`; no `$34.50` target touch and no daily-close breach below `$30.40` occurred.
- Normalized gross P/L from the `$32.16` entry, before fees, using the conservative close bid: chosen real 75-share path `-$3.00`; smaller 40-share path `-$1.60`; no trade `$0.00`.
- AVT remains `UNSCORABLE`, not a win or loss: IEX bars show price in the `$93.00-$94.50` range, but the original alternative required entry after stabilization and was explicitly `NOT_SUBMITTED`; no objective activation or executable alternative fill was recorded.
- Conclusion so far: the bounded stock entry was nearly flat but trailed no trade and the smaller size at the first close; the evidence is too early to judge the rebound thesis or update a durable lesson. No lesson change.
- Next checkpoint: first later daily close, or immediately if the original `$30.40` daily-close invalidation or `$34.50` target-touch rule activates.

## 2026-09-15 close checkpoint

- The earlier submission snapshot said `new`/unfilled, but the later individual broker read confirms the order filled all 75 shares at `$32.16` on September 14 and the current ESI position is 75 shares long; no fill is inferred from the stale snapshot alone.
- The September 15 IEX 1Day bar closed at `$31.79`, with a `$32.695` high and `$31.435` low. The near-close IEX quote at `2026-09-15T19:59:55.952214082Z` was `$31.65` bid / `$32.06` ask. No daily close below `$30.40` or `$34.50` target touch occurred.
- Gross P/L: chosen 75-share path `-$38.25`; smaller 40-share path `-$20.40`; no trade `$0.00`. The conditional AVT alternative remains unentered and `UNSCORABLE`: no objective stabilization trigger and executable fill were recorded. This is an interim checkpoint with no lesson change. Next checkpoint: 2026-09-16 regular-session close, or earlier on an original trigger.

## 2026-09-16 close checkpoint

- The September 16 Alpaca IEX 1Day bar closed at `$32.11` (high `$33.07`, low `$31.76`); the last IEX quote was `$30.79` bid / `$32.28` ask at `2026-09-16T19:59:56.895803504Z`. The unusually wide quote is retained as a data-quality caveat and the bid is used as the conservative mark.
- No daily close below `$30.40` or `$34.50` target touch occurred. Gross P/L from the `$32.16` entry: chosen 75-share path `-$102.75`; smaller 40-share path `-$54.80`; no trade `$0.00`. The conditional AVT alternative remains unentered and `UNSCORABLE`; no objective stabilization-and-entry trigger was recorded.
- This is an interim checkpoint and supports no lesson change. Next checkpoint: 2026-09-17 regular-session close.

## 2026-09-17 close checkpoint

- The September 17 Alpaca IEX 1Day bar closed at `$33.15` (high `$33.18`, low `$32.54`). The near-close IEX quote at `2026-09-17T19:59:59.688630Z` was `$33.14` bid / `$33.26` ask and is usable for a conservative stock mark.
- No daily close below `$30.40` or `$34.50` target touch occurred. Gross P/L from the `$32.16` entry: chosen 75-share path `+$73.50`; smaller 40-share path `+$39.20`; no trade `$0.00`. The conditional AVT alternative remains unentered and `UNSCORABLE`; no objective stabilization-and-entry trigger was recorded.
- This remains an interim checkpoint and supports no lesson change. Next checkpoint: 2026-09-18 regular-session close.

## 2026-09-18 close checkpoint

- Read-only broker reconciliation confirms the 75-share entry filled at `$32.16`; 75 shares remain fully available. The September 18 IEX 1Day bar closed at `$32.73` (high `$33.535`, low `$32.535`). Near-close quotes were mostly around `$32.78/$32.80` before ending dislocated at `$31.53/$33.12`; the daily bar is retained as a disclosed non-executable proxy.
- Gross P/L from the `$32.16` entry: chosen 75-share path `+$42.75`; smaller 40-share path `+$22.80`; no trade `+$0.00`. The conditional AVT alternative remains `UNSCORABLE`: no objective stabilization-and-entry trigger or executable fill was recorded.
- No daily close below `$30.40` or `$34.50` target touch occurred. This interim checkpoint supports no lesson change. Next checkpoint: 2026-09-22 regular-session close.

## 2026-09-22 real-path update

- Alpaca paper order `608ca399-3331-471a-94c5-e3a520ca36d3` and its order-specific FILL activity confirm that 35 shares were sold at $35.17 on 2026-09-22, for $1,230.95 gross proceeds. The remaining broker position is 40 shares at the original $32.16 average entry, fully available.
- This records a real-path reduction for subsequent common-window accounting; it is not a new mark or a checkpoint. Include the proceeds alongside the remaining 40 shares in comparisons. The scheduled 2026-09-22 close checkpoint remains due.

## 2026-09-22 close checkpoint

- The IEX 1Day bar closed at `$35.18` (high `$35.36`, low `$33.52`). The stable near-close quote at `2026-09-22T19:59:56.115642253Z` was `$35.18` bid x100 / `$35.31` ask x100, sufficient for the remaining 40 shares and the 75-share comparison.
- Including actual proceeds from selling 35 at `$35.17`, the chosen 75-share path is `+$226.15`; holding all 75 to the bid would be `+$226.50`; the smaller 40-share entry would be `+$120.80`; no trade `$0`. The `$34.50` review level was exceeded; the `$30.40` daily-close invalidation did not occur. The conditional AVT comparison remains unentered/unscorable.
- Interim result, partial overall quality due to the AVT alternative, and no lesson change. Next checkpoint: final `2026-09-25` close.
