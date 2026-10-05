# NICE — original pretrade definition

## Identity

- decision_id: alpaca-stage2-20260930-NICE-buy
- creator_run_id: c0323edf-44f5-469c-a26d-86c326f5a680
- decision_at: 2026-09-30T21:57:47+02:00
- ticker: NICE
- status: NOT_SUBMITTED
- client_order_id: alpaca-stage2-20260930-NICE-buy
- broker_order_id: null

## Original decision

Investment decision: BUY a 30-share cash-funded starter, limit at most $111.50, DAY, regular hours only. Execution decision: NOT SUBMITTED. Initial IEX ask $111.44 permitted a limit at $111.50 (six-cent allowance). The subsequent $112.34 asks persistently exceeded that bound, spreads widened, and the third validation response repeated the prior timestamp. Only about two minutes remained before the close; the sequence did not establish a fresh usable entry at the selected price. Do not retry this client ID later without a new decision.

Pretrade NICE exposure zero. Moderate confidence in a 1-3 week recovery above the $105-$107 base: current company cash flow and net-cash facts, raised FY EPS guidance, and technical higher low outweigh some AI-displacement concern. GAAP margins/EPS have fallen and exact upgrade date is disputed. The thesis does not require the event to have occurred today. MSFT and DT add software correlation. Thirty shares would cost at most $3,345: 20% gap $669; nominal loss to $105 review price $195; full capital can be lost. Size was derived from an incremental adverse-gap allowance around $700 while the existing small MU position carries earnings and biotech risk remains. No leverage or cash floor.

Daily close below $105 or material revenue/retention/cash-flow deterioration invalidates and triggers next-session bounded exit review; this is not a guaranteed stop. At observed executable bid $118.30 review trimming half; $124.50-$128 review the runner. Review October 1; October 16 exit-or-explicit-renew deadline. Stock preferred to adding theta/levered AI overlap; no selected option trade.

## Evaluation rules

Unsubmitted study only. Observation window starts at decision time and ends October 16 regular close; no real fill anchor. Hypothetical execution is conditional, not asserted: first fresh regular-session positive, uncrossed bid/ask through October 2 with ask at/below $111.50 for a cash-stock limit variant. If no observable qualifying ask, mark NOT_ACTIVATED. Simulated entry price remains null and UNSCORABLE until evidence exists. Compare after an observed qualifying entry; no hindsight fill from a daily low. Checkpoints: first eligible entry, October 2 close, October 9 close, and October 16 close. Apply the same daily-close $105 invalidation with next-session bid exit, and the same observed target reviews. No inferred unseen touch. A skipped/unobservable checkpoint stays unknown.

## Initial evidence

- Shortlist state September 30 completed; technical completed bars September 29; experts generated 2026-09-30T19:27:05Z. Enriched hash d49f843d9b09772ba5b4af344be8a968fc8848f06ba7235d96e1497f73e55e1c.
- IEX at 19:46:00.202291Z: bid111.74 size200 / ask112.34 size200.
- IEX at 19:52:20.597891Z: bid111.20 size100 / ask111.44 size100, spread0.24.
- IEX at 19:54:15.413371Z: bid111.26 size100 / ask112.34 size200, spread1.08.
- IEX at 19:56:31.125450Z: bid111.10 size100 / ask112.34 size100, spread1.24. Next read at about19:57:44Z returned this identical quote timestamp. No third newly updated observation.
- Account ACTIVE/unblocked, cash57291.97, no NICE position or any open orders. Client-ID lookup explicitly returned broker404 order not found. Asset active/tradable. Regular market open at15:57:47 ET; close16:00.
- [Fundamental](../../research/2026-09-30/214452-NICE-fundamental.md), [technical](../../research/2026-09-30/215038-NICE-technical.md), [primary corrections](../../research/2026-09-30/primary-source-notes.md). IEX is one exchange; no reliable consolidated executable book. Future prices/fills unknown.

## Alternatives

### A — no trade

Question: does abstaining outperform accepting overnight software risk? Rationale: event dating and margins conflict, near-close liquidity weak. Instrument NONE, side NONE, quantity0, notional0. Entry at decision time, simulated entry0, maximum loss0, capital0, P/L0 throughout common observation window. No contracts or exit required.

### B — half-size conditional starter

