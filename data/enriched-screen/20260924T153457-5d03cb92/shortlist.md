# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-23
- Expert data generated at: 2026-09-24T14:36:45Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 35

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | DTE | DTE Energy | 1 | all-stocks #9 56 mentions 192 upvotes; options #1 7 mentions 63 upvotes |
| 2 | SPY | SPDR S&amp;P 500 ETF Trust | 1 | all-stocks #1 211 mentions 637 upvotes; options #3 2 mentions 4 upvotes |
| 3 | ARM | Arm Holdings | 2 | all-stocks #5 9 mentions 23 upvotes; options #2 3 mentions 15 upvotes |
| 4 | META | Meta Platforms (Facebook) | 2 | all-stocks #2 175 mentions 359 upvotes; options #21 1 mentions 2 upvotes |
| 5 | MU | Micron Technology | 3 | all-stocks #3 121 mentions 533 upvotes |
| 6 | CC | Chemours | 4 | all-stocks #37 11 mentions 23 upvotes; options #4 2 mentions 4 upvotes |
| 7 | GOOGL | Alphabet (Google) | 4 | all-stocks #4 81 mentions 227 upvotes |
| 8 | QQQ | Invesco QQQ ETF | 5 | all-stocks #5 67 mentions 156 upvotes; options #36 1 mentions 0 upvotes |
| 9 | TP | Ticketplus | 5 | options #5 1 mentions 1 upvotes |
| 10 | HELP | Helus Pharma | 6 | options #6 1 mentions 2 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | PAYX | Paychex | mixed | high | 2026-09-24 | 6 | 6 | MarketBeat | On Sep 24, JPMorgan upgraded Paychex to Neutral while four firms cut price targets and RBC reiterated Sector Perform. | Fresh multi-firm analyst cluster includes both a rating upgrade and multiple target cuts. |
| 2 | NBIS | Nebius Group | bullish | high | 2026-09-24 | 1 | 1 | MarketBeat | BNP Paribas Exane upgraded Nebius Group from Neutral to Outperform and raised its target from $260 to $399 on Sep 24. | Fresh upgrade paired with a large target increase. |
| 3 | CRWV | CoreWeave | bullish | medium | 2026-09-24 | 1 | 1 | MarketBeat | JPMorgan upgraded CoreWeave from Neutral to Overweight and raised its target from $120 to $125 on Sep 24. | Fresh rating upgrade and target increase. |
| 4 | MAC | Macerich | bullish | medium | 2026-09-24 | 1 | 1 | MarketBeat | JPMorgan upgraded Macerich from Neutral to Overweight on Sep 24 and set a $26 target. | Fresh rating upgrade from Neutral to Overweight. |
| 5 | SNPS | Synopsys | bullish | medium | 2026-09-24 | 1 | 1 | MarketBeat | BNP Paribas Exane upgraded Synopsys from Underperform to Neutral on Sep 24 with a $420 target. | Fresh upgrade from Underperform to Neutral. |
| 6 | WELL | Welltower | bullish | medium | 2026-09-24 | 1 | 1 | MarketBeat | JPMorgan upgraded Welltower from Neutral to Overweight on Sep 24 and set a $260 target. | Fresh upgrade from Neutral to Overweight. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | PAYX | 0.298084 | volume_anomaly r7 s=0.9968; momentum_breakout r3 s=0.9699; stretched_reversal r1 s=1; wildcard r4 s=0.9328 | bullish_reversal | high | $104.53 | relative volume is 4.97x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 91% percentile, relative volume 4.97x; stock moved 4.19 ATR today and is 6.57 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 100% percentile, volatility expansion 95% percentile, stretch 100% percentile |
| 2 | ABNB | 0.249158 | volume_anomaly r17 s=0.9914; momentum_breakout r2 s=0.9699; stretched_reversal r2 s=0.997; wildcard r12 s=0.8412 | bullish_reversal | high | $149.44 | relative volume is 4.08x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 92% percentile, relative volume 4.08x; stock moved 2.82 ATR today and is 6.03 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 99% percentile, volatility expansion 90% percentile, stretch 99% percentile |
| 3 | PAY | 0.181818 | momentum_breakout r1 s=0.9767; compression_breakout r1 s=0.9783 | bearish | normal | $29.95 | bearish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 2.82x; 20-day bearish range breakout after volatility compression in the lowest 2% of recent history, with 2.82x normal volume |
| 4 | IUSB | 0.163736 | volume_anomaly r4 s=0.9984; stretched_reversal r29 s=0.9755; wildcard r5 s=0.884 | non_directional | high | $44.53 | relative volume is 5.33x its 20-day median; stock moved 2.78 ATR today and is 4.26 ATR from its 20-day mean; relaxed-liquidity stock showing volume 100% percentile, normalized move 99% percentile, volatility expansion 98% percentile, stretch 94% percentile |
| 5 | BFH | 0.154304 | volume_anomaly r18 s=0.9909; momentum_breakout r14 s=0.9287; compression_breakout r3 s=0.9538 | non_directional | normal | $99.19 | relative volume is 3.94x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 86% percentile, relative volume 3.94x; 20-day bearish range breakout after volatility compression in the lowest 7% of recent history, with 3.94x normal volume |
| 6 | WBD | 0.15 | volume_anomaly r5 s=0.9978; volatility_expansion r2 s=0.9995 | non_directional | normal | $30.76 | relative volume is 5.23x its 20-day median; 5-day realized volatility is 1.82x its 20-day level |
| 7 | MCD | 0.14787 | volume_anomaly r25 s=0.9871; stretched_reversal r5 s=0.9922; wildcard r9 s=0.8599 | bullish_reversal | high | $238.30 | relative volume is 3.70x its 20-day median; stock moved 3.27 ATR today and is 4.93 ATR from its 20-day mean; relaxed-liquidity stock showing volume 98% percentile, normalized move 100% percentile, volatility expansion 93% percentile, stretch 98% percentile |
| 8 | VMBS | 0.144444 | stretched_reversal r20 s=0.9839; volatility_expansion r8 s=0.9962; wildcard r8 s=0.8612 | non_directional | high | $44.87 | stock moved 2.78 ATR today and is 4.62 ATR from its 20-day mean; 5-day realized volatility is 1.66x its 20-day level; relaxed-liquidity stock showing volume 94% percentile, normalized move 99% percentile, volatility expansion 99% percentile, stretch 96% percentile |
| 9 | BKNG | 0.143541 | volume_anomaly r1 s=1; momentum_breakout r9 s=0.9364 | non_directional | normal | $155.90 | relative volume is 8.34x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 88% percentile, relative volume 8.34x |
| 10 | MBB | 0.135747 | volume_anomaly r3 s=0.9989; wildcard r7 s=0.8701 | non_directional | high | $90.53 | relative volume is 6.31x its 20-day median; relaxed-liquidity stock showing volume 100% percentile, normalized move 97% percentile, volatility expansion 98% percentile, stretch 95% percentile |
| 11 | PCVX | 0.126984 | volatility_expansion r4 s=0.9984; compression_breakout r8 s=0.9215 | non_directional | normal | $56.50 | 5-day realized volatility is 1.69x its 20-day level; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 2.21x normal volume |
| 12 | RSI | 0.119298 | volume_anomaly r9 s=0.9957; momentum_breakout r5 s=0.9597 | non_directional | normal | $20.55 | relative volume is 4.70x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 4.70x |
| 13 | NYT | 0.119048 | volume_anomaly r11 s=0.9946; momentum_breakout r4 s=0.9609 | non_directional | normal | $61.91 | relative volume is 4.15x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 4.15x |
| 14 | IEI | 0.1125 | stretched_reversal r6 s=0.9919; wildcard r10 s=0.8591 | bullish_reversal | high | $113.69 | stock moved 2.67 ATR today and is 5.54 ATR from its 20-day mean; relaxed-liquidity stock showing volume 96% percentile, normalized move 99% percentile, volatility expansion 95% percentile, stretch 99% percentile |
| 15 | FTDR | 0.102632 | momentum_breakout r10 s=0.9346; compression_breakout r9 s=0.9194 | bearish | normal | $73.98 | bearish 20-day breakout, 5-day momentum is in the 86% percentile, relative volume 2.81x; 20-day bearish range breakout after volatility compression in the lowest 18% of recent history, with 2.81x normal volume |
| 16 | FSLY | 0.091082 | volume_anomaly r21 s=0.9892; momentum_breakout r7 s=0.9507 | non_directional | normal | $29.65 | relative volume is 3.78x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 3.78x |
| 17 | STUB | 0.091082 | momentum_breakout r21 s=0.9149; compression_breakout r7 s=0.9246 | bearish | normal | $5.30 | bearish 20-day breakout, 5-day momentum is in the 90% percentile, relative volume 1.93x; 20-day bearish range breakout after volatility compression in the lowest 7% of recent history, with 1.93x normal volume |
| 18 | CGEM | 0.090909 | wildcard r1 s=0.9715 | bearish | high | $16.87 | relaxed-liquidity stock showing volume 98% percentile, normalized move 100% percentile, volatility expansion 100% percentile, stretch 99% percentile |
| 19 | ZTO | 0.090909 | volatility_expansion r1 s=1 | non_directional | normal | $19.62 | 5-day realized volatility is 1.82x its 20-day level |
| 20 | ACMR | 0.088889 | volume_anomaly r8 s=0.9962; momentum_breakout r20 s=0.9152 | non_directional | normal | $80.75 | relative volume is 4.76x its 20-day median; bullish 5-day momentum, 5-day momentum is in the 99% percentile, relative volume 4.76x |
