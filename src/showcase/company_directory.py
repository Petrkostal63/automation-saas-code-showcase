"""Typed sample data and deterministic promotional directory ordering."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Company:
    company_id: str
    display_name: str
    country: str
    sector: str
    confirmed_promotion_usd: int
    total_confirmed_at: datetime


def order_promotional_directory(companies: list[Company]) -> list[Company]:
    """Order by confirmed promotional support, then timestamp, then stable ID.

    This demo's ranking reflects promotion only; it is not a quality or trust score.
    """
    return sorted(
        companies,
        key=lambda company: (
            -company.confirmed_promotion_usd,
            company.total_confirmed_at,
            company.company_id,
        ),
    )