Question: does halving exposure improve the recovery trade's risk-adjusted outcome? Rationale: retain upside while cutting software/gap risk. Instrument STOCK, side BUY, quantity15, maximum notional1672.50 at limit111.50. Same first qualifying regular ask rule through October2, no assumed fill. Simulated entry price null, UNSCORABLE until qualifying quote; full capital maximum loss up to1672.50, 20% gap334.50. Same invalidation, targets, review window and exit handling as original. Only size changes.

### C — wait for reclaim

Question: is verified momentum worth the higher entry price? Rationale: require reversal of the afternoon fade. Instrument STOCK, side BUY, quantity30. Trigger: first completed regular daily close above113.35 through October7, then first observed next-session fresh ask at/below115; otherwise NOT_ACTIVATED. Simulated entry price null, UNSCORABLE until trigger/quote. Maximum notional3450 and full-capital maximum loss3450; daily-close105 invalidation and same October16 end. Future ask is unknown; no invented $113.35 fill. No options or extended-hours action.

## Execution

No order submitted. Broker order ID null; filled quantity0; fill price/time null. No buying power reserved. Investment and execution decisions are separate.

## Reviewer updates

Reserved for reviewer after handoff.

### 2026-09-30 handoff adoption

- Adopted this original definition from the handoff manifest; the source SHA-256 matches its immutable packet snapshot. Read-only Alpaca paper lookup for client ID `alpaca-stage2-20260930-NICE-buy` returned order-not-found, and no NICE position is open.
- Execution remains NOT_SUBMITTED. No fill or comparison start is inferred. Keep the original no-trade, half-size, and reclaim alternatives unchanged. Next observation is the Oct 1 regular-session first-eligible-entry check; the conditional entry window and checkpoints remain as predeclared.

### 2026-10-01 first-eligible-entry check

- Read-only paper MCP lookup for client ID `alpaca-stage2-20260930-NICE-buy` returned HTTP 404 order-not-found. Oct 1 IEX history returned 5,721 quotes from 13:30:00.007659588Z through 19:59:59.508617093Z, with no positive, uncrossed quote whose ask was at or below $111.50. This is IEX-only evidence, not a consolidated book.
- No real order or fill is confirmed. The original alternatives remain unchanged and no hypothetical entry or comparison start is recorded. Recheck the predeclared A/B entry condition during the Oct 2 regular session; C's reclaim trigger remains open through Oct 7.

### 2026-10-02 conditional-entry check — partial session

- The Alpaca paper IEX 1Day bar for October 1 closed at `$116.605`, above C's predeclared `$113.35` reclaim trigger. On October 2, the first fresh positive, uncrossed regular-session quote with ask at or below `$115` was `$114.40` bid x200 / `$115.00` ask x100 at `2026-10-02T16:24:57.062617131Z` (12:24:57 ET). C is now active as a hypothetical 30-share entry at `$115.00`; this is not a broker order, actual fill, or real-path comparison start.
- From the regular-session open through `12:26:22 ET`, the lowest observed ask was `$115.00`, above A/B's `$111.50` cap; neither A nor B activated. Their entry window remains open through the October 2 close. This is a partial-session check, not a final window result; the Oct 2 daily bar is incomplete and is not used as a close mark.
- Keep the actual decision `NOT_SUBMITTED` with zero real shares. C's next common checkpoint is the October 2 close; the `$105` daily-close invalidation and `$118.30` executable-bid review remain in force. No lesson change.

### 2026-10-02 entry-window close and checkpoint

- The remaining regular-session IEX quotes after the earlier 12:26 ET check contained no ask at or below `$111.50`; the minimum was `$113.19`. Alternatives A/B therefore ended their predeclared October 2 entry window `NOT_ACTIVATED`, with no fill or return assigned. C remains a 30-share hypothetical path from `$115.00` after its original reclaim and qualifying ask.
- After the C entry, the maximum observed bid was `$115.07`; the October 2 IEX daily bar high was `$117.51`, below the `$118.30` target review. The close was `$113.87`, above the `$105` invalidation. The final IEX book was dislocated at `$98.46 x100` bid / `$130.11 x100` ask, so C's close P/L is `UNSCORABLE`; the daily close is not substituted for an executable bid.
- This remains a `NOT_SUBMITTED` study with one active hypothetical path, not a real fill. Next checkpoint: October 9 close (C continues); final horizon remains October 16. No lesson change.
