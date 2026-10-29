import unittest
from showcase.jobs import JobListing, rank_jobs, score_job


class JobScoringTests(unittest.TestCase):
    def test_risk_phrase_rejects_even_if_skills_match(self):
        job = JobListing("risk", "Python API", "Guaranteed profit using Python API", 300)
        result = score_job(job)
        self.assertTrue(result.rejected)
        self.assertEqual(result.score, 0)

    def test_relevant_job_scores_and_matches_skills(self):
        job = JobListing("good", "Python API integration", "Please build and test a REST integration. " * 5, 250)
        result = score_job(job)
        self.assertFalse(result.rejected)
        self.assertIn("python", result.matched_skills)
        self.assertGreaterEqual(result.score, 50)

    def test_ranking_is_deterministic(self):
        jobs = [JobListing("b", "Misc", "short"), JobListing("a", "Python", "Python automation " * 12, 200)]
        first = [j.job_id for j in rank_jobs(jobs)]
        second = [j.job_id for j in rank_jobs(jobs)]
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
