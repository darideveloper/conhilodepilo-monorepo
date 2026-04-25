# Project Context

## Purpose
The `leochan.sh.dashboard` project is a modern Django-based dashboard and administration system designed to manage content and media for the leochan.sh ecosystem. It prioritizes a clean administrative experience using the Unfold theme and provides a robust API for external consumption.

## Tech Stack
- **Backend:** Python 3.12, Django 5.2+
- **Database:** PostgreSQL (via `psycopg` 3)
- **API:** Django REST Framework (DRF)
- **Admin UI:** Django Unfold (Modern Tailwind-based theme)
- **Storage:** `django-storages` with AWS S3 or DigitalOcean Spaces (S3 compatible)
- **Static Files:** WhiteNoise for production serving
- **Deployment:** Docker (slim images), Gunicorn, Coolify
- **Frontend Utilities:** SimpleMDE for Markdown, Tailwind CSS (via Unfold)
- **Other:** `python-dotenv` for config, `django-solo` for singleton models, `django-cors-headers`

## Project Conventions

### Code Style
- **Environment Driven:** Configuration is strictly environment-variable-first using `python-dotenv`.
- **Naming:** Standard Django/Python (PEP 8) conventions.
- **Admin UI:** Custom Tailwind styles are injected via `static/js/add_tailwind_styles.js`.
- **Markdown:** All text areas in the admin are enhanced with SimpleMDE, featuring a custom typography layer that adapts to the project's dynamic brand colors.

### Architecture Patterns
- **Environment Isolation:** Uses `.env`, `.env.dev`, and `.env.prod` to manage configurations.
- **Dynamic Backends:** Database and Storage backends switch automatically based on the `ENV` and `STORAGE_AWS` flags.
- **Custom Backends:** Storage logic is centralized in `project/storage_backends.py`.
- **API Standards:** Standardized error responses via `project/handlers.py` and metadata-rich pagination via `project/pagination.py`.
- **API Synchronization:** Any modification, creation, or deletion of an API endpoint must be accompanied by corresponding updates to the automated tests AND the Bruno OpenCollection files (`bruno/**/*.yml`) in the same development cycle.
- **Utility Helpers:** Logic is organized into modular utility files (e.g., `utils/media.py`, `utils/admin_helpers.py`).

### Testing Strategy
- **Isolation:** Uses a separate SQLite database for testing (`testing.sqlite3`).
- **Tools:** Supports both standard Django tests and E2E browser automation with Selenium.
- **Reproduction:** Bugs must be empirically reproduced with a test case before applying fixes.

### Git Workflow
- **Commit Format:** Strictly follows [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): subject`.
- **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- **Branching:** Strategy is project-specific (defaults to feature branches).

## Domain Context
- **Media Management:** Includes specialized features like "Copy Link" for images, which uses a cookie-based strategy to bridge server-side actions with client-side clipboard APIs.
- **Admin Experience:** Heavily customized Unfold interface with environment-specific badges (Development, Production, etc.).

## Important Constraints
- **Private Files:** Must bypass custom CDN domains to support Signed URLs correctly.
- **Docker Build:** Credentials for S3 must be available during the Docker build process if `collectstatic` is run during build.
- **Containerization:** Must remain compatible with `python:3.12-slim`.

## External Dependencies
- **Cloud Storage:** AWS S3 or DigitalOcean Spaces.
- **SMTP:** Required for email notifications (if enabled).
- **CDNs:** Uses SimpleMDE CSS/JS from JSDelivr for the admin interface.
