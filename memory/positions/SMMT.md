# SMMT

## Current state
Alpaca confirmed 500 shares at $16.83, market value $8,415.00, unrealized P/L −$250.00. Fresh IEX quote was $16.85 bid / $16.86 ask; price is below the $17.00–$17.07 consolidation support but above the live $16.75 stop. HOLD the reduced residual inside the exact GTC OCO: parent `c9e3996c-4e38-47d5-b2a8-d816918d14e1` target $18.50 `new`, stop leg `e4356cf9-e1b0-474c-b93b-4c1daa173b7b` at $16.75 `held`; 0 filled. No further reduction or option hedge was selected because the position was already halved, the hard invalidation was not confirmed, and clinical gap risk remains the main overnight concern.

## Current plan

REDUCE исполнен: 500/1000 проданы по $17.09; остаток 500. GTC OCO $18.50/$16.75. Горизонт до 11 сентября; следующий пересмотр до конца текущей сессии и 11 сентября. Уверенность умеренная. Положительный HARMONi-2 не отменяет риск разрыва; полный выход отвергнут ради оставшейся клинической опциональности. Новые опционы/хедж не открывать: OPRA 403.


Fresh independent research: [180944-SMMT-fundamental.md](../research/2026-09-10/180944-SMMT-fundamental.md)

## Option-data clarification
Indicative chains were available and structures compared; no option order selected. This supersedes earlier OPRA-only unavailability wording. See [follow-up](../../data/independent-stage2-16e6df9f/indicative-followup.md).

## Memory provenance
Migrated from existing records; no new broker reconciliation. Dates in the retained evidence govern freshness.
[History](history/SMMT.jsonl) — load only for a specific past decision.
