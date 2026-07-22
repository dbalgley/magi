# Agent instructions

## Project intent

Magi is a provider-neutral multi-model deliberation engine. Preserve independence between
initial participant responses and preserve unresolved disagreement in final results.

## Engineering constraints

- Python 3.12 or newer.
- Keep provider-specific SDK objects inside `magi.providers`.
- Domain and orchestration code must depend on the `ModelProvider` protocol, not concrete SDKs.
- Use Pydantic models at external and persistence boundaries.
- Use explicit exception types for expected provider failures; do not use a bare
  `except Exception` unless re-raising after recording unexpected failure context.
- Add or update tests for every behavior change.
- Keep orchestration rounds bounded and deterministic in structure.
- Do not add LangChain, LangGraph, CrewAI, or another orchestration framework without an ADR.
- Do not add a database, web API, or frontend before the CLI vertical slice works.

## Required checks

Run before declaring a task complete:

```bash
ruff check src tests
ruff format --check src tests
mypy src
pytest
```

## Change discipline

- Make one focused change per task.
- Explain assumptions before implementing ambiguous behavior.
- Report commands run and any checks that were not run.
