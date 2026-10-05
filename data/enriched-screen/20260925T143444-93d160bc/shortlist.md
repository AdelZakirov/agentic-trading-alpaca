# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-24
- Expert data generated at: 2026-09-25T14:18:46Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 40

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | DTE | DTE Energy | 1 | all-stocks #8 54 mentions 173 upvotes; options #1 9 mentions 32 upvotes |
| 2 | META | Meta Platforms (Facebook) | 1 | all-stocks #1 310 mentions 1743 upvotes |
| 3 | NVDA | NVIDIA | 2 | all-stocks #11 46 mentions 212 upvotes; options #2 3 mentions 6 upvotes |
| 4 | SPY | SPDR S&amp;P 500 ETF Trust | 2 | all-stocks #2 257 mentions 754 upvotes |
| 5 | IBKR | Interactive Brokers | 3 | options #3 2 mentions 9 upvotes |
| 6 | MU | Micron Technology | 3 | all-stocks #3 120 mentions 315 upvotes; options #25 1 mentions 1 upvotes |
| 7 | AMD | AMD | 4 | all-stocks #4 74 mentions 285 upvotes; options #11 1 mentions 1 upvotes |
| 8 | MSFT | Microsoft | 4 | all-stocks #12 45 mentions 66 upvotes; options #4 1 mentions 1 upvotes |
| 9 | AAPL | Apple | 5 | all-stocks #26 16 mentions 88 upvotes; options #5 1 mentions 1 upvotes |
| 10 | SNDK | Sandisk | 5 | all-stocks #5 70 mentions 159 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | PAYX | Paychex | mixed | high | 2026-09-24 | 7 | 7 | MarketBeat | Seven firms reported fresh actions on Sep 24: six target cuts or reiterations and one JPMorgan upgrade. | Fresh multi-firm cluster includes conflicting rating and target actions. |
| 2 | COST | Costco Wholesale | bearish | high | 2026-09-25 | 2 | 2 | MarketBeat | Mizuho and Sanford C. Bernstein cut Costco's targets on Sep 25, maintaining Outperform ratings. | Two firms cut targets on Sep 25 while maintaining Outperform ratings. |
| 3 | NBIS | Nebius Group | bullish | high | 2026-09-24 | 1 | 1 | MarketBeat | BNP Paribas Exane upgraded Nebius from Neutral to Outperform and raised its target from $260 to $399 on Sep 24. | Fresh upgrade paired with a material target increase. |
| 4 | MAC | Macerich | bullish | medium | 2026-09-24 | 1 | 1 | MarketBeat | JPMorgan upgraded Macerich from Neutral to Overweight on Sep 24 and set a $26 target. | Fresh rating upgrade from Neutral to Overweight. |
| 5 | WELL | Welltower | bullish | medium | 2026-09-24 | 1 | 1 | MarketBeat | JPMorgan upgraded Welltower from Neutral to Overweight on Sep 24 and set a $260 target. | Fresh rating upgrade from Neutral to Overweight. |
| 6 | SNPS | Synopsys | bullish | medium | 2026-09-24 | 1 | 1 | MarketBeat | BNP Paribas Exane upgraded Synopsys from Underperform to Neutral on Sep 24 with a $420 target. | Fresh upgrade from Underperform to Neutral. |
| 7 | CRWV | CoreWeave | bullish | medium | 2026-09-24 | 1 | 1 | MarketBeat | JPMorgan upgraded CoreWeave from Neutral to Overweight and raised its target from $120 to $125 on Sep 24. | Fresh rating upgrade and target increase. |
| 8 | MMM | 3M | neutral | medium | 2026-09-24 | 1 | 1 | MarketBeat | Wells Fargo initiated 3M coverage at Equal Weight with a $195 target on Sep 24. | Fresh analyst initiation with a neutral rating. |
| 9 | BP | BP | bullish | medium | 2026-09-23 | 1 | 1 | MarketBeat | JPMorgan upgraded BP from Neutral to Overweight on Sep 23. | Fresh dated rating upgrade from Neutral to Overweight. |
| 10 | TTE | TotalEnergies | bearish | medium | 2026-09-23 | 1 | 1 | MarketBeat | JPMorgan downgraded TotalEnergies from Overweight to Neutral on Sep 23. | Fresh dated rating downgrade from Overweight to Neutral. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | MGM | 0.39908 | volume_anomaly r2 s=0.9995; momentum_breakout r6 s=0.9861; stretched_reversal r1 s=1; volatility_expansion r4 s=0.9984; wildcard r1 s=0.9976 | bullish_reversal | high | $33.69 | relative volume is 13.37x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 13.37x; stock moved 5.04 ATR today and is 8.00 ATR from its 20-day mean; 5-day realized volatility is 1.80x its 20-day level; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 100% percentile, stretch 100% percentile |
| 2 | GIL | 0.303361 | volume_anomaly r7 s=0.9968; momentum_breakout r7 s=0.9854; stretched_reversal r5 s=0.9973; volatility_expansion r18 s=0.9909; wildcard r2 s=0.9768 | bullish_reversal | high | $40.58 | relative volume is 6.85x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 6.85x; stock moved 3.70 ATR today and is 5.98 ATR from its 20-day mean; 5-day realized volatility is 1.60x its 20-day level; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 99% percentile, stretch 100% percentile |
| 3 | ACAD | 0.268722 | volume_anomaly r17 s=0.9915; momentum_breakout r4 s=0.9925; stretched_reversal r2 s=0.9992; wildcard r3 s=0.9589 | bullish_reversal | high | $22.17 | relative volume is 4.92x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 4.92x; stock moved 4.11 ATR today and is 7.16 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 100% percentile, volatility expansion 98% percentile, stretch 100% percentile |
| 4 | GRAL | 0.258608 | momentum_breakout r3 s=0.9932; stretched_reversal r3 s=0.9981; volatility_expansion r20 s=0.9899; wildcard r4 s=0.9544 | bearish_reversal | high | $125.14 | bullish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 3.46x; stock moved 3.09 ATR today and is 7.79 ATR from its 20-day mean; 5-day realized volatility is 1.59x its 20-day level; relaxed-liquidity stock showing volume 98% percentile, normalized move 100% percentile, volatility expansion 99% percentile, stretch 100% percentile |
| 5 | GEN | 0.233766 | volume_anomaly r4 s=0.9984; momentum_breakout r1 s=0.997; stretched_reversal r4 s=0.9976 | non_directional | normal | $23.05 | relative volume is 7.76x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 7.76x; stock moved 3.25 ATR today and is 7.09 ATR from its 20-day mean |
| 6 | BOIL | 0.198499 | volume_anomaly r16 s=0.992; momentum_breakout r2 s=0.9947; stretched_reversal r22 s=0.9656; wildcard r12 s=0.8225 | bullish | high | $24.43 | relative volume is 5.00x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 5.00x; stock moved 2.70 ATR today and is 4.19 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 100% percentile, volatility expansion 94% percentile, stretch 93% percentile |
| 7 | CDNA | 0.198361 | momentum_breakout r15 s=0.9629; stretched_reversal r6 s=0.9952; volatility_expansion r17 s=0.9915; wildcard r7 s=0.8599 | bearish_reversal | high | $61.36 | bullish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 2.33x; stock moved 3.86 ATR today and is 5.27 ATR from its 20-day mean; 5-day realized volatility is 1.60x its 20-day level; relaxed-liquidity stock showing volume 91% percentile, normalized move 100% percentile, volatility expansion 99% percentile, stretch 99% percentile |
| 8 | QURE | 0.182841 | volume_anomaly r19 s=0.9904; momentum_breakout r8 s=0.9844; stretched_reversal r23 s=0.9651; wildcard r6 s=0.8677 | non_directional | high | $38.34 | relative volume is 4.61x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 4.61x; stock moved 2.55 ATR today and is 4.21 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 100% percentile, volatility expansion 98% percentile, stretch 93% percentile |
| 9 | BLLN | 0.169997 | momentum_breakout r16 s=0.9602; stretched_reversal r16 s=0.9795; volatility_expansion r12 s=0.9941; wildcard r11 s=0.8302 | non_directional | high | $124.76 | bullish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 2.40x; stock moved 2.05 ATR today and is 4.70 ATR from its 20-day mean; 5-day realized volatility is 1.64x its 20-day level; relaxed-liquidity stock showing volume 92% percentile, normalized move 99% percentile, volatility expansion 99% percentile, stretch 96% percentile |
| 10 | VKTX | 0.160256 | volume_anomaly r3 s=0.9989; volatility_expansion r2 s=0.9995 | non_directional | normal | $36.76 | relative volume is 8.72x its 20-day median; 5-day realized volatility is 1.82x its 20-day level |
| 11 | KGC | 0.150718 | momentum_breakout r12 s=0.9739; stretched_reversal r9 s=0.9859; wildcard r9 s=0.8436 | bullish_reversal | high | $24.42 | bearish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 2.61x; stock moved 2.94 ATR today and is 4.77 ATR from its 20-day mean; relaxed-liquidity stock showing volume 94% percentile, normalized move 100% percentile, volatility expansion 97% percentile, stretch 97% percentile |
| 12 | ROL | 0.145629 | momentum_breakout r22 s=0.9383; stretched_reversal r7 s=0.9925; wildcard r8 s=0.8481 | bullish_reversal | high | $30.42 | bearish 20-day breakout, 5-day momentum is in the 87% percentile, relative volume 2.59x; stock moved 2.59 ATR today and is 5.25 ATR from its 20-day mean; relaxed-liquidity stock showing volume 94% percentile, normalized move 100% percentile, volatility expansion 96% percentile, stretch 99% percentile |
| 13 | WY | 0.141667 | stretched_reversal r10 s=0.9853; volatility_expansion r14 s=0.9931; wildcard r10 s=0.8363 | non_directional | high | $20.14 | stock moved 2.16 ATR today and is 4.89 ATR from its 20-day mean; 5-day realized volatility is 1.62x its 20-day level; relaxed-liquidity stock showing volume 91% percentile, normalized move 99% percentile, volatility expansion 99% percentile, stretch 97% percentile |
| 14 | XENE | 0.129555 | volume_anomaly r9 s=0.9957; volatility_expansion r3 s=0.9989 | non_directional | normal | $38.05 | relative volume is 6.34x its 20-day median; 5-day realized volatility is 1.81x its 20-day level |
| 15 | TWST | 0.127619 | momentum_breakout r11 s=0.9778; stretched_reversal r15 s=0.9811; wildcard r15 s=0.8066 | bearish_reversal | high | $184.03 | bullish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 2.81x; stock moved 2.78 ATR today and is 4.63 ATR from its 20-day mean; relaxed-liquidity stock showing volume 95% percentile, normalized move 100% percentile, volatility expansion 94% percentile, stretch 96% percentile |
| 16 | EQPT | 0.127156 | volume_anomaly r28 s=0.9856; momentum_breakout r24 s=0.9362; compression_breakout r4 s=0.9558 | non_directional | normal | $16.32 | relative volume is 3.68x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 94% percentile, relative volume 3.68x; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 3.68x normal volume |
| 17 | FSLR | 0.120401 | momentum_breakout r13 s=0.973; compression_breakout r3 s=0.9589 | bearish | normal | $172.15 | bearish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 2.59x; 20-day bearish range breakout after volatility compression in the lowest 7% of recent history, with 2.59x normal volume |
| 18 | SNX | 0.108187 | volume_anomaly r8 s=0.9963; volatility_expansion r9 s=0.9957 | non_directional | normal | $259.40 | relative volume is 6.52x its 20-day median; 5-day realized volatility is 1.65x its 20-day level |
| 19 | UNG | 0.106891 | volume_anomaly r22 s=0.9888; momentum_breakout r10 s=0.9806; stretched_reversal r29 s=0.9419 | non_directional | normal | $11.54 | relative volume is 4.28x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 4.28x; stock moved 2.31 ATR today and is 3.71 ATR from its 20-day mean |
| 20 | RUN | 0.095238 | momentum_breakout r25 s=0.9321; compression_breakout r5 s=0.9518 | bearish | normal | $7.77 | bearish 20-day breakout, 5-day momentum is in the 94% percentile, relative volume 2.10x; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 2.10x normal volume |
