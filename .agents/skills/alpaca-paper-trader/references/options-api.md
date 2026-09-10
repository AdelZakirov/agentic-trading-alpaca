# Options research

For options research, use the Alpaca Option Chain API:

```text
GET https://data.alpaca.markets/v1beta1/options/snapshots/{UNDERLYING}?feed=indicative
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

For an advanced bearish candidate, the long-only stock restriction is a reason
to investigate options, not a reason to reject the ticker. Begin with a focused
put chain around the thesis horizon and relevant price levels. Compare at least
a long put with a put debit spread when both are available and plausible; assess
maximum loss, breakeven, payoff cap, implied volatility, theta, liquidity, and
executable spread. Other supported bearish structures remain eligible when their
full payoff and assignment or exercise risks fit the current risk posture.

Before recording no bearish option trade, state either the examined expiration
and strike area or the concrete condition that made a chain request pointless,
such as no listed contracts, insufficient account permission, an invalid thesis,
or clearly unusable liquidity. `Stock is long only` is not such a condition.

Use the Alpaca credentials from `.env`. Explicitly set `feed=indicative` for
option-data requests in this paper-trading skill. The API value is `indicative`
(not `inductive` or the stock feed `iex`). Do not request `opra` unless the user
explicitly asks to change the feed.

Parse snapshot prices from `latestQuote.bp` / `latestQuote.ap`, displayed sizes
from `latestQuote.bs` / `latestQuote.as`, quote time from `latestQuote.t`, and
last trade price from `latestTrade.p`. Do not use `bidPrice`, `askPrice`, or
`latestTrade.price` for this response schema. Greeks are under `greeks` and IV
under `impliedVolatility`; missing values mean unavailable, not zero.

Indicative quotes support paper-trading analysis and order evaluation. Label
prices and derived debit, breakeven, maximum loss and payoff as indicative
estimates, not firm OPRA quotes or guaranteed fills. Use the long-leg ask and
short-leg bid for conservative comparisons; inspect timestamps, sizes, zero or
crossed quotes and spread width. Refresh selected contracts before a bounded
limit order and confirm execution from Alpaca order status.

An OPRA `403` such as `OPRA agreement is not signed` is a data-feed access error,
not proof that option trading is disabled or contracts have no quotes. If it
appears from an older request, correct the request to `feed=indicative` and
inspect that response before declaring a data blocker. Check trading permission
separately on the account. Do not stop option analysis merely because OPRA is
unavailable, or present indicative data as live consolidated market prices.

Option orders use the normal Alpaca order endpoint:

```text
POST ${ALPACA_ENDPOINT}/orders
```

Use the option contract symbol for a single-leg order. For a multi-leg order,
follow Alpaca's current `mleg` order format. Check the account's option trading
level, buying power, current positions, and fresh quotes before submitting.
