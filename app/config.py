from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from the environment."""

    app_name: str = "Python Template"
    log_level: str = "INFO"

    model_config: dict[str, str] = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
"""Singleton settings instance loaded from .env."""
