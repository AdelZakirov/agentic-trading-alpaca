---
name: alpaca-paper-trader
description: Run autonomous Stage 2 trading from the latest shortlist using moneyheap research, Alpaca paper trading, adaptive risk policy, and durable memory. Use for normal or management-only paper-trading cycles. Never use for live trading.
---

# Alpaca paper trader

Run one autonomous Stage 2 paper-trading cycle. Make decisions and submit valid paper orders without asking for approval. HOLD is valid when it is best. Maximize paper-trading returns within the policy and current risk posture. Be aggresive. Take risks. Earn as much as possible.

## Safety gate

Load `.env` without printing it. Require both:

- `ALPACA_PAPER_TRADE=true`
- `ALPACA_ENDPOINT=https://paper-api.alpaca.markets/v2`

Never submit or mutate an order when either value differs. Never use or configure live trading, expose credentials, assume a fill, or blindly retry an uncertain mutation. Alpaca is the source of truth for account state.

## Progressive reference routing

Read each triggered reference completely and only once per cycle.

Always read:

1. [core-policy.md](references/core-policy.md)
2. [memory-contract.md](references/memory-contract.md)

Then select exactly one cycle mode:

- Normal Stage 2 cycle: read [normal-cycle.md](references/normal-cycle.md).
- Explicit management-only cycle: read [management-only.md](references/management-only.md).

Do not preload the remaining references. Read them when their trigger occurs:

- Before requesting moneyheap research: [moneyheap-api.md](references/moneyheap-api.md).
- trdrbot second opinion is DISABLED until the user explicitly re-enables it. Do not load second-opinion.md, run its helper, read its cache, or use its nominations/comparisons. Retained code and historical mentions do not enable it.
- Before researching, selecting, or managing an option or option order: [options-api.md](references/options-api.md).
- Before submitting, replacing, or cancelling an order—or allowing a risk-increasing order to remain open: [order-execution.md](references/order-execution.md).
- After selecting a real trade but before submitting it: [ghost-pretrade.md](references/ghost-pretrade.md).

## Common cycle

1. Run `python3 -m alpaca_agent.ghost_queue begin` before trading work and retain its run_id. If another cycle is active, do not overlap; reconcile that task first. Read memory under the memory contract.
2. Read the Alpaca clock, account, positions, and open orders.
3. Form one portfolio risk posture before ticker actions.
4. Execute the selected normal or management-only mode.
5. Make separate stock and option decisions where applicable. Record thesis, confidence, holding period, invalidation, and size rationale.
6. Load the execution reference before any order action. Load ghost-pretrade only for a selected real trade before submission.
7. Reconcile orders, positions, and account after every mutation. Only `filled` means filled.
8. Persist trading memory and publish the completed handoff under the memory contract. Create new pre-submission ghost definition files under ghost-pretrade.md and attach them to the handoff. After handoff, do not edit those files, read the ghost index, maintain checkpoints, or evaluate/update lessons. The separate ghost reviewer owns those tasks.
9. After memory persistence succeeds, refresh the separate Machine Earning Site when its local project exists by running:
   `python3 /Users/adel/Projects/machine-earning-site/scripts/sync_dashboard.py --agent-root /Users/adel/Projects/alpaca-hack`
   Treat a dashboard-sync failure as a reporting issue only; never retry an Alpaca order because the dashboard upload failed.
10. Return a concise report covering scope, decisions, orders or blockers, pre-trade alternatives and handoff status, errors, and final portfolio state.

Use `data/stage1_shortlist.md` as the source of new candidates in normal mode. Always manage existing Alpaca positions and open orders, even when absent from the shortlist.

## Alpaca MCP

Use project server `alpaca_paper` for all agent Alpaca reads and mutations, including account, positions, orders, assets and market data. It loads project paper credentials via scripts/alpaca_mcp.py. Read [alpaca-mcp.md](references/alpaca-mcp.md) once before the first call. Do not use the old market-data app, ad hoc HTTP scripts or retained Alpaca CLI as an automatic fallback. If MCP is unavailable, report the blocker; never change transport to retry an uncertain order. Local screening, Moneyheap and memory commands remain in use.

## Compact data-tool output

Use MCP for quote and option-chain reads. When custom Python is needed, use a multiline script with explicit indentation: collect rows inside the loop, then print the selected result once after the loop. Never print the growing accumulator on every iteration. Avoid semicolon-packed loop bodies, where a trailing print can accidentally remain inside the loop.

Save large raw responses to a local artifact and return its path, counts and decision-relevant fields. For option chains, filter by the requested expiration/strike range and show relevant quotes and Greeks. If output is truncated, narrow columns or read disjoint row batches; do not rerun the same full dump with a larger output limit. This limits displayed data, not required ticker coverage or execution reconciliation.
