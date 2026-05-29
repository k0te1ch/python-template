# Python Project Template

A ready-to-use Python project template with:

- `logger` logging into `logs/` directory
- `.env` configuration loading via `pydantic-settings`
- `pytest` testing support
- `poetry` dependency management
- `ruff` static analysis
- `commitizen` — Conventional Commits validation (pre-commit) and version bump
- `git-cliff` — automated `CHANGELOG.md` + GitHub Release notes

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

To cut a release:

```bash
poetry run cz bump          # bumps version in pyproject.toml, commits, creates tag
git push --follow-tags      # pushing the tag triggers .github/workflows/release.yml
```

The release workflow generates Release Notes for the new tag with `git-cliff --latest`,
publishes a GitHub Release, regenerates the full `CHANGELOG.md`, and commits it back to `main` —
so you do not need `git-cliff` installed locally.

Before the first release, set `owner`/`repo` in `cliff.toml` so PR and author links resolve.

To preview the changelog locally (optional), install `git-cliff` (`scoop install git-cliff`
on Windows, `cargo install git-cliff`, or download from
[git-cliff releases](https://github.com/orhun/git-cliff/releases)) and run:

```bash
git-cliff --unreleased      # preview pending changes
git-cliff -o CHANGELOG.md   # rewrite the full changelog
```

## Logging

Application logs are written to `logs/app.log` and the `logs/` directory is ignored by Git.

## Project layout

- `main.py` — entry point
- `app/config.py` — configuration model
- `app/logger.py` — logger setup
- `tests/` — test suite
- `.github/workflows/python-app.yml` — GitHub Actions CI
- `.github/workflows/release.yml` — Release workflow (triggered by `v*` tags)
- `.pre-commit-config.yaml` — pre-commit configuration
- `cliff.toml` — git-cliff (changelog generator) configuration
- `CHANGELOG.md` — auto-generated changelog
- `.env.example` — example environment settings
