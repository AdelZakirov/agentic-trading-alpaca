from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from alpaca_agent.ghost_queue import operate

class QueueTests(unittest.TestCase):
    def test_handoff_claim_and_ack(self):
        with TemporaryDirectory() as d:
            root=Path(d)/'queue';log=Path(d)/'log';summary=Path(d)/'summary'
            rid=operate('begin',root)['run_id']
            self.assertFalse(operate('claim',root)['ready'])
            log.write_text('trade\n<!-- run-checkpoint: 2026-09-10T18:00:00+02:00 -->')
            summary.write_text('Covers full log through 2026-09-10T18:00:00+02:00')
            operate('finish',root,rid,log,summary)
            log.write_text('changed')
            self.assertIn('trade',(root/rid/'trading-log.md').read_text())
            self.assertTrue(operate('claim',root)['ready'])
            self.assertFalse(operate('claim',root)['ready'])
            operate('ack',root,rid)
            self.assertEqual(operate('status',root)['pending'],[])
    def test_incomplete_log_not_published(self):
        with TemporaryDirectory() as d:
            root=Path(d)/'queue';log=Path(d)/'log';log.write_text('incomplete')
            rid=operate('begin',root)['run_id']
            with self.assertRaises(ValueError):operate('finish',root,rid,log,log)
            self.assertEqual(operate('status',root)['pending'],[])

    def test_ghost_snapshot_and_invalid_attachment(self):
        import json
        with TemporaryDirectory() as d:
            root=Path(d)/'queue'; log=Path(d)/'log'; summary=Path(d)/'summary'
            log.write_text('<!-- run-checkpoint: now -->')
            summary.write_text('Covers full log through now')
            ghost=Path(d)/'ghost-trades'/'2026-09-10'/'decision.md'
            ghost.parent.mkdir(parents=True);ghost.write_text('original alternatives')
            rid=operate('begin',root)['run_id']
            with self.assertRaises(ValueError):
                operate('finish',root,rid,log,summary,ghost_files=[log])
            self.assertEqual(operate('status',root)['active'],rid)
            with self.assertRaises(ValueError):
                operate('finish',root,rid,log,summary,ghost_files=[ghost,ghost])
            operate('finish',root,rid,log,summary,ghost_files=[ghost])
            ghost.write_text('later checkpoint')
            manifest=json.loads((root/rid/'handoff.json').read_text())['ghost_files']
            self.assertEqual(len(manifest),1)
            self.assertEqual(manifest[0]['source'],str(ghost.resolve()))
            self.assertEqual((root/rid/manifest[0]['snapshot']).read_text(),'original alternatives')
