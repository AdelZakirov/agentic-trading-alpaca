# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-22
- Expert data generated at: 2026-09-23T15:15:17Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 40

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | CC | Chemours | 1 | all-stocks #21 22 mentions 575 upvotes; options #1 4 mentions 6 upvotes |
| 2 | SPY | SPDR S&amp;P 500 ETF Trust | 1 | all-stocks #1 243 mentions 611 upvotes; options #2 2 mentions 17 upvotes |
| 3 | MU | Micron Technology | 2 | all-stocks #2 240 mentions 983 upvotes; options #28 1 mentions 1 upvotes |
| 4 | META | Meta Platforms (Facebook) | 3 | all-stocks #3 157 mentions 600 upvotes |
| 5 | MSFT | Microsoft | 3 | all-stocks #1 51 mentions 241 upvotes; options #3 1 mentions 1 upvotes |
| 6 | AAPL | Apple | 4 | all-stocks #24 21 mentions 32 upvotes; options #4 1 mentions 1 upvotes |
| 7 | QQQ | Invesco QQQ ETF | 4 | all-stocks #4 108 mentions 443 upvotes |
| 8 | AMD | AMD | 5 | all-stocks #5 101 mentions 2718 upvotes; options #11 1 mentions 1 upvotes |
| 9 | AMZN | Amazon | 5 | all-stocks #2 23 mentions 190 upvotes; options #5 1 mentions 3 upvotes |
| 10 | GOOG | Alphabet (Google) | 6 | all-stocks #6 67 mentions 140 upvotes; options #6 1 mentions 2 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | CLDX | Celldex Therapeutics | bullish | high | 2026-09-22 to 2026-09-23 | 5 | 5 | MarketBeat | Five fresh actions on September 22–23 included four target raises across four firms. | Fresh multi-firm target activity, including four increases. |
| 2 | CMPX | Compass Therapeutics | bearish | high | 2026-09-22 to 2026-09-23 | 2 | 2 | MarketBeat | Two fresh bearish actions: Wedbush downgraded and cut its target; Citizens JMP lowered its target. | Fresh bearish actions from two distinct firms. |
| 3 | CIFR | Cipher Mining | bearish | high | 2026-09-21 | 2 | 2 | MarketBeat | Two fresh firm actions included a Weiss sell reiteration and a neutral Rothschild Redburn initiation. | Recent multi-firm attention includes an explicit sell rating. |
| 4 | MGY | Magnolia Oil & Gas | bullish | medium | 2026-09-23 | 1 | 1 | MarketBeat | Siebert Williams Shank upgraded the rating from Hold to Buy and raised its target from $30 to $32. | Fresh rating upgrade with a target increase. |
| 5 | CRMD | CorMedix | bullish | medium | 2026-09-23 | 1 | 1 | MarketBeat | Oppenheimer initiated coverage with an Outperform rating and a $15 target. | Fresh directional initiation with a published target. |
| 6 | CMI | Cummins | bearish | medium | 2026-09-23 | 1 | 1 | MarketBeat | JPMorgan lowered its target from $690 to $600 while maintaining a Neutral rating. | Fresh material target reduction. |
| 7 | GPK | Graphic Packaging | mixed | medium | 2026-09-23 | 1 | 1 | MarketBeat | JPMorgan upgraded Neutral to Overweight while reducing its target from $12.50 to $11.50. | Fresh rating upgrade with an offsetting lower target. |
| 8 | APH | Amphenol | bullish | low | 2026-09-22 | 1 | 1 | MarketBeat | BNP Paribas Exane raised its target from $107.50 to $110 and kept Outperform. | Single fresh, modest target increase. |
| 9 | CORZ | Core Scientific | neutral | low | 2026-09-21 | 1 | 1 | MarketBeat | Rothschild & Co Redburn initiated coverage at Neutral with a $16 target on September 21. | Fresh neutral initiation. |
| 10 | APLD | Applied Digital | neutral | low | 2026-09-21 | 1 | 1 | MarketBeat | Rothschild & Co Redburn set a Neutral rating and $22 target on September 21. | Fresh analyst target setting. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | VKTX | 0.406656 | volume_anomaly r6 s=0.9973; momentum_breakout r1 s=0.9971; stretched_reversal r1 s=0.9997; volatility_expansion r4 s=0.9984; wildcard r1 s=0.9918 | bearish_reversal | high | $40.83 | relative volume is 9.38x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 9.38x; stock moved 7.50 ATR today and is 5.95 ATR from its 20-day mean; 5-day realized volatility is 1.71x its 20-day level; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 100% percentile, stretch 100% percentile |
| 2 | RMBS | 0.24807 | volume_anomaly r21 s=0.9892; momentum_breakout r2 s=0.9901; stretched_reversal r8 s=0.9898; compression_breakout r3 s=0.9722 | bullish | normal | $105.28 | relative volume is 4.66x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 4.66x; stock moved 2.12 ATR today and is 4.76 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 7% of recent history, with 4.66x normal volume |
| 3 | VICR | 0.215812 | momentum_breakout r3 s=0.9792; stretched_reversal r2 s=0.9992; compression_breakout r8 s=0.9408 | bearish_reversal | normal | $267.87 | bullish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 2.47x; stock moved 3.29 ATR today and is 5.72 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 12% of recent history, with 2.47x normal volume |
| 4 | LPLA | 0.215675 | volume_anomaly r10 s=0.9952; momentum_breakout r11 s=0.9564; stretched_reversal r6 s=0.9925; wildcard r8 s=0.9252 | non_directional | high | $307.44 | relative volume is 6.02x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 88% percentile, relative volume 6.02x; stock moved 2.64 ATR today and is 4.70 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 99% percentile, volatility expansion 97% percentile, stretch 99% percentile |
| 5 | ALL | 0.197378 | volume_anomaly r30 s=0.9844; momentum_breakout r10 s=0.9574; stretched_reversal r3 s=0.997; compression_breakout r12 s=0.9331 | bullish_reversal | normal | $229.42 | relative volume is 3.94x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 89% percentile, relative volume 3.94x; stock moved 2.69 ATR today and is 5.37 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 18% of recent history, with 3.94x normal volume |
| 6 | RCL | 0.196919 | stretched_reversal r5 s=0.9938; volatility_expansion r7 s=0.9968; wildcard r4 s=0.9415 | non_directional | high | $234.84 | stock moved 2.44 ATR today and is 4.93 ATR from its 20-day mean; 5-day realized volatility is 1.66x its 20-day level; relaxed-liquidity stock showing volume 97% percentile, normalized move 99% percentile, volatility expansion 100% percentile, stretch 99% percentile |
| 7 | PLNT | 0.188312 | momentum_breakout r4 s=0.9765; stretched_reversal r4 s=0.9965; wildcard r12 s=0.854 | bullish_reversal | high | $42.67 | bearish 20-day breakout, 5-day momentum is in the 95% percentile, relative volume 3.46x; stock moved 2.78 ATR today and is 5.31 ATR from its 20-day mean; relaxed-liquidity stock showing volume 97% percentile, normalized move 100% percentile, volatility expansion 92% percentile, stretch 99% percentile |
| 8 | BAI | 0.176557 | volume_anomaly r4 s=0.9984; momentum_breakout r16 s=0.9481; compression_breakout r5 s=0.9568 | non_directional | normal | $47.64 | relative volume is 13.50x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 91% percentile, relative volume 13.50x; 20-day bullish range breakout after volatility compression in the lowest 7% of recent history, with 13.50x normal volume |
| 9 | NKTR | 0.174426 | volume_anomaly r16 s=0.9919; momentum_breakout r20 s=0.944; stretched_reversal r10 s=0.9887; wildcard r9 s=0.8945 | non_directional | high | $60.91 | relative volume is 5.33x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 84% percentile, relative volume 5.33x; stock moved 2.35 ATR today and is 4.25 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 99% percentile, volatility expansion 95% percentile, stretch 98% percentile |
| 10 | PGR | 0.161414 | volume_anomaly r13 s=0.9935; stretched_reversal r27 s=0.9488; compression_breakout r1 s=0.9783 | non_directional | normal | $206.95 | relative volume is 5.49x its 20-day median; stock moved 1.55 ATR today and is 3.42 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 5% of recent history, with 5.49x normal volume |
| 11 | BLLN | 0.160563 | momentum_breakout r19 s=0.945; stretched_reversal r16 s=0.982; volatility_expansion r15 s=0.9925; wildcard r11 s=0.8687 | non_directional | high | $116.16 | bullish 20-day breakout, 5-day momentum is in the 91% percentile, relative volume 2.61x; stock moved 2.80 ATR today and is 3.84 ATR from its 20-day mean; 5-day realized volatility is 1.61x its 20-day level; relaxed-liquidity stock showing volume 95% percentile, normalized move 100% percentile, volatility expansion 99% percentile, stretch 96% percentile |
| 12 | PLXS | 0.151905 | momentum_breakout r15 s=0.9526; stretched_reversal r25 s=0.9585; compression_breakout r2 s=0.9726 | bullish | normal | $263.56 | bullish 20-day breakout, 5-day momentum is in the 89% percentile, relative volume 3.39x; stock moved 1.90 ATR today and is 3.43 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 5% of recent history, with 3.39x normal volume |
| 13 | GEN | 0.14824 | momentum_breakout r13 s=0.9546; stretched_reversal r20 s=0.965; compression_breakout r4 s=0.9586 | bullish_reversal | normal | $27.30 | bearish 20-day breakout, 5-day momentum is in the 92% percentile, relative volume 2.62x; stock moved 2.18 ATR today and is 3.45 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 7% of recent history, with 2.62x normal volume |
| 14 | TWLO | 0.145978 | momentum_breakout r6 s=0.9695; stretched_reversal r15 s=0.9825; compression_breakout r13 s=0.9319 | bearish_reversal | normal | $284.65 | bullish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 2.60x; stock moved 1.78 ATR today and is 4.74 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 15% of recent history, with 2.60x normal volume |
| 15 | MUD | 0.114286 | momentum_breakout r5 s=0.9707; compression_breakout r11 s=0.9333 | bearish | normal | $8.84 | bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 3.03x; 20-day bearish range breakout after volatility compression in the lowest 15% of recent history, with 3.03x normal volume |
| 16 | UNG | 0.097222 | volume_anomaly r8 s=0.9962; compression_breakout r14 s=0.9243 | non_directional | normal | $10.85 | relative volume is 6.36x its 20-day median; 20-day bullish range breakout after volatility compression in the lowest 7% of recent history, with 6.36x normal volume |
| 17 | SCHW | 0.091667 | stretched_reversal r14 s=0.9838; wildcard r10 s=0.8765 | bullish_reversal | high | $100.36 | stock moved 3.25 ATR today and is 3.92 ATR from its 20-day mean; relaxed-liquidity stock showing volume 96% percentile, normalized move 100% percentile, volatility expansion 98% percentile, stretch 96% percentile |
| 18 | MBB | 0.090909 | volume_anomaly r1 s=1 | non_directional | normal | $91.46 | relative volume is 22.50x its 20-day median |
| 19 | ZTO | 0.090909 | volatility_expansion r1 s=1 | non_directional | normal | $19.84 | 5-day realized volatility is 1.82x its 20-day level |
| 20 | ACWX | 0.083333 | volume_anomaly r2 s=0.9995 | non_directional | normal | $77.87 | relative volume is 18.15x its 20-day median |
