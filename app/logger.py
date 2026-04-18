import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from app.config import Settings


def configure_logger(settings: Settings) -> logging.Logger:
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(settings.app_name)
    logger.setLevel(settings.log_level.upper())
    logger.propagate = False

    formatter = logging.Formatter(
        "%Y-%m-%d %H:%M:%S | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        log_dir / "app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(settings.log_level.upper())

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
