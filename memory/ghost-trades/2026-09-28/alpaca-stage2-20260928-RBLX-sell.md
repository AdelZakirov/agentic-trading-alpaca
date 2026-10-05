# RBLX close-basis exit alternatives

## Identity
- decision_id: alpaca-stage2-20260928-RBLX-sell
- creator_run_id: 3392dda4-ef42-486f-a2a1-e172b49ed51a
- decision_at: 2026-09-28T16:59:59.830945+02:00
- ticker: RBLX
- status: COMPLETE
- client_order_id: alpaca-stage2-20260928-RBLX-sell
- broker_order_id: 11ef0ea5-56f0-427e-9a79-d120c5f58394

## Original decision
SELL all 50 owned shares, ordinary DAY limit, no new option. Friday Sep25 IEX completed close $46.46 broke the predeclared $46.80 daily-close review. Today's ~$42.8 also lies below $44.50 structural failure. Exit is an application of the original close-based plan, not a newly invented intraday stop. Fresh moneyheap technical research confirms corrective momentum/50-day average test and $39.20-$40 downside. No renewed long edge justifies the failed runner. Confidence high in the risk-reducing decision; news attribution remains uncertain. Cost basis $40.41; sell only owned/available 50. Maximum slippage allowance $0.10 below the final executable bid, with a replacement floor no lower than $42.60; do not chase below it. Review any unfilled DAY order at pre-close.

## Evaluation rules
Common comparison begins only at broker-confirmed real first fill; reviewer reconciles all partial fills. Compare incremental economics of the original 50-share exposure using actual weighted real exit as the baseline. Prior realized returns/cost basis are context, not new comparison P/L. Check decision-day close and next trading closes through Oct2, ending earlier at each predeclared alternative exit. No reopening after an alternative exits. The original runner invalidation is already breached; retained-share variants below are explicitly separate rescue/timing scenarios, not extensions of the invalidated original trade.

## Initial evidence
Alpaca IEX quote sequence: 14:55:00Z bid42.58/ask42.72 (100x100); 14:56:50.473926779Z bid42.83/ask43.44 (100x100); 14:57:47.819766115Z bid42.79/ask42.82 (100x100); 14:58:40.063821133Z bid42.83/ask42.84 (100x100). The single wide observation was not cherry-picked; later fresh books tightened. Final preflight quote to be attached before submission. Friday broker IEX completed close46.46, current broker lastday46.44. Research: memory/research/2026-09-28/165532-RBLX-technical.md. Option quotes are not needed for these stock-only alternatives; none fabricated.

## Alternatives
1. PARTIAL25_RESCUE25 — test retaining a small rebound claim rather than full exit. Hypothetical SELL25 at contemporaneous bid42.83; retain25 of the existing shares, no new purchase, mark carry at the common fill anchor. NEW rescue rule: next-session bounded exit after a completed close below41.80; executable bid46.00 triggers full remaining exit; terminal exit at Oct2 15:45ET if neither fires. Original46.80 rule is already resolved by the real exit and is not rewritten. Maximum capital loss on retained25 is 25 times the common starting price; stop is not guaranteed. Pricing: sell executable bid at rule observation; quote gaps may make UNSCORABLE. Rationale: oversold bounce possible, but half exposure limits further decline.
2. DELAY_TODAY_BOUNCE — test better exit timing without overnight carry. Keep50 only until executable bid44.50 is observed, then hypothetically SELL50 at that bid; otherwise sell at first available valid bid at/after today's15:45ET. Intraday bid below41.80 triggers earlier full sale at valid bid. Quote sampling is discrete; do not invent an unseen touch or price. Maximum capital risk is the full retained share value until exit; exposure ends today. Simulated immediate anchor quote42.83 is evidence only, not a fabricated future fill. Rationale: a rebound could improve exit economics, but adds same-day downside.

## Execution
Broker order and fills: null. No assumed fill or comparison activation.

## Reviewer updates

### 2026-09-28 independent broker reconciliation
- Alpaca paper order `11ef0ea5-56f0-427e-9a79-d120c5f58394` is `filled`, 50/50 at `$42.76`. Order-specific FILL activities are 13 shares at `15:01:22.388804Z` and 37 at `15:01:23.256261Z`, both `$42.76`; common comparison starts at the first confirmed fill, `2026-09-28T15:01:22.388804Z`.
- Current positions show no RBLX shares; open orders are zero. Gross realized gain against the recorded `$40.41` cost is `$117.50` before fees. No hypothetical alternative is treated as an actual fill.
- The paper clock is open at `2026-09-28T13:24:14.986101-04:00`; the Sep 28 close mark is still pending. Next checkpoint: Sep 29 close.

## Final pre-submission quote
Alpaca IEX 2026-09-28T15:00:03.265949457Z bid42.66/ask42.70,100x100. The extra quotes span 3m13s from the wide quote and both tightened. Selected SELL50 DAY limit42.60, six cents below current bid; no replacement below42.60.

