# Indicative option follow-up — 2026-09-10T18:29:07.574785+02:00

Run 43042ec4-c8a5-4e5a-ad6c-7e083984f7db. Explicit user request to recheck previously OPRA-blocked contracts through indicative. No new company research or trade cycle widening. Prior independent fundamental decisions remain the inputs. Successfully obtained 72 contracts: {'BRZE': 6, 'PINS': 34, 'SMMT': 32}; no pagination remains. Correct fields latestQuote.bp/ap and greeks. Raw data: BRZE-indicative-puts.json, PINS-indicative-puts.json, SMMT-indicative-puts.json in this directory. Most selected observations around 16:23–16:25 UTC September 10. These are transformed indicative references, not firm OPRA quotes and not guaranteed order execution prices. They support paper comparisons; OPRA refusal does NOT mean options trading is disabled.

Calculations use long leg ask minus short leg bid, multiplier 100, one contract each, no fees. Expiration payoffs assume both legs remain intact, with explicit closing before expiry if selected in a later cycle. No current order.

| Underlying / expiry | Structure | Indicative cost / maximum loss | Maximum profit | Breakeven at expiry |
|---|---|---:|---:|---:|
| BRZE Sep18 | Long $25 put, ask 1.37 | $137 | $2363 at stock zero | $23.63 |
| BRZE Sep18 | Buy $25 put 1.37 / sell $22.50 put 0.18 | $119 | $131 at/below $22.50 | $23.81 |
| BRZE Oct16 | Buy $25 put 2.44 / sell $22.50 put 0.97 | $147 | $103 at/below $22.50 | $23.53 |
| PINS Sep25 | Long $19 put, ask 0.82 | $82 | $1818 at stock zero | $18.18 |
| PINS Sep25 | Buy $19 put 0.82 / sell $18 put 0.37 | $45 | $55 at/below $18 | $18.55 |
| PINS Sep25 | Buy $20 put 1.61 / sell $18 put 0.37 | $124 | $76 at/below $18 | $18.76 |
| SMMT Sep18 | Long $17 put, ask 1.28 | $128 | $1572 at stock zero | $15.72 |
| SMMT Sep18 | Buy $17 put 1.28 / sell $15 put 0.42 | $86 | $114 at/below $15 | $16.14 |

BRZE: 6 contracts found (Sep18 and Oct16). Sep18 $25 bid/ask 1.23/1.37, $22.50 0.18/0.23; synthetic spread roundtrip 1.00 bid /1.19 ask. Long $25 IV .622, delta −.6044, theta −.0522 (~$5.22 per day per contract); spread delta −.4294, theta −.019 (~$1.90/day), sensitivities not guarantees. Oct16 gives time but less favorable payoff at ask/bid. Stock latest $24.27/$24.28 is rebounding, independent fundamentals did not establish terminal impairment. No bearish trigger below $23.50; no puts bought. Long stock remains WATCH pending $24.73–$25 restoration. Sep18 $20 put has zero bid and old 15:36 quote, excluded from executable-side spread comparison.

PINS: 34 contracts found. Sep25 $19 bid/ask .76/.82, $18 .37/.40; synthetic spread .36/.45, 9-cent roundtrip (~22% midpoint). Long $19 IV .4507, delta −.5271, theta −.0217; $19/$18 spread delta −.2171, theta −.0008 (~$0.08/day), lower net IV/time exposure but capped profit. Current stock $18.77/$18.78 is above session low $18.06 and without confirmed bearish continuation. Positive EPS revisions and value/rebound thesis conflict with puts; NO ORDER. If future break below $18.06 persists and fundamentals worsen, this spread becomes a viable defined-risk paper candidate after fresh quotes and contract checks. Bullish conditions remain daily close >$18.85 or confirmed $19.10 reclaim. Availability of a cheap contract alone is not an entry signal.

SMMT: 32 contracts. Sep18 $17 bid/ask .92/1.28, IV 1.1499, delta −.4505, theta −.0711 (~$7.11/day). Five $17 puts would cover payoff of 500 retained shares for $640 premium, ~7.5% of stock value for eight calendar days; initial delta hedge only ~225 shares, not 500 delta. $17/$15 spread references .39/.86 are wide, and protection stops growing below $15, leaving stock downside tail. Five spreads cost $430 for at most $1000 expiry payoff; not a full crash hedge. Reduction already halved concentration; adding this expensive short-duration hedge is inferior to the selected smaller stock size under the current moderate bullish thesis. No hedge order, no reversal of reduction; retain 500 and GTC $18.50/$16.75. If bought protective puts while OCO stock exit remains, a stock exit would leave standalone puts: later execution must explicitly manage that interaction. No such complication introduced now.

Stock exposure risk unchanged, no mutations and no new ghosts. Options are technically available for paper orders at account level 3. Precise contract tradability, current quotes, assignment/exercise and buying power must be rechecked if a future order is selected. Do not read OPRA 403 as a universal options blocker. Earlier independent report statements that numeric payoff comparison was impossible are superseded by this follow-up.

Final reconciliation 2026-09-10T12:27:11.977440899-04:00: equity $101315.27, cash $65301.79, six positions, two GTC OCO groups. Original NVDA DAY stop queried by historical ID is canceled, correctly; new NVDA OCO and held GTC stop remain open in orders. No unknown execution. Temporary TMO/MMED IEX quote anomalies seen in broad snapshots do not establish asset price breakdown; MMED broker mark $22.465 and latest trade ~$22.485, versus isolated $21.58 bid, so no sell triggered from that outlier. Existing close-review $22.40 remains material.

Handoff prepared: 43042ec4-c8a5-4e5a-ad6c-7e083984f7db; no new ghost definitions. Dashboard refresh follows publication.
