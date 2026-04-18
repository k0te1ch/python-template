# Python Project Template

A ready-to-use Python project template with:

- `logger` logging into `logs/` directory
- `.env` configuration loading via `pydantic-settings`
- `pytest` testing support
- `poetry` dependency management
- `ruff` static analysis

## Quick start

1. Install dependencies:

   ```bash
   poetry install
   ```

2. Copy `.env.example` to `.env` and update values:

   ```bash
   copy .env.example .env
   ```

3. Run the application:

   ```bash
   poetry run python main.py
   ```

4. Run tests:

   ```bash
   poetry run pytest
   ```

5. Run pre-commit hooks:

   ```bash
   poetry run pre-commit install
   poetry run pre-commit run --all-files
   ```

## Logging

Application logs are written to `logs/app.log` and the `logs/` directory is ignored by Git.

## Project layout

- `main.py` — entry point
- `app/config.py` — configuration model
- `app/logger.py` — logger setup
- `tests/` — test suite
- `.github/workflows/python-app.yml` — GitHub Actions CI
- `.pre-commit-config.yaml` — pre-commit configuration
- `.env.example` — example environment settings
