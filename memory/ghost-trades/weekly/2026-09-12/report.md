# Weekly ghost-trade lessons review — 2026-09-12

## Scope and coverage

- Reviewer-only run. No broker mutations, discovery, moneyheap calls, trading-log edits, ticker-file edits, portfolio-state edits, or lesson edits were made.
- The compact registry snapshot is [`reviews-input.json`](reviews-input.json).
- Registry coverage: 11/11 records are `reviewed`, 0 remain `awaiting_backfill`, and there are 9 independent decision IDs after grouping dependent sets. Quality is 1 `scorable` and 10 `partial`.
- Five records were evaluated after the prior weekly report (GTLB, MMED entry/exit, and MSTR option entry/exit), so a targeted cross-case review is due.

## Queue coordination

- Initial readiness was blocked by active run `e1078b10-589a-4b8d-ae9a-dd2350362c2b`, started `2026-09-11T19:30:21Z`, with no pending or claimed packet. The app showed no running Alpaca trader or ghost-review task, and a read-only local process check found no matching process. After a 60-second recheck the marker remained; it was preserved because another task's marker must not be cleared automatically.
- The owning task cleared the marker during this review and published the run. Final status was `active=null`, `claimed=null`, `pending=[e1078b10-589a-4b8d-ae9a-dd2350362c2b]`. The pending packet belongs to the daily reviewer; it was not claimed or processed here.
- No active 2026-09-11 ghost definitions were used as completed evidence.

## Verified patterns

- Continuation timing and selection: `alpaca-stage2-20260902-GTLB-buy` and the prior `alpaca-stage2-20260831-GAP-buy` both underperformed no trade over their selected windows. GTLB's exit after the documented invalidation beat retaining half size on a capital-normalized basis, but this is only two related common-stock continuation cases and does not establish a universal filter.
- Event-risk sizing: the dependent MMED entry/reduction pair (`alpaca-stage2-20260902-MMED-buy`, `alpaca-stage2-20260902-MMED-sell`) shows that reducing half limited loss versus holding all, while full exit was best at the endpoint. It supports the risk-control mechanism, not a half-versus-full rule.
- Defined-risk options and expiry handling: the dependent MSTR entry/trim pair (`alpaca-stage2-20260902-MSTR-option-buy`, `alpaca-stage2-20260903-MSTR-option-sell`) produced +$801 gross versus no trade; the partial trim finished $27 below fixed full-close proceeds while avoiding unscorable hold/expiry exposure. Stock and uncapped-call alternatives remain unscorable at the endpoint.

## Lesson result

- No candidate pattern justified a new, merged, retired, or strengthened lesson. `memory/lessons.md` was not changed; existing evidence counts and confidence levels remain calibrated.
- The five new records are all `partial`; two pairs are correlated within the same MMED and MSTR campaigns. Coverage remains selected-trade evidence, and raw P/L is not pooled across instruments, sizes, or horizons.

## Next evidence needed

- The daily reviewer should process the pending 2026-09-11 handoff. The next weekly run should review only any newly completed/changed registry records and preserve this snapshot as the audit baseline.
