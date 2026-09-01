# Order execution

Read this reference before submitting, replacing, or cancelling any Alpaca order, or before deciding whether an existing risk-increasing order may remain open.

## Preflight

Immediately before an order action:

1. Read the market clock. Require the regular market to be open for submission or replacement. A risk-reducing cancellation may proceed outside regular hours when Alpaca accepts it.
2. Re-read the account, relevant position, cash, and open orders.
3. For a new order, get a fresh quote with positive bid and ask. Apply stock quote validation below when a stock quote is temporarily unusable. For options, confirm each contract is active and tradable.
4. Confirm the action still fits the thesis and current risk posture.
5. Confirm it fits available cash, buying power, owned quantities, and the risk posture.

If a required check fails, retain the investment decision but do not submit the order. Record the exact blocker.

## Stock quote validation

- One wide or abnormal stock quote is not a final execution blocker when the thesis remains valid and the symbol is normally liquid.
- Collect two additional fresh quotes over the next two to five minutes. Record every timestamp, bid, ask, displayed size, and spread; judge persistence from the sequence and never cherry-pick the most favorable observation.
- Stop early only for a concrete reason such as a persistent zero or crossed market, stale feed, halted or non-tradable asset, regular-session end, or a price move that invalidates the thesis or exceeds the entry bound.
- If the sequence supports a bounded limit inside the thesis entry range and slippage allowance, the trade remains executable even when a market order would be unsafe. Otherwise record the sequence and exact blocker.

## Stock orders

Use a limit order by default for entries and ordinary non-urgent exits, with `time_in_force=day` and `extended_hours=false`. Set the limit from the latest quote, thesis bound, and a pre-stated maximum slippage allowance. Never exceed the thesis-consistent entry or exit bound merely to obtain a fill.

After submission, poll order status and the current quote during a short bounded window. If it remains open and the thesis holds, one replacement at a newly justified limit is eligible after re-reading the order, account, position, and quote. Never blindly chase price. Reconcile both original and replacement order IDs because a replacement response does not prove the original was replaced before a fill.

If the order remains unfilled, retain the investment decision, report the exact open or terminal broker status, and let the pre-close management cycle decide whether it may remain open.

A stock market order is exceptional: use it only for an urgent risk-reducing exit when delay creates more risk than bounded slippage, the market is sufficiently liquid, and the rationale is recorded before submission. Never use it merely to force an entry fill.

## Options and idempotency

Before an option order, read [options-api.md](options-api.md) completely and choose an order type suited to the structure and current spread.

Use client ID `alpaca-stage2-YYYYMMDD-{symbol}-{side}` and check for it before submitting. If submission, replacement, or cancellation is uncertain, reconcile by client ID and broker order ID; never retry blindly.

After any submission or mutation, read the order again and refresh the account and positions. Report broker status exactly. Only `filled` means filled.

## Alpaca endpoints

Use credentials from `.env` as `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` headers.

- `GET ${ALPACA_ENDPOINT}/orders/{order_id}`
- `GET ${ALPACA_ENDPOINT}/orders:by_client_order_id?client_order_id=...`
- `POST ${ALPACA_ENDPOINT}/orders`
- `PATCH ${ALPACA_ENDPOINT}/orders/{order_id}`
- `DELETE ${ALPACA_ENDPOINT}/orders/{order_id}`
