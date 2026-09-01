# Memory contract

Memory lives in `memory/`. Alpaca is always the source of truth for live account state.

## Read

At each run, read:

1. `memory/portfolio-state.md` completely.
2. `memory/lessons.md` completely.
3. Today's `memory/logs/YYYY-MM-DD-summary.md` when present. Using a targeted search or tail, confirm its `Covers full log through` value matches the latest `run-checkpoint` marker in `memory/logs/YYYY-MM-DD.md` and that no nonblank log content follows that marker. Do not load the full log merely to perform this check.
4. If today's summary is absent, its checkpoint does not match, or content follows the latest marker, read the uncaptured tail or necessary sections of the full daily log and repair the summary. Read the complete full log only when targeted recovery cannot establish the current decision state.
5. Prefer the latest earlier dated summary linked from `portfolio-state.md`; read its full log only when details omitted from the summary are material to the current decision.
6. `memory/positions/README.md`.
7. The ticker file for each live position, open order, proposed trade, active ghost set, or material earlier decision.
8. `memory/ghost-trades/index.md` completely. Do not load every active ghost file.
9. Load an individual ghost file only when its indexed checkpoint is due or overdue, the real trade filled further or was reduced, closed, or rolled, an indexed objective ghost trigger may have activated, or its completion or lesson is under review.
10. Only the latest research files linked from those ticker files when they are relevant to the current decision.

Do not load every old log.

## Write

Persist a successful moneyheap response immediately under [moneyheap-api.md](moneyheap-api.md). After final Alpaca reconciliation:

1. Append the detailed run to today's Europe/Amsterdam full log, without a checkpoint marker yet.
2. Create or update relevant ghost files, including any completed evaluations.
3. Rewrite `memory/ghost-trades/index.md` after any ghost creation, update, completion, or real-path state change.
4. Update `memory/lessons.md` when a completed evaluation provides generalizable evidence.
5. Update relevant `memory/positions/{TICKER}.md` files.
6. Rewrite `memory/portfolio-state.md`.
7. Append `<!-- run-checkpoint: ISO-8601 Europe/Amsterdam timestamp -->` to the full log and rewrite today's dated summary with the identical checkpoint.

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
- links to the latest dated summary, full log, and relevant ticker files;
- errors or reconciliation warnings.

## Daily log

Append every run to `memory/logs/YYYY-MM-DD.md`. Record the timestamp, market status, shortlist date, pre-action Alpaca state, risk posture, stock and option decisions, applicable lessons, moneyheap research used, submitted or blocked orders, pre-execution ghost definitions for submitted orders, ghost sets created or updated, completed evaluations, lessons changed, post-action state, errors, and summary.

Record the investment decision separately from execution. For BUY or SELL, record whether it was submitted, not submitted, or blocked and why.

## Compact daily summary

Rewrite `memory/logs/YYYY-MM-DD-summary.md` after every completed run. It is the normal entry point for today's history; `YYYY-MM-DD.md` remains the append-only audit record.

Start the summary with its update time, an exact `Covers full log through` checkpoint matching the latest full-log `run-checkpoint`, and a link to the full log. Keep it current-state oriented and aim for at most 6,000 characters; exceed that only to preserve unresolved risk or execution facts.

Include only decision-relevant context not already obvious from `portfolio-state.md`:

- material actions and thesis changes today;
- unresolved orders, conditional decisions, blockers, and exact next triggers;
- research conclusions still relevant to current positions or near-term candidates;
- active ghost count, due evaluations, lesson changes, material errors, and reconciliation warnings;
- links to the detailed log, ticker memory, research, or ghost files when detail may be needed.

Do not reproduce the full chronology, complete research, quote sequences, ghost definitions, or portfolio tables. Replace superseded facts rather than accumulating them. The summary is a cache, not a source of truth: Alpaca, the full log, ticker files, and research artifacts win on disagreement.

## moneyheap research

Before new moneyheap research, read [moneyheap-api.md](moneyheap-api.md). It defines request handling, artifact paths, exact-response persistence, and retry rules. Link saved research from today's log and from the ticker file when relevant; do not copy the full response into other memory files.

## Ghost trades

Before a real order, follow [ghost-pretrade.md](ghost-pretrade.md). After an actual fill or when an indexed evaluation or trigger is due, follow [ghost-lifecycle.md](ghost-lifecycle.md).

Keep `memory/ghost-trades/index.md` as the compact routing source. One row per ghost set must include its file link, ticker, status, real-path state, evaluation end, last completed checkpoint, next checkpoint, any objective trigger that requires attention between checkpoints, and last update. Use `None outside checkpoints` when no separate trigger exists. The full ghost file remains authoritative for definitions, marks, and evaluations.

Link each created ghost file from the daily log and ticker file. Keep only the aggregate active count and evaluations due before the next run in portfolio state.

## Lessons

Read `memory/lessons.md` completely before making decisions. Before completing an evaluation or changing durable lessons, read [lessons-learned.md](lessons-learned.md). Keep case detail in ghost files and daily logs rather than expanding lesson text.

## Ticker memory

Use `memory/positions/{TICKER}.md` for stock and option positions, open orders, and material decisions. Keep current Alpaca state, option contract symbols, the holding and expiration plan, key ticker risks, relevant research and ghost links, review triggers, and append-only dated history.

When a ticker file disagrees with Alpaca, Alpaca wins. Append a reconciliation note to the ticker file and daily log. Mark closed positions `CLOSED`. Do not create a file for a routine unowned HOLD.

Never store secrets in memory.
