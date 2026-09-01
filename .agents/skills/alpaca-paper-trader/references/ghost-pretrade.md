# Ghost alternatives before execution

Read this reference after selecting a real trade and before calling the order endpoint. Ghosts are counterfactual analysis records only; never submit them, reserve cash for them, or include them in portfolio risk.

Define two to four realistic alternatives that were genuinely considered. Record their definitions and the contemporaneous quote snapshot in the daily log before submitting the real order. Do not invent alternatives after observing later prices.

Each ghost should test one meaningful choice, such as:

- stock instead of options, or options instead of stock;
- a different option structure, strike, or expiration;
- a different position size;
- different entry timing with an objective trigger;
- no trade.

Prefer changing one decision at a time. Do not add random variants or several nearly identical contracts. Include no trade when the main question is whether exposure should be added at all.

For each alternative, record a stable label, question tested, rationale, instrument or no-trade choice, side, quantity or notional, option structure and contracts when applicable, entry rule, simulated entry price, maximum loss when knowable, exit or expiration handling, pricing assumptions, and missing data.

Use only data observable at the real decision. Price a hypothetical buy at the contemporaneous ask and a hypothetical sale at the bid unless a more realistic conservative fill is documented. Price multi-leg structures from the executable side of each leg. A no-trade ghost starts at zero P/L and zero capital at risk. If reliable data is unavailable, keep the question but mark the alternative `UNSCORABLE`; never manufacture a price.

If the real order remains unfilled at final reconciliation, leave the pre-trade record tied to its client order ID. Create no ghost set unless an actual fill is later confirmed.

Those ghost trades eventually will be studied and reflected to derive valuable lessons.
