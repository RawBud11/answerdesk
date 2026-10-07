# AnswerDesk

An embeddable support chat assistant that answers only from a business's own
help-center content, cites its sources, says "I don't know" when it should, and
hands off to a person. Built with a published English/Spanish evaluation.

**Status: early development (Milestone 1).** Only the backend scaffold exists: a
FastAPI app with a health check, PostgreSQL with pgvector, migrations, and CI.
There is no retrieval, chat, widget, or admin console yet.

The demo business, Larchwick Outfitters, is fictional; all content is synthetic.

## Run it locally

Prerequisites: Docker with Compose, and [uv](https://docs.astral.sh/uv/) for
running the backend tools outside Docker.

```sh
cp .env.example .env          # then choose your own password in .env
docker compose up --build
```

Then open <http://127.0.0.1:8000/api/v1/health>. It returns
`{"status": "ok", "database": "ok"}`, or HTTP 503 with `"degraded"` if the
database is unreachable. The interactive API docs are at
<http://127.0.0.1:8000/docs>.

The backend container applies database migrations on startup.

## Development

```sh
cd backend
uv sync                       # create .venv with the locked dependencies
uv run ruff check .           # lint
uv run ruff format --check .  # formatting
uv run mypy                   # type check (strict)
uv run pytest                 # tests
uv run alembic upgrade head   # apply migrations to the database in .env
```

Integration tests run against the database in `DATABASE_URL` (from `.env` or the
environment) and are skipped when it is not set. Start the database alone with
`docker compose up -d db`.

Optional git hook that runs lint, format, and type checks before each commit:

```sh
uv run --project backend pre-commit install
```

## Repository layout

| Path | Contents |
|---|---|
| `backend/` | FastAPI app, Alembic migrations, tests |
| `content/` | Synthetic help-center articles (drafts) |
| `eval/` | Evaluation question set (draft) |
| `docs/strategy.md` | Development plan |
| `docs/decisions/` | Architecture decision records |
| `docs/proposals/` | Plans awaiting or after approval |
