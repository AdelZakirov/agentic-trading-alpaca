# Stage 2 normal cycle — 2026-09-14

Run `f69753d6-76b4-4255-b370-bdb39af6070f`; decision time 2026-09-14 Europe/Amsterdam. Alpaca clock: New York date 2026-09-14, regular market open, timestamp 12:33:43 ET at final reconciliation. Safety gate passed: `ALPACA_PAPER_TRADE=true`, paper endpoint exact.

## Artifact gate and discovery

`data/daily_shortlist_state.json` completed successfully for 2026-09-14 at 10:18:32 ET. `stage1_screen.json` had 192 candidates and completed-bar/as-of date 2026-09-11. `stage1_experts.json` had 19 candidates, generated 2026-09-14T14:07:00Z. `stage1_shortlist.md` matched the screen date and expert timestamp and contained community, expert and technical sections. The enriched build covered all 40 unique tickers and matched shortlist hash `6597460e...d864a5c`; Yahoo was 8 ok / 32 partial, technical was 35 ok / 1 stale / 2 partial / 2 missing. Partial Yahoo fields were preserved as unknown after one permitted retry plus the user-requested follow-up retry.

## Pre-action broker state and risk posture

Account was ACTIVE and unblocked: equity $101,487.97, cash $85,921.43, long stock market value $15,571.54, buying power $367,644.02, options buying power $73,582.06. Positions were HOOD 30, MMED 125, MU 6, RBLX 75, and the COO Sep. 18 $55/$50 put spread. META had the only pre-existing open parent order: 30-share GTC buy at $644 with held $678 target / $634.50 stop. Risk posture was selective aggressive with moderate caution: no material breach, no minimum cash floor, but avoid compounding MU/electronics correlation, MMED gap/supply risk, COO illiquidity/expiry, and stale/wide quote risk.

## Research funnel and coverage ledger

Research advanced: AVT fundamental, ARW fundamental, ESI fundamental, IREN fundamental plus a focused indicative call-chain check, MU technical management review, and RBLX technical management review. Successful research artifacts: `memory/research/2026-09-14/182416-AVT-fundamental.md`, `182455-ARW-fundamental.md`, `182522-ESI-fundamental.md`, `182557-IREN-fundamental.md`, `182650-MU-technical.md`, `182721-RBLX-technical.md`. IREN chain covered Sep. 25–Oct. 16 calls, strikes $35–$60: IV was roughly 82%–95%, so no option order was selected despite the defined-risk path being examined.

Coverage in shortlist order, one disposition per unique ticker:

- `META` manage/hold existing $644 GTC bracket; `SPY` reject broad-beta duplicate; `DTE` reject bearish/no actionable long catalyst; `MU` manage/research hold; `GOOG` watch, no differentiated catalyst; `QQQ` reject broad-beta duplicate; `GOOGL` watch, duplicate and weak short-term tape; `NVDA` watch, semiconductor overlap and -4.5% 5-day tape; `AGI` watch, -4.7% 5-day and negative EPS revision; `ATAI` insufficient_evidence, stale technical/quote and missing fields.
- `BLSH` reject, 54x forward P/E, -42% EPS revision and target only about +2%; `CAPR` insufficient_evidence, binary biotech/partial technical and -9.6% 5-day move after a +98% 20-day move; `COIN` watch, -9% 5-day, 69x P/E and only about +5% target upside; `IREN` research/no trade, high-beta negative-profitability and dilution risk despite upgrade; `SPRO` insufficient_evidence, missing technical and most fields; `CIZN` insufficient_evidence, missing technical and stale 2023 quote; `GEV` watch, fresh target but -8.8% 20-day and 34.6x P/E; `ESI` research/selected buy order; `IP` watch, target cut and -16.5% 20-day; `ATO` reject long stock, downgrade not sufficient for a researched put trade.
- `COO` manage existing put spread/no add; `NAVN` reject, -24% 5-day/-29% 20-day breakdown without catalyst; `TTAN` reject, -41% 20-day bearish breakdown; `TENB` reject, -25% 20-day with only about +3% target upside; `ARW` research/watch conditional, value/revision setup but same distributor correlation and stabilization needed; `VTIP` reject ETF anomaly; `HDB` watch, high-volume non-directional setup; `OKLO` reject/watch, negative earnings and bearish technical; `GT` reject/watch, bearish breakdown and negative revisions; `MUB` reject ETF anomaly; `HPE` watch, strong recent move but no confirmed earnings timing; `TRP` reject/watch, bearish breakout; `AVT` research/watch conditional, strong value/revision setup but do not stack with ESI; `LULU` reject/watch, -17% 20-day and -59% EPS revision; `ACVA` reject/watch, +55% 5-day chase risk and partial technical; `ACWX` reject ETF anomaly; `DAMD` insufficient_evidence, extreme local return anomaly and missing fundamentals; `STIP` reject ETF; `EXR` watch, -7.8% 20-day without catalyst; `VTEB` reject ETF anomaly.

## Decisions and execution

- RBLX investment decision: trim 25 of 75 into overbought gap-fill resistance; stock order submitted as day limit sell at $50.50, then confirmed `filled` 25/25 at $50.50. Broker order `76114a4e-bd9f-486b-95e9-ea3582305a9b`, filled 16:30:51Z. Position is 50 shares; ghost definition is `memory/ghost-trades/2026-09-14/alpaca-stage2-20260914-RBLX-sell.md`.
- ESI investment decision: tactical 75-share buy within $31.80–$32.30, sized for about $132 to $30.40 daily-close invalidation. Day limit buy at $32.16 submitted as `3b2caccb-8451-473f-ab70-f955bbccd657`, final status `new`, 0/75; no replacement or chase. Ghost definition is `memory/ghost-trades/2026-09-14/alpaca-stage2-20260914-ESI-buy.md`.
- Existing positions: HOOD HOLD; MMED HOLD pending daily-close rule; MU HOLD/no add with updated $894/$880 reviews; COO HOLD defined-risk spread; META HOLD existing conditional bracket because current IEX quote $659.32/$662.12 is above the $644 entry. No other order action.

Execution used MCP only. Delayed-SIP inputs were about 15 minutes delayed and labeled; current IEX spot checks were positive except an unusually wide HOOD market. No SIP, live endpoint, direct REST/CLI fallback, or assumed fill was used. Post-action final Alpaca state: equity $101,537.72, cash $87,183.93, long stock market value $14,358.79, buying power $366,886.31, options buying power $72,400.93. Open parents: ESI new 0/75 and META new 0/30.

## Memory and handoff

Updated portfolio state, ticker plans, RBLX/MU/ESI histories, and two new ghost definitions before publication. No lesson update was made; active lessons applied were bounded/idempotent execution, daily-close invalidation, overlap mapping, target activation, and timing-limited provenance. Handoff will be published after checkpoint validation with both ghost files attached. Dashboard sync is a post-publication reporting step.

<!-- run-checkpoint: 2026-09-14T18:40:44+02:00 -->
