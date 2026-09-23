# Weekly ghost-trade lessons review — 2026-09-19

## Scope and coverage

- Reviewer-only run. No broker mutations, discovery, moneyheap calls, trading-log edits, ticker-file edits, or portfolio-state edits were made. The lesson update below was applied atomically after the evidence check.
- The exact compact registry snapshot is [`reviews-input.json`](reviews-input.json).
- Registry coverage: 32/32 records are `reviewed`; 0 remain `awaiting_backfill`; grouping dependent paths leaves 30 independent decision IDs. Quality is 1 `scorable` and 31 `partial`.
- Since the 2026-09-12 weekly snapshot, 21 records covering 21 new decision IDs were added; all are `partial`.
- Across 125 recorded outcomes, 97 are scorable and 28 are unscorable. Fourteen records contain an unscorable option/call/spread path. The sample is selected trade decisions, not an unbiased market sample; multiple paths within one decision and repeated ticker campaigns are not independent evidence.

## Queue coordination

- `python3 -m alpaca_agent.ghost_queue status` showed `active=null`, `pending=[]`, and `claimed=null` before review. The same clear state remained after review.
- No daily reviewer packet was claimed or processed. Active checkpoint work remains owned by the daily reviewer.
- Legacy inventory reported 32 sets, 32 reviewed, 0 awaiting backfill, and 30 independent decisions.

## Targeted cross-case evidence

### Exit and reduction timing is conditional, not universal

- Immediate exits led retention after confirmed failure in [`2026-09-04 SLB`](../../2026-09-04/alpaca-stage2-20260904-SLB-sell.md) and [`2026-09-08 GTLB`](../../2026-09-08/alpaca-stage2-20260908-GTLB-sell.md).
- Waiting or retaining led earlier exits or trims in [`2026-09-10 GAP`](../../2026-09-10/alpaca-stage2-20260910-GAP-sell.md), [`2026-09-04 RBLX`](../../2026-09-04/alpaca-stage2-20260904-RBLX-sell.md), and [`2026-09-10 SMMT`](../../2026-09-10/alpaca-stage2-20260910-SMMT-sell.md). The later [`2026-09-14 RBLX`](../../2026-09-14/alpaca-stage2-20260914-RBLX-sell.md) favored a larger trim over both the chosen smaller trim and full retention.
- These cases test different triggers, horizons, and risk states. They support keeping the existing lesson to preserve a stated time basis unless a documented thesis change justifies earlier action; they do not support a general “exit immediately” or “always wait” rule.

### Bounded sizing limits damage but does not identify a fixed optimum

- The [`MMED` entry and lock-up reduction](../../2026-09-02/alpaca-stage2-20260902-MMED-buy.md) and [`MMED` reduction](../../2026-09-02/alpaca-stage2-20260902-MMED-sell.md) show that reducing exposure limited loss versus holding full size, while full exit was still best at the endpoint.
- The [`CHYM` event-risk starter](../../2026-09-16/alpaca-stage2-20260916-CHYM-buy.md) lost less than the predeclared 200-share alternative, but no trade was better. Favorable continuation cases in HOOD, MU, and RBLX also show full size outperforming half size over their marked windows.
- The repeated mechanism supports adaptive, predeclared risk sizing, not a durable half-size or starter-size rule. No new lesson is warranted.

### Expiring protection is a repeatable operational failure mode

- [`SMMT pullback`](../../2026-09-04/alpaca-stage2-20260904-SMMT-buy.md) was profitable, but its day-only exits expired at the close and left an unintended overnight position despite the stated holding plan.
- [`COO expiry close`](../../2026-09-16/alpaca-stage2-20260916-COO-sell.md) closed the paired spread before expiry; the real path beat holding through expiration by $60 gross and removed assignment/pin risk. The one-session and October-roll alternatives remain unscorable, so the lesson is about expiry-risk handling, not a universal close-now P/L rule.
- This is sufficient to strengthen the existing `Reconcile expiring protection at the close` lesson from one low-confidence case to two independent cases with medium confidence. The NVDA GTC-versus-DAY study is neutral on P/L and does not contradict the operational requirement.

### Re-entry and confirmation evidence is too narrow

- Both [`NVDA` continuation entry](../../2026-09-04/alpaca-stage2-20260904-NVDA-buy.md) and [`NVDA` re-entry](../../2026-09-04/alpaca-stage2-20260904-NVDA-reentry-buy.md) were beaten by no trade, but the confirmation alternatives were unentered or unscorable and the decisions belong to one campaign.
- This is a useful risk warning for that failed continuation sequence, not independent evidence for a universal re-entry rule.

### Option comparisons remain data-limited

- The [`MSTR` spread](../../2026-09-02/alpaca-stage2-20260902-MSTR-option-buy.md) produced a positive realized result, and the [`COO` spread](../../2026-09-11/alpaca-stage2-20260911-COO-bear-put-spread.md) narrowly beat the outright-put counterfactual; however, the continuation or roll paths are unavailable in executable historical marks.
- The [`SLB` option add](../../2026-09-01/alpaca-stage2-20260901-SLB-option-buy.md) duplicated the stock thesis and lost more than a small stock add. The evidence continues to support payoff/overlap checks, but unscorable option paths cannot establish a broader instrument preference.

## Lesson result

- `memory/lessons.md` was atomically updated: `Reconcile expiring protection at the close` now covers expiring brackets and multi-leg option risk, has 2 independent supporting cases, and moves from low to medium confidence.
- No new generic timing, sizing, re-entry, or instrument-preference lesson was justified. The time-basis lesson remains conditional and low-confidence: PCG is direct supporting evidence, while SLB and GTLB show that a confirmed invalidation can still justify an immediate exit.

## Limits and next evidence

- Do not pool raw P/L across instruments, sizes, horizons, or endpoint proxies. Several stock endpoints use disclosed non-executable daily-bar/IEX proxies, and 28 outcome paths remain unscorable.
- The evidence is dependent and selected: HOOD, RBLX, MU, NVDA, MMED, and SLB each contribute multiple related decisions or management paths.
- The next weekly run should review only newly completed or materially revised registry records after the daily reviewer’s due checkpoints, preserving this snapshot as the comparison baseline.
