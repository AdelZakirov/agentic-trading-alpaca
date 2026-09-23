# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-18
- Expert data generated at: 2026-09-21T14:06:12Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 37

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | IBKR | Interactive Brokers | 1 | all-stocks #3 8 mentions 19 upvotes; options #1 4 mentions 13 upvotes |
| 2 | MU | Micron Technology | 1 | all-stocks #1 126 mentions 1131 upvotes; options #24 1 mentions 1 upvotes |
| 3 | ET | Energy Transfer Partners | 2 | all-stocks #27 9 mentions 189 upvotes; options #2 3 mentions 12 upvotes |
| 4 | SPY | SPDR S&amp;P 500 ETF Trust | 2 | all-stocks #2 89 mentions 467 upvotes |
| 5 | AAPL | Apple | 3 | all-stocks #48 6 mentions 4 upvotes; options #3 1 mentions 2 upvotes |
| 6 | AMD | AMD | 3 | all-stocks #3 78 mentions 170 upvotes; options #9 1 mentions 1 upvotes |
| 7 | GOOG | Alphabet (Google) | 4 | all-stocks #18 11 mentions 16 upvotes; options #4 1 mentions 3 upvotes |
| 8 | META | Meta Platforms (Facebook) | 4 | all-stocks #4 49 mentions 119 upvotes |
| 9 | MA | Mastercard | 5 | options #5 1 mentions 1 upvotes |
| 10 | SNDK | Sandisk | 5 | all-stocks #5 49 mentions 89 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | CADL | Candel Therapeutics | bullish | high | 2026-09-21 | 1 | 1 | MarketBeat | Bank of America upgraded Candel Therapeutics from Neutral to Buy and raised its target from $12 to $18 on 2026-09-21. | Fresh bullish upgrade with a material target increase. |
| 2 | SECZ | Securitize | bullish | high | 2026-09-21 | 2 | 2 | MarketBeat | Securitize received a fresh Cantor Fitzgerald initiation at Overweight and a same-day Rosenblatt target raise to $13 on 2026-09-21. | Fresh multi-firm bullish attention combining an initiation and a target raise. |
| 3 | NNE | Nano Nuclear Energy | bullish | high | 2026-09-21 | 1 | 1 | MarketBeat | Needham initiated coverage of Nano Nuclear Energy with a Buy rating and a $33 target on 2026-09-21. | Fresh bullish initiation with a published target. |
| 4 | VECO | Veeco Instruments | bullish | high | 2026-09-21 | 1 | 1 | MarketBeat | Northland Securities upgraded Veeco Instruments from Market Perform to Outperform with a $66 target on 2026-09-21. | Fresh bullish upgrade with a published target. |
| 5 | AMH | American Homes 4 Rent | bullish | medium | 2026-09-21 | 1 | 1 | MarketBeat | Mizuho upgraded American Homes 4 Rent from Neutral to Outperform and raised its target from $35 to $36 on 2026-09-21. | Fresh bullish upgrade with a modest target increase. |
| 6 | T | AT&T | bullish | medium | 2026-09-21 | 1 | 1 | MarketBeat | BNP Paribas Exane upgraded AT&T from Neutral to Outperform with a $30 target on 2026-09-21. | Fresh bullish upgrade with a published target. |
| 7 | CORZ | Core Scientific | bullish | medium | 2026-09-17 | 1 | 1 | MarketBeat | Wells Fargo initiated Core Scientific coverage at Overweight with a $28 target on 2026-09-17. | Recent bullish initiation with a published target inside the short lookback window. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | GENI | 0.342075 | volume_anomaly r1 s=1; momentum_breakout r1 s=0.996; stretched_reversal r2 s=0.9924; wildcard r3 s=0.8328 | non_directional | high | $5.63 | relative volume is 6.78x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 6.78x; stock moved 2.30 ATR today and is 4.65 ATR from its 20-day mean; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, stretch 99% percentile |
| 2 | AN | 0.19 | volume_anomaly r15 s=0.9924; momentum_breakout r2 s=0.9863; wildcard r5 s=0.7394 | non_directional | high | $168.40 | relative volume is 3.50x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 3.50x; relaxed-liquidity stock showing volume 98% percentile, volatility expansion 95% percentile, stretch 99% percentile |
| 3 | WU | 0.174145 | momentum_breakout r14 s=0.9457; stretched_reversal r3 s=0.9889; wildcard r8 s=0.6878 | bullish_reversal | high | $6.18 | bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 1.86x; stock moved 1.88 ATR today and is 4.77 ATR from its 20-day mean; relaxed-liquidity stock showing normalized move 98% percentile, volatility expansion 92% percentile, stretch 99% percentile |
| 4 | GM | 0.162959 | volume_anomaly r25 s=0.987; compression_breakout r1 s=0.9756; wildcard r13 s=0.6496 | non_directional | high | $82.21 | relative volume is 3.28x its 20-day median; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 3.28x normal volume; relaxed-liquidity stock showing volume 98% percentile, normalized move 98% percentile, volatility expansion 96% percentile |
| 5 | NFLX | 0.161998 | momentum_breakout r11 s=0.95; stretched_reversal r7 s=0.9502; compression_breakout r8 s=0.9406 | bullish_reversal | normal | $71.80 | bearish 20-day breakout, 5-day momentum is in the 89% percentile, relative volume 2.51x; stock moved 1.59 ATR today and is 3.41 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 13% of recent history, with 2.51x normal volume |
| 6 | ALKS | 0.157287 | stretched_reversal r8 s=0.9478; volatility_expansion r23 s=0.9881; wildcard r4 s=0.7636 | non_directional | high | $43.42 | stock moved 2.83 ATR today and is 3.14 ATR from its 20-day mean; 5-day realized volatility is 1.63x its 20-day level; relaxed-liquidity stock showing volume 94% percentile, normalized move 100% percentile, volatility expansion 99% percentile |
| 7 | RCAT | 0.150548 | volume_anomaly r22 s=0.9886; momentum_breakout r5 s=0.9731; compression_breakout r9 s=0.9404 | non_directional | normal | $6.77 | relative volume is 3.32x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 3.32x; 20-day bearish range breakout after volatility compression in the lowest 12% of recent history, with 3.32x normal volume |
| 8 | PEP | 0.149733 | stretched_reversal r1 s=0.9962; wildcard r7 s=0.6939 | bullish_reversal | high | $129.62 | stock moved 2.14 ATR today and is 5.08 ATR from its 20-day mean; relaxed-liquidity stock showing volume 97% percentile, normalized move 99% percentile, stretch 99% percentile |
| 9 | L | 0.142857 | volume_anomaly r4 s=0.9984; compression_breakout r4 s=0.9567 | non_directional | normal | $107.75 | relative volume is 4.80x its 20-day median; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 4.80x normal volume |
| 10 | ALHC | 0.140461 | volume_anomaly r19 s=0.9903; momentum_breakout r13 s=0.9457; wildcard r6 s=0.7041 | non_directional | high | $8.33 | relative volume is 3.34x its 20-day median; bearish 5-day momentum, 5-day momentum is in the 100% percentile, relative volume 3.34x; relaxed-liquidity stock showing volume 98% percentile, volatility expansion 99% percentile, stretch 100% percentile |
| 11 | FPS | 0.139423 | momentum_breakout r3 s=0.9848; compression_breakout r6 s=0.9469 | bullish | normal | $39.49 | bullish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 2.98x; 20-day bullish range breakout after volatility compression in the lowest 12% of recent history, with 2.98x normal volume |
| 12 | BCS | 0.129937 | volume_anomaly r10 s=0.9951; momentum_breakout r19 s=0.9302; stretched_reversal r12 s=0.9261 | non_directional | normal | $24.86 | relative volume is 3.74x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 88% percentile, relative volume 3.74x; stock moved 1.51 ATR today and is 3.07 ATR from its 20-day mean |
| 13 | BTU | 0.126923 | momentum_breakout r10 s=0.961; stretched_reversal r16 s=0.8901; compression_breakout r16 s=0.917 | bearish | normal | $25.14 | bearish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 2.14x; stock moved 1.82 ATR today and is 2.65 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 17% of recent history, with 2.14x normal volume |
| 14 | KD | 0.115385 | momentum_breakout r16 s=0.9424; compression_breakout r3 s=0.9677 | bearish | normal | $12.05 | bearish 20-day breakout, 5-day momentum is in the 92% percentile, relative volume 2.53x; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 2.53x normal volume |
| 15 | DNTH | 0.10101 | momentum_breakout r8 s=0.9632; compression_breakout r12 s=0.9336 | bearish | normal | $96.81 | bearish 20-day breakout, 5-day momentum is in the 94% percentile, relative volume 2.60x; 20-day bearish range breakout after volatility compression in the lowest 15% of recent history, with 2.60x normal volume |
| 16 | ARQT | 0.09697 | volume_anomaly r23 s=0.9881; volatility_expansion r5 s=0.9978 | non_directional | normal | $25.37 | relative volume is 3.30x its 20-day median; 5-day realized volatility is 1.69x its 20-day level |
| 17 | WEN | 0.096429 | volume_anomaly r30 s=0.9843; momentum_breakout r4 s=0.9814 | non_directional | normal | $6.73 | relative volume is 3.11x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 3.11x |
| 18 | FANG | 0.095861 | volume_anomaly r17 s=0.9913; volatility_expansion r7 s=0.9968 | non_directional | normal | $192.43 | relative volume is 3.48x its 20-day median; 5-day realized volatility is 1.69x its 20-day level |
| 19 | MSTR | 0.094298 | momentum_breakout r9 s=0.9614; stretched_reversal r14 s=0.909 | bullish | normal | $153.91 | bullish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 2.00x; stock moved 2.44 ATR today and is 2.75 ATR from its 20-day mean |
| 20 | VC | 0.092803 | momentum_breakout r23 s=0.9285; stretched_reversal r6 s=0.9599 | bullish_reversal | normal | $94.50 | bearish 20-day breakout, 5-day momentum is in the 85% percentile, relative volume 2.33x; stock moved 1.78 ATR today and is 3.50 ATR from its 20-day mean |
