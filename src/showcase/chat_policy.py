"""A deterministic response policy for a group-chat assistant prototype."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class IncomingMessage:
    text: str
    mentioned_bot: bool = False
    is_reply_to_bot: bool = False
    group_enabled: bool = True
    user_opted_out: bool = False
    quiet_hours: bool = False
    admin_command: bool = False


@dataclass(frozen=True)
class ResponseDecision:
    should_respond: bool
    reason: str


def decide_response(message: IncomingMessage) -> ResponseDecision:
    """Keep response gating separate from the actual Telegram/LLM integration."""
    if not message.group_enabled:
        return ResponseDecision(False, "AI is disabled for this group")
    if message.user_opted_out:
        return ResponseDecision(False, "User has opted out")
    if message.quiet_hours and not message.admin_command:
        return ResponseDecision(False, "Quiet hours are active")
    if message.admin_command:
        return ResponseDecision(True, "Administrative command requires handling")
    if message.mentioned_bot:
        return ResponseDecision(True, "Bot was explicitly mentioned")
    if message.is_reply_to_bot:
        return ResponseDecision(True, "Message replies to the bot")
    return ResponseDecision(False, "No direct interaction signal")
