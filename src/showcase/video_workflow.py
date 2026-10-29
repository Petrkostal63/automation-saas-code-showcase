"""Build a dry-run plan for a video workflow; no APIs or media are invoked."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class WorkflowStep:
    name: str
    purpose: str
    requires_external_service: bool = False


DEFAULT_STEPS = (
    WorkflowStep("source_selection", "Choose eligible news or trend inputs"),
    WorkflowStep("script_draft", "Draft a script and validate the expected duration", True),
    WorkflowStep("voiceover", "Create narration and word timing", True),
    WorkflowStep("visual_assets", "Select stock footage or approved assets", True),
    WorkflowStep("subtitles", "Build timed captions"),
    WorkflowStep("render", "Assemble clips, audio and captions with a media renderer", True),
    WorkflowStep("quality_check", "Verify duration, missing assets and output file"),
    WorkflowStep("upload", "Publish only after an explicit approval gate", True),
)


def build_dry_run_plan(*, upload_approved: bool = False) -> list[dict[str, str | bool]]:
    """Return the planned steps; the final upload step remains blocked by default."""
    plan = []
    for step in DEFAULT_STEPS:
        status = "planned"
        if step.name == "upload" and not upload_approved:
            status = "blocked: explicit approval required"
        plan.append({
            "step": step.name,
            "purpose": step.purpose,
            "external_service": step.requires_external_service,
            "status": status,
        })
    return plan
