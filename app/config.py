from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

_VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


class Settings(BaseSettings):
    """Application settings loaded from the environment."""

    app_name: str = "Python Template"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @field_validator("log_level")
    @classmethod
    def _validate_log_level(cls, value: str) -> str:
        normalized = value.upper()
        if normalized not in _VALID_LOG_LEVELS:
            valid = sorted(_VALID_LOG_LEVELS)
            raise ValueError(f"Invalid log level {value!r}; expected one of {valid}")
        return normalized


settings = Settings()
"""Singleton settings instance loaded from .env."""
