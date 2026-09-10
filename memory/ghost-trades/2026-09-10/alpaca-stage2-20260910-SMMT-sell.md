# Independent SMMT concentration reduction

## Identity
- decision_id: alpaca-stage2-20260910-SMMT-sell
- creator_run_id: 16e6df9f-7cf3-4e1d-85e0-ba4c397eba71
- decision_at: 2026-09-10T18:13:58.896655+02:00
- ticker: SMMT
- status: ACTIVE
- client_order_id: alpaca-stage2-20260910-SMMT-sell
- broker_order_id: null

## Original decision
Sell 500 of 1000 shares, retaining 500 protected at $16.75/$18.50 through September 11. Confidence moderate. Positive China HARMONi-2 OS confirmed in SEC September 2 filing, but Western applicability and timing remain uncertain. No assertion of imminent FDA event or numerical offering probability. At $17.10 a hypothetical 30% gap costs ~$5130 for 1000 shares; 500 leaves ~$2565 (~2.5% equity). Target total stress loss near $5500-$6000 including semiconductor 10% and other growth/medical 15%; no cash target. Reduction is risk control, not a bearish drug forecast. Maximum sale concession $0.02 from current bid; limit $17.07. Existing cost $17.33. Stock thesis invalidation $16.75; do not widen it.

## Evaluation rules
Start at confirmed real fill; common endpoint September 11 2026 15:45 America/New_York. Compare total SMMT sleeve change from contemporaneous mark including sold and retained amounts, with unchanged $16.75 stop and $18.50 target for retained shares; gap fills at executable next price, never assume exact stop fill. Checkpoints next regular close and endpoint. No extensions. If unfilled, retain WAITING_FOR_FILL.

## Initial evidence
Alpaca IEX quote observed 2026-09-10T16:13:58.665338667Z: bid 17.09 x 200, ask 17.12 x 1500. Paper position 1000 shares. Source SEC https://www.sec.gov/Archives/edgar/data/1599298/000159929826000076/smmt-20260902.htm and independent moneyheap 180944-SMMT-fundamental.md. OPRA returned 403 agreement not signed for September 18–October 16 $15–$18 puts; hedge not priceable.

## Alternatives
1. HOLD_ALL: Test whether retaining clinical upside outweighs gap concentration. Stock hold 1000, no new entry; reference liquidation bid $17.09, 1000 shares remain at risk, worst-case remaining value loss $17090.00. Same stop/target and endpoint. No sale proceeds. This is an existing-position hold, not zero-risk cash.
2. EXIT_ALL: Test full de-risking versus retaining a runner. Sell 1000 at contemporaneous bid $17.09, no subsequent reentry, remaining capital at risk zero, subsequent stock P/L zero after sale. Cash has zero interest over this window.
3. REDUCE_250: Test smaller trim. Sell 250 at bid $17.09, retain 750 marked at same bid, maximum remaining value loss $12817.50; same stop/target and endpoint. No fees/slippage beyond bid assumption; actual gaps apply.

## Execution
Pending. Prior OCO must be canceled and confirmed terminal; replacement OCO protects 500 before ordinary day-limit sale of other 500. Any uncertain mutation halts for reconciliation, never retry blindly.

## Reviewer updates

### Pre-handoff confirmed execution
{
  "sale": {
    "id": "580c204c-3ff8-4638-af9e-71ba2f103ab1",
    "client_order_id": "alpaca-stage2-20260910-SMMT-sell",
    "created_at": "2026-09-10T16:14:05.675234812Z",
    "updated_at": "2026-09-10T16:14:06.333487591Z",
    "submitted_at": "2026-09-10T16:14:05.708456759Z",
    "filled_at": "2026-09-10T16:14:06.332113633Z",
    "expired_at": null,
    "canceled_at": null,
    "failed_at": null,
    "replaced_at": null,
    "replaced_by": null,
    "replaces": null,
    "asset_id": "8595d349-c51b-4e60-b861-44b64780a4d4",
    "symbol": "SMMT",
    "asset_class": "us_equity",
    "notional": null,
    "qty": "500",
    "filled_qty": "500",
    "filled_avg_price": "17.09",
    "order_class": "",
    "order_type": "limit",
    "type": "limit",
    "side": "sell",
    "position_intent": "sell_to_close",
    "time_in_force": "day",
    "limit_price": "17.07",
    "stop_price": null,
    "status": "filled",
    "extended_hours": false,
    "legs": null,
    "trail_percent": null,
    "trail_price": null,
    "hwm": null,
    "subtag": null,
    "source": null,
    "expires_at": "2026-09-10T20:00:00Z"
  },
  "replacement_oco_id": "c9e3996c-4e38-47d5-b2a8-d816918d14e1",
  "old_oco_status": "canceled"
}

### Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`; evaluation starts at the confirmed sale fill and ends at the predeclared `2026-09-11T15:45:00-04:00` endpoint.
- Paper endpoint confirmed: `https://paper-api.alpaca.markets/v2`, with `ALPACA_PAPER_TRADE=true`.
- Broker order `580c204c-3ff8-4638-af9e-71ba2f103ab1` is `filled`, `SELL 500/500` SMMT at average `$17.09`, limit `$17.07`, filled `2026-09-10T16:14:06.332114Z`. The exact paper fill activity agrees; no partial-fill or price discrepancy.
- The prior 1,000-share OCO was canceled and replacement OCO `c9e3996c-4e38-47d5-b2a8-d816918d14e1` protects the remaining 500 shares at `$18.50`/`$16.75`. This protection change is part of the real path; no additional stock fill occurred.
- No checkpoint mark is recorded yet. Next checkpoint: next regular-session close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: SMMT close `$17.005`; the after-close quote was wide at `$15.96/$18.08`, so the bar is a disclosed non-executable proxy. The replacement 500-share GTC OCO remained unfilled; the `$16.75` stop and `$18.50` target did not trigger.
- Real path: `$8,545.00` sale proceeds plus 500 retained shares worth `$8,502.50` = `$17,047.50`, or `-$42.50` versus the `$17,090.00` pre-trade sleeve reference. `HOLD_ALL`: `$17,005.00` (`-$85.00`); `EXIT_ALL`: fixed `$17,090.00`; `REDUCE_250`: `$17,026.25` (`-$63.75`).
- Full exit led the real path by `$42.50`; the real half reduction led the 250-share trim by `$21.25` and full retention by `$42.50` at this proxy. Next checkpoint: 2026-09-11 endpoint.
