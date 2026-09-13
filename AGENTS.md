# Project instructions

Before making implementation changes:

1. Read `docs/PRD.md` for product requirements and acceptance criteria.
2. Read `docs/ARCHITECTURE.md` for system boundaries, data flow, and technical decisions.
3. Preserve the research profile separately from production-only enhancements.
4. Do not introduce a new service, datastore, framework, or cross-module dependency
   without updating `docs/ARCHITECTURE.md` and recording the reason.
5. Run the tests and evaluation checks appropriate to the affected module.

If the PRD and architecture document conflict, stop and resolve the documentation
before implementing the conflicting behavior.

## Code Review Rules

- Flag implementation that conflicts with `docs/PRD.md` or
  `docs/ARCHITECTURE.md`, including graph-memory functionality while it remains
  deferred.
- Flag any new service, datastore, framework, or cross-module dependency that is
  introduced without updating `docs/ARCHITECTURE.md` and recording the reason.
- Flag implementation changes that lack tests or evaluation checks appropriate
  to the affected module, or that mix the research profile with production-only
  enhancements.
