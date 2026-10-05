# Stage 1 investigation shortlist

- Stage 1 as-of date: 2026-09-28
- Expert data generated at: 2026-09-29T15:03:49Z
- Community selection: top 10 unique tickers by best rank across community sources
- Expert selection: top 10 candidates in expert source rank order
- Technical selection: top 20 by RRF score, with k=10
- Technical category rank: descending category score; ties are ordered by ticker; ranks are 1-based
- Unique tickers across sections: 39

## Community attention — top 10

| Rank | Ticker | Name | Best source rank | Source details |
|---:|:---|:---|---:|:---|
| 1 | ES | Eversource Energy | 1 | all-stocks #3 18 mentions 40 upvotes; options #1 15 mentions 35 upvotes |
| 2 | SPY | SPDR S&amp;P 500 ETF Trust | 1 | all-stocks #1 257 mentions 937 upvotes |
| 3 | DTE | DTE Energy | 2 | all-stocks #6 59 mentions 235 upvotes; options #2 4 mentions 6 upvotes |
| 4 | MU | Micron Technology | 2 | all-stocks #2 175 mentions 4475 upvotes; options #24 1 mentions 1 upvotes |
| 5 | API | Agora.io | 3 | all-stocks #45 14 mentions 112 upvotes; options #3 4 mentions 13 upvotes |
| 6 | NVDA | NVIDIA | 3 | all-stocks #3 101 mentions 3998 upvotes; options #12 1 mentions 1 upvotes |
| 7 | BE | Bloom Energy | 4 | all-stocks #4 71 mentions 172 upvotes; options #42 1 mentions 1 upvotes |
| 8 | PEP | Pepsico | 4 | options #4 3 mentions 7 upvotes |
| 9 | MSFT | Microsoft | 5 | all-stocks #25 22 mentions 3697 upvotes; options #5 1 mentions 1 upvotes |
| 10 | QQQ | Invesco QQQ ETF | 5 | all-stocks #5 68 mentions 173 upvotes |

## Expert attention — top 10

| Rank | Ticker | Company | Direction | Strength | Event dates | Events | Firms | Sources | Summary | Reason |
|---:|:---|:---|:---|:---|:---|---:|---:|:---|:---|:---|
| 1 | PEP | PepsiCo | bearish | high | 2026-09-28 to 2026-09-29 | 4 | 3 | 24/7 Wall St.; MarketBeat | Fresh Deutsche Bank and JPMorgan rating cuts and target reductions, plus a TD Cowen target cut. | A three-firm bearish cluster includes two fresh target cuts and rating deterioration. |
| 2 | RCL | Royal Caribbean Cruises | bullish | high | 2026-09-28 | 4 | 3 | 24/7 Wall St.; MarketBeat | Three firms reported fresh positive analyst actions, including two upgrades and a Buy reiteration. | Fresh actions from three firms include upgrades with a target raise and a Buy reiteration. |
| 3 | LBRT | Liberty Energy | bullish | high | 2026-09-28 to 2026-09-29 | 3 | 2 | 24/7 Wall St.; MarketBeat | Barclays upgraded and raised its target; Scotiabank initiated coverage the following day. | Two firms added fresh coverage or upgrades, including a Barclays target increase. |
| 4 | PK | Park Hotels & Resorts | bullish | high | 2026-09-28 | 3 | 2 | 24/7 Wall St.; MarketBeat | Raymond James upgraded Park Hotels to Strong Buy, and MarketBeat records a separate UBS upgrade. | Two firms made fresh upgrades; both sources corroborate the Raymond James rating change. |
| 5 | FSLR | First Solar | bullish | high | 2026-09-28 | 2 | 2 | 24/7 Wall St.; MarketBeat | KeyBanc upgraded the rating, while MarketBeat records a same-day Guggenheim Buy reiteration. | Fresh bullish actions from two firms include a rating upgrade and Buy reiteration. |
| 6 | TFX | Teleflex | bullish | high | 2026-09-28 | 2 | 1 | 24/7 Wall St.; MarketBeat | Bank of America’s upgrade and target raise are independently reported by both sources. | Bank of America’s fresh upgrade and $145-to-$158 target increase have cross-source confirmation. |
| 7 | RBLX | Roblox | bearish | high | 2026-09-28 | 2 | 1 | 24/7 Wall St.; MarketBeat | Jefferies downgraded Hold to Underperform with a $38 target; both sources report the action. | A fresh Jefferies downgrade and $38 target are confirmed in both required sources. |
| 8 | ADSK | Autodesk | mixed | high | 2026-09-28 | 2 | 1 | 24/7 Wall St.; MarketBeat | Piper Sandler initiated Overweight coverage while cutting the target from $338 to $300. | New bullish coverage came with a fresh target reduction, creating mixed directional evidence. |
| 9 | NFLX | Netflix | mixed | medium | 2026-09-29 | 1 | 1 | MarketBeat | Deutsche Bank upgraded Hold to Buy while lowering its target from $100 to $95. | The rating upgrade and target cut point in opposite directions. |
| 10 | RGA | Reinsurance Group of America | bullish | medium | 2026-09-28 | 1 | 1 | MarketBeat | Morgan Stanley upgraded Equal Weight to Overweight and set a $295 target. | A dated analyst history confirms a fresh single-firm upgrade. |

