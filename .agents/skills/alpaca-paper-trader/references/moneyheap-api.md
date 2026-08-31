# moneyheap Analysis API

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
- A successful moneyheap response is JSON. Use `python3 -m alpaca_agent.moneyheap` with one JSON request object on stdin so the code that receives the response also persists it. The helper writes the exact parsed response to a sibling `.json` artifact and one rendered Markdown artifact. If the file write or formatting step fails, it retries only local persistence from the captured in-memory response; never call moneyheap again to reconstruct, save, re-read, or reformat an already successful result. A new API request is permitted only after no valid response object was captured and the endpoint-specific retry rules allow it.

## Response

```json
{
  "ticker": "AAPL",
  "analysis_type": "fundamental", #or "technical"
  "analysis": "..."
}
```

`analysis` may be JSON or formatted text. Treat it as evidence, not as an order instruction.

Save every successful response immediately using the Markdown and sibling-JSON research-file rules in `memory-contract.md`. Retain the already-returned JSON object in memory, use that same object for reasoning, and render the Markdown artifact directly from it while preserving all returned fields in the JSON sidecar. Keep the exact request prompt and previous context alongside it so later runs can understand what was asked and answered. If rendering or writing the Markdown file fails, retry only that local operation from the retained response; do not call moneyheap again.

- HTTP 502: analyst failure; decide whether the remaining evidence is enough. Do not retry repeatedly.
