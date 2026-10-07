"""GET /api/v1/health: liveness plus a database check."""

from typing import Annotated, Literal

from fastapi import APIRouter, Depends, Response, status
from pydantic import BaseModel

from app.db.session import database_is_reachable, get_engine

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: Literal["ok", "degraded"]
    database: Literal["ok", "unavailable"]


def check_database() -> bool:
    return database_is_reachable(get_engine())


@router.get("/health", response_model=HealthResponse)
def health(
    response: Response, database_ok: Annotated[bool, Depends(check_database)]
) -> HealthResponse:
    if database_ok:
        return HealthResponse(status="ok", database="ok")
    # 503 tells load balancers and uptime checks that the service cannot do its job.
    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return HealthResponse(status="degraded", database="unavailable")
