"""Run a small end-to-end demonstration with synthetic sample inputs."""

from __future__ import annotations
import json
from pathlib import Path
from .jobs import JobListing, rank_jobs
from .chat_policy import IncomingMessage, decide_response
from .video_workflow import build_dry_run_plan
from .market_data import Observation, detect_burst

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    sample_jobs = json.loads((ROOT / "sample_data" / "jobs.json").read_text(encoding="utf-8"))
    jobs = [JobListing(item["job_id"], item["title"], item["description"], item.get("budget_usd")) for item in sample_jobs]
    print("JOB SCORING")
    for result in rank_jobs(jobs):
        print(f"- {result.job_id}: score={result.score}, rejected={result.rejected}, matched={result.matched_skills}")

    print("\nCHAT RESPONSE POLICY")
    print(decide_response(IncomingMessage("hello", mentioned_bot=True)))

    print("\nVIDEO WORKFLOW PLAN")
    for step in build_dry_run_plan():
        print(f"- {step['step']}: {step['status']}")

    print("\nMARKET ALERT (SYNTHETIC DATA)")
    print(detect_burst([Observation(100, 100), Observation(100.1, 100), Observation(102, 200)]))


if __name__ == "__main__":
    main()
