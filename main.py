"""Application entry point for the Python project template."""

from app.config import settings
from app.logger import configure_logger


def main() -> None:
    """Run the template application.

    Loads environment settings, configures logging, and emits startup log messages.
    """
    logger = configure_logger(settings)
    logger.info("Application started")
    logger.debug("Current settings loaded: %s", settings.model_dump())
    logger.info("Hello from the Python project template!")


if __name__ == "__main__":
    main()
