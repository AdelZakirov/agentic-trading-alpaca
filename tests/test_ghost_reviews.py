import unittest
from tempfile import TemporaryDirectory
from pathlib import Path
from alpaca_agent.ghost_reviews import update, summary, validate

class ReviewTests(unittest.TestCase):
    def test_inventory_is_not_evidence_and_upsert_is_idempotent(self):
        with TemporaryDirectory() as d:
            root=Path(d);(root/'2026-09-10').mkdir();source=root/'2026-09-10'/'order.md';source.write_text('- Status: COMPLETE\n')
            self.assertEqual(summary(update(root))['reviewed'],0)
            r=dict(ghost_id='order',source=str(source),review_status='reviewed',decision_id='decision',ticker='ABC',evaluated_at='2026-09-10',conditions=['trend'],question='timing',outcomes=[dict(label='real',pnl=None,capital_at_risk=None,scorable=False,reason='missing quotes')],data_quality='unscorable',conclusion='No payoff conclusion',lesson_ids=[])
            update(root,r);update(root,r)
            stats=summary(update(root));self.assertEqual(stats['sets'],1);self.assertEqual(stats['independent_decisions'],1)
    def test_missing_fields_rejected(self):
        with self.assertRaises(ValueError):validate({})
