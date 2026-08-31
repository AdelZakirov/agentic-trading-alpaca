# Memory contract

Memory lives in `memory/`. Alpaca is always the source of truth for live account state.

## Read

At each run, read:

1. `memory/portfolio-state.md` completely.
2. `memory/lessons.md` completely.
3. Today's `memory/logs/YYYY-MM-DD.md` when present.
4. The latest earlier log linked from `portfolio-state.md` only when needed.
5. `memory/positions/README.md`.
6. The ticker file for each live position, open order, proposed trade, active ghost set, or material earlier decision.
7. Each active ghost file and any completed ghost file needed for an evaluation or lesson under review.
8. Only the latest research files linked from those ticker files when they are relevant to the current decision.

Do not load every old log.

## Write

Capture each moneyheap JSON response as soon as the first successful request returns. Keep that response object in memory and render and save it into the required Markdown research artifact. If rendering or persistence fails, retry only the local render or write from the captured response; never repeat the successful API call merely to recreate the file. After final Alpaca reconciliation:

1. Append the run to today's Europe/Amsterdam log.
2. Create or update relevant ghost files, including any completed evaluations.
3. Update `memory/lessons.md` when a completed evaluation provides generalizable evidence.
4. Update relevant `memory/positions/{TICKER}.md` files.
5. Rewrite `memory/portfolio-state.md`.

If Alpaca state is incomplete or unreliable, keep the previous portfolio snapshot and record the failure in today's log.

## Portfolio state

Keep `portfolio-state.md` short. Include:

- generation time and last completed run;
- shortlist path and date;
- equity, cash, market value, return, position count, and open-order count;
- current positions and open orders;
- latest stock decision and option decision for each reviewed ticker;
- active ghost-set count and any evaluations due before the next run;
- risk posture, constraints, breaches, main risks, and reassessment triggers;
- links to the latest log and relevant ticker files;
- errors or reconciliation warnings.

## Daily log

Append every run to `memory/logs/YYYY-MM-DD.md`. Record the timestamp, market status, shortlist date, pre-action Alpaca state, risk posture, stock and option decisions, applicable lessons, moneyheap research used, submitted or blocked orders, pre-execution ghost definitions for submitted orders, ghost sets created or updated, completed evaluations, lessons changed, post-action state, errors, and summary.

Record the investment decision separately from execution. For BUY or SELL, record whether it was submitted, not submitted, or blocked and why.

## moneyheap research

Save each new complete response to:

`memory/research/YYYY-MM-DD/HHMMSS-{TICKER}-{fundamental|technical}.md`

Use Europe/Amsterdam time. The Markdown file must include the request time, ticker, analysis type, endpoint, exact prompt and previous context, response model when present, and the complete returned analysis without shortening it. It must contain that analysis exactly once under one rendered analysis section; do not also paste the raw response object into the Markdown file. The exact parsed response object belongs in a sibling file with the same stem and a `.json` suffix.

The source for both artifacts must be the complete JSON object captured from the first successful API call, including any additional fields the service returns. Use that same in-memory object for reasoning and for rendering the Markdown file. Do not reconstruct it or obtain it with another request. If rendering or saving fails, retain the captured response and retry only the local render or file write. A new API request is allowed only after a request failure where no valid response object was captured, subject to the moneyheap API retry rules.

Link the file from today's log. Also link it from the ticker file when it affects an open position, proposed trade, or future review. Do not copy the full response into the daily log, ticker file, or portfolio state.

## Ghost trades

Store each ghost set at:

`memory/ghost-trades/YYYY-MM-DD/{REAL_CLIENT_ORDER_ID}.md`

The date is the real trade's first fill date. Follow `ghost-trades.md` for creation, pricing, checkpoints, completion, and comparison. Link the ghost file from the daily log and ticker file; keep only its status and next evaluation date in portfolio state.

Ghost trades never appear as Alpaca positions or orders and never affect portfolio totals, exposure, buying power, or risk-limit calculations.

## Lessons

Keep durable learned principles in `memory/lessons.md` using `lessons-learned.md`. Read the whole file before making decisions. Keep case detail in ghost files and daily logs rather than expanding the lesson text.

## Ticker memory

Use `memory/positions/{TICKER}.md` for stock and option positions, open orders, and material decisions. Keep current Alpaca state, option contract symbols, the holding and expiration plan, key ticker risks, relevant research and ghost links, review triggers, and append-only dated history.

When a ticker file disagrees with Alpaca, Alpaca wins. Append a reconciliation note to the ticker file and daily log. Mark closed positions `CLOSED`. Do not create a file for a routine unowned HOLD.

Never store secrets in memory.
