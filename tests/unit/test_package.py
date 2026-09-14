"""Package-level smoke tests."""

from importlib import import_module
from importlib.metadata import version

import memory_service

ARCHITECTURAL_NAMESPACES = (
    "api",
    "application",
    "config",
    "domain",
    "ingestion",
    "prompts",
    "providers",
    "repositories",
    "retrieval",
    "telemetry",
    "workflows",
)


def test_package_exposes_distribution_version() -> None:
    """The public package version matches the installed project metadata."""
    assert memory_service.__version__ == "0.1.0"
    assert memory_service.__version__ == version("mem0-text-memory")


def test_architectural_namespaces_import() -> None:
    """Every package boundary defined by the architecture is importable."""
    for namespace in ARCHITECTURAL_NAMESPACES:
        module = import_module(f"memory_service.{namespace}")
        assert module.__name__ == f"memory_service.{namespace}"
