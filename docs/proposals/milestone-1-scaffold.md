# Proposal: Milestone 1 scaffold

**Status: Step 1 approved and implemented on 2026-10-07 (uv, Python 3.13, no GitHub
remote yet). Later steps still need their own plans and approval.**

This answers the Milestone 1 kickoff prompt (strategy, Section 9): the files, the
dependencies and why, and the decisions needed before any code is written. Per
CLAUDE.md, each step below starts with a 3-6 line plan and waits for approval.

## Machine check (2026-10-06)
Available locally: Docker 29.8 with Compose v5.5, Python 3.14 / 3.13 / 3.10,
uv 0.12, Node 24, GitHub CLI 2.102. Versions of packages are pinned at install
time, not from this document.

## Step 1: scaffold only (no retrieval code)

### Files
```
docker-compose.yml        # postgres (pgvector image) + backend
.env.example              # every setting, no real values
README.md                 # stub: what it is, how to run
backend/
  pyproject.toml          # dependencies, ruff, mypy and pytest settings
  Dockerfile
  alembic.ini
  alembic/env.py
  alembic/versions/0001_enable_pgvector.py   # CREATE EXTENSION vector only
  app/main.py             # FastAPI app, /api/v1 router
  app/config.py           # settings read from environment variables
  app/api/health.py       # GET /api/v1/health: liveness + DB check
  app/db/session.py       # engine and session factory
  tests/test_health.py
.pre-commit-config.yaml   # ruff + mypy on commit
.github/workflows/ci.yml  # lint, type check, tests with a Postgres service
```

### Dependencies (each needs your approval)
| Package | Kind | What it does | Why it is needed |
|---|---|---|---|
| fastapi | runtime | Web framework | The backend API (stack table) |
| uvicorn | runtime | ASGI server | Runs the FastAPI app |
| pydantic-settings | runtime | Typed settings from env vars | `config.py`; CLAUDE.md requires env-based config |
| sqlalchemy (2.x) | runtime | ORM and SQL toolkit | DB access (stack table) |
| psycopg (v3) | runtime | PostgreSQL driver | SQLAlchemy needs a driver |
| alembic | runtime | Schema migrations | Stack table |
| pytest | dev | Test runner | Testing strategy |
| httpx | dev | HTTP client | Required by FastAPI's `TestClient` |
| ruff | dev | Linter and formatter | Tooling baseline |
| mypy | dev | Type checker | "Keep functions small and typed" |
| pre-commit | dev | Runs checks on commit | Tooling baseline |

Docker image: `pgvector/pgvector` (Postgres with the extension preinstalled).

**Done when:** `docker compose up` starts both services, `/api/v1/health` reports
the database as reachable, and CI passes on a pull request.

## Later Milestone 1 steps (separate plans, separate approvals)
1. `articles` and `chunks` tables + migration (needs the embedding dimension).
2. Article loader for `content/articles/` (front-matter parser: new dependency).
3. Chunker, tests first (strategy's chunker prompt).
4. Embedding service (`sentence-transformers` and PyTorch: large download, CPU
   only is enough).
5. Hybrid retrieval: vector + full-text (ADR 0003), RRF, tests first.
6. Refusal decision (ADR 0002) and citation verifier (ADR 0004), tests first.
7. LLM adapter, fake LLM, one real provider (ADR 0008).
8. `/api/v1/chat` returning a cited answer (not streamed yet).

## Decisions needed from you
1. **Package manager:** uv (fast, lockfile for reproducible installs; one more
   tool to learn) or pip + venv (most familiar; no lockfile unless added).
   Recommendation: uv, since it is already installed and a lockfile makes CI and
   Docker match your machine.
2. **Python version:** 3.12 or 3.13 in Docker and CI. 3.14 is installed locally,
   but check that PyTorch publishes wheels for it before choosing it.
   Recommendation: 3.13 everywhere.
3. **Embedding model** (needed by step 1 of the later list, because it fixes the
   `vector(n)` column size). Candidates to evaluate: small multilingual E5-class
   or MiniLM-class models. Check licence, size and EN/ES quality before choosing.
4. **LLM provider:** ADR 0008, due at the start of Milestone 1.
5. **GitHub repository:** CI needs a remote. Create it yourself, or approve
   creating a private one with `gh repo create`.
