# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-16
- Expert data generated at: 2026-09-17T14:02:33Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 40

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | DTE | DTE Energy | 1 | all-stocks #6 64 mentions 353 upvotes; options #1 6 mentions 20 upvotes |
| 2 | SPY | SPDR S&amp;P 500 ETF Trust | 1 | all-stocks #1 403 mentions 1295 upvotes |
| 3 | CBOE | Cboe | 2 | options #2 2 mentions 7 upvotes |
| 4 | QQQ | Invesco QQQ ETF | 2 | all-stocks #2 129 mentions 317 upvotes |
| 5 | MSFT | Microsoft | 3 | all-stocks #27 18 mentions 36 upvotes; options #3 1 mentions 1 upvotes |
| 6 | MU | Micron Technology | 3 | all-stocks #3 87 mentions 169 upvotes; options #26 1 mentions 1 upvotes |
| 7 | AAPL | Apple | 4 | all-stocks #23 19 mentions 36 upvotes; options #4 1 mentions 1 upvotes |
| 8 | SPCX | SpaceX | 4 | all-stocks #4 78 mentions 173 upvotes |
| 9 | GOOG | Alphabet (Google) | 5 | all-stocks #29 17 mentions 49 upvotes; options #5 1 mentions 3 upvotes |
| 10 | NBIS | Nebius Group | 5 | all-stocks #5 75 mentions 188 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | UNP | Union Pacific | bullish | high | 2026-09-16 | 3 | 3 | 24/7 Wall St.; MarketBeat | Fresh multi-firm bullish upgrades included UBS moving the rating to Buy and raising its target. | Fresh multi-source, multi-firm upgrade cluster. |
| 2 | BAP | Credicorp | bullish | high | 2026-09-16 | 2 | 1 | 24/7 Wall St.; MarketBeat | JPMorgan upgraded Credicorp and raised its target, with the dated event confirmed by MarketBeat. | Fresh multi-source bullish rating and target change. |
| 3 | RCKT | Rocket Pharmaceuticals | bullish | high | 2026-09-16 | 3 | 2 | 24/7 Wall St.; MarketBeat | Needham raised Rocket Pharmaceuticals from Hold to Buy; Wedbush also reiterated Outperform on the same date. | Fresh multi-source upgrade plus a separate bullish reiteration. |
| 4 | PAYX | Paychex | bullish | medium | 2026-09-16 | 2 | 1 | 24/7 Wall St.; MarketBeat | Wolfe Research upgraded Paychex from Underperform to Peer Perform without a published target change. | Fresh multi-source rating improvement, though the new rating is not outright bullish. |
| 5 | SMWB | Similarweb | bullish | medium | 2026-09-16 | 1 | 1 | 24/7 Wall St. | Needham raised Similarweb from Hold to Buy with an $11 target. | Fresh single-firm bullish upgrade. |
| 6 | BROS | Dutch Bros | bullish | medium | 2026-09-16 | 1 | 1 | 24/7 Wall St. | Seaport Research initiated coverage of Dutch Bros with a Buy rating and a $50 target. | Fresh bullish initiation with a published target. |
| 7 | BKNG | Booking Holdings | bullish | medium | 2026-09-16 | 1 | 1 | 24/7 Wall St. | Morgan Stanley initiated Booking Holdings at Overweight with a $230 target. | Fresh bullish initiation with a published target. |
| 8 | ABNB | Airbnb | neutral | medium | 2026-09-16 | 1 | 1 | 24/7 Wall St. | Morgan Stanley initiated Airbnb at Equal Weight with a $170 target. | Fresh initiation with a neutral published rating. |
| 9 | FIVN | Five9 | bullish | medium | 2026-09-16 | 1 | 1 | 24/7 Wall St. | FBN initiated Five9 at Outperform with a $40 target. | Fresh bullish initiation with a published target. |
| 10 | YUM | Yum! Brands | bullish | medium | 2026-09-16 | 1 | 1 | 24/7 Wall St. | Seaport Research initiated Yum! Brands at Buy with a $162 target. | Fresh bullish initiation with a published target. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | JBHT | 0.438185 | volume_anomaly r2 s=0.9995; momentum_breakout r4 s=0.9832; stretched_reversal r3 s=0.9919; volatility_expansion r21 s=0.9892; compression_breakout r2 s=0.9887; wildcard r1 s=0.967 | non_directional | high | $236.74 | relative volume is 10.56x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 95% percentile, relative volume 10.56x; stock moved 5.96 ATR today and is 5.10 ATR from its 20-day mean; 5-day realized volatility is 1.62x its 20-day level; 20-day bearish range breakout after volatility compression in the lowest 3% of recent history, with 10.56x normal volume; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 99% percentile, stretch 98% percentile |
| 2 | ALHC | 0.335671 | volume_anomaly r10 s=0.9951; momentum_breakout r1 s=0.9962; stretched_reversal r4 s=0.9916; compression_breakout r15 s=0.9297; wildcard r2 s=0.9526 | bearish | high | $8.70 | relative volume is 4.53x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 4.53x; stock moved 2.38 ATR today and is 6.18 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 20% of recent history, with 4.53x normal volume; relaxed-liquidity stock showing volume 99% percentile, normalized move 99% percentile, volatility expansion 98% percentile, stretch 100% percentile |
| 3 | HBAN | 0.27381 | volume_anomaly r6 s=0.9973; stretched_reversal r13 s=0.9568; compression_breakout r1 s=0.9925; wildcard r3 s=0.83 | non_directional | high | $15.82 | relative volume is 5.10x its 20-day median; stock moved 3.18 ATR today and is 3.72 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 2% of recent history, with 5.10x normal volume; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 97% percentile, stretch 91% percentile |
| 4 | FANG | 0.249096 | volume_anomaly r1 s=1; volatility_expansion r9 s=0.9957; compression_breakout r10 s=0.9411; wildcard r8 s=0.7438 | non_directional | high | $194.53 | relative volume is 12.25x its 20-day median; 5-day realized volatility is 1.71x its 20-day level; 20-day bearish range breakout after volatility compression in the lowest 10% of recent history, with 12.25x normal volume; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 100% percentile |
| 5 | EPRT | 0.240826 | volume_anomaly r16 s=0.9919; momentum_breakout r9 s=0.9683; stretched_reversal r1 s=0.9965; wildcard r7 s=0.795 | bullish_reversal | high | $26.81 | relative volume is 4.25x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 91% percentile, relative volume 4.25x; stock moved 2.75 ATR today and is 7.47 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 99% percentile, stretch 100% percentile |
| 6 | ARWR | 0.221429 | volume_anomaly r4 s=0.9984; momentum_breakout r2 s=0.9933; wildcard r5 s=0.8098 | non_directional | high | $65.76 | relative volume is 5.48x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 5.48x; relaxed-liquidity stock showing volume 100% percentile, normalized move 92% percentile, volatility expansion 95% percentile, stretch 98% percentile |
| 7 | RCAT | 0.19952 | volume_anomaly r21 s=0.9892; momentum_breakout r6 s=0.9789; stretched_reversal r20 s=0.9349; compression_breakout r4 s=0.974 | non_directional | normal | $7.09 | relative volume is 3.93x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 3.93x; stock moved 1.91 ATR today and is 3.57 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 5% of recent history, with 3.93x normal volume |
| 8 | ELVN | 0.181201 | momentum_breakout r3 s=0.9856; stretched_reversal r7 s=0.9849; wildcard r12 s=0.7083 | bearish | high | $49.14 | bearish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 3.09x; stock moved 2.36 ATR today and is 5.24 ATR from its 20-day mean; relaxed-liquidity stock showing volume 97% percentile, normalized move 99% percentile, stretch 99% percentile |
| 9 | GPOR | 0.169021 | momentum_breakout r18 s=0.9294; stretched_reversal r19 s=0.9365; compression_breakout r7 s=0.9511; wildcard r15 s=0.6984 | bearish | high | $162.38 | bearish 20-day breakout, 5-day momentum is in the 87% percentile, relative volume 2.32x; stock moved 3.31 ATR today and is 3.37 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 7% of recent history, with 2.32x normal volume; relaxed-liquidity stock showing volume 91% percentile, normalized move 100% percentile, volatility expansion 98% percentile |
| 10 | COO | 0.158756 | volume_anomaly r30 s=0.9843; momentum_breakout r26 s=0.915; volatility_expansion r6 s=0.9973; wildcard r13 s=0.7042 | non_directional | high | $54.62 | relative volume is 3.46x its 20-day median; bearish 5-day momentum, 5-day momentum is in the 97% percentile, relative volume 3.46x; 5-day realized volatility is 1.74x its 20-day level; relaxed-liquidity stock showing volume 98% percentile, volatility expansion 100% percentile, stretch 99% percentile |
| 11 | NNN | 0.154762 | stretched_reversal r2 s=0.9946; wildcard r4 s=0.8205 | bullish_reversal | high | $41.65 | stock moved 2.62 ATR today and is 5.90 ATR from its 20-day mean; relaxed-liquidity stock showing volume 94% percentile, normalized move 99% percentile, volatility expansion 92% percentile, stretch 100% percentile |
| 12 | ON | 0.116667 | volatility_expansion r10 s=0.9951; compression_breakout r5 s=0.9732 | non_directional | normal | $66.59 | 5-day realized volatility is 1.71x its 20-day level; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 2.82x normal volume |
| 13 | BA | 0.111406 | volume_anomaly r19 s=0.9903; compression_breakout r3 s=0.9791 | non_directional | normal | $202.00 | relative volume is 3.97x its 20-day median; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 3.97x normal volume |
| 14 | NOVT | 0.1025 | momentum_breakout r15 s=0.9359; compression_breakout r6 s=0.9575 | bearish | normal | $132.81 | bearish 20-day breakout, 5-day momentum is in the 90% percentile, relative volume 2.27x; 20-day bearish range breakout after volatility compression in the lowest 3% of recent history, with 2.27x normal volume |
| 15 | ENVA | 0.096078 | momentum_breakout r24 s=0.9157; volatility_expansion r5 s=0.9978 | non_directional | normal | $172.29 | bearish 5-day momentum, 5-day momentum is in the 100% percentile, relative volume 2.82x; 5-day realized volatility is 1.77x its 20-day level |
| 16 | QRVO | 0.090909 | volatility_expansion r1 s=1 | non_directional | normal | $113.89 | 5-day realized volatility is 1.85x its 20-day level |
| 17 | ARQT | 0.084656 | volume_anomaly r17 s=0.9914; wildcard r11 s=0.7104 | non_directional | high | $26.16 | relative volume is 4.22x its 20-day median; relaxed-liquidity stock showing volume 99% percentile, normalized move 100% percentile, volatility expansion 98% percentile |
| 18 | WPC | 0.083333 | volume_anomaly r20 s=0.9897; stretched_reversal r10 s=0.9738 | non_directional | normal | $66.61 | relative volume is 3.94x its 20-day median; stock moved 2.05 ATR today and is 4.63 ATR from its 20-day mean |
| 19 | SWKS | 0.083333 | volatility_expansion r2 s=0.9995 | non_directional | normal | $85.65 | 5-day realized volatility is 1.84x its 20-day level |
| 20 | ABG | 0.079937 | momentum_breakout r19 s=0.9286; stretched_reversal r12 s=0.9643 | bullish_reversal | normal | $195.27 | bearish 20-day breakout, 5-day momentum is in the 88% percentile, relative volume 2.22x; stock moved 2.48 ATR today and is 3.98 ATR from its 20-day mean |
