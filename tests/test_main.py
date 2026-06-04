from pathlib import Path

import pytest

import main as main_module
from app.config import Settings
from app.logger import configure_logger


def test_settings_load_from_env(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Verify settings load from a temporary .env file."""
    env_file = tmp_path / ".env"
    env_file.write_text("APP_NAME=TestApp\nLOG_LEVEL=DEBUG\n")

    monkeypatch.chdir(tmp_path)
    settings = Settings()

    assert settings.app_name == "TestApp"
    assert settings.log_level == "DEBUG"


def test_logger_writes_to_log_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Verify logger writes entries into the logs directory."""
    monkeypatch.chdir(tmp_path)
    settings = Settings(app_name="TestApp", log_level="DEBUG")
    logger = configure_logger(settings)

    logger.debug("Unit test log entry")
    log_file = tmp_path / "logs" / "app.log"

    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "Unit test log entry" in content


def test_main_runs_without_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Verify the entry point runs end-to-end without raising."""
    monkeypatch.chdir(tmp_path)

    main_module.main()

    assert (tmp_path / "logs" / "app.log").exists()


def test_invalid_log_level_rejected() -> None:
    """Verify an unknown log level is rejected at settings construction."""
    with pytest.raises(ValueError):
        Settings(log_level="NOPE")
