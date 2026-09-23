# ET entry alternatives

## Identity
- decision_id: alpaca-stage2-20260922-ET-buy
- creator_run_id: 0593e73b-6b59-4624-b8e2-3174b6eaa24f
- decision_at: 2026-09-22T17:44:30+02:00
- ticker: ET
- status: WAITING_FOR_FILL
- client_order_id: alpaca-stage2-20260922-ET-buy
- broker_order_id: null

## Original decision
Cancel unfilled EGO buy200@$43.95; after confirmed cancellation and reconciliation buy400 ET DAY limit20.95, extended_hours=false. No ET position beforehand. Moderate-confidence 1–4week support-rebound thesis, confirmed consolidated SMA50 20.8442 and improving company earnings/guidance. Correct capex5.6–5.9B and Oct5 exchange transfer incorporated; not an event-free trade. Review before Oct5 and final horizon Oct20. No options: modest target move favors units over theta/spread friction.

Size400: notional8380, planned tactical downside160 to20.55 (0.16% of102817 equity), 10% gap838 (0.82%). Lower than displaced EGO690 planned downside/879 gap. Portfolio long exposure~66.6% after fill, combined planned review-level downside~4.5%; biotech/tech gaps remain. Cash-funded, no minimum cash target. No simultaneous new EAT or other entries. GTC OCO protection after confirmed fill: stop-market20.55, take-profit21.80 for filled units. Executable bid21.35 triggers review only, no promised continuous discretionary trim. Stop can slip/gap. Parent DAY order expiration does not imply persistent protection; verify GTC exits separately.

## Evaluation rules
Filled comparison starts at actual ET fill. Checkpoints first session close, +1/+5 trading days and Oct2 pre-transfer review, final Oct20 close. Common exit:20.55 intraday stop or21.80 target, using broker-compatible bars/quotes, stop gaps at next executable bid; simultaneous ambiguous intrabar touches conservatively stop-first. No dividends assumed. No fill by parent DAY expiration means waiting/not-activated, not zero-return filled trade. Alternatives observed only during regular session through Oct20; trigger alternative can activate before that deadline. Preserve actual executed prices separately.

## Initial evidence
Alpaca regular session open11:43:34ET; account active, cash42693.43, equity102816.98; 11 stock positions. EGO only open buy,0filled. ET active/tradable, intended client ID404notfound. IEX ET15:44:09Z bid20.95 size3600, ask20.96 size10000, spread0.01. EGO15:44:13Z44.51/44.53. ET max entry20.95 below current ask, zero allowance above thesis cap. Sources: independent-review.md and ET173711 technical /173914 fundamental with primary-source corrections.

## Alternatives
1. NO_TRADE: test whether adding exposure helps; no instrument/order, quantity0, entry0, maximum loss0, zero P/L over common window. Keep capital unused; same endpoints.
2. HALF_SIZE: test400vs200 units, buy200 with identical20.95DAY limit. No hypothetical immediate fill at ask20.96; activates only upon documented executable ask<=20.95 while DAY order valid, or actual selected fill contemporaneously with adequate liquidity. Planned stop risk80, maximum unlevered loss4190, gap/slippage uncapped by stop. Same20.55/21.80 exits.
3. CONFIRMATION_ENTRY: test waiting for reversal confirmation rather than support entry. Buy400 after completed1hour bar closes above21.15; next regular-session executable ask, provided<=21.20, otherwise no entry. Simulated price unknown until trigger; no fabricated current fill. Stop20.55,target21.80; maximum stock loss<=8480, planned stop risk<=260. Same horizon. If future executable quotes unavailable mark UNSCORABLE.

## Execution
No order submitted at definition time; fills null. Chosen buy uses actual broker fills only. EGO cancellation must reconcile before ET submission.

## Reviewer updates
Reserved for reviewer after handoff.

## Execution facts before handoff
- EGO cancellation confirmed 2026-09-22T15:45:08.457624365Z, 0 filled.
- ET BUY 400 limit20.95 order 7c2a4d36-e8ee-482c-b2f9-f1e599a65a1c filled400 at20.95, final fill 2026-09-22T15:48:02.020199769Z. Three fill activities171+59+170.
- Before persistent protection could be submitted in the resumed run, price fell through20.55; all400 sold at20.55 on separate decision. Gross trade P/L -160 before fees. No ET position at handoff.
