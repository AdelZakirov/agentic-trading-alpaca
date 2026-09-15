# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-14
- Expert data generated at: 2026-09-14T14:07:00Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 40

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | SPY | SPDR S&amp;P 500 ETF Trust | 1 | all-stocks #1 218 mentions 919 upvotes; options #1 13 mentions 14 upvotes |
| 2 | DTE | DTE Energy | 2 | all-stocks #7 49 mentions 511 upvotes; options #2 4 mentions 14 upvotes |
| 3 | NVDA | NVIDIA | 2 | all-stocks #2 85 mentions 304 upvotes; options #13 1 mentions 4 upvotes |
| 4 | BP | BP | 3 | options #3 2 mentions 5 upvotes |
| 5 | MU | Micron Technology | 3 | all-stocks #3 62 mentions 117 upvotes; options #26 1 mentions 1 upvotes |
| 6 | QQQ | Invesco QQQ ETF | 4 | all-stocks #4 56 mentions 387 upvotes |
| 7 | UBER | Uber | 4 | options #4 2 mentions 13 upvotes |
| 8 | IQ | iQIYI | 5 | all-stocks #5 53 mentions 303 upvotes; options #37 1 mentions 1 upvotes |
| 9 | MSFT | Microsoft | 5 | all-stocks #14 31 mentions 165 upvotes; options #5 1 mentions 1 upvotes |
| 10 | AAPL | Apple | 6 | all-stocks #3 12 mentions 31 upvotes; options #6 1 mentions 1 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | BLSH | Bullish | bullish | high | 2026-09-14 | 1 | 1 | MarketBeat | Compass Point upgraded Bullish from Neutral to Buy and raised its target from $30 to $51 on September 14. | Fresh rating upgrade with a material target increase. |
| 2 | CAPR | Capricor Therapeutics | bullish | high | 2026-09-14 | 1 | 1 | MarketBeat | B. Riley upgraded Capricor Therapeutics from Neutral to Buy with a $21 target on September 14. | Fresh rating upgrade with a published target substantially above the listed price. |
| 3 | COIN | Coinbase Global | bullish | high | 2026-09-14 | 1 | 1 | MarketBeat | Compass Point upgraded Coinbase from Sell to Neutral and raised its target from $130 to $177 on September 14. | Fresh move away from a bearish rating combined with a material target increase. |
| 4 | IREN | IREN | bullish | high | 2026-09-14 | 1 | 1 | MarketBeat | JPMorgan upgraded IREN from Underweight to Overweight and raised its target from $46 to $65 on September 14. | Fresh strong rating upgrade with a material target increase. |
| 5 | SPRO | Spero Therapeutics | bullish | medium | 2026-09-14 | 1 | 1 | MarketBeat | HC Wainwright raised its Spero Therapeutics target from $5 to $6 while maintaining Buy on September 14. | Fresh bullish target raise from an active covering firm. |
| 6 | CIZN | Citizens | neutral | medium | 2026-09-10 | 1 | 1 | MarketBeat | UBS set an $8 target for Citizens on September 10 without publishing a rating. | Freshly dated analyst target with no published directional rating. |
| 7 | GEV | GE Vernova | neutral | medium | 2026-09-11 | 1 | 1 | MarketBeat | Jefferies set a $1,185 target for GE Vernova on September 11 without publishing a rating. | Freshly dated analyst target from a major covering firm. |
| 8 | ESI | Element Solutions | bullish | medium | 2026-09-11 | 1 | 1 | 24/7 Wall St. | Goldman Sachs reinstated Element Solutions with a Buy rating and a $44 target on September 11. | Fresh reinstatement with a bullish published rating. |
| 9 | IP | International Paper Company | mixed | medium | 2026-09-11 | 1 | 1 | 24/7 Wall St. | Bank of America upgraded International Paper to Buy from Neutral but cut its target from $48 to $46 on September 11. | Fresh rating upgrade offset by a same-report target cut. |
| 10 | ATO | Atmos Energy | bearish | high | 2026-09-11 | 1 | 1 | 24/7 Wall St. | JPMorgan downgraded Atmos Energy to Neutral from Overweight and cut its target from $198 to $180 on September 11. | Fresh rating downgrade with a material target cut. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | TTAN | 0.273388 | volume_anomaly r1 s=1; momentum_breakout r10 s=0.9457; volatility_expansion r8 s=0.9962; wildcard r3 s=0.7286 | non_directional | high | $58.97 | relative volume is 7.43x its 20-day median; bearish 5-day momentum, 5-day momentum is in the 100% percentile, relative volume 7.43x; 5-day realized volatility is 1.69x its 20-day level; relaxed-liquidity stock showing volume 100% percentile, volatility expansion 100% percentile, stretch 99% percentile |
| 2 | NTSK | 0.217721 | volume_anomaly r13 s=0.9935; momentum_breakout r1 s=0.98; compression_breakout r2 s=0.9811 | non_directional | normal | $17.00 | relative volume is 3.72x its 20-day median; bullish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 3.72x; 20-day bullish range breakout after volatility compression in the lowest 0% of recent history, with 3.72x normal volume |
| 3 | COO | 0.195455 | volume_anomaly r10 s=0.9951; momentum_breakout r12 s=0.9434; volatility_expansion r20 s=0.9897; wildcard r5 s=0.7199 | non_directional | high | $54.19 | relative volume is 4.10x its 20-day median; bearish 5-day momentum, 5-day momentum is in the 100% percentile, relative volume 4.10x; 5-day realized volatility is 1.60x its 20-day level; relaxed-liquidity stock showing volume 99% percentile, volatility expansion 99% percentile, stretch 100% percentile |
| 4 | BAC | 0.187892 | stretched_reversal r19 s=0.9303; compression_breakout r1 s=0.9926; wildcard r6 s=0.7138 | bearish | high | $59.47 | stock moved 3.02 ATR today and is 2.96 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 2.83x normal volume; relaxed-liquidity stock showing volume 97% percentile, normalized move 100% percentile, volatility expansion 96% percentile |
| 5 | OII | 0.15803 | momentum_breakout r7 s=0.9539; stretched_reversal r26 s=0.9181; compression_breakout r4 s=0.9485 | bearish | normal | $46.58 | bearish 20-day breakout, 5-day momentum is in the 93% percentile, relative volume 2.28x; stock moved 2.75 ATR today and is 2.85 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 8% of recent history, with 2.28x normal volume |
| 6 | ASML | 0.15674 | momentum_breakout r22 s=0.9271; stretched_reversal r5 s=0.9565; compression_breakout r7 s=0.9332 | bullish_reversal | normal | $1,575.21 | bearish 20-day breakout, 5-day momentum is in the 90% percentile, relative volume 1.94x; stock moved 2.73 ATR today and is 3.58 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 8% of recent history, with 1.94x normal volume |
| 7 | LSCC | 0.143725 | momentum_breakout r9 s=0.9496; stretched_reversal r16 s=0.9333; wildcard r9 s=0.7006 | bearish | high | $106.45 | bearish 20-day breakout, 5-day momentum is in the 90% percentile, relative volume 2.55x; stock moved 3.41 ATR today and is 2.96 ATR from its 20-day mean; relaxed-liquidity stock showing volume 95% percentile, normalized move 100% percentile, volatility expansion 96% percentile |
| 8 | RBLX | 0.132576 | stretched_reversal r1 s=0.9967; wildcard r14 s=0.6606 | bearish_reversal | high | $51.28 | stock moved 3.06 ATR today and is 5.72 ATR from its 20-day mean; relaxed-liquidity stock showing normalized move 100% percentile, volatility expansion 94% percentile, stretch 100% percentile |
| 9 | SPXC | 0.125 | momentum_breakout r14 s=0.941; stretched_reversal r18 s=0.932; wildcard r11 s=0.6932 | bearish | high | $182.56 | bearish 20-day breakout, 5-day momentum is in the 86% percentile, relative volume 2.96x; stock moved 1.86 ATR today and is 3.75 ATR from its 20-day mean; relaxed-liquidity stock showing volume 97% percentile, normalized move 93% percentile, volatility expansion 92% percentile, stretch 93% percentile |
| 10 | PEG | 0.121324 | volume_anomaly r7 s=0.9967; compression_breakout r6 s=0.9362 | non_directional | normal | $70.93 | relative volume is 4.44x its 20-day median; 20-day bearish range breakout after volatility compression in the lowest 18% of recent history, with 4.44x normal volume |
| 11 | MTSI | 0.118056 | momentum_breakout r8 s=0.9512; stretched_reversal r6 s=0.9513 | bullish_reversal | normal | $239.47 | bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 2.07x; stock moved 3.32 ATR today and is 3.31 ATR from its 20-day mean |
| 12 | TENB | 0.116923 | volume_anomaly r3 s=0.9989; wildcard r15 s=0.6606 | non_directional | high | $35.08 | relative volume is 7.05x its 20-day median; relaxed-liquidity stock showing volume 100% percentile, normalized move 98% percentile, volatility expansion 95% percentile |
| 13 | BCS | 0.107226 | volume_anomaly r23 s=0.988; compression_breakout r3 s=0.9693 | non_directional | normal | $25.85 | relative volume is 3.33x its 20-day median; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 3.33x normal volume |
| 14 | SIG | 0.107226 | momentum_breakout r23 s=0.9225; volatility_expansion r3 s=0.9989 | non_directional | normal | $100.77 | bullish 5-day momentum, 5-day momentum is in the 99% percentile, relative volume 2.25x; 5-day realized volatility is 1.75x its 20-day level |
| 15 | MATX | 0.094298 | stretched_reversal r9 s=0.9428; compression_breakout r14 s=0.9074 | bearish_reversal | normal | $236.38 | stock moved 1.84 ATR today and is 4.12 ATR from its 20-day mean; 20-day bullish range breakout after volatility compression in the lowest 3% of recent history, with 1.55x normal volume |
| 16 | DAMD | 0.090909 | volatility_expansion r1 s=1 | non_directional | normal | $14.48 | 5-day realized volatility is 1.86x its 20-day level |
| 17 | DV | 0.090909 | wildcard r1 s=0.8101 | bullish | high | $13.51 | relaxed-liquidity stock showing volume 100% percentile, normalized move 98% percentile, stretch 98% percentile |
| 18 | GRID | 0.088889 | stretched_reversal r20 s=0.9292; compression_breakout r8 s=0.9267 | bullish_reversal | normal | $172.95 | stock moved 3.04 ATR today and is 2.94 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 5% of recent history, with 1.86x normal volume |
| 19 | NAVN | 0.087619 | momentum_breakout r15 s=0.9387; volatility_expansion r11 s=0.9946 | non_directional | normal | $21.38 | bearish 5-day momentum, 5-day momentum is in the 100% percentile, relative volume 2.93x; 5-day realized volatility is 1.67x its 20-day level |
| 20 | KGS | 0.086081 | momentum_breakout r11 s=0.9448; compression_breakout r16 s=0.9039 | bearish | normal | $56.61 | bearish 20-day breakout, 5-day momentum is in the 94% percentile, relative volume 2.33x; 20-day bearish range breakout after volatility compression in the lowest 18% of recent history, with 2.33x normal volume |
