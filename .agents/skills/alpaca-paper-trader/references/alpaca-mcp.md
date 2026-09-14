# Alpaca paper MCP

Server: `alpaca_paper`; official alpaca-mcp-server 2.3.1, project .env, exact paper endpoint checked by launcher. Account must reconcile successfully before trading. Use actual exposed schemas, not parameter names from the old connector.

- State: get_clock, get_account_info, get_all_positions/get_open_position, get_orders (`status=open`, `nested=true`). Follow pagination when needed; retain held protective legs.
- Evidence: get_account_activities, get_asset, get_option_contracts/get_option_contract; get_stock_latest_quote (`symbols`, explicit feed), get_stock_bars/quotes.
- Options: get_option_chain (`underlying_symbol`, `type`, expiration/strike filters, `feed=indicative`), get_option_snapshot/latest_quote. Inspect next_page_token; do not confuse a limited page with the full requested set.
- Execution: place_stock_order, place_option_order; get_order_by_client_id before submission, get_order_by_id afterward; replace_order_by_id/cancel_order_by_id for explicit management decisions. Follow order-execution.md and options-api.md unchanged. Set order type explicitly: server default may be market. Stable client IDs and reconciliation are mandatory; never blindly retry a timeout.

Results wrap API payloads in `data` (sometimes JSON text); list responses may be under `data.result`. Inspect isError and payload error/status fields; a successful tool call does not prove a successful order. Retain broker IDs, status, fills and leg details. Print selected fields once; save large raw results to files. Never print credentials. Ghost reviewers use only read tools.

## Compact responses

In functions.exec, keep the original result in `store` (or persist it locally when needed), decode one representation, then print selected fields. Do not print both content and structuredContent or stringify a bundle of raw MCP results. Never repeat a broker call merely to reformat its response.

```javascript
function payload(r) {
  const parse = x => typeof x === 'string' ? JSON.parse(x) : x;
  let d = r.structuredContent;
  if (d == null) d = parse((r.content ?? []).filter(x => x.type === 'text').map(x => x.text).join('\n'));
  d = parse(d?.data ?? d);
  if (d && typeof d.text === 'string') d = parse(d.text);
  if (r.isError || d?.error || Number(d?.code) >= 400) throw new Error(JSON.stringify(d));
  return d?.result ?? d;
}
// Save before decoding: errors or formatting failures must not trigger resubmission.
const r = await tools.mcp__alpaca_paper__get_account_info({});
store('account_raw', r);
const a = payload(r);
text(Object.fromEntries(['status','trading_blocked','account_blocked','equity','cash','buying_power','options_buying_power','options_trading_level'].map(k => [k, a[k] ?? null])));
```

Select fields for the decision; unknown values remain null. Keep error details visible; unexpected/non-JSON shapes require inspecting the saved response, not interpreting them as empty data.

- Positions: symbol, asset_class, side, qty, qty_available, avg_entry_price, market_value, unrealized_pl.
- Orders: id, client_order_id, symbol, side, status, qty, filled_qty, filled_avg_price, type, order_class, time_in_force, limit_price, stop_price, submitted_at, filled_at, replaces/replaced_by; recursively include legs and their protection/fill state. Do not omit held stops.
- Quotes: symbol, bid/ask, displayed sizes, timestamp and requested feed; option candidates also need IV/Greeks. Contracts: symbol, expiry, strike, type, status, tradable. Keep counts and pagination tokens.

Discover exact tool names first; print only names for inventory. Load one tool's description/schema when needed, never the full ALL_TOOLS metadata list. These display limits do not reduce required preflight or post-order reconciliation.

The retained project CLI is not the agent's Alpaca transport. If this server is absent from a running task, restart in this project to load its configuration; report blocked rather than bypassing it.
