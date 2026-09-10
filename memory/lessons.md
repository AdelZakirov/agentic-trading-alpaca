# Lessons learned

Operational and performance evidence are now tracked; weekly reports document coverage, data gaps, and calibrated confidence.

## Keep order execution bounded and idempotent

- Status: active
- Pattern / conditions: An order is unfilled or its status is uncertain.
- Lesson: Use a unique client ID and capped limit. Refresh once before at most one replacement, reconcile the terminal broker state, and never duplicate an uncertain order.
- Evidence count: 14 completed logical orders.
- Supporting cases: [`2026-09-01`](logs/2026-09-01.md), [`2026-09-02`](logs/2026-09-02.md) — 14 logical orders filled; two bounded option replacements; no failures or duplicates.
- Contradicting cases: None yet.
- Confidence: high
- Last updated: 2026-09-04

## Reconcile time-sensitive inputs before committing capital

- Status: active
- Pattern / conditions: A thesis depends on a current price, event, supply change, or short-lived catalyst.
- Lesson: Reconcile research price/time with the broker and verify exact event timing before adding risk. If unresolved, skip or size for the uncertainty.
- Evidence count: 3 independently reviewed decisions.
- Supporting cases: [`PCG`](positions/PCG.md) — stale price; [`MMED`](positions/MMED.md) — lock-up date found after entry; [`2026-09-03 audit`](logs/2026-09-03.md) — stale research blocked orders.
- Contradicting cases: None yet.
- Confidence: medium
- Last updated: 2026-09-04

## Match option payoff and overlap to the thesis

- Status: active
- Pattern / conditions: Selecting options or adding them beside stock in the same underlying.
- Lesson: Map payoff at invalidation and targets, and aggregate stock-plus-option exposure. Avoid a short strike below the main target or an overlapping option without a distinct edge.
- Evidence count: 2 completed option-entry decisions.
- Supporting cases: [`MSTR`](positions/MSTR.md) — $135 cap below $137.50-$150 targets; [`SLB`](positions/SLB.md) — spread duplicated the stock thesis.
- Contradicting cases: None yet; performance comparisons are pending.
- Confidence: medium
- Last updated: 2026-09-04

## Define exactly what activates a target

- Status: active
- Pattern / conditions: A tactical target may be reached between management runs.
- Lesson: Before entry, define whether an executable touch, sustained trade, or close activates a specific reduction. If it cannot be monitored, use an alert or bounded exit when warranted.
- Evidence count: 1 completed target-handling event.
- Supporting cases: [`RBLX`](positions/RBLX.md) — target touched, no reduction, then retraced.
- Contradicting cases: [`HOOD`](positions/HOOD.md), [`MSTR`](positions/MSTR.md) — observed targets produced partial reductions.
- Confidence: low
- Last updated: 2026-09-04

## Preserve the stated time basis of invalidation

- Status: active
- Pattern / conditions: A trade plan defines an invalidation using a daily close or another explicit confirmation window.
- Lesson: Do not silently convert that condition into an intraday exit. If new evidence warrants earlier de-risking, record the thesis change and compare it explicitly with the original time-based rule.
- Evidence count: 1 completed decision episode.
- Supporting cases: [`PCG entry`](ghost-trades/2026-08-31/alpaca-stage2-20260831-PCG-buy.md) and [`PCG exit`](ghost-trades/2026-09-01/alpaca-stage2-20260901-PCG-sell.md) — an intraday exit preceded a documented close/reclaim recovery.
- Contradicting cases: None yet.
- Confidence: low
- Last updated: 2026-09-08

## Reconcile expiring protection at the close

- Status: active
- Pattern / conditions: A late-session fill relies on day-only bracket exits but the holding plan does not authorize carry exposure overnight.
- Lesson: Before the close, either exit, deliberately approve overnight retention with fresh risk levels, or replace expiring protection with an eligible persistent order. Never assume day legs remain active.
- Evidence count: 1 completed decision set.
- Supporting cases: [`SMMT pullback`](ghost-trades/2026-09-04/alpaca-stage2-20260904-SMMT-buy.md) — profitable entry, but both day exit legs expired/canceled and left unintended overnight exposure.
- Contradicting cases: None yet.
- Confidence: low
- Last updated: 2026-09-08
