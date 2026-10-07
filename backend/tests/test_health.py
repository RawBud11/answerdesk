from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from app.api.health import check_database
from app.config import get_settings
from app.db.session import database_is_reachable, get_engine
from app.main import create_app


def client_with_database(reachable: bool) -> TestClient:
    app = create_app()
    app.dependency_overrides[check_database] = lambda: reachable
    return TestClient(app)


def test_health_ok_when_database_reachable() -> None:
    response = client_with_database(reachable=True).get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}


def test_health_503_when_database_unavailable() -> None:
    response = client_with_database(reachable=False).get("/api/v1/health")

    assert response.status_code == 503
    assert response.json() == {"status": "degraded", "database": "unavailable"}


@pytest.fixture
def real_database() -> Iterator[None]:
    """Skip when no database is configured; fail (not skip) if one is configured but down."""
    try:
        get_settings()
    except ValidationError:
        pytest.skip("DATABASE_URL not set in the environment or .env")
    get_engine.cache_clear()
    yield
    get_engine().dispose()
    get_engine.cache_clear()


@pytest.mark.integration
@pytest.mark.usefixtures("real_database")
def test_real_database_is_reachable() -> None:
    assert database_is_reachable(get_engine())


@pytest.mark.integration
@pytest.mark.usefixtures("real_database")
def test_health_against_real_database() -> None:
    response = TestClient(create_app()).get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["database"] == "ok"
