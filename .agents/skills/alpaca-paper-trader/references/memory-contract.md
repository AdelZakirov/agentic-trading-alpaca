# Memory contract

Memory lives in `memory/`. Alpaca is always the source of truth for live account state.

## Read

At each run, read:

1. `memory/portfolio-state.md` completely.
2. `memory/lessons.md` completely.
3. Today's `memory/logs/YYYY-MM-DD-summary.md` when present. Using a targeted search or tail, confirm its `Covers full log through` value matches the latest `run-checkpoint` marker in `memory/logs/YYYY-MM-DD.md` and that no nonblank log content follows that marker. Do not load the full log merely to perform this check.
4. If today's summary is absent, its checkpoint does not match, or content follows the latest marker, read the uncaptured tail or necessary sections of the full daily log and repair the summary. Read the complete full log only when targeted recovery cannot establish the current decision state.
5. Read the latest earlier dated summary linked from `portfolio-state.md` only to answer a current decision question not resolved by current portfolio/ticker state and today's summary. Read its full log only for material details absent from that summary.
6. `memory/positions/README.md`.
7. The ticker file for each live position, open order or proposed trade. Read other ticker files only for a specific current decision question.
8. Only the latest research files linked from those ticker files when relevant to the current decision.

Trading agents do not read the ghost index or ghost histories. Read active lessons as priors; open one lesson's evidence only if a specific contradiction requires it.

Do not load every old log.

## Write

Persist a successful moneyheap response immediately under [moneyheap-api.md](moneyheap-api.md). After final Alpaca reconciliation:

1. Append the detailed run to today's Europe/Amsterdam full log, without a checkpoint marker yet.
2. Update relevant ticker files and portfolio-state.md with actual decisions, order IDs and confirmed fills, including reductions, closes and rolls. Append known execution facts to new ghost files owned by this run before handoff; never edit previously handed-off ghost files.
3. Append `<!-- run-checkpoint: ISO-8601 Europe/Amsterdam timestamp -->` at the end of the full log and rewrite today's summary with `Covers full log through` and the identical timestamp.
4. Publish only after persistence succeeds:
   `python3 -m alpaca_agent.ghost_queue finish --run-id RUN_ID --log memory/logs/YYYY-MM-DD.md --summary memory/logs/YYYY-MM-DD-summary.md`
   Repeat `--ghost-file memory/ghost-trades/YYYY-MM-DD/DECISION_ID.md` for every new definition file, including unfilled/unsubmitted decisions. Omit it if none were created. The helper validates checkpoints and copies immutable trading inputs and attached definitions for the reviewer. Successful finish transfers file ownership to the reviewer. A later trading cycle can proceed without modifying those inputs. If a cycle fails, retain the active marker until actual broker state and any partial writes are reconciled; never publish incomplete work as complete. Use `abort --run-id RUN_ID` only after reconciliation, recording the failure and arranging a recovery handoff in the next completed cycle.

If Alpaca state is incomplete or unreliable, keep the previous portfolio snapshot and record the failure in today's log.

## Portfolio state

Keep `portfolio-state.md` short. Include:

- generation time and last completed run;
- shortlist path and date;
- equity, cash, market value, return, position count, and open-order count;
- current positions and open orders;
- stock/option plans for current positions and open orders, plus actionable watch conditions with a concrete next trigger; keep rejected candidates and other completed screening decisions in the daily log;
- latest published trading handoff ID;
- risk posture, constraints, breaches, main risks, and reassessment triggers;
- links to the latest dated summary, full log, and relevant ticker files;
- errors or reconciliation warnings.

## Daily log

Append every run to `memory/logs/YYYY-MM-DD.md`. Record the timestamp, market status, shortlist date, pre-action Alpaca state, risk posture, stock and option decisions, applicable lessons, moneyheap research used, submitted or blocked orders, short decisions and links to newly created ghost files (no duplicated alternative definitions), handoff status, post-action state, errors, and summary.

Record the investment decision separately from execution. For BUY or SELL, record whether it was submitted, not submitted, or blocked and why.

## Compact daily summary

Rewrite `memory/logs/YYYY-MM-DD-summary.md` after every completed run. It is the normal entry point for today's history; `YYYY-MM-DD.md` remains the append-only audit record.

Start the summary with its update time, an exact `Covers full log through` checkpoint matching the latest full-log `run-checkpoint`, and a link to the full log. Keep it current-state oriented and aim for at most 6,000 characters; exceed that only to preserve unresolved risk or execution facts.

Include only decision-relevant context not already obvious from `portfolio-state.md`:

- material actions and thesis changes today;
- unresolved orders, conditional decisions, blockers, and exact next triggers;
- research conclusions still relevant to current positions or near-term candidates;
- handoff status, material errors, and reconciliation warnings;
- links to the detailed log, ticker memory, research, or ghost files when detail may be needed.

Do not reproduce the full chronology, complete research, quote sequences, ghost definitions, or portfolio tables. Replace superseded facts rather than accumulating them. The summary is a cache, not a source of truth: Alpaca, the full log, ticker files, and research artifacts win on disagreement.

## moneyheap research

Before new moneyheap research, read [moneyheap-api.md](moneyheap-api.md). It defines request handling, artifact paths, exact-response persistence, and retry rules. Link saved research from today's log and from the ticker file when relevant; do not copy the full response into other memory files.

## Ghost trades and lessons: ownership

Before a real order, create the original definition file under ghost-pretrade.md, with timestamps and contemporaneous quotes. The daily log contains only a short decision and link. Add known client/broker IDs and confirmed fills to the new file before attaching it to ghost_queue finish. Preserve files even when unfilled.

After successful handoff, the reviewer exclusively owns those files, the active index/archive, completed reviews, and updates to memory/lessons.md. The trader records subsequent execution events in trading memory for the next handoff. It never opens old ghost histories routinely or edits handed-off files. The reviewer follows ghost-review.md, ghost-lifecycle.md and lessons-learned.md and never edits trading logs, portfolio state or position files. Publish lessons atomically; trading agents read lessons but do not edit them.

## Ticker memory

Use `memory/positions/{TICKER}.md` only for the latest dated state and plan: exposure, active orders/contracts, thesis, stock/option decision, targets, invalidation, review/expiry dates, risks and current evidence links. Replace superseded content; never prepend competing “current” blocks. Aim for 3,000 characters, preserving unresolved execution facts when more is necessary.

Append material plan/execution changes to `memory/positions/history/{TICKER}.jsonl`: one object per line with `event_at`, `run_id`, `event_id`, `change`, `reason`, `sources`. Use a stable event_id to avoid duplicate retries; save history before atomically replacing the current file. No event for unchanged HOLD and no copied daily logs. Legacy history is split into dated legacy_event rows; date-only values have day precision, unknown run IDs/reasons remain null. Exact originals and undated context are in history/legacy/{TICKER}.jsonl for exceptional audits; resolve old links against source_base. Multiple records on one date need not be independent decisions.

Read current files routinely. For a historical question, parse JSONL with Python and select event_at dates/title/change keywords before printing; do not dump the whole file or legacy archive. Alpaca wins on state conflicts; record the correction as an event. Mark closed positions CLOSED; do not create files for routine unowned HOLD. Keep positions/README.md as links; portfolio-state.md holds the portfolio summary.

Never store secrets in memory.
