"""Mem0 text-memory service."""

from importlib.metadata import version as _distribution_version

__version__: str = _distribution_version("mem0-text-memory")

__all__ = ["__version__"]