## Technical RRF — top 20

| Rank | Ticker | RRF score | Category rank and score | Direction | Risk | Price | Reasons |
|---:|:---|---:|:---|:---|:---|---:|:---|
| 1 | NU | 0.283333 | volume_anomaly r10 s=0.9953; momentum_breakout r2 s=0.9927; stretched_reversal r2 s=0.9932; wildcard r5 s=0.8824 | non_directional | high | $12.22 | relative volume is 3.97x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 98% percentile, relative volume 3.97x; stock moved 3.02 ATR today and is 4.90 ATR from its 20-day mean; relaxed-liquidity stock showing volume 99% percentile, normalized move 100% percentile, volatility expansion 94% percentile, stretch 98% percentile |
| 2 | MDB | 0.260522 | volume_anomaly r1 s=1; momentum_breakout r1 s=0.9939; stretched_reversal r17 s=0.9365; wildcard r14 s=0.748 | non_directional | high | $334.66 | relative volume is 6.08x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 6.08x; stock moved 4.05 ATR today and is 3.29 ATR from its 20-day mean; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 95% percentile |
| 3 | BA | 0.248853 | volume_anomaly r3 s=0.999; momentum_breakout r5 s=0.9686; stretched_reversal r9 s=0.955; wildcard r9 s=0.8088 | non_directional | high | $184.26 | relative volume is 5.22x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 91% percentile, relative volume 5.22x; stock moved 2.44 ATR today and is 3.65 ATR from its 20-day mean; relaxed-liquidity stock showing volume 100% percentile, normalized move 100% percentile, volatility expansion 95% percentile, stretch 90% percentile |
| 4 | GFI | 0.20202 | momentum_breakout r8 s=0.9643; stretched_reversal r1 s=0.9974; wildcard r8 s=0.8233 | bullish_reversal | high | $35.17 | bearish 20-day breakout, 5-day momentum is in the 99% percentile, relative volume 1.95x; stock moved 3.39 ATR today and is 5.84 ATR from its 20-day mean; relaxed-liquidity stock showing normalized move 100% percentile, volatility expansion 97% percentile, stretch 99% percentile |
| 5 | VKTX | 0.153587 | volume_anomaly r17 s=0.9916; momentum_breakout r29 s=0.9163; volatility_expansion r1 s=1 | non_directional | normal | $33.04 | relative volume is 3.50x its 20-day median; bullish 5-day momentum, 5-day momentum is in the 94% percentile, relative volume 3.50x; 5-day realized volatility is 1.91x its 20-day level |
| 6 | SMG | 0.153571 | momentum_breakout r25 s=0.9249; stretched_reversal r6 s=0.977; wildcard r6 s=0.8659 | bullish_reversal | high | $48.49 | bearish 20-day breakout, 5-day momentum is in the 81% percentile, relative volume 2.71x; stock moved 1.57 ATR today and is 4.81 ATR from its 20-day mean; relaxed-liquidity stock showing volume 97% percentile, normalized move 97% percentile, volatility expansion 98% percentile, stretch 97% percentile |
| 7 | IAUM | 0.150241 | volume_anomaly r21 s=0.9895; momentum_breakout r28 s=0.9168; stretched_reversal r14 s=0.9396; compression_breakout r10 s=0.929 | non_directional | normal | $41.08 | relative volume is 3.23x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 76% percentile, relative volume 3.23x; stock moved 2.45 ATR today and is 3.37 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 20% of recent history, with 3.23x normal volume |
| 8 | RACE | 0.15 | volume_anomaly r5 s=0.9979; compression_breakout r2 s=0.9719 | non_directional | normal | $398.09 | relative volume is 4.83x its 20-day median; 20-day bearish range breakout after volatility compression in the lowest 0% of recent history, with 4.83x normal volume |
| 9 | MGM | 0.145833 | volume_anomaly r2 s=0.9995; momentum_breakout r6 s=0.9683 | non_directional | normal | $31.86 | relative volume is 5.41x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 5.41x |
| 10 | DASH | 0.142157 | momentum_breakout r20 s=0.936; stretched_reversal r7 s=0.9642; wildcard r10 s=0.7951 | bullish_reversal | high | $178.44 | bearish 20-day breakout, 5-day momentum is in the 90% percentile, relative volume 2.41x; stock moved 2.21 ATR today and is 3.91 ATR from its 20-day mean; relaxed-liquidity stock showing volume 95% percentile, normalized move 99% percentile, volatility expansion 97% percentile, stretch 92% percentile |
| 11 | SIVR | 0.136364 | momentum_breakout r12 s=0.9517; compression_breakout r1 s=0.9744 | bearish | normal | $57.77 | bearish 20-day breakout, 5-day momentum is in the 90% percentile, relative volume 2.82x; 20-day bearish range breakout after volatility compression in the lowest 3% of recent history, with 2.82x normal volume |
| 12 | GLL | 0.124542 | momentum_breakout r3 s=0.9737; stretched_reversal r11 s=0.9477 | bullish | normal | $25.31 | bullish 20-day breakout, 5-day momentum is in the 96% percentile, relative volume 2.40x; stock moved 2.54 ATR today and is 3.50 ATR from its 20-day mean |
| 13 | CLF | 0.114379 | volume_anomaly r7 s=0.9969; compression_breakout r8 s=0.9397 | non_directional | normal | $11.22 | relative volume is 4.48x its 20-day median; 20-day bearish range breakout after volatility compression in the lowest 2% of recent history, with 4.48x normal volume |
| 14 | WPM | 0.114286 | momentum_breakout r11 s=0.9528; compression_breakout r5 s=0.9567 | bearish | normal | $135.58 | bearish 20-day breakout, 5-day momentum is in the 90% percentile, relative volume 2.44x; 20-day bearish range breakout after volatility compression in the lowest 8% of recent history, with 2.44x normal volume |
| 15 | SLV | 0.112637 | momentum_breakout r18 s=0.9407; compression_breakout r3 s=0.9643 | bearish | normal | $54.96 | bearish 20-day breakout, 5-day momentum is in the 90% percentile, relative volume 2.34x; 20-day bearish range breakout after volatility compression in the lowest 3% of recent history, with 2.34x normal volume |
| 16 | UGL | 0.112526 | momentum_breakout r13 s=0.9498; stretched_reversal r18 s=0.9349; compression_breakout r20 s=0.8983 | bearish | normal | $45.02 | bearish 20-day breakout, 5-day momentum is in the 95% percentile, relative volume 1.95x; stock moved 2.34 ATR today and is 3.32 ATR from its 20-day mean; 20-day bearish range breakout after volatility compression in the lowest 20% of recent history, with 1.95x normal volume |
| 17 | GEN | 0.10989 | volume_anomaly r16 s=0.9922; momentum_breakout r4 s=0.9714 | non_directional | normal | $20.86 | relative volume is 3.58x its 20-day median; bearish 20-day breakout, 5-day momentum is in the 100% percentile, relative volume 3.58x |
| 18 | PSLV | 0.108466 | momentum_breakout r17 s=0.9411; compression_breakout r4 s=0.9594 | bearish | normal | $19.73 | bearish 20-day breakout, 5-day momentum is in the 91% percentile, relative volume 2.16x; 20-day bearish range breakout after volatility compression in the lowest 3% of recent history, with 2.16x normal volume |
| 19 | ASHR | 0.102381 | volume_anomaly r18 s=0.9911; stretched_reversal r5 s=0.9775 | non_directional | normal | $32.51 | relative volume is 3.47x its 20-day median; stock moved 1.93 ATR today and is 4.36 ATR from its 20-day mean |
| 20 | GDX | 0.092803 | momentum_breakout r23 s=0.9266; compression_breakout r6 s=0.9544 | bearish | normal | $87.88 | bearish 20-day breakout, 5-day momentum is in the 87% percentile, relative volume 2.11x; 20-day bearish range breakout after volatility compression in the lowest 5% of recent history, with 2.11x normal volume |
