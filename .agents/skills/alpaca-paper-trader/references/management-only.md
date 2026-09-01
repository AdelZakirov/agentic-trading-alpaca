# Management-only cycle

Read this reference only when the task explicitly requests a management-only cycle.

- Manage existing positions, open orders, and due ghost checkpoints only.
- Do not scan the shortlist for new candidates, open a new position, add to a position, or otherwise increase exposure.
- A fresh shortlist is not required because existing risk must remain manageable when discovery is unavailable.
- Reassess each thesis, invalidation, target, holding deadline, current quote, open-order status, and overnight event or gap risk. Decide HOLD, reduce, close, cancel, or replace as warranted.
- Cancel stale risk-increasing entry orders before the close unless the current thesis, limit, remaining quantity, and overnight risk explicitly justify leaving them eligible. Record that reasoning.
- Use current research. Before requesting new moneyheap analysis, read [moneyheap-api.md](moneyheap-api.md) completely; request it only when a material development makes it necessary to manage exposure safely.
- Before managing an existing option position or order, read [options-api.md](options-api.md) completely.
- Reconcile all mutations, update due ghost checkpoints, and persist memory in the normal required order.
