"""Metadata-only upload validation example; not a complete file-security layer."""

from __future__ import annotations
from dataclasses import dataclass


ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_UPLOAD_BYTES = 12 * 1024 * 1024


@dataclass(frozen=True)
class UploadCheck:
    accepted: bool
    reason: str


def validate_upload(*, filename: str, content_type: str, size_bytes: int) -> UploadCheck:
    """Check metadata only; production code must also inspect/decode file contents."""
    if not filename.strip():
        return UploadCheck(False, "Filename is required")
    if content_type.lower() not in ALLOWED_CONTENT_TYPES:
        return UploadCheck(False, "Unsupported content type")
    if size_bytes <= 0:
        return UploadCheck(False, "File must not be empty")
    if size_bytes > MAX_UPLOAD_BYTES:
        return UploadCheck(False, "File exceeds the 12 MiB demo limit")
    return UploadCheck(True, "Metadata accepted; file contents still need safe validation")
