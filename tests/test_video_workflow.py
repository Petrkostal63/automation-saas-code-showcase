import unittest
from showcase.video_workflow import build_dry_run_plan


class VideoWorkflowTests(unittest.TestCase):
    def test_upload_is_blocked_by_default(self):
        plan = {item["step"]: item for item in build_dry_run_plan()}
        self.assertIn("blocked", plan["upload"]["status"])

    def test_plan_has_expected_order(self):
        names = [item["step"] for item in build_dry_run_plan()]
        self.assertEqual(names[0], "source_selection")
        self.assertEqual(names[-1], "upload")

    def test_explicit_upload_approval_changes_plan_label_only(self):
        plan = {item["step"]: item for item in build_dry_run_plan(upload_approved=True)}
        self.assertEqual(plan["upload"]["status"], "planned")
        # The planner does not actually upload media.


if __name__ == "__main__":
    unittest.main()
