# Stage 2 summary — 2026-09-16

Updated 2026-09-16T17:11:41+02:00. Covers full log through `2026-09-16T17:11:41+02:00`. [Full audit log](2026-09-16.md).

## Material actions

- BUY CHYM 100-share pre-Fed starter FILLED at $32.47, broker 4115f7d1-12d2-4c8c-ae3c-6ed621580651. GTC target $35.45 is NEW; catastrophic stop $30.95 is HELD. Daily close below $31.40 triggers thesis review. No add before a post-event hold above $32.40 or confirmed close above $33.50. [Ticker state](../positions/CHYM.md), [fundamental](../research/2026-09-16/164702-CHYM-fundamental.md), [technical](../research/2026-09-16/164733-CHYM-technical.md), [alternatives](../ghost-trades/2026-09-16/alpaca-stage2-20260916-CHYM-buy.md).
- CLOSE COO Sep 18 55/50 put spread FILLED at $0.60 net credit via replacement 341117e2-7c5b-467e-82e3-b3fb5903936d. Original $0.64 order 7005ae93-4364-43b6-b2aa-f601c950fb47 is REPLACED. Both legs are absent; gross realized loss $135 before fees. [Ticker state](../positions/COO.md), [alternatives](../ghost-trades/2026-09-16/alpaca-stage2-20260916-COO-sell.md).

## Current portfolio and risk

Final broker snapshot around 11:06 ET: equity $101,173.55, cash $66,109.48, day -$198.05/-0.19537%. Long CHYM100, ESI75, HOOD15, MSFT20, MU6, RBLX50, SPY13; no options. Open groups are CHYM target/held stop and META buy30@$644 GTC with held $678 target/$634.50 stop.

Pre-Fed posture remains aggressive but event-bounded. Estimated stress including full pending META is $5,587.77/5.52% of equity, below the temporary approximately $6,000 guardrail. No leverage, unbounded loss, default cash floor, or active breach. Reassess after the Fed and on stated close-based triggers.

Existing holdings remain HOLD. HOOD's intraday move below $107.50 did not convert its daily-close rule into an automatic exit. MSFT remains above $485.50 invalidation; MU has not completed a close above $930 for adding; RBLX remains above $46.80 review; ESI remains above $30.40 review; SPY gets no second tranche before post-Fed confirmation. META's pullback bracket is retained and fully counted in risk.

## Researched conditional opportunities

- AFRM: strong fundamentals; post-Fed daily close above $74 or held $69.80-$71 dip. [Research](../research/2026-09-16/164617-AFRM-technical.md).
- IREN: constructive but high-beta/capital-intensive; post-Fed close above $44/$45.10 or held $41.60-$42.20. [Research](../research/2026-09-16/165425-IREN-technical.md).
- ONON: strong fundamentals but mature downtrend; post-Fed close above $28 or orderly $27.10-$27.30 support test. [Research](../research/2026-09-16/165311-ONON-technical.md).
- ZION: strong valuation but rate-sensitive; post-Fed $66.20-$66.70 reversal or close above $69.60. [Research](../research/2026-09-16/165348-ZION-technical.md).
- NVDA: base-building only; close above $218.60 or $212.50-$213.60 pullback hold. [Research](../research/2026-09-16/165030-NVDA-technical.md).
- SYY: no long stock. Oct 16 80/75 put spread was about $2.21 indicative; consider only after a failed $79.60-$80 retest or confirmed break below $78.50 post-Fed. [Research](../research/2026-09-16/165230-SYY-technical.md).

The full log contains the reconciled 40-name coverage ledger. Research stopped after 11 advanced tickers because remaining names were duplicates, execution-blocked, binary without event timing, or lacked a confirmed base.

## Handoff and warnings

Handoff `6f8ea019-ab92-447e-b483-1b27102e3458` attaches the CHYM and COO definitions. Initial moneyheap connection failures were resolved after the local service started; all selected serial research then succeeded. SIP snapshots were unavailable by subscription, so fresh IEX stock and indicative option data were used and labeled. No unresolved broker mutation or reconciliation warning.
