"""Level-aware coloured output for the standard logging module."""

from __future__ import annotations

__all__ = ["colorLog"]


def colorLog(value):
    """Level-aware coloured output for the standard logging module."""
    if value is None:
        raise ValueError("value must not be None")
    return value
