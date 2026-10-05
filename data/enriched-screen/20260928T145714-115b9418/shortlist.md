# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-25
- Expert data generated at: 2026-09-28T14:42:05Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 36

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | IBKR | Interactive Brokers | 1 | all-stocks #34 9 mentions 160 upvotes; options #1 6 mentions 2 upvotes |
| 2 | MU | Micron Technology | 1 | all-stocks #1 161 mentions 451 upvotes; options #26 1 mentions 1 upvotes |
| 3 | API | Agora.io | 2 | all-stocks #43 7 mentions 10 upvotes; options #2 4 mentions 3 upvotes |
| 4 | SPY | SPDR S&amp;P 500 ETF Trust | 2 | all-stocks #2 110 mentions 490 upvotes |
| 5 | AMD | AMD | 3 | all-stocks #5 46 mentions 319 upvotes; options #3 2 mentions 2 upvotes |
| 6 | NVDA | NVIDIA | 3 | all-stocks #3 108 mentions 837 upvotes; options #11 1 mentions 1 upvotes |
| 7 | META | Meta Platforms (Facebook) | 4 | all-stocks #4 80 mentions 314 upvotes |
| 8 | MSFT | Microsoft | 4 | all-stocks #6 32 mentions 49 upvotes; options #4 1 mentions 1 upvotes |
| 9 | AAPL | Apple | 5 | all-stocks #16 18 mentions 26 upvotes; options #5 1 mentions 1 upvotes |
| 10 | AMZN | Amazon | 6 | all-stocks #15 19 mentions 269 upvotes; options #6 1 mentions 1 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | TFX | Teleflex | bullish | high | 2026-09-24 to 2026-09-28 | 2 | 2 | MarketBeat | Two firms upgraded Teleflex within the lookback window, including Bank of America on Sep. 28. | Two recent upgrades from distinct firms, including a same-day rating and target increase. |
| 2 | LBRT | Liberty Energy | bullish | medium | 2026-09-28 | 1 | 1 | MarketBeat | Barclays upgraded Liberty Energy to Overweight from Equal Weight on Sep. 28. | Fresh rating upgrade with a published $27 target. |
| 3 | RCL | Royal Caribbean Cruises | bullish | high | 2026-09-24 | 2 | 2 | MarketBeat | Two firms raised Royal Caribbean price targets on Sep. 24, including JPMorgan from $345 to $394. | Same-day target increases from two distinct firms, including a substantial revision. |
| 4 | SPTX | Seaport Therapeutics | bullish | medium | 2026-09-25 | 1 | 1 | MarketBeat | Raymond James initiated coverage with a Strong-Buy rating and a $46 target on Sep. 25. | Fresh coverage initiation with a clearly directional rating and target. |
| 5 | CF | CF Industries | bullish | medium | 2026-09-25 | 1 | 1 | MarketBeat | Sanford C. Bernstein initiated CF Industries coverage at Outperform with a $162 target on Sep. 25. | Fresh initiation with a clearly directional rating and a published target. |
| 6 | SFIX | Stitch Fix | bearish | high | 2026-09-24 | 5 | 5 | MarketBeat | Five firms acted on Sep. 24; UBS and Telsey cut targets, and William Blair downgraded its rating. | Cluster of fresh bearish actions from five distinct firms, including a downgrade and two target cuts. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | MGM | 0.308608 | volume_anomaly r4 s=0.9984; momentum_breakout r3 s=0.99; volatility_expansion r3 s=0.9989; wildcard r2 s=0.8928 | non_directional | high | $32.58 | relative volume is 5.63x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 5.63x; 5-day realized volatility is 1.77x its 20-day level; relaxed-liquidity stock showing volume 100% percentile, normalized move 92% percentile, volatility expansion 100% percentile, stretch 100% percentile |
| 2 | ACAD | 0.249072 | volume_anomaly r28 s=0.9857; momentum_breakout r2 s=0.9942; stretched_reversal r6 s=0.9908; wildcard r3 s=0.877 | bearish | high | $20.68 | relative volume is 3.18x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 3.18x; stock moved 1.58 ATR today and is 7.21 ATR from its 20-day mean; relaxed-liquidity stock showing volume 98% percentile, normalized move 98% percentile, volatility expansion 93% percentile, stretch 100% percentile |
| 3 | USFR | 0.248485 | stretched_reversal r1 s=0.9992; volatility_expansion r5 s=0.9979; wildcard r1 s=0.966 | bullish_reversal | high | $50.35 | stock moved 11.94 ATR today and is 6.61 ATR from its 20-day mean; 5-day realized volatility is 1.75x its 20-day level; relaxed-liquidity stock showing volume 98% percentile, normalized move 100% percentile, volatility expansion 100% percentile, stretch 100% percentile |
| 4 | GEN | 0.207832 | volume_anomaly r3 s=0.9989; momentum_breakout r1 s=0.9986; wildcard r15 s=0.6893 | non_directional | high | $21.61 | relative volume is 5.64x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 5.64x; relaxed-liquidity stock showing volume 100% percentile, normalized move 95% percentile, stretch 100% percentile |
| 5 | PPLI | 0.206999 | volume_anomaly r17 s=0.9916; momentum_breakout r11 s=0.9479; stretched_reversal r16 s=0.8503; volatility_expansion r22 s=0.9889; wildcard r9 s=0.7221 | non_directional | high | $40.02 | relative volume is 3.71x its 20-day median; bullish 5-day momentum, 5-day momentum is in the 96% percentile, relative volume 3.71x; stock moved 4.13 ATR today and is 2.22 ATR from its 20-day mean; 5-day realized volatility is 1.59x its 20-day level; relaxed-liquidity stock showing volume 99% percentile, normalized move 100% percentile, volatility expansion 99% percentile |
| 6 | AESI | 0.200442 | volume_anomaly r2 s=0.9995; momentum_breakout r22 s=0.938; volatility_expansion r23 s=0.9884; wildcard r8 s=0.7241 | non_directional | high | $12.45 | relative volume is 6.25x its 20-day median; bearish 5-day momentum, 5-day momentum is in the 92% percentile, relative volume 6.25x; 5-day realized volatility is 1.59x its 20-day level; relaxed-liquidity stock showing volume 100% percentile, normalized move 99% percentile, volatility expansion 99% percentile |
| 7 | VIAV | 0.199375 | momentum_breakout r4 s=0.975; stretched_reversal r17 s=0.8398; compression_breakout r1 s=0.9798 | bullish | normal | $40.69 | bullish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 2.79x; stock moved 1.65 ATR today and is 2.19 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 0% of recent history, with 2.79x normal volume |
| 8 | VKTX | 0.197352 | volume_anomaly r11 s=0.9947; momentum_breakout r7 s=0.9623; volatility_expansion r1 s=1 | non_directional | normal | $35.53 | relative volume is 4.41x its 20-day median; bullish 5-day momentum, 5-day momentum is in the 100% percentile, relative volume 4.41x; 5-day realized volatility is 1.84x its 20-day level |
| 9 | SBLK | 0.171679 | volume_anomaly r18 s=0.991; momentum_breakout r9 s=0.9583; compression_breakout r2 s=0.9695 | non_directional | normal | $29.54 | relative volume is 3.67x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 93% percentile, relative volume 3.67x; 20-day bearish range breakout after volatility compression in the lowest 3% of recent history, with 3.67x normal volume |
| 10 | MCHP | 0.145911 | momentum_breakout r19 s=0.9407; stretched_reversal r15 s=0.8503; compression_breakout r4 s=0.9547 | bullish | normal | $78.64 | bullish 20-day breakout, 5-day momentum is in the 89% percentile, relative volume 2.12x; stock moved 1.65 ATR today and is 2.29 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 7% of recent history, with 2.12x normal volume |
| 11 | AKAM | 0.143452 | volume_anomaly r6 s=0.9974; momentum_breakout r20 s=0.9402; volatility_expansion r11 s=0.9947 | non_directional | normal | $113.87 | relative volume is 5.01x its 20-day median; bullish 5-day momentum, 5-day momentum is in the 93% percentile, relative volume 5.01x; 5-day realized volatility is 1.65x its 20-day level |
| 12 | CDNA | 0.133333 | momentum_breakout r5 s=0.9748; wildcard r5 s=0.818 | bullish | high | $63.68 | bullish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 2.81x; relaxed-liquidity stock showing volume 98% percentile, normalized move 91% percentile, volatility expansion 98% percentile, stretch 99% percentile |
| 13 | DRI | 0.124542 | stretched_reversal r11 s=0.9044; compression_breakout r3 s=0.9574 | bearish | normal | $199.77 | stock moved 1.65 ATR today and is 2.79 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 1.76x normal volume |
| 14 | AAON | 0.118056 | momentum_breakout r8 s=0.9608; compression_breakout r6 s=0.9259 | bullish | normal | $89.12 | bullish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 1.85x; 20-day bullish range breakout after volatility compression in the lowest 12% of recent history, with 1.85x normal volume |
| 15 | TFLO | 0.097222 | volume_anomaly r8 s=0.9963; wildcard r14 s=0.6994 | non_directional | high | $50.65 | relative volume is 4.70x its 20-day median; relaxed-liquidity stock showing volume 100% percentile, normalized move 97% percentile, stretch 99% percentile |
| 16 | CGON | 0.094758 | volume_anomaly r21 s=0.9894; momentum_breakout r6 s=0.9666 | non_directional | normal | $67.21 | relative volume is 3.56x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 95% percentile, relative volume 3.56x |
| 17 | BSV | 0.090909 | volume_anomaly r1 s=1 | non_directional | normal | $76.50 | relative volume is 10.23x its 20-day median |
| 18 | TWLO | 0.085455 | momentum_breakout r15 s=0.9444; stretched_reversal r12 s=0.8852 | bullish | normal | $275.82 | bullish 5-day momentum, 5-day momentum is in the 98% percentile, relative volume 2.48x; stock moved 2.03 ATR today and is 2.61 ATR from its 20-day mean |
| 19 | CRML | 0.083333 | volatility_expansion r2 s=0.9995 | non_directional | normal | $7.83 | 5-day realized volatility is 1.77x its 20-day level |
| 20 | VBIL | 0.083333 | stretched_reversal r2 s=0.9966 | bearish_reversal | normal | $75.69 | stock moved 2.10 ATR today and is 6.35 ATR from its 20-day mean |
