"""Tiny alert-only price/volume calculation over caller-supplied observations."""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Observation:
    close: float
    volume: float


@dataclass(frozen=True)
class BurstAlert:
    triggered: bool
    price_change_pct: float
    latest_volume: float
    prior_average_volume: float
    reasons: tuple[str, ...]


def detect_burst(observations: list[Observation], *, price_threshold_pct: float = 1.0, volume_multiple: float = 1.5) -> BurstAlert:
    if len(observations) < 2:
        raise ValueError("At least two observations are required")
    if any(item.close <= 0 or item.volume < 0 for item in observations):
        raise ValueError("Prices must be positive and volume nonnegative")
    previous, latest = observations[-2], observations[-1]
    price_change = (latest.close / previous.close - 1.0) * 100.0
    prior_volumes = [item.volume for item in observations[:-1]]
    prior_average = sum(prior_volumes) / len(prior_volumes)
    price_hit = abs(price_change) >= price_threshold_pct
    volume_hit = prior_average > 0 and latest.volume >= prior_average * volume_multiple
    reasons = tuple(reason for hit, reason in ((price_hit, "price threshold crossed"), (volume_hit, "relative volume threshold crossed")) if hit)
    return BurstAlert(price_hit and volume_hit, price_change, latest.volume, prior_average, reasons)
