# NVDA protection duration

## Identity
- decision_id: alpaca-stage2-20260910-NVDA-oco
- creator_run_id: 16e6df9f-7cf3-4e1d-85e0-ba4c397eba71
- decision_at: 2026-09-10T18:17:14.771690+02:00
- ticker: NVDA
- status: ACTIVE
- client_order_id: alpaca-stage2-20260910-NVDA-oco
- broker_order_id: null

## Original decision
HOLD 55 existing shares; cancel confirmed DAY exits and submit GTC OCO 55 shares with same $226 limit/$210.50 stop. No entry, no change to exposure. Bracket expires today despite multi-session thesis. Current independent technical report 181120-NVDA-technical.md supports $226 range target. Reject wider $208 stop because it expands downside without stronger evidence. Moderate confidence, review September 11; maximum holding September 24 unless re-underwritten. Stops do not guarantee fill prices or overnight execution.

## Evaluation rules
Unsubmitted/working protective-order study starts upon confirmed new OCO acceptance; no stock fill is assumed. Reference mark is contemporaneous bid $218.33. Compare retained 55-share sleeve through September 11 15:45 ET; checkpoint today close and tomorrow close/endpoint. Respect gaps using first executable bid, no invented exact stop fill. Position maximum value loss 12008.15; no incremental capital. If protection submission fails, status NOT_SUBMITTED and reviewer reports operational failure separately.

## Initial evidence
Alpaca IEX 2026-09-10T16:17:14.579742055Z: bid 218.33 x 300, ask 218.36 x 200. Broker confirms 55 shares, DAY stop $210.50 held until September 10 20:00 UTC. No option quotes used.

## Alternatives
1. KEEP_DAY: Keep original 55-share DAY target/stop, then no automatic protection after expiry. Tests persistence only. No new stock entry; bid reference $218.33; $226/$210.50 exits valid today only, thereafter liquidate at evaluation endpoint bid. Maximum retained capital loss $12008.15. No trade costs at initialization.
2. WIDER_GTC: Same 55 shares, GTC $226 target and $208 stop. Tests moneyheap wider-stop recommendation. No new entry; bid reference $218.33; full value at risk, stop gap/slippage explicitly possible. Same endpoint. Chosen $210.50 stop avoids $137.50 additional nominal downside versus $208.

## Execution
Pending protective order only; no new shares and no assumed fill.

## Reviewer updates

### Pre-handoff execution
Protective order accepted; study active at acceptance, no stock fill.
{
  "id": "41aef279-077e-4007-afb3-6d7636b82bf4",
  "client_order_id": "alpaca-stage2-20260910-NVDA-oco",
  "created_at": "2026-09-10T16:17:18.505921123Z",
  "updated_at": "2026-09-10T16:17:18.511234804Z",
  "submitted_at": "2026-09-10T16:17:18.510165463Z",
  "filled_at": null,
  "expired_at": null,
  "canceled_at": null,
  "failed_at": null,
  "replaced_at": null,
  "replaced_by": null,
  "replaces": null,
  "asset_id": "4ce9353c-66d1-46c2-898f-fce867ab0247",
  "symbol": "NVDA",
  "asset_class": "us_equity",
  "notional": null,
  "qty": "55",
  "filled_qty": "0",
  "filled_avg_price": null,
  "order_class": "oco",
  "order_type": "limit",
  "type": "limit",
  "side": "sell",
  "position_intent": "sell_to_close",
  "time_in_force": "gtc",
  "limit_price": "226",
  "stop_price": null,
  "status": "new",
  "extended_hours": false,
  "legs": [
    {
      "id": "8dc0aeb9-ed37-4e36-918f-c7297d998ede",
      "client_order_id": "8c473bf6-fcba-4235-9ae6-50a5c736a8a4",
      "created_at": "2026-09-10T16:17:18.505921123Z",
      "updated_at": "2026-09-10T16:17:18.506845199Z",
      "submitted_at": "2026-09-10T16:17:18.505921123Z",
      "filled_at": null,
      "expired_at": null,
      "canceled_at": null,
      "failed_at": null,
      "replaced_at": null,
      "replaced_by": null,
      "replaces": null,
      "asset_id": "4ce9353c-66d1-46c2-898f-fce867ab0247",
      "symbol": "NVDA",
      "asset_class": "us_equity",
      "notional": null,
      "qty": "55",
      "filled_qty": "0",
      "filled_avg_price": null,
      "order_class": "oco",
      "order_type": "stop",
      "type": "stop",
      "side": "sell",
      "position_intent": "sell_to_close",
      "time_in_force": "gtc",
      "limit_price": null,
      "stop_price": "210.5",
      "status": "held",
      "extended_hours": false,
      "legs": null,
      "trail_percent": null,
      "trail_price": null,
      "hwm": null,
      "subtag": null,
      "source": null,
      "expires_at": "2026-12-09T21:00:00Z"
    }
  ],
  "trail_percent": null,
  "trail_price": null,
  "hwm": null,
  "subtag": null,
  "source": null,
  "expires_at": "2026-12-09T21:00:00Z"
}

### Reviewer activation and broker reconciliation

- Reviewer status: `ACTIVE`; evaluation starts at confirmed OCO acceptance and ends at the predeclared `2026-09-11T15:45:00-04:00` endpoint.
- Paper endpoint confirmed: `https://paper-api.alpaca.markets/v2`, with `ALPACA_PAPER_TRADE=true`.
- Broker OCO `41aef279-077e-4007-afb3-6d7636b82bf4` is `new`, GTC, for 55 NVDA shares with target `$226.00`; its held stop leg is GTC at `$210.50`. No leg has filled or been canceled.
- This is a protection-duration comparison only: no new NVDA shares were bought, and the entry fill belongs to the separate `alpaca-stage2-20260910-NVDA-buy` set.
- No checkpoint mark is recorded yet. Next checkpoint: next regular-session close.

## 2026-09-10 close checkpoint

- Observed at `2026-09-10T20:00:00Z` from the Alpaca IEX official 1Day bar: NVDA close `$218.37`; the after-close quote had no ask and a `$209.47` bid, so the bar is a disclosed non-executable proxy.
- The selected GTC OCO path is marked at `$12,010.35` for 55 shares, `+$2.20` versus the `$12,008.15` reference mark at acceptance. `KEEP_DAY` has the same marked value at this checkpoint but its DAY protection expired at the close; `WIDER_GTC` also has the same value, with a wider `$208.00` stop. No target or stop triggered, so the evidence currently distinguishes protection persistence and stop width, not P/L.
- The study remains active through the predeclared `2026-09-11T15:45:00-04:00` endpoint. Next checkpoint: 2026-09-11 endpoint.

## 2026-09-11 endpoint

- The exact endpoint was `2026-09-11T19:45:00Z` (15:45 ET). Alpaca IEX 1-minute bar close `$218.80` is used as a disclosed non-executable proxy.
- The selected GTC OCO path is marked at `$12,034.00`, or `+$25.85` versus the `$12,008.15` acceptance reference. `KEEP_DAY` and `WIDER_GTC` have the same marked value at this endpoint; no target or stop triggered before the endpoint, so the evidence distinguishes protection persistence and stop width but not P/L.
- Comparison complete with partial endpoint data; no lesson change. Later broker activity after this endpoint does not alter the predeclared comparison window.
