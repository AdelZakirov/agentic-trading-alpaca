# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-17
- Expert data generated at: 2026-09-18T14:05:08Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 33

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | MSFT | Microsoft | 1 | all-stocks #34 16 mentions 33 upvotes; options #1 1 mentions 1 upvotes |
| 2 | SPY | SPDR S&amp;P 500 ETF Trust | 1 | all-stocks #1 232 mentions 642 upvotes |
| 3 | AAPL | Apple | 2 | all-stocks #28 23 mentions 32 upvotes; options #2 1 mentions 1 upvotes |
| 4 | QQQ | Invesco QQQ ETF | 2 | all-stocks #2 105 mentions 203 upvotes |
| 5 | GOOG | Alphabet (Google) | 3 | all-stocks #21 28 mentions 75 upvotes; options #3 1 mentions 3 upvotes |
| 6 | MU | Micron Technology | 3 | all-stocks #3 86 mentions 212 upvotes; options #27 1 mentions 1 upvotes |
| 7 | INTC | Intel | 4 | all-stocks #4 67 mentions 128 upvotes; options #7 1 mentions 5 upvotes |
| 8 | WMT | Walmart | 4 | options #4 1 mentions 4 upvotes |
| 9 | AMD | AMD | 5 | all-stocks #5 59 mentions 444 upvotes; options #1 1 mentions 2 upvotes |
| 10 | MA | Mastercard | 5 | options #5 1 mentions 1 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | CCK | Crown | bullish | medium | 2026-09-18 | 1 | 1 | MarketBeat | JPMorgan upgraded Crown from Neutral to Overweight with a $121 target on 2026-09-18. | Fresh dated bullish upgrade from a major brokerage. |
| 2 | DT | Dynatrace | bullish | medium | 2026-09-18 | 1 | 1 | MarketBeat | Needham upgraded Dynatrace from Hold to Buy and set a $68 target on 2026-09-18. | Fresh dated bullish rating upgrade with a published target. |
| 3 | ETSY | Etsy | bullish | medium | 2026-09-18 | 1 | 1 | MarketBeat | BTIG upgraded Etsy from Neutral to Buy and set a $90 target on 2026-09-18. | Fresh dated bullish rating upgrade with a published target. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | FLNC | 0.344239 | volume_anomaly r12 s=0.9941; momentum_breakout r1 s=0.9957; stretched_reversal r2 s=0.9949; compression_breakout r11 s=0.9312; wildcard r3 s=0.8312 | bearish | high | $7.65 | relative volume is 4.70x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 4.70x; stock moved 2.46 ATR today and is 5.11 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 20% of recent history, with 4.70x normal volume; relaxed-liquidity stock showing volume 99% percentile, normalized move 100% percentile, stretch 99% percentile |
| 2 | AN | 0.323975 | volume_anomaly r7 s=0.9968; momentum_breakout r2 s=0.9935; stretched_reversal r1 s=0.9987; wildcard r1 s=0.9483 | bullish_reversal | high | $175.15 | relative volume is 5.54x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 5.54x; stock moved 3.93 ATR today and is 5.34 ATR from its 20-day mean; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 97% percentile, stretch 100% percentile |
| 3 | FPS | 0.222756 | volume_anomaly r6 s=0.9973; momentum_breakout r3 s=0.9896; compression_breakout r2 s=0.9733 | non_directional | normal | $38.07 | relative volume is 5.58x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 5.58x; 20-day bullish range breakout after volatility compression in the lowest 5% of recent history, with 5.58x normal volume |
| 4 | MTZ | 0.222619 | volume_anomaly r30 s=0.9844; momentum_breakout r5 s=0.9797; stretched_reversal r11 s=0.9725; wildcard r2 s=0.8489 | non_directional | high | $207.75 | relative volume is 3.54x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 3.54x; stock moved 1.87 ATR today and is 3.70 ATR from its 20-day mean; relaxed-liquidity stock showing volume 98% percentile, normalized move 99% percentile, volatility expansion 96% percentile, stretch 95% percentile |
| 5 | ENVA | 0.21699 | volume_anomaly r16 s=0.9919; momentum_breakout r15 s=0.9644; volatility_expansion r1 s=1; wildcard r11 s=0.7328 | non_directional | high | $179.73 | relative volume is 4.15x its 20-day median; bearish 5-day momentum, 5-day momentum is in the 99% percentile, relative volume 4.15x; 5-day realized volatility is 1.82x its 20-day level; relaxed-liquidity stock showing volume 99% percentile, volatility expansion 100% percentile, stretch 99% percentile |
| 6 | GNRC | 0.196078 | volume_anomaly r2 s=0.9995; stretched_reversal r24 s=0.8765; volatility_expansion r20 s=0.9898; wildcard r10 s=0.7369 | non_directional | high | $207.36 | relative volume is 6.91x its 20-day median; stock moved 4.42 ATR today and is 2.33 ATR from its 20-day mean; 5-day realized volatility is 1.64x its 20-day level; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 99% percentile |
| 7 | TEM | 0.180252 | momentum_breakout r4 s=0.9831; stretched_reversal r10 s=0.9728; compression_breakout r7 s=0.9498 | bullish | normal | $80.32 | bullish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 2.47x; stock moved 2.47 ATR today and is 3.66 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 10% of recent history, with 2.47x normal volume |
| 8 | ARE | 0.178023 | momentum_breakout r9 s=0.9723; stretched_reversal r19 s=0.9167; compression_breakout r1 s=0.9797 | bullish | normal | $56.33 | bullish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 2.39x; stock moved 1.85 ATR today and is 2.80 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 0% of recent history, with 2.39x normal volume |
| 9 | TMUS | 0.172019 | momentum_breakout r27 s=0.9453; stretched_reversal r17 s=0.9512; compression_breakout r12 s=0.927; wildcard r6 s=0.7778 | bullish_reversal | high | $166.42 | bearish 20-day breakout, 5-day momentum is in the 85% percentile, relative volume 3.42x; stock moved 2.12 ATR today and is 3.25 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 20% of recent history, with 3.42x normal volume; relaxed-liquidity stock showing volume 98% percentile, normalized move 99% percentile, volatility expansion 94% percentile, stretch 91% percentile |
| 10 | NVST | 0.170462 | momentum_breakout r13 s=0.966; stretched_reversal r8 s=0.9798; wildcard r4 s=0.8012 | bullish_reversal | high | $23.68 | bearish 20-day breakout, 5-day momentum is in the 93% percentile, relative volume 2.96x; stock moved 1.77 ATR today and is 4.20 ATR from its 20-day mean; relaxed-liquidity stock showing volume 97% percentile, normalized move 98% percentile, volatility expansion 91% percentile, stretch 97% percentile |
| 11 | XRAY | 0.154933 | momentum_breakout r7 s=0.9775; stretched_reversal r13 s=0.9628; wildcard r9 s=0.7483 | bearish | high | $9.38 | bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 3.22x; stock moved 1.81 ATR today and is 3.52 ATR from its 20-day mean; relaxed-liquidity stock showing volume 98% percentile, normalized move 99% percentile, stretch 94% percentile |
| 12 | ARKG | 0.151923 | momentum_breakout r14 s=0.9651; stretched_reversal r20 s=0.9159; compression_breakout r3 s=0.9723 | bullish | normal | $51.58 | bullish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 2.18x; stock moved 2.56 ATR today and is 2.74 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 0% of recent history, with 2.18x normal volume |
| 13 | ALHC | 0.146465 | volume_anomaly r8 s=0.9962; momentum_breakout r12 s=0.9682; wildcard r12 s=0.7254 | non_directional | high | $8.70 | relative volume is 5.20x its 20-day median; bearish 5-day momentum, 5-day momentum is in the 100% percentile, relative volume 5.20x; relaxed-liquidity stock showing volume 100% percentile, volatility expansion 99% percentile, stretch 100% percentile |
| 14 | WGS | 0.140278 | momentum_breakout r26 s=0.9479; stretched_reversal r6 s=0.9881; compression_breakout r10 s=0.9319 | bearish_reversal | normal | $104.95 | bullish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 1.72x; stock moved 1.93 ATR today and is 4.57 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 5% of recent history, with 1.72x normal volume |
| 15 | LAD | 0.129167 | momentum_breakout r6 s=0.9788; stretched_reversal r5 s=0.9895 | bullish_reversal | normal | $321.86 | bearish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 2.90x; stock moved 1.85 ATR today and is 4.86 ATR from its 20-day mean |
| 16 | ATRO | 0.103175 | momentum_breakout r11 s=0.9691; compression_breakout r8 s=0.9354 | bearish | normal | $64.95 | bearish 20-day breakout, 5-day momentum is in the 97% percentile, relative volume 3.10x; 20-day bearish range breakout after volatility compression in the lowest 13% of recent history, with 3.10x normal volume |
| 17 | TMO | 0.102679 | momentum_breakout r22 s=0.9542; compression_breakout r4 s=0.9673 | bullish | normal | $658.69 | bullish 20-day breakout, 5-day momentum is in the 94% percentile, relative volume 2.50x; 20-day bullish range breakout after volatility compression in the lowest 2% of recent history, with 2.50x normal volume |
| 18 | VBIL | 0.090909 | volume_anomaly r1 s=1 | non_directional | normal | $75.61 | relative volume is 7.02x its 20-day median |
| 19 | ILMN | 0.09 | momentum_breakout r10 s=0.9707; stretched_reversal r15 s=0.9536 | bullish | normal | $245.33 | bullish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 2.11x; stock moved 1.82 ATR today and is 3.32 ATR from its 20-day mean |
| 20 | ARQT | 0.088346 | volume_anomaly r9 s=0.9957; momentum_breakout r18 s=0.9604 | non_directional | normal | $26.49 | relative volume is 5.06x its 20-day median; bullish 5-day momentum, 5-day momentum is in the 98% percentile, relative volume 5.06x |
