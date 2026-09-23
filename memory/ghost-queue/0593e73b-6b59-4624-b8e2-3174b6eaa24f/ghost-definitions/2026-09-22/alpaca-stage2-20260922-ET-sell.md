# ET early invalidation alternatives

## Identity
- decision_id: alpaca-stage2-20260922-ET-sell
- creator_run_id: 0593e73b-6b59-4624-b8e2-3174b6eaa24f
- decision_at: 2026-09-22T21:16:20+02:00
- ticker: ET
- status: WAITING_FOR_FILL
- client_order_id: alpaca-stage2-20260922-ET-sell
- broker_order_id: null

## Original decision
Owned 400 ET at20.95 after three confirmed fills at15:48:00–02Z. The predeclared intraday tactical exit20.55 is now broken: live IEX19:16:19Z bid20.54 size2800, ask20.55 size6400; delayed SIP19:01Z20.54/20.55 and trade20.545. Close all400 with DAY sell limit20.54, regular session open and liquid spread0.01. If not filled promptly, reassess urgency and price. Planned gross loss164 at20.54 versus baseline20.95. Do not re-enter automatically. No standing ET exit order exists. Portfolio position12 stocks prior to exit; no option positions.

## Evaluation rules
Compare actual gross execution and post-exit ET mid/close next1 and5 trading days, through2026-09-29. Simulate alternative fills conservatively: sell at observable bid and buy at ask. If no reliable quote or bar at endpoint, mark unscorable. ETF distributions not included. Subsequent market movement is not a retroactive entry/exit rationale.

## Initial evidence
Broker filled BUY400 ET avg20.95 at15:48:02Z, order7c2a4d36-e8ee-482c-b2f9-f1e599a65a1c. No open orders; broker cash34313.43, equity103285.22. IEX19:16:19Z20.54/20.55, displayed2800/6400. Delayed SIP19:01Z20.54/20.55. Market open15:16ET, closes16:00ET. Initial response to stop breach is bounded risk-reducing sell.

## Alternatives
1. HOLD_TO_CLOSE: no sell now; keep400 until regular session close, then sell at contemporaneous bid if available. Entry price20.95, current mark20.54; incremental loss can grow; max unlevered loss remaining~8216. Observation window through today's close, then next1/5day checkpoints.
2. HALF_EXIT: sell200 now at contemporaneous bid20.54, retain200 to close; no hypothetical fill claim until quote/fill validation. Planned immediate gross loss82 on half; remaining exposure~4108 at current mark, maximum residual loss4108 before any further exit.
3. STOP_LIMIT_20_50: sell400 stop20.55 limit20.50 GTC, preserving price floor but risking nonfill below20.50; hypothetical activation now, fill only if executable bid>=20.50. Max unlevered loss8380 if no fill and stock goes to zero.

## Execution
No sell submitted at definition time; fill/ID null. Reviewer update reserved.

## Execution facts before handoff
- SELL400 ET DAY limit20.54, client alpaca-stage2-20260922-ET-sell, broker3124202f-fd96-4196-a455-4c794b9b8d73, filled400 at20.55 on2026-09-22T19:16:55.558216496Z. Gross loss -160 against20.95 entry. Subsequent broker positions show0 ET,0 open orders.
