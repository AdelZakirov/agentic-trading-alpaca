# ET entry alternatives

## Identity
- decision_id: alpaca-stage2-20260922-ET-buy
- creator_run_id: 0593e73b-6b59-4624-b8e2-3174b6eaa24f
- decision_at: 2026-09-22T17:44:30+02:00
- ticker: ET
- status: ACTIVE
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

### 2026-09-22 broker reconciliation
- Lifecycle state: `ACTIVE` from the confirmed 400-share fill at $20.95 on broker order `7c2a4d36-e8ee-482c-b2f9-f1e599a65a1c` (`2026-09-22T15:48:02.020199769Z`). Three order-specific FILL activities (171+59+170) total 400 shares.
- The real path then sold all 400 at $20.55 on the separate stop-decision order `3124202f-fd96-4196-a455-4c794b9b8d73`; one order-specific 400-share FILL activity confirms `2026-09-22T19:16:55.558216496Z`. Gross realized result is -$160 before fees. Current Alpaca positions show no ET shares.
- This is not a completed comparison: the original hypothetical paths continue through their declared horizon. First checkpoint is the 2026-09-22 close; no close marks recorded yet.

## Execution facts before handoff
- EGO cancellation confirmed 2026-09-22T15:45:08.457624365Z, 0 filled.
- ET BUY 400 limit20.95 order 7c2a4d36-e8ee-482c-b2f9-f1e599a65a1c filled400 at20.95, final fill 2026-09-22T15:48:02.020199769Z. Three fill activities171+59+170.
- Before persistent protection could be submitted in the resumed run, price fell through20.55; all400 sold at20.55 on separate decision. Gross trade P/L -160 before fees. No ET position at handoff.

## 2026-09-22 first close checkpoint

- The same-session real path is closed: 400 shares bought at `$20.95` and sold at `$20.55`, gross `-$160` before fees. The half-size alternative using the same observed entry and exit prices is `-$80`; no-trade is `$0`. The confirmation alternative stayed untriggered because the session high was `$20.99`, below `$21.15`.
- No hypothetical fill beyond the bounded actual executions is inferred. This is an interim checkpoint; no lesson change. Next checkpoint: `2026-09-23` close (+1 session), then Sep 29 / Oct 2 / Oct 20 under the original schedule.

### 2026-09-23 +1-session checkpoint

- Project `alpaca_paper` historical IEX quote at `2026-09-23T19:59:59.805782808Z` was ET `$20.49/$20.50` bid/ask, with 3,700 bid shares; the IEX daily bar closed at `$20.49`. The Sep 23 hourly bars never closed above the `$21.15` confirmation threshold (maximum hourly close `$20.67`, high `$20.70`); the prior Sep 22 high was `$20.99`.
- All filled paths had already exited under the original `$20.55` stop rule: real `-$160`, HALF_SIZE `-$80`; NO_TRADE and untriggered CONFIRMATION_ENTRY remain `$0`. The breakout alternative did not activate. No lesson change; IEX depth was adequate for the tested ET quantities.
- Next checkpoint: Sep 29 (+5 trading days), then the pre-transfer and final dates already defined.

### 2026-09-29 +5-session checkpoint

- The IEX daily bar closed at `$19.90`; the near-close quote at `2026-09-29T19:59:59.995515338Z` was `$19.90/$19.91` with 3,300/900 shares displayed. Hourly IEX bars from September 24–29 never closed above the `$21.15` confirmation threshold (maximum `$20.615`), so `CONFIRMATION_ENTRY` did not activate.
- The real 400-share path and `HALF_SIZE` had already exited under the original `$20.55` stop on September 22 (`-$160` and `-$80` respectively); `NO_TRADE` remains `$0`. No later entry or re-entry is inferred. Comparison remains active through its original October 20 horizon; next scheduled review is October 2.

### 2026-10-02 pre-transfer checkpoint

- Common Alpaca paper IEX quote `2026-10-02T19:59:59.758927Z` was `$20.48 x2900` bid / `$20.49 x1300` ask. The real path remains fixed at `-$160` after 400 shares were stopped at `$20.55`; the half-size path remains `-$80`, and no-trade remains `$0`.
- The confirmation-entry alternative did not activate: the 62 IEX hourly bars from September 22 through October 2 had a maximum completed hourly close of `$20.95` (high `$20.99`), below `$21.15`. Current Alpaca positions and open orders contain no ET position or order. No re-entry is assumed.
- The October 2 review is not the final endpoint; the original horizon remains October 20. Next checkpoint: October 20 close. No lesson change.
