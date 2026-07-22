# Magi

Magi is a provider-neutral experiment in multi-model deliberation. Independent model
participants answer the same question, critique anonymized alternatives, revise their own
answers, and pass the resulting evidence to an adjudicator.

## Current milestone

The repository currently contains:

- Provider-neutral request and response models
- An asynchronous provider protocol
- A deterministic fake provider for tests
- A minimal independent-response round
- A CLI smoke command

No commercial model provider is wired in yet. That is intentionally the next bounded task.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
pip install -e '.[dev,test]'
pre-commit install
pytest
mypy src
ruff check src tests
magi doctor
```

## Docker

The image derives its version from Git tags through `hatch-vcs`, so build from a Git checkout:

```bash
docker build -t magi:dev .
docker run --rm magi:dev doctor
```

## Intended workflow

```text
question
  -> independent answers
  -> blind critiques
  -> participant revisions
  -> adjudication
  -> final answer plus unresolved disagreements
```

The first implementation should keep this workflow fixed and bounded rather than creating an
open-ended agent conversation.
