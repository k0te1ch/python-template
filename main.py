from app.config import Settings
from app.logger import configure_logger


def main() -> None:
    settings = Settings()
    logger = configure_logger(settings)
    logger.info("Application started")
    logger.debug("Current settings loaded: %s", settings.dict())
    logger.info("Hello from the Python project template!")


if __name__ == "__main__":
    main()
