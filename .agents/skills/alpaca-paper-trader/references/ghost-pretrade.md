# Ghost alternatives before execution

Read this reference after selecting a real trade and before calling the order endpoint. Ghosts are counterfactual analysis records only; never submit them, reserve cash for them, or include them in portfolio risk.

Define two to four realistic alternatives that were genuinely considered. No only for chosen orders, but from the whole analysis in general. Create their definition file before submitting the real order; put only a short decision and file link in the daily log. Do not invent alternatives after observing later prices.

Each ghost should test one meaningful choice, such as:

- stock instead of options, or options instead of stock;
- a different option structure, strike, or expiration;
- a different position size;
- different entry timing with an objective trigger;
- no trade.

Prefer changing one decision at a time. Do not add random variants or several nearly identical contracts. Include no trade when the main question is whether exposure should be added at all.

For each alternative, record a stable label, question tested, rationale, instrument or no-trade choice, side, quantity or notional, option structure and contracts when applicable, entry rule, simulated entry price, maximum loss when knowable, exit or expiration handling, pricing assumptions, and missing data.

Use only data observable at the real decision. Price a hypothetical buy at the contemporaneous ask and a hypothetical sale at the bid unless a more realistic conservative fill is documented. Price multi-leg structures from the executable side of each leg. A no-trade ghost starts at zero P/L and zero capital at risk. If reliable data is unavailable, keep the question but mark the alternative `UNSCORABLE`; never manufacture a price.

Create the file even if the real order has not filled. Mark it `WAITING_FOR_FILL`; use `NOT_SUBMITTED` for an alternative decision with no submitted real order. Do not fabricate fills or start a fill-anchored comparison. The reviewer activates a filled comparison only after confirming execution. Unsubmitted studies need an explicitly predeclared observation window to be scoreable.

Those ghost trades eventually will be studied and reflected to derive valuable lessons.

## File and handoff contract

Create one new file at `memory/ghost-trades/YYYY-MM-DD/{DECISION_ID}.md`, using the decision date and a stable unique decision ID (prefer the intended client order ID). Never overwrite an existing decision file or rename it when a later fill occurs. The main trader does not read the old ghost index or histories to create a file.

Use these compact sections:

- Identity: decision_id, creator_run_id from ghost_queue begin, decision_at with timezone, ticker, status, client_order_id, broker_order_id (unknown values null).
- Original decision: thesis, chosen action, pre-trade exposure, size rationale, invalidation and holding period.
- Evaluation rules: common window/start trigger, checkpoints, end rule and exit handling, fixed before outcomes are known.
- Initial evidence: source and observation timestamp, underlying and relevant executable option quotes; missing data explicitly marked.
- Alternatives: the fields specified above, one entry per genuinely considered alternative.
- Execution: confirmed fills and IDs known before handoff; leave unknown facts null.
- Reviewer updates: initially empty; reserved for subsequent reconciliation, observations and review.

Save original definitions and evidence before submission. Before handoff, the trader may append actual execution facts to its new file but must not rewrite original hypotheses or rules. Repeat `--ghost-file PATH` for every new file on ghost_queue finish, including waiting/unsubmitted files. For a cycle with no new definitions omit the flag. The queue saves an immutable copy and manifest alongside the completed trading packet.

After successful finish, ownership of the source file transfers to the reviewer. The trader never edits that handed-off file again: later fills, reductions, closes and rolls go in trading memory and the next handoff. The reviewer alone maintains checkpoints, index/archive, completed reviews and lessons. On failed finish retain the run and reconcile/retry; do not create duplicate definitions. Recover and attach any not-yet-handed-off files from an interrupted cycle before completing its recovery handoff.
