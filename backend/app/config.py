"""Application settings, read from environment variables (or a local .env file)."""

from functools import lru_cache
from pathlib import Path

from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

# The single .env file lives at the repository root, shared with Docker Compose.
# Real environment variables take precedence; a missing file is ignored.
ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    # Required, with no default, so a missing value fails at startup instead of
    # silently connecting somewhere unexpected.
    database_url: PostgresDsn = Field(
        description="SQLAlchemy URL, e.g. postgresql+psycopg://user:pass@host:5432/db"
    )
    environment: str = Field(default="local", description="local, ci or production")


@lru_cache
def get_settings() -> Settings:
    return Settings()  # values come from the environment or .env
