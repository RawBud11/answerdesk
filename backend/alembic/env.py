"""Alembic migration environment. The database URL comes from app settings."""

from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, pool

from app.config import get_settings

if context.config.config_file_name is not None:
    fileConfig(context.config.config_file_name)

# No ORM models yet; set this to the models' metadata once tables exist.
target_metadata = None


def run_migrations_offline() -> None:
    """Write the SQL to stdout instead of running it (alembic upgrade --sql)."""
    context.configure(url=str(get_settings().database_url), target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    engine = create_engine(str(get_settings().database_url), poolclass=pool.NullPool)
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
