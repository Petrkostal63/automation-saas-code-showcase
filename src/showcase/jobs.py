"""Explainable rule-based scoring for supplied job-listing records."""

from __future__ import annotations
from dataclasses import dataclass
import re
import unicodedata

TARGET_SKILLS = ("python", "api", "automation", "telegram", "scraping", "data", "fastapi", "javascript", "react")
RISK_PHRASES = ("guaranteed profit", "bypass protection", "steal credentials", "access someone else's account", "payment after profit")


@dataclass(frozen=True)
class JobListing:
    job_id: str
    title: str
    description: str
    budget_usd: int | None = None


@dataclass(frozen=True)
class JobScore:
    job_id: str
    score: int
    matched_skills: tuple[str, ...]
    rejected: bool
    reasons: tuple[str, ...]


def _normalise(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text or "")
    without_marks = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", without_marks.casefold()).strip()


def score_job(job: JobListing) -> JobScore:
    text = _normalise(f"{job.title} {job.description}")
    matched = tuple(skill for skill in TARGET_SKILLS if skill in text)
    risks = tuple(phrase for phrase in RISK_PHRASES if phrase in text)
    if risks:
        return JobScore(job.job_id, 0, matched, True, tuple(f"risk phrase: {p}" for p in risks))
    score = min(100, len(matched) * 12 + (15 if job.budget_usd and job.budget_usd > 0 else 0))
    reasons = tuple([f"matched: {skill}" for skill in matched] or ["no target keyword match"])
    return JobScore(job.job_id, score, matched, False, reasons)


def rank_jobs(jobs: list[JobListing]) -> list[JobScore]:
    """Rank supplied records deterministically; rejected jobs always rank last."""
    return sorted(jobs and [score_job(job) for job in jobs] or [], key=lambda item: (item.rejected, -item.score, item.job_id))
