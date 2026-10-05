# PK pretrade comparison — 2026-09-29

## Identity
- decision_id: `alpaca-stage2-20260929-PK-buy`
- creator_run_id: `48a49638-dc63-4f52-b695-5e0875b1fcd6`
- decision_at: `2026-09-29T12:49:00-04:00`
- ticker: PK
- status: `ACTIVE`
- client_order_id: `alpaca-stage2-20260929-PK-buy`
- broker_order_id: `19819f81-37d8-433a-b2aa-8208871b3c92`

## Original decision
- Chosen action: cash-funded BUY 100 PK shares, DAY limit $15.55, regular hours only. If final preflight fails, no submission.
- Thesis: Sep 28 Raymond James/UBS upgrades; company Q2 comparable RevPAR +5.8%, adjusted FFO $0.70/share, adjusted EBITDA +8.6%, and declared $0.25 distribution with Sep 30 record date. Two-to-four-week lodging and renovated-resort re-rating.
- Pretrade exposure: no PK; MAC 200 shares about $4,518; broker nine stocks/no options, cash $58,846.98 and equity ~$100,803 at 12:46 ET. Hotel and mall REIT exposure totals about $6,073 after entry, with shared rate/consumer risk.
- Size rationale: $1,555 maximum committed cash, $95 to daily-close invalidation <$14.60, about $311 on a 20% gap; all capital can be lost. Smaller size limits correlated property drawdown while MU earnings risk is unresolved. Review Oct 16; exit-or-renew Oct 23 ahead of Nov 5 earnings.
- Invalidation: daily close below $14.60, or deterioration in RevPAR, refinancing, or guidance. Profit reviews at observed executable bid $16.20 then $17.25; dividend is not free profit because ex-dividend price adjusts.

## Evaluation rules
- Start only at broker-confirmed real fill. Compare alternatives through earliest of Oct 23 15:30 ET, completed-close invalidation, or real exit; use observed executable bid for target and terminal marks. Include any broker-confirmed distribution in total return after ex-date. Do not count record eligibility as cash received. Cash alternative remains zero P/L. No re-entry.

## Initial evidence
- Alpaca IEX 2026-09-28 close $15.72, high $15.90; 20-day low $14.62. Quotes 16:46:06Z $15.54/$15.55 1800x1000, 16:46:35Z $15.54/$15.55 1800x900, 16:48:08Z $15.54/$15.55 2000x900, 16:48:45Z $15.54/$15.55 1200x900. Latest ask $15.55 is the conservative hypothetical buy price.
- [Company Q2](https://www.pkhotelsandresorts.com/investors/news-and-events/press-releases/2026/08-06-2026-211554607); [dividend](https://www.pkhotelsandresorts.com/investors/financial-information/dividends-and-tax-information); [moneyheap](../../research/2026-09-29/171441-PK-fundamental.md). FFO estimates and analyst targets are not guaranteed returns.

## Alternatives
1. `NO_TRADE`: Tests no added property exposure. No instrument or order; quantity, cash spent and max loss $0; zero P/L at all checkpoints.
2. `DOUBLE_SIZE`: Tests 200 shares with the same $15.55 DAY entry, notional $3,110, nominal daily-close invalidation loss $190 and 20% gap scenario $622; full $3,110 at risk. Same fill anchor and exits as real. Missing hypothetical fill evidence makes the path UNSCORABLE. This tests whether extra property concentration helps enough to justify the added downside.

## Execution
- Submission status: not yet submitted.
- Fills: none confirmed.

## Reviewer updates

## Trader execution update before handoff
- Broker order ID: `19819f81-37d8-433a-b2aa-8208871b3c92`.
- Actual status: FILLED 100 shares at $15.55 on 2026-09-29T16:51:13.325714Z; exact FILL activities 52+27+2+19.
- Account cash after fill: $57,291.98.

### Independent reviewer activation — 2026-09-29

- Alpaca paper order `19819f81-37d8-433a-b2aa-8208871b3c92` is `filled`, 100/100 at `$15.55`; order-specific FILL activities are 52+27+2+19 shares, all at `$15.55`. The common comparison starts at the first confirmed FILL, `2026-09-29T16:51:11.146901Z`. Current Alpaca positions confirm 100 PK shares at `$15.55`; open PK/RGA orders are empty.
- The original alternatives remain unchanged. `NO_TRADE` is the only fully specified comparator; `DOUBLE_SIZE` remains `UNSCORABLE` because no hypothetical 200-share fill evidence exists.
- Evaluation end: `2026-10-23 15:30 ET` unless the predeclared invalidation, material event, or real exit ends it. First checkpoint: `2026-09-29` close; no close mark is recorded while the regular market remains open. Status `ACTIVE`.

## 2026-09-29 first close checkpoint

- The IEX daily bar closed at `$15.59` (high `$15.76`, low `$15.48`). The near-close quote at `2026-09-29T19:59:59.978844557Z` was `$15.58` bid x1,200 / `$15.59` ask x700.
- From the confirmed `$15.55` fill: real 100 shares `+$3.00`; `NO_TRADE` `$0`; `DOUBLE_SIZE` remains `UNSCORABLE` for lack of hypothetical 200-share execution evidence. The `$14.60` close invalidation and `$16.20` executable-bid target did not trigger. The Sep 30 dividend record date is not a cash return. Good displayed depth but single-exchange IEX data; no lesson change. Next checkpoint: October 23 end review or an original trigger.
