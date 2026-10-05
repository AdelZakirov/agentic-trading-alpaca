# RBLX close-basis exit alternatives

## Identity
- decision_id: alpaca-stage2-20260928-RBLX-sell
- creator_run_id: 3392dda4-ef42-486f-a2a1-e172b49ed51a
- decision_at: 2026-09-28T16:59:59.830945+02:00
- ticker: RBLX
- status: WAITING_FOR_FILL
- client_order_id: alpaca-stage2-20260928-RBLX-sell
- broker_order_id: null

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

## Final pre-submission quote
Alpaca IEX 2026-09-28T15:00:03.265949457Z bid42.66/ask42.70,100x100. The extra quotes span 3m13s from the wide quote and both tightened. Selected SELL50 DAY limit42.60, six cents below current bid; no replacement below42.60.

## Confirmed execution before handoff
Broker order11ef0ea5-56f0-427e-9a79-d120c5f58394 FILLED50@$42.76 at2026-09-28T15:01:23.256261249Z. Exact FILL activity quantities13+37, both42.76. Cash59939.38→62077.38 equals2138.00proceeds; broker position absent and zero open orders. Gross realized P/L117.50 before fees. File remains reviewer WAITING_FOR_FILL until independent activation.
