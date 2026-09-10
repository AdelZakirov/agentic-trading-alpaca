"""File-based trading-to-ghost handoff; no broker operations."""
import argparse
from datetime import datetime, timezone
import fcntl
import json
import hashlib
from pathlib import Path
import re
import uuid
from .moneyheap import _atomic_write

ROOT = Path('memory/ghost-queue')


def operate(action, root=ROOT, run_id=None, log=None, summary=None, ghost_files=None):
    root.mkdir(parents=True, exist_ok=True)
    with (root/'lock').open('w') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        state_path=root/'state.json'
        state=json.loads(state_path.read_text()) if state_path.exists() else {'active':None,'pending':[],'claimed':None}
        if action=='begin':
            if state['active']: raise ValueError('Trading cycle already active; reconcile its task before clearing')
            run_id=str(uuid.uuid4());state['active']=run_id
            state['started_at']=datetime.now(timezone.utc).isoformat()
            result={'run_id':run_id}
        elif action=='finish':
            if not run_id or state['active']!=run_id: raise ValueError('Active run ID mismatch')
            text=Path(log).read_text(); small=Path(summary).read_text()
            markers=re.findall(r'<!-- run-checkpoint: (.*?) -->',text)
            if not markers or not text.rstrip().endswith(f'<!-- run-checkpoint: {markers[-1]} -->') or markers[-1] not in small or 'Covers full log through' not in small:
                raise ValueError('Log and summary checkpoints must match before handoff')
            # Validate all attachments before publishing anything or clearing the active run.
            attachments=[]; seen=set()
            ghost_root=(root.parent/'ghost-trades').resolve()
            for source in ghost_files or []:
                source=Path(source).resolve()
                if not source.is_relative_to(ghost_root) or source.suffix != '.md':
                    raise ValueError('Ghost attachment must be a Markdown file within memory/ghost-trades')
                relative=source.relative_to(ghost_root)
                if len(relative.parts)!=2:
                    raise ValueError('Ghost attachment must be a dated definition file')
                if source in seen: raise ValueError('Duplicate ghost attachment')
                seen.add(source)
                content=source.read_text()
                attachments.append((source, relative, content))
            folder=root/run_id;folder.mkdir(exist_ok=True)
            manifest=[]
            for source, relative, content in attachments:
                snapshot=Path('ghost-definitions')/relative
                (folder/snapshot).parent.mkdir(parents=True,exist_ok=True)
                _atomic_write(folder/snapshot,content)
                manifest.append({'source':str(source),'snapshot':str(snapshot),
                                 'sha256':hashlib.sha256(content.encode()).hexdigest()})
            _atomic_write(folder/'trading-log.md',text)
            _atomic_write(folder/'trading-summary.md',small)
            _atomic_write(folder/'handoff.json',json.dumps({'run_id':run_id,'checkpoint':markers[-1],'log_source':str(log),'ghost_files':manifest,'created_at':datetime.now(timezone.utc).isoformat()}))
            state['pending'].append(run_id);state['active']=None
            result={'published':run_id}
        elif action=='abort':
            if state['active']!=run_id: raise ValueError('Active run ID mismatch')
            state['active']=None;result={'aborted':run_id,'warning':'No completed handoff published; partial trading work must be reconciled separately'}
        elif action=='claim':
            if state['active'] or state['claimed']: result={'ready':False, **state}
            elif state['pending']:
                state['claimed']=state['pending'][0];result={'ready':True,'run_id':state['claimed'],'path':str(root/state['claimed'])}
            else: result={'ready':False,'reason':'No pending completed trading cycle'}
        elif action=='ack':
            if not run_id or state['claimed']!=run_id: raise ValueError('Claim ID mismatch')
            state['pending'].remove(run_id);state['claimed']=None
            _atomic_write(root/run_id/'processed.json',json.dumps({'processed_at':datetime.now(timezone.utc).isoformat()}))
            result={'processed':run_id}
        else: return state
        _atomic_write(state_path,json.dumps(state,indent=2))
        return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('action',choices=['begin','finish','abort','status','claim','ack'])
    p.add_argument('--run-id');p.add_argument('--log');p.add_argument('--summary')
    p.add_argument('--ghost-file',action='append',default=[],help='New ghost definition file; repeat for each file')
    a=p.parse_args()
    if a.action=='finish' and (not a.log or not a.summary):p.error('finish requires --log and --summary')
    print(json.dumps(operate(a.action,run_id=a.run_id,log=a.log,summary=a.summary,ghost_files=a.ghost_file)))

if __name__=='__main__': main()
