"""FastAPI application entry point."""

from fastapi import APIRouter, FastAPI

from app.api import health

API_PREFIX = "/api/v1"


def create_app() -> FastAPI:
    app = FastAPI(
        title="AnswerDesk API",
        version="0.1.0",
        description="Grounded, cited answers from a help center.",
    )
    api = APIRouter(prefix=API_PREFIX)
    api.include_router(health.router)
    app.include_router(api)
    return app


app = create_app()
