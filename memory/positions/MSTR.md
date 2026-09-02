# MSTR — OPEN ORDER, NO POSITION

## Current Alpaca state

- Position: none
- Open order: buy two Sep. 11 $125/$135 bull call debit spreads at a $2.66 maximum net debit
- Original order: `81fa7e82-6798-47a1-86b4-e41af3f31692`, client ID `alpaca-stage2-20260902-MSTR-option-buy`, status `replaced`, filled 0/2
- Replacement order: `c7592541-fa86-48f3-bacb-160d2e45b232`, client ID `2baa0d9b-ba7d-4230-9c5d-42090a26f00e`, status `new`, filled 0/2
- Contracts: buy 2 `MSTR260911C00125000`; sell 2 `MSTR260911C00135000`
- Reconciled: 2026-09-02 18:38 Europe/Amsterdam

## Current plan

- Thesis: bullish flag continuation from the $120-$122.50 demand zone toward $133 and $137.50-$139.80.
- Confidence: moderate.
- Holding period if filled: through 2026-09-09; avoid expiration/assignment without a fresh decision.
- Invalidation: underlying below $117.50.
- Size rationale: two spreads add at most $532 risk at the replacement limit while capping 24/7 Bitcoin gap exposure and correlated growth risk.
- Stock decision: HOLD/no stock order because the IEX quote was temporarily wide and stock carries uncapped overnight crypto-beta risk.
- Option decision: BUY submitted, not filled. No further replacement or chase is allowed.

## Relevant evidence

- Shortlist: [`../../data/stage1_shortlist.md`](../../data/stage1_shortlist.md)
- Technical research: [`../research/2026-09-02/181406-MSTR-technical.md`](../research/2026-09-02/181406-MSTR-technical.md)
- Pre-trade ghost definitions and execution log: [`../logs/2026-09-02.md`](../logs/2026-09-02.md)

## History

### 2026-09-02

- Submitted two Sep. 11 $125/$135 spreads at $2.60; 0/2 filled.
- Replaced once at $2.66 after a complete quote/account/order refresh. Replacement remains `new`, 0/2 filled. No ghost set exists unless Alpaca confirms a fill.
