# moneyheap analysis API

Use moneyheap when additional research would help a trading decision. Do not call it automatically for every ticker.

## Naming

In prose and memory, call the service `moneyheap` or `moneyheap.ai`. Never capitalize it.

Base URL: `${MONEYHEAP_API_URL}`

## Endpoints

`POST /v1/analysis/fundamental`

Company fundamentals, financial health, valuation, analyst opinions, news, catalysts, and risks.

`POST /v1/analysis/technical`

Trend, momentum, market regime, timing, support and resistance, volume, and invalidation levels.

## Request

```json
{
  "ticker": "AAPL",
  "prompt": "Your specific research question",
  "previous_context": null
}
```

`prompt` and `previous_context` are optional. Use `previous_context` for a follow-up because the API does not remember earlier calls.

## Request execution

- Never send moneyheap requests in parallel. Keep at most one request in flight, wait for it to succeed or fail, and save a successful response before starting the next request. Serial execution protects service capacity and makes failures attributable to one payload.
- Prefer an HTTP client with a JSON parameter, such as Python `requests.post(url, json=payload)`. Use the client's JSON encoder; do not manually construct or shell-escape JSON request bodies.
- Technical analysis can legitimately take longer than 180 seconds. Never use 180 seconds as the hard read timeout for `/v1/analysis/technical`; use a longer bounded read timeout appropriate for an unattended run and keep waiting while the request remains healthy.
- Prompts may contain apostrophes, quotation marks, newlines, and other special characters. They must remain ordinary string values in the in-memory payload.
- A valid request body has a `ticker`, an optional `prompt`, and an optional `previous_context`. Do not add unsupported fields.
- Invoke the repository helper with the request object on stdin, for example:

  ```bash
  python3 -m alpaca_agent.moneyheap --timeout 360 <<'JSON'
  {"ticker":"AAPL","analysis_type":"fundamental","prompt":"Your specific research question","previous_context":null}
  JSON
  ```

  The request heredoc contains request data only; the returned analysis is handled and written by the helper.
- Always inspect the response status and response body on errors.
- HTTP 422 means the request body is invalid. Read the validation body, correct the payload, and never retry the same request unchanged.
- Do not use curl `--fail` while diagnosing because it hides the API's validation response body. If curl is unavoidable for a read-only diagnostic, preserve and inspect both the status and body; do not manually shell-escape a trading-research payload.
- A successful moneyheap response is JSON. The helper that receives it also persists it. If formatting or writing fails, retry only local persistence from the captured response. Never call moneyheap again to reconstruct, save, re-read, or reformat a valid result. A new API request is permitted only when no valid response object was captured and the endpoint-specific retry rules allow it.

## Response

```json
{
  "ticker": "AAPL",
  "analysis_type": "fundamental", #or "technical"
  "analysis": "..."
}
```

`analysis` may be JSON or formatted text. Treat it as evidence, not as an order instruction.

## Persistence

Save every successful response immediately using Europe/Amsterdam time:

`memory/research/YYYY-MM-DD/HHMMSS-{TICKER}-{fundamental|technical}.{md,json}`

The sibling `.json` is the exact complete parsed object from the first valid response, including extra fields. Use that same captured object for reasoning and for rendering Markdown; never reconstruct or refetch it.

The Markdown artifact must include request time, ticker, analysis type, endpoint, exact prompt and previous context, response model when present, and the complete analysis without shortening it. Render the analysis exactly once; do not duplicate the raw response object.

Link the Markdown from today's log and from ticker memory when it affects a position, proposed trade, or future review. Do not copy the full response into the daily log, ticker file, or portfolio state.

- HTTP 502: analyst failure; decide whether the remaining evidence is enough. Do not retry repeatedly.
