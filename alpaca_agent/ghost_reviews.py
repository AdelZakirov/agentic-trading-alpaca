"""Compact completed-comparison registry, separate from the full Markdown archive."""
import argparse
import fcntl
import json
import math
from pathlib import Path
import re
from .moneyheap import _atomic_write

ROOT = Path('memory/ghost-trades')


def update(root=ROOT, record=None):
    root.mkdir(parents=True, exist_ok=True)
    with (root/'reviews.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        path=root/'reviews.json'
        rows=json.loads(path.read_text()) if path.exists() else []
        by_id={r['ghost_id']:r for r in rows}
        if record is None:
            for file in sorted(root.glob('*/*.md')):
                if re.search(r'^- Status:\s*COMPLETE\b',file.read_text(),re.M):
                    by_id.setdefault(file.stem,dict(ghost_id=file.stem, source=str(file), review_status='awaiting_backfill'))
        else:
            validate(record)
            if not Path(record['source']).is_file():raise ValueError('Missing source file')
            by_id[record['ghost_id']]=record
        _atomic_write(path,json.dumps(list(by_id.values()),ensure_ascii=False,indent=2,allow_nan=False))
        return list(by_id.values())


def validate(r):
    required=['ghost_id','source','review_status','decision_id','ticker','evaluated_at','conditions','question','outcomes','data_quality','conclusion','lesson_ids']
    if any(k not in r for k in required):raise ValueError('Missing review fields')
    if r['review_status']!='reviewed':raise ValueError('Expected reviewed record')
    for k in ['ghost_id','source','decision_id','ticker','evaluated_at','question','conclusion']:
        if not isinstance(r[k],str) or not r[k].strip():raise ValueError(f'Invalid {k}')
    for k in ['conditions','outcomes','lesson_ids']:
        if not isinstance(r[k],list):raise ValueError(f'Invalid {k}')
    if r['data_quality'] not in ['scorable','partial','unscorable']:raise ValueError('Invalid data quality')
    if not r['outcomes']:raise ValueError('Outcomes required, even if unscorable')
    for o in r['outcomes']:
        if not isinstance(o,dict) or not {'label','pnl','capital_at_risk','scorable','reason'}<=o.keys():raise ValueError('Invalid outcome')
        if not isinstance(o['scorable'],bool):raise ValueError('scorable must be boolean')
        for k in ['pnl','capital_at_risk']:
            v=o[k]
            if v is not None and (isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v)):raise ValueError('Non-finite outcome')
        if o['scorable'] and o['pnl'] is None:raise ValueError('Scorable outcome requires P&L')
        if not o['scorable'] and o['pnl'] is not None:raise ValueError('Unscorable outcome must not claim P&L')


def summary(rows):
    reviewed=[r for r in rows if r['review_status']=='reviewed']
    return dict(sets=len(rows),reviewed=len(reviewed),awaiting_backfill=len(rows)-len(reviewed),independent_decisions=len({r['decision_id'] for r in reviewed}))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('action',choices=['inventory','upsert','summary']);p.add_argument('--record',type=Path);a=p.parse_args()
    if a.action=='upsert':
        if not a.record:p.error('--record required')
        rows=update(record=json.loads(a.record.read_text()))
    elif a.action=='inventory':rows=update()
    else:rows=json.loads((ROOT/'reviews.json').read_text()) if (ROOT/'reviews.json').exists() else []
    print(json.dumps(summary(rows)))

if __name__=='__main__':main()
