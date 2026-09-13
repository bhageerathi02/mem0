# ADR-0001: Defer Mem0g Graph Memory

## Status

Accepted on 2026-09-13.

## Context

The initial PRD and architecture included both the paper's Mem0 text-memory
pipeline and the Mem0g graph-memory extension. Implementing both at once adds a
second datastore, additional extraction and conflict-resolution prompts, an
asynchronous projection path, retrieval fusion, and a separate evaluation
surface before the foundational text-memory behavior has been validated.

The immediate product goal is to master the paper's Mem0 text-memory path:
message-pair ingestion, summary and recency context, salient fact extraction,
dense similarity, four-way reconciliation, retrieval, answer generation, and
LOCOMO evaluation.

## Decision

Mem0g is outside the active product and implementation scope. The current
architecture must not include a graph datastore, graph repository, graph
projection workflow, entity or relationship extraction, graph retrieval,
retrieval fusion, graph-specific APIs, graph SLOs, or graph acceptance gates.

The paper's Mem0g design remains a future reference only. Reintroducing it
requires a new ADR plus coordinated PRD and architecture updates after the Mem0
text-memory research profile has passed its evaluation gates.

## Consequences

- PostgreSQL with pgvector is the only memory datastore in the active design.
- The implementation and evaluation plan targets Mem0 text memory only.
- Production hardening follows the text-memory evaluation instead of waiting
  for Mem0g.
- No graph-related dependency or module may be introduced under the current
  architecture.
- A future Mem0g design must preserve the stable text-memory research profile
  and independently resolve the paper-fidelity questions around graph input,
  thresholds, traversal, and result combination.
