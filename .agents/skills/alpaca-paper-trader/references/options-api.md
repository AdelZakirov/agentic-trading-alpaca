# Options research

For options research, use the Alpaca Option Chain API:

```text
GET https://data.alpaca.markets/v1beta1/options/snapshots/{UNDERLYING}
```

Pass the underlying ticker in the path. When useful, filter by:

- `type=call|put`
- `strike_price_gte` and `strike_price_lte`
- `expiration_date_gte` and `expiration_date_lte`
- `limit` and `page_token`

The response can include the latest bid and ask, latest trade, implied
volatility, and delta, gamma, theta, vega, and rho for each contract.

Do not request the full chain unless it is truly needed. First choose a useful
expiration and strike range from the trade idea.

Research the option space iteratively. Start with a focused part of the chain,
inspect the results, then adjust the expiration, strikes, option type, or other
assumptions and query again when that would help. Refresh the final candidates
before trading. One API call does not have to lead directly to a decision.

Use the Alpaca credentials from `.env`. The option feed is `opra` or
`indicative`, not the stock `iex` feed. Missing Greeks or implied volatility
mean that the value is unavailable, not zero.

Option orders use the normal Alpaca order endpoint:

```text
POST ${ALPACA_ENDPOINT}/orders
```

Use the option contract symbol for a single-leg order. For a multi-leg order,
follow Alpaca's current `mleg` order format. Check the account's option trading
level, buying power, current positions, and fresh quotes before submitting.
