# Alpaca paper MCP

Server: `alpaca_paper`; official alpaca-mcp-server 2.3.1, project .env, exact paper endpoint checked by launcher. Account must reconcile successfully before trading. Use actual exposed schemas, not parameter names from the old connector.

- State: get_clock, get_account_info, get_all_positions/get_open_position, get_orders (`status=open`, `nested=true`). Follow pagination when needed; retain held protective legs.
- Evidence: get_account_activities, get_asset, get_option_contracts/get_option_contract; get_stock_latest_quote (`symbols`, explicit feed), get_stock_bars/quotes.
- Options: get_option_chain (`underlying_symbol`, `type`, expiration/strike filters, `feed=indicative`), get_option_snapshot/latest_quote. Inspect next_page_token; do not confuse a limited page with the full requested set.
- Execution: place_stock_order, place_option_order; get_order_by_client_id before submission, get_order_by_id afterward; replace_order_by_id/cancel_order_by_id for explicit management decisions. Follow order-execution.md and options-api.md unchanged. Set order type explicitly: server default may be market. Stable client IDs and reconciliation are mandatory; never blindly retry a timeout.

Results wrap API payloads in `data` (sometimes JSON text); list responses may be under `data.result`. Inspect isError and payload error/status fields; a successful tool call does not prove a successful order. Retain broker IDs, status, fills and leg details. Print selected fields once; save large raw results to files. Never print credentials. Ghost reviewers use only read tools.

The retained project CLI is not the agent's Alpaca transport. If this server is absent from a running task, restart in this project to load its configuration; report blocked rather than bypassing it.
