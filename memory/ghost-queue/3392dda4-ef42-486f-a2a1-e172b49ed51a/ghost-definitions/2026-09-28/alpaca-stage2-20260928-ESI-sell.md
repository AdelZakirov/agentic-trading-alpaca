# ESI horizon exit alternatives

## Identity
- decision_id: alpaca-stage2-20260928-ESI-sell
- creator_run_id: 3392dda4-ef42-486f-a2a1-e172b49ed51a
- decision_at: 2026-09-28T16:59:59.830945+02:00
- ticker: ESI
- status: WAITING_FOR_FILL
- client_order_id: alpaca-stage2-20260928-ESI-sell
- broker_order_id: null

## Original decision
SELL all40 owned shares at a bounded DAY limit. The original tactical oversold rebound reached its first profit review and today is the predeclared exit-or-renew deadline. Current fundamental research is moderate: ~3.4x leverage, $50.8M trailing FCF and no verified new near-term catalyst; renewed growth confirmation is expected at late-Oct/early-Nov earnings, outside the initial rebound horizon. Primary company evidence confirms strong electronics growth and Aug27 merger termination, but those are already-known background, not a fresh renewal trigger. Choose realized rebound gain and reduce semiconductor-cycle overlap. Confidence moderate; longer-term business thesis may remain positive. Cost32.16, qty40/40available. No options or short stock. Max slippage $0.10 below the last positive executable bid; floor35.10 for this logical exit. Review unfilled DAY order at pre-close.

## Evaluation rules
Comparison starts only after broker-confirmed real first fill and uses the weighted real40-share exit as baseline; no invented entry or fill. Observe daily closes through Oct12, with profit review at37.50, daily-close invalidation30.40, terminal exit Oct12 15:45ET. Both renewed carry scenarios use the same30.40 close basis and end permanently at their first rule exit. These are separately declared renewals beyond today's original deadline, not a silent extension. Max loss is retained share value; no guaranteed stop.

## Initial evidence
Alpaca IEX quote14:58:40.002150148Z bid35.24/ask35.33 (100x200), earlier14:57:49.342025827Z35.29/35.34 (100x200). Friday completed IEX close35.69 exceeds original30.40, so this is horizon/edge exit, not an invalidation claim. Current broker40shares avg32.16, lastday35.71. Research memory/research/2026-09-28/165635-ESI-fundamental.md; primary SEC Aug27 termination release and company Q2 report. Option quotes absent and unnecessary for these stock alternatives.

## Alternatives
1. RENEW40 — test full runner renewal for the standalone electronics growth thesis. HOLD40 existing shares, no new trade; start mark at common real-fill baseline. Daily close below30.40 triggers next-session bounded sale at observed bid; executable bid37.50 triggers full sale, else Oct12 15:45ET terminal sale at observed valid bid. Full retained40share value is maximum capital risk; pricing gaps may be UNSCORABLE. Rationale: strong organic electronics growth could overcome leverage/technical consolidation.
2. SELL20_RENEW20 — test partial de-risking. Hypothetical SELL20 now at contemporaneous bid35.24; HOLD20 under identical RENEW40 rules and timeline, no new purchase or option. Maximum carry capital risk20 times common anchor; sold half uses recorded executable bid, not assumed real-order fill. Rationale: retain upside while cutting cyclical risk; one size change versus full-renewal alternative.

## Execution
Order/fills:null. Reviewer activation awaits broker evidence.

## Reviewer updates

## Final pre-submission quote validation
Initial abnormal IEX15:00:03.074923986Z bid33.62/ask35.16,100x100. Extra1 at15:02:23.700427981Z bid35.08/ask35.13,300x100; extra2 at15:03:24.949616762Z bid35.09/ask35.53,200x100. Sequence spans3m22s and shows stable positive recent bids around35.08-35.09 despite ask-width variation. Selected SELL40 DAY limit35.10 inside the current spread and above the recent bid; do not lower below35.10 merely to obtain a fill. Preflight clock11:03ET open, accountACTIVE, cash62077.38, qty40/40available, noopenorders, clientID confirmed404before submission.

## Confirmed execution before handoff
Brokeraf81f800-b0d0-48ce-801b-6a22053f0870 FILLED40@$35.10 at2026-09-28T15:05:15.37464557Z. Exact FILL40@$35.10. Cash62077.38→63481.38 equals1404.00proceeds. ESI absent, zeroopenorders. Gross realized P/L117.60before fees. Reviewer activation remains independent.
