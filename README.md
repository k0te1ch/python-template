# Python Project Template

A ready-to-use Python project template with:

- `logger` logging into `logs/` directory
- `.env` configuration loading via `pydantic-settings`
- `pytest` testing support
- `poetry` dependency management
- `ruff` static analysis
- `commitizen` — Conventional Commits validation (pre-commit)
- `release-please` — automated version bump, `CHANGELOG.md`, tags and GitHub Releases via CI

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

5. Install and run pre-commit hooks (the `--hook-type commit-msg` is required so
   commitizen validates commit messages):

   ```bash
   poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg
   poetry run pre-commit run --all-files
   ```

6. Setup self-hosted runner if project private

## Commits & releases

Полный гайд с диаграммами — [docs/WORKFLOW.md](docs/WORKFLOW.md).

Commit messages must follow [Conventional Commits](https://www.conventionalcommits.org/)
(`feat:`, `fix:`, `docs:`, `chore:`, `feat(scope)!: …` for breaking, etc.).
The commitizen `commit-msg` hook rejects non-conforming messages.

Releases are automated by [release-please](https://github.com/googleapis/release-please)
in CI — you never bump versions, write `CHANGELOG.md`, or create tags by hand:

1. Land well-formed Conventional Commits on `main` (the commit types decide the bump:
   `fix:` → patch, `feat:` → minor, `!` / `BREAKING CHANGE` → major).
2. `release-please` opens and maintains a **release PR** with the version bump in
   `pyproject.toml` + the changelog entry.
3. Merge that PR — release-please creates the `vX.Y.Z` tag and the GitHub Release.

The current released version is seeded in `.release-please-manifest.json`.

> Enable **Settings → Actions → General → Workflow permissions → "Read and write
> permissions"** and **"Allow GitHub Actions to create and approve pull requests"**,
> otherwise the action cannot open the release PR.

## Logging

Application logs are written to `logs/app.log` and the `logs/` directory is ignored by Git.

## Project layout

- `main.py` — entry point
- `app/config.py` — configuration model
- `app/logger.py` — logger setup
- `tests/` — test suite
- `.github/workflows/python-app.yml` — GitHub Actions CI (lint + tests on PRs)
- `.github/workflows/release-please.yml` — release automation (runs on push to `main`)
- `release-please-config.json` — release-please configuration (release-type, changelog)
- `.release-please-manifest.json` — current released version, owned by release-please
- `.pre-commit-config.yaml` — pre-commit configuration
- `CHANGELOG.md` — auto-generated changelog (owned by release-please)
- `.env.example` — example environment settings
