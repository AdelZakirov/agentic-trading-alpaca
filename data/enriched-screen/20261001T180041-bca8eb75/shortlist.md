# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-30
- Expert data generated at: 2026-10-01T17:43:53Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 38

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | MU | Micron Technology | 1 | all-stocks #1 1389 mentions 8286 upvotes; options #27 1 mentions 4 upvotes |
| 2 | SPY | SPDR S&amp;P 500 ETF Trust | 1 | all-stocks #2 276 mentions 791 upvotes; options #1 7 mentions 13 upvotes |
| 3 | BP | BP | 2 | options #2 3 mentions 6 upvotes |
| 4 | EWZ | BlackRock Institutional Trust Company N.A. - iShares MSCI Brazil ETF | 3 | options #3 3 mentions 4 upvotes |
| 5 | QQQ | Invesco QQQ ETF | 3 | all-stocks #3 131 mentions 264 upvotes |
| 6 | GOOG | Alphabet (Google) | 4 | all-stocks #4 106 mentions 477 upvotes; options #4 2 mentions 4 upvotes |
| 7 | ES | Eversource Energy | 5 | options #5 2 mentions 3 upvotes |
| 8 | NVDA | NVIDIA | 5 | all-stocks #5 101 mentions 1307 upvotes; options #15 1 mentions 3 upvotes |
| 9 | CD | Chindata | 6 | options #6 2 mentions 6 upvotes |
| 10 | GOOGL | Alphabet (Google) | 6 | all-stocks #6 88 mentions 1247 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | OXY | Occidental Petroleum | bullish | high | 2026-10-01 | 1 | 1 | 24/7 Wall St. | Goldman Sachs upgraded the rating from Neutral to Buy and raised its target from $63 to $69. | Fresh rating upgrade with a raised price target. |
| 2 | ORA | Ormat Technologies | bearish | high | 2026-10-01 | 1 | 1 | 24/7 Wall St. | UBS cut the rating from Buy to Neutral and reduced its target from $157 to $100. | Fresh downgrade paired with a substantial target reduction. |
| 3 | DLTR | Dollar Tree | bullish | medium | 2026-10-01 | 1 | 1 | 24/7 Wall St. | Loop Capital upgraded the rating from Hold to Buy and raised its target from $130 to $140. | Fresh Buy upgrade and target increase. |
| 4 | BP | BP p.l.c. | bullish | medium | 2026-10-01 | 1 | 1 | 24/7 Wall St. | Morgan Stanley raised the rating from Equal Weight to Overweight and the target from $69 to $71. | Fresh rating upgrade and small target increase. |
| 5 | UTHR | United Therapeutics | bullish | medium | 2026-10-01 | 1 | 1 | 24/7 Wall St. | BTIG upgraded the rating from Neutral to Buy and set a $728 target. | Fresh rating upgrade from Neutral to Buy. |
| 6 | XOM | Exxon Mobil | bearish | medium | 2026-10-01 | 1 | 1 | 24/7 Wall St. | Wells Fargo downgraded the rating from Overweight to Equal Weight and set a $182 target. | Fresh downgrade from Overweight to Equal Weight. |
| 7 | SE | Sea Limited | bearish | medium | 2026-10-01 | 1 | 1 | 24/7 Wall St. | DBS Bank cut the rating from Buy to Hold and set a $105 target. | Fresh rating cut from Buy to Hold. |
| 8 | CBNK | Capital Bancorp | bearish | medium | 2026-10-01 | 1 | 1 | 24/7 Wall St. | Hovde Group downgraded the rating from Outperform to Market Perform; its $42 target was unchanged. | Fresh rating downgrade with an unchanged target. |
| 9 | LEN | Lennar | bearish | medium | 2026-10-01 | 1 | 1 | 24/7 Wall St. | Morgan Stanley initiated coverage with an Underweight rating and a $65 target. | Fresh bearish coverage initiation. |
| 10 | RKLB | Rocket Lab | bullish | medium | 2026-10-01 | 1 | 1 | 24/7 Wall St. | Citigroup initiated coverage with a Buy rating and a $105 target. | Fresh Buy coverage initiation. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | LQDA | 0.518398 | volume_anomaly r2 s=0.9995; momentum_breakout r1 s=0.9998; stretched_reversal r1 s=1; volatility_expansion r1 s=1; compression_breakout r4 s=0.9554; wildcard r1 s=0.9988 | bullish_reversal | high | $30.14 | relative volume is 11.54x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 11.54x; stock moved 12.88 ATR today and is 12.13 ATR from its 20-day mean; 5-day realized volatility is 1.85x its 20-day level; 20-day bearish range breakout after volatility compression in the lowest 13% of recent history, with 11.54x normal volume; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 100% percentile, stretch 100% percentile |
| 2 | UTHR | 0.326786 | volume_anomaly r5 s=0.9979; momentum_breakout r2 s=0.9871; stretched_reversal r11 s=0.9876; volatility_expansion r6 s=0.9974; wildcard r5 s=0.9497 | non_directional | high | $541.87 | relative volume is 7.13x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 7.13x; stock moved 5.68 ATR today and is 4.52 ATR from its 20-day mean; 5-day realized volatility is 1.71x its 20-day level; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 100% percentile, stretch 97% percentile |
| 3 | PAAA | 0.226874 | stretched_reversal r2 s=0.9995; volatility_expansion r9 s=0.9959; compression_breakout r12 s=0.9244; wildcard r12 s=0.9055 | bullish_reversal | high | $51.28 | stock moved 11.26 ATR today and is 9.18 ATR from its 20-day mean; 5-day realized volatility is 1.67x its 20-day level; 20-day bearish range breakout after volatility compression in the lowest 17% of recent history, with 2.30x normal volume; relaxed-liquidity stock showing volume 93% percentile, normalized move 100% percentile, volatility expansion 100% percentile, stretch 100% percentile |
| 4 | FNV | 0.196429 | volume_anomaly r6 s=0.9974; momentum_breakout r4 s=0.9765; compression_breakout r6 s=0.9453 | non_directional | normal | $238.14 | relative volume is 6.63x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 94% percentile, relative volume 6.63x; 20-day bearish range breakout after volatility compression in the lowest 15% of recent history, with 6.63x normal volume |
| 5 | MTG | 0.191302 | momentum_breakout r3 s=0.9841; stretched_reversal r7 s=0.9956; wildcard r8 s=0.9336 | bullish_reversal | high | $25.86 | bearish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 3.16x; stock moved 3.67 ATR today and is 6.23 ATR from its 20-day mean; relaxed-liquidity stock showing volume 97% percentile, normalized move 100% percentile, volatility expansion 99% percentile, stretch 99% percentile |
| 6 | JAAA | 0.186335 | stretched_reversal r4 s=0.9974; volatility_expansion r4 s=0.9984; wildcard r13 s=0.9023 | non_directional | high | $50.47 | stock moved 10.56 ATR today and is 7.86 ATR from its 20-day mean; 5-day realized volatility is 1.71x its 20-day level; relaxed-liquidity stock showing volume 93% percentile, normalized move 100% percentile, volatility expansion 100% percentile, stretch 100% percentile |
| 7 | NLY | 0.176786 | momentum_breakout r5 s=0.976; stretched_reversal r6 s=0.9956; wildcard r11 s=0.9139 | bullish_reversal | high | $18.88 | bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 2.68x; stock moved 3.42 ATR today and is 6.62 ATR from its 20-day mean; relaxed-liquidity stock showing volume 96% percentile, normalized move 100% percentile, volatility expansion 99% percentile, stretch 99% percentile |
| 8 | GBIL | 0.157576 | stretched_reversal r5 s=0.9959; compression_breakout r1 s=0.9758 | bearish_reversal | normal | $100.11 | stock moved 2.28 ATR today and is 8.33 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 0% of recent history, with 2.19x normal volume |
| 9 | JBL | 0.149854 | volume_anomaly r9 s=0.9959; momentum_breakout r14 s=0.9529; compression_breakout r8 s=0.9336 | non_directional | normal | $286.91 | relative volume is 5.01x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 91% percentile, relative volume 5.01x; 20-day bearish range breakout after volatility compression in the lowest 15% of recent history, with 5.01x normal volume |
| 10 | QURE | 0.149813 | volume_anomaly r13 s=0.9938; momentum_breakout r24 s=0.9327; volatility_expansion r3 s=0.999 | non_directional | normal | $24.07 | relative volume is 4.58x its 20-day median; bearish 5-day momentum, 5-day momentum is in the 100% percentile, relative volume 4.58x; 5-day realized volatility is 1.74x its 20-day level |
| 11 | FNF | 0.14693 | momentum_breakout r9 s=0.9624; stretched_reversal r9 s=0.9917; wildcard r14 s=0.8978 | bullish_reversal | high | $38.69 | bearish 20-day breakout, 5-day momentum is in the 92% percentile, relative volume 2.76x; stock moved 2.80 ATR today and is 5.44 ATR from its 20-day mean; relaxed-liquidity stock showing volume 96% percentile, normalized move 99% percentile, volatility expansion 98% percentile, stretch 99% percentile |
| 12 | NOC | 0.144163 | momentum_breakout r25 s=0.9258; stretched_reversal r21 s=0.9508; compression_breakout r2 s=0.9726 | bearish | normal | $483.57 | bearish 20-day breakout, 5-day momentum is in the 86% percentile, relative volume 2.10x; stock moved 2.06 ATR today and is 3.51 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 2.10x normal volume |
| 13 | PULS | 0.14359 | stretched_reversal r3 s=0.999; volatility_expansion r5 s=0.9979 | bullish_reversal | normal | $49.45 | stock moved 10.67 ATR today and is 9.07 ATR from its 20-day mean; 5-day realized volatility is 1.71x its 20-day level |
| 14 | USFR | 0.138889 | volume_anomaly r8 s=0.9964; volatility_expansion r2 s=0.9995 | non_directional | normal | $50.39 | relative volume is 5.66x its 20-day median; 5-day realized volatility is 1.82x its 20-day level |
| 15 | JBTM | 0.128947 | momentum_breakout r10 s=0.957; stretched_reversal r28 s=0.898; compression_breakout r9 s=0.9313 | bearish | normal | $105.64 | bearish 20-day breakout, 5-day momentum is in the 89% percentile, relative volume 3.26x; stock moved 1.99 ATR today and is 2.92 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 18% of recent history, with 3.26x normal volume |
| 16 | CAG | 0.126564 | volume_anomaly r27 s=0.9865; momentum_breakout r6 s=0.9757; stretched_reversal r17 s=0.9682 | non_directional | normal | $13.46 | relative volume is 3.43x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 95% percentile, relative volume 3.43x; stock moved 1.72 ATR today and is 4.03 ATR from its 20-day mean |
| 17 | DOCS | 0.115385 | momentum_breakout r16 s=0.9474; compression_breakout r3 s=0.9678 | bullish | normal | $28.34 | bullish 20-day breakout, 5-day momentum is in the 89% percentile, relative volume 2.60x; 20-day bullish range breakout after volatility compression in the lowest 5% of recent history, with 2.60x normal volume |
| 18 | SUB | 0.112944 | volume_anomaly r15 s=0.9927; stretched_reversal r16 s=0.9744; volatility_expansion r19 s=0.9907 | non_directional | normal | $104.52 | relative volume is 4.26x its 20-day median; stock moved 2.03 ATR today and is 4.08 ATR from its 20-day mean; 5-day realized volatility is 1.56x its 20-day level |
| 19 | FAF | 0.10101 | momentum_breakout r8 s=0.9651; stretched_reversal r12 s=0.9863 | bullish_reversal | normal | $60.80 | bearish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 2.25x; stock moved 1.81 ATR today and is 5.29 ATR from its 20-day mean |
| 20 | EDV | 0.098456 | volume_anomaly r4 s=0.9984; momentum_breakout r27 s=0.9232 | non_directional | normal | $55.38 | relative volume is 7.25x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 86% percentile, relative volume 7.25x |
