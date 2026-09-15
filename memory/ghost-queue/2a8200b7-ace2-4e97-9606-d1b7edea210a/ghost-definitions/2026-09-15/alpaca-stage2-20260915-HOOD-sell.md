# HOOD partial trim — pre-submission alternatives

## Identity
- decision_id / client_order_id: alpaca-stage2-20260915-HOOD-sell
- creator_run_id: 2a8200b7-ace2-4e97-9606-d1b7edea210a
- decision_at: 2026-09-15T20:54:40+02:00
- ticker: HOOD
- status: WAITING_FOR_FILL
- broker_order_id: null

## Original decision
SELL 15 of 30 owned shares; retain 15. Day limit $107.85, extended_hours=false. Maximum initial slippage $0.05 below observed bid; any one eligible replacement must be justified by a refreshed quote, no lower than $107.40.
Fresh research and broker bars show a sharp high-beta fintech selloff, loss of the 20-day mean, and deterioration of momentum. This discretionary partial reduction explicitly changes the prior intraday HOLD decision because fresh evidence weakened the thesis; it does not claim that today's daily-close invalidation already occurred.
Size: halve $3,200 exposure to reduce Fed/correlated-fintech gap risk while retaining upside at the $103.20–$103.50 structural support.
Remaining-stock plan: review today's completed daily close below $107.50; exit/reduce on confirmed failure. Re-entry/add requires daily reclaim $108.50 plus $110 confirmation. Horizon 1–5 trading sessions; reassess before next session.

## Evaluation rules
Start at confirmed real fill; use actual fill for chosen-sale reference. Checkpoints: next completed close, third and fifth trading-session close; end September22 2026 16:00 America/New_York. Compare total forward portfolio P/L on the predecision 30-share exposure, including sale proceeds and remaining shares, against its contemporaneous bid mark; exclude historical gains.
Alternative long positions use the stated daily-close $107.50 review and next-session bounded exit on confirmed failure; otherwise mark/exit at end-window bid. Options close together at executable long bid minus short ask at end or earlier underlying invalidation. No exercise; close before expiration.

## Initial evidence
- Alpaca IEX quote 2026-09-15T18:54:23.003896639Z: bid $107.9, ask $108.28, sizes 100/200.
- Full validation sequence: 18:51:12Z 106.98/109.01 sizes100/100; 18:52:05Z 107.02/107.11 sizes100/100; 18:53:43Z 108.01/111.24 sizes100/100; final 18:54:23Z 107.90/108.28 sizes100/200. Wide asks are intermittent; every quote is retained. Bounded sale remains inside the positive quoted bid; no market-order inference.
- Research: ../../research/2026-09-15/204907-HOOD-technical.md.
- Indicative October16 puts at18:49:51–52Z: 105P 7.07bid/7.17ask sizes46/14 delta-0.435 IV0.6371 theta-0.1194; 95P 3.09bid/3.19ask sizes23/25 delta-0.2427 IV0.6432 theta-0.0972. Indicative estimates, not OPRA or guaranteed fills.

## Alternatives
1. HOLD_ALL: retain30 existing shares, no new order. Tests waiting for daily-close confirmation. No simulated new entry; existing exposure marked at $107.90bid ($3,237). Future maximum stock loss $3,237 if worthless; apply common close-based exit/window. Rationale: potential support bounce.
2. EXIT_ALL: sell30 at contemporaneous $107.90bid, $3,237proceeds; no future exposure. Tests full versus partial reduction. Zero future capital at risk; remainflat through commonwindow.
3. HOLD_WITH_PUT_SPREAD: retain30 and buy1 HOOD261016P00105000 / sell1 HOOD261016P00095000, ratio1:1, indicative debit $4.08 ($408) from longask7.17 minus shortbid3.09. Tests option hedge versus stock reduction. Spread maximum loss $408, maximum expiry profit $592, breakeven$100.92; stock loss remains possible. Rejected because delta/100-share contract granularity overwhelms a small stock holding and target$103.20 produces only$180 intrinsic value versus$408debit at expiry; no demonstrated separate bearish edge. Entry immediately at evidenced conservative debit only; closebothlegs per commonrules, neverexercise.
Missing data: future execution/marks unknown; indicative quotes modified/delayed.

## Execution
- Submitted day limit $107.85 with client ID alpaca-stage2-20260915-HOOD-sell; broker ID bb4040e2-0e27-4916-93a9-41d1bfbf27b1.
- Submission-time IEX quote 2026-09-15T18:55:50.291882325Z: bid108.90 / ask108.98 sizes100/100. Original alternative prices/rules remain unchanged.
- Confirmed broker status filled, 15/15 at $108.94 on 2026-09-15T18:55:59.003411657Z; subsequent positions confirm15shares remain.

## Reviewer updates
