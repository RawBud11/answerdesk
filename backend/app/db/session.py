"""Database engine and connectivity check."""

from functools import lru_cache

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from app.config import get_settings

# Seconds to wait for a new connection, so /health fails fast instead of hanging.
CONNECT_TIMEOUT_SECONDS = 5


@lru_cache
def get_engine() -> Engine:
    # pool_pre_ping replaces connections the database has closed, e.g. after a restart.
    return create_engine(
        str(get_settings().database_url),
        pool_pre_ping=True,
        connect_args={"connect_timeout": CONNECT_TIMEOUT_SECONDS},
    )


def database_is_reachable(engine: Engine) -> bool:
    """Return True if a trivial query succeeds, False on any database error."""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        return False
    return True
