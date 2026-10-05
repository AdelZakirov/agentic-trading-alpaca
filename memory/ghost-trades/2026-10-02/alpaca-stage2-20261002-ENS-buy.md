# ENS starter alternatives

## Identity
- decision_id: alpaca-stage2-20261002-ENS-buy
- creator_run_id: 2c215101-4a65-42a2-b094-f832bb6de4ac
- decision_at: 2026-10-02T13:36:16.901797396-04:00
- ticker: ENS
- status: ACTIVE
- client_order_id: alpaca-stage2-20261002-ENS-buy
- broker_order_id: 171ac764-17db-4110-8295-bef429965bf1

## Original decision
BUY30 ENS shares, cash funded, DAY limit195.50, extended_hours=false. No pre-trade ENS exposure or open order; client ID absent by explicit broker404. October1 completed bullish compression breakout close189.61 on2.55x relative volume; industrial/data-center/defense demand, low net leverage and strong cash generation support continuation. Primary August12 release confirms sales935.6M up4.8%, adjusted EPS3.66, underlying adjusted EPS excluding45X/tariff refund1.78 up42%, net leverage0.8x and FCF217.8M (partly tax-refund-supported). Fundamentals support rather than guarantee future returns. Starter acknowledges extension and growth/power-theme correlation. Moderate confidence;1-4weeks.

Absolute entry ceiling195.50; no replacement above that ceiling. Initial195.50 limit can rest inside a wide IEX book. Sequence all retained:17:27:54Z192/196.83 sizes100/100;17:30:10Z192/196.83 sizes100/100;17:31:50Z195.14/195.68 sizes100/100;17:35:28Z195.27/196.83 sizes100/100;latest2026-10-02T17:35:51.746308799Z 192/196.83 sizes100/100. No market order, no selection of only the tightest observation. Completed hourly prints around195.13 support passive bounded execution, not crossing196.83. If order remains unfilled, preserve bound and report exact broker status; normal preclose management owns any remaining order.

Daily close below185.00 triggers next-session bounded exit review; material operating/guidance deterioration triggers thesis review. At observed executable bid203.65-205.00 review selling15, then214.50-217.00 runner review. No unseen target touch assumed. ReviewOctober5/8; exit or explicitly renew byOctober29 before estimatedNovember4 earnings. No default standing intraday stop.

Size30 cost at most5865; nominal entry-to-review loss315; illustrative20% gap1173; full capital5865 at risk. Existing post-CADL scenario ~7365 plus ENS20% stress1173 gives~8538/~8.5% equity, not a probability or bound. Uniform30% shock of combined stock book~14.8% equity. No leverage/default cash floor; this measured industrial starter diversifies direct company exposure but overlaps AI/power themes. No option selected: cash shares suit multiweek continuation; a100-share option unit and theta add no distinct payoff advantage.

## Evaluation rules
Filled comparison starts only at reviewer-confirmed actual fill. Until then WAITING_FOR_FILL; no invented start. CheckpointsOctober2close,October5close,October8close,October16close,October29 final. All stock paths share daily-close185 invalidation and next-session executable exit, target reviews and maximumOctober29 horizon; frozen after exit. Mark long stock at trustworthy executable bid, fills at conservative ask subject to the predeclared limit. Corporate actions/dividends included if applicable. No re-entry. Missing marks UNSCORABLE.

## Initial evidence
Alpaca paper clock 2026-10-02T13:36:16.901797396-04:00, sessionopen. Fresh IEX quote 2026-10-02T17:35:51.746308799Z, bid192/ask196.83, sizes100/100. Assetactive/tradable. AccountACTIVE/unblocked/cash57120.96. [Evidence](../../research/2026-10-02/option-and-leader-evidence-2c215101.json), [fundamental](../../research/2026-10-02/192913-ENS-fundamental.md), [technical](../../research/2026-10-02/192929-ENS-technical.md). Technical response calls October2 value a close despite sessionopen; treat it as partial and use broker completedOctober1/bar timestamps. Actual latest quote remains wide.

## Alternatives
### A — No trade
Question: whether extension and uncertainty justify waiting entirely.
No instrument, qty0, capital0/P&L0. Start at confirmed real fill; common window toOctober29; no execution assumption. Considered, rejected because smaller cash starter captures validated breakout without full sizing.

### B — Wait for190.50 retest,30shares
Question: improved entry versus missed continuation.
Stocklong30. Activate only if a fresh regular-session executable ask is at/below190.50 byOctober8close. Conservative simulated fill at observed ask, capped190.50; no fabricated future price. While inactive capital/P&L0. After entry same185 daily-close rule, target bands andOctober29deadline. Maximumcapital5715; nominal loss to185 at ceiling165; fullcapital at risk/gapsuncapped. Rejected as sole actual path because runaway continuation can miss it; conditional alternative remains WAITING_FOR_TRIGGER, unscorable if trigger quotes unavailable.

### C — Larger60share starter at same ceiling
Question: size choice under identical price/exit rules.
Stocklong60; executable ask must be at/below195.50 within the actual real-order fill window. Conservative simulated buy at that contemporaneous ask; current196.83ask exceeds bound, so initial entryprice null/WAITING_FOR_TRIGGER. Never use midpoint. Maximumcapital11730, nominal loss630 to185 at ceiling,20%gap2346/fullcapital at risk. Same invalidation/targets/time. Rejected for doubled industrial/growth downside while current extension and quote depth reduce confidence. Missing reliable eligible ask makes fill comparison UNSCORABLE; no invented fill at real order price.

## Execution
No submission or confirmed fill at definition time; facts appended before handoff.

## Reviewer updates


## Execution facts appended before handoff
Submitted2026-10-02T17:38:01.78819827Z, broker171ac764-17db-4110-8295-bef429965bf1/clientalpaca-stage2-20261002-ENS-buy. At 2026-10-02T13:42:10.12481259-04:00 orderstatusnew, qty30/filled0, averagefillnull; FILLactivitiesempty, noENSposition. Finalquote17:42:16Z192/196.83, sizes100/100. No replacement; maintain195.50ceiling through preclose review. WAITING_FOR_FILL; comparison not activated.

### 2026-10-03 reviewer activation and October 2 close checkpoint

- The manifest source SHA-256 matches its immutable packet snapshot. Read-only Alpaca paper order `171ac764-17db-4110-8295-bef429965bf1` is `filled`, BUY 30/30 at `$195.46`; two matching order-specific FILL activities of 15 shares each total 30, with final fill at `2026-10-02T18:02:25.892015Z`. The current paper position is 30 shares at `$195.46`, with no open ENS order. Lifecycle state is `ACTIVE`; common start is the confirmed fill.
- Historical IEX quotes covered the regular session without a page token. Alternative C's original actual-order fill window contains a positive, uncrossed `$195.45` ask x100 / `$192.00` bid x100 at `2026-10-02T18:02:24.330049Z`, just before the real fill. C therefore activates at its observable ask of `$195.45` for 60 shares. Alternative B remains `WAITING_FOR_TRIGGER`: the lowest observed session ask was `$193.81`, above its `$190.50` condition; its window stays open through October 8.
- The October 2 IEX daily bar was `$196.32` close (high `$198.985`, low `$194.54`), but the last near-close IEX book widened to `$168.43 x100` bid / `$196.43 x100` ask at `2026-10-02T19:59:59.491133Z`. This is not a trustworthy executable close mark for either open position; real and C outcomes are `UNSCORABLE` at this checkpoint. The `$185` close invalidation and `$203.65` first executable-bid review were not reached. Next checkpoint: October 5 close; final horizon remains October 29. No lesson change.
