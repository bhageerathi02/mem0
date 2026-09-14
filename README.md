# Mem0 Paper Reimplementation

This project is intended to reproduce and productize the text-memory architecture
described in *Mem0: Building Production-Ready AI Agents with Scalable Long-Term
Memory*. Mem0g graph memory is deferred until the text-memory implementation and
LOCOMO evaluation are stable.

- [Product requirements document](docs/PRD.md)
- [Implementation architecture](docs/ARCHITECTURE.md)
- [Source paper](mem0paper.pdf)

The PRD distinguishes the April 2025 paper algorithm from later changes in the
upstream Mem0 project.

## Development

The project requires Python 3.12 or newer and uses
[uv](https://docs.astral.sh/uv/) for Python installation, dependency locking,
and package management.

Install the project and all development tools from the committed lockfile:

```shell
uv sync --locked --all-groups
```

Run the local quality checks:

```shell
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked mypy src tests
uv run --locked pytest
uv build
```

The installable distribution is named `mem0-text-memory`; its Python import
package is `memory_service`.