## Confirmed execution before handoff
Broker order11ef0ea5-56f0-427e-9a79-d120c5f58394 FILLED50@$42.76 at2026-09-28T15:01:23.256261249Z. Exact FILL activity quantities13+37, both42.76. Cash59939.38→62077.38 equals2138.00proceeds; broker position absent and zero open orders. Gross realized P/L117.50 before fees. File remains reviewer WAITING_FOR_FILL until independent activation.

## 2026-09-28 close checkpoint

- The IEX daily bar closed at `$41.88` (high `$44.475`, low `$41.86`). DELAY_TODAY_BOUNCE did not see its `$44.50` bid target or intraday `$41.80` review trigger; under its original timing rule, the first valid bid at/after 15:45 ET was `$42.40` x100 / `$42.42` ask x100 at `2026-09-28T19:45:04.941633984Z`. Gross P/L for 50 shares versus `$40.41` basis is `+$99.50`; the real 50-share path remains `+$117.50`.
- PARTIAL25_RESCUE25 marked its retained 25 at the late IEX bid `$40.58` x100 / `$41.89` ask x100 at `2026-09-28T19:59:56.204189087Z` (wide 3.2% spread). Its incremental result versus the real `$42.76` sale anchor is `-$52.75` (25 sold at `$42.83`: `+$1.75`; 25 marked at `$40.58`: `-$54.50`). The prior-cost-basis gross figure `+$64.75` is context, not comparison P/L. Treat this as a partial-quality mark. The daily close stayed above `$41.80`, and the high stayed below `$46.00`; no rescue exit fired.
- Partial-quality checkpoint; no lesson change. Next checkpoint: `2026-09-29` close.

## 2026-09-29 close checkpoint

- The IEX daily bar closed at `$41.175` (high `$42.25`, low `$40.78`). The last tight near-close IEX book was `$41.18` bid x600 / `$41.19` ask x500 at `2026-09-29T19:59:54.054607050Z`; later quotes degraded, so retain a single-exchange/near-close caveat.
- The close below the rescue path's `$41.80` threshold triggers its predeclared next-session exit. `PARTIAL25_RESCUE25` is not marked as finally exited yet; at the close its incremental result versus the actual `$42.76` sale anchor is `-$37.75` (25 at `$42.83`, 25 marked at `$41.18`). `DELAY_TODAY_BOUNCE` remains frozen at its September 28 `$42.40` exit, `-$18.00` versus the real sale; the real path is `$0` on this comparison anchor. Cost-basis profit is historical context only.
- This is a partial-quality interim checkpoint. Next observation: September 30 first valid regular-session bid for the triggered rescue exit; do not reopen the path.

## 2026-09-30 completion review

- Broker reconciliation: order `11ef0ea5-56f0-427e-9a79-d120c5f58394` remains filled 50/50 at `$42.76`; order-specific FILL activities remain 13 + 37 shares at `$42.76`. No RBLX position or open RBLX order remains. The hypothetical paths did not submit orders.
- The September 29 close at `$41.175` was below the rescue path's predeclared `$41.80` threshold. The first regular-session IEX quote on September 30 was `2026-09-30T13:30:00.016506255Z`, bid `$38.96` x100 / ask `$43.47` x100 (11.58% spread; regular-session condition). Its displayed bid covered the hypothetical 25-share exit, so the path exits at the first bid as specified. Data quality is partial: the opening book was sharply dislocated, and a tighter quote appeared 1.113 seconds later at `$41.01` / `$41.28`. Keep the first quote under the original rule; do not substitute the later higher bid.
- Incremental gross economics versus selling all 50 shares at the actual `$42.76` fill: real path `$0` baseline; `DELAY_TODAY_BOUNCE` sold 50 at `$42.40`, `-$18.00`; `PARTIAL25_RESCUE25` sold 25 at `$42.83` and the remaining 25 at `$38.96`, `-$93.25` (`+$1.75` on the first 25 and `-$95.00` on the retained 25). In prior-cost-basis context, gross gains were `$117.50` real, `$99.50` delayed, and `$24.25` rescue, before fees.
- Decision review: thesis/research and forecast were mixed because the close-based breakdown was clear but news attribution and rebound odds remained uncertain. Full stock exit and timing worked against both stated alternatives; the partial-retention path carried downside through the triggered close. Sizing/risk worked by removing overnight exposure. Real execution was confirmed at `$42.76`; the hypothetical opening exit is only partial-quality because the IEX spread was dislocated. Strike/expiration selection is not applicable to this stock-only comparison.
- Supported conclusion: the real full exit beat the same-day delay by `$18.00` and the partial rescue by `$93.25` on the original 50-share comparison. Treat the rescue mark as partial-quality and ticker-specific. No durable lesson change: this single comparison and unstable opening quote do not establish a general rule beyond the existing invalidation and path-freeze lessons.
- Assessment complete; move this routing row to `archive-index.md`.
