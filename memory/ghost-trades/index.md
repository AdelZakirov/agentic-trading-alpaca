# Ghost-trade routing index

- Updated: 2026-09-15 21:44 Europe/Amsterdam
- Active sets: 8
- Source of truth: each linked ghost file; this index controls which files need to be loaded.

| Ghost set | Ticker | Status | Real path | Evaluation end | Last checkpoint | Next checkpoint | Between-checkpoint trigger | Last updated |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| [`alpaca-stage2-20260910-NVDA-buy`](2026-09-10/alpaca-stage2-20260910-NVDA-buy.md) | NVDA | ACTIVE | 55 shares bought at $217.97; stopped 55 at $209.732181 on 2026-09-14 | 2026-09-24 close | 2026-09-14 close | 2026-09-15 close | None outside checkpoints | 2026-09-14 22:36 |
| [`alpaca-stage2-20260911-COO-bear-put-spread`](2026-09-11/alpaca-stage2-20260911-COO-bear-put-spread.md) | COO | ACTIVE | 1 Sep 18 $55/$50 bear put spread filled at $1.95 debit | 2026-09-18 expiration | 2026-09-14 close | 2026-09-15 close | COO $50/$51 target or $55.60/$57.40 review | 2026-09-14 22:36 |
| [`alpaca-stage2-20260914-RBLX-sell`](2026-09-14/alpaca-stage2-20260914-RBLX-sell.md) | RBLX | ACTIVE | 25 sold at $50.50; 50 shares remain | 2026-09-18 close | 2026-09-14 close | 2026-09-15 close | Daily close below $46.80; continuation touch $53.50-$55.00 | 2026-09-14 22:27 |
| [`alpaca-stage2-20260914-ESI-buy`](2026-09-14/alpaca-stage2-20260914-ESI-buy.md) | ESI | ACTIVE | 75 shares bought at $32.16 | 2026-09-25 close | 2026-09-14 close | 2026-09-15 close | Daily close below $30.40; target touch $34.50 | 2026-09-14 22:27 |
| [`alpaca-stage2-20260914-SPY-buy`](2026-09-14/alpaca-stage2-20260914-SPY-buy.md) | SPY | ACTIVE | 13 shares bought at $762.89 | 2026-09-25 close | 2026-09-14 close | 2026-09-15 close | Daily close below $750.50; target touch $779.00 | 2026-09-14 22:27 |
| [`alpaca-stage2-20260915-HOOD-sell`](2026-09-15/alpaca-stage2-20260915-HOOD-sell.md) | HOOD | ACTIVE | 15 sold at $108.94; 15 shares remain | 2026-09-22 close | Fill 2026-09-15 | 2026-09-15 close | Daily close below $107.50; reclaim $108.50/$110 before add | 2026-09-15 21:44 |
| [`alpaca-stage2-20260915-MMED-sell`](2026-09-15/alpaca-stage2-20260915-MMED-sell.md) | MMED | ACTIVE | 125 sold at $22.06; no shares remain | 2026-09-29 close | Fill 2026-09-15 | 2026-09-15 close | Daily close below $21.80; target bid touch $24.55/$26 | 2026-09-15 21:44 |
| [`alpaca-stage2-20260915-MSFT-buy`](2026-09-15/alpaca-stage2-20260915-MSFT-buy.md) | MSFT | ACTIVE | 20 bought at $497.4715 | 2026-10-13 close | Fill 2026-09-15 | 2026-09-15 close | Daily close below $485.50; executable bid $510–514 trim 10 | 2026-09-15 21:44 |
