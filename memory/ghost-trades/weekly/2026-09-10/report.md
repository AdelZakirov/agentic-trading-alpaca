# Weekly ghost-trade lessons review — 2026-09-10

## Scope and coverage

- Reviewer-only run. No broker mutations, discovery, moneyheap calls, trading-log edits, ticker-file edits, or portfolio-state edits.
- Ghost queue status before review: no active, pending, or claimed packet; no reviewer overlap detected.
- Reviewed 6 legacy completed ghost sets from the input snapshot [`reviews-input.json`](reviews-input.json).
- Coverage: 6/6 sets reviewed; 0 `awaiting_backfill`; 4 independent decisions after grouping dependent sets:
  - GAP entry: `alpaca-stage2-20260831-GAP-buy`
  - PCG capitulation entry and exit: `alpaca-stage2-20260831-PCG-capitulation` (2 ghost sets, 1 decision)
  - SLB breakout-pullback stock entry and option add: `decision-20260901-SLB-breakout-pullback` (2 ghost sets, 1 decision)
  - SMMT pullback entry: `decision-20260904-SMMT-pullback-entry`
- Record quality: 1 fully scorable set and 5 partial sets. Five alternative paths lacked synchronized executable endpoint marks; they remain unscorable rather than being converted from last-trade proxies.

## Verified patterns

- Existing invalidation-time-basis lesson: supported by the dependent PCG entry/exit pair (`alpaca-stage2-20260831-PCG-buy`, `alpaca-stage2-20260901-PCG-sell`). The full exit realized -$165, while retention through the documented reclaim produced +$562.50 relative to the decision reference. This is one low-confidence independent case, not two.
- Existing option payoff/overlap lesson: supported by the single SLB decision set (`alpaca-stage2-20260901-SLB-buy`, `alpaca-stage2-20260901-SLB-option-buy`). The short-dated debit spread lost $79; no incremental option add was best and the small stock add lost less. The unscorable long-call path does not add evidence.
- Existing close-reconciliation lesson: supported by `alpaca-stage2-20260904-SMMT-buy`. The pullback entry gained $270 and beat confirmation/no-trade, but day-only protection expired and left unintended overnight exposure.
- GAP selection evidence: `alpaca-stage2-20260831-GAP-buy` finished -$28 while PYPL gained $147.60; this is a single selected-case observation and does not support a general ranking or timing rule.

## Lesson changes

- No new lesson created, retired, merged, or strengthened.
- Existing lesson evidence counts and confidence levels were preserved because PCG and SLB records are dependent within their decision episodes, and several option outcomes are formally unscorable.
- Updated the lessons header meta-note to reflect that reviewed performance evidence is now tracked; the actionable lesson set is unchanged.

## Limits and next evidence

- The sample is selected from trades that were actually taken or explicitly compared, not an unbiased market sample; outcomes mix intraday and multi-session windows, stocks and options, and different exit rules.
- Catch-up observations and non-executable option/close proxies limit endpoint precision. Raw P/L should not be pooled across instruments or sizes.
- Next weekly review should process only newly reviewed/changed records and any newly completed legacy backfill. Routine due checkpoints remain the daily ghost reviewer’s responsibility.

## Registry result

The compact registry now contains 6 reviewed records, 0 awaiting backfill, and 4 independent decision IDs. Full source evidence remains in the linked ghost files; this report is the concise cross-case audit.
