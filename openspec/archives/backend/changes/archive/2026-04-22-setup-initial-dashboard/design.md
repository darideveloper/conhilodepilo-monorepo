# Design: Setup Initial Dashboard

## Architectural Overview
The project follows a modular, environment-centric architecture.

### Configuration Management
We use `python-dotenv` to load environment variables from three files:
1. `.env`: Main entry point (determines the environment: `dev`, `prod`).
2. `.env.dev`: Local development defaults.
3. `.env.prod`: Production placeholders.

This ensures that the same code can run in different environments by simply changing the environment variables.

### Admin UI (Unfold)
`django-unfold` is used to provide a modern, Tailwind-based interface. We extend it by:
- Injecting custom CSS/JS in `project/templates/admin/base.html`.
- Using `static/js/add_tailwind_styles.js` for on-the-fly styling.
- Integrating `SimpleMDE` for markdown support in text fields.

### Storage Strategy
The `project/storage_dashboards.py` file centralizes S3-compatible storage logic. We use conditional logic in `settings.py` to switch between local file storage (dev) and AWS S3/DigitalOcean Spaces (prod) based on the `STORAGE_AWS` flag.

### API Standards
- **Pagination**: `CustomPageNumberPagination` provides metadata-rich responses (count, next, previous, page, page_size, total_pages).
- **Error Handling**: `custom_exception_handler` standardizes error responses across the API.

### Deployment
A multi-stage-like Dockerfile (though single-stage here for simplicity) uses `python:3.12-slim` and handles static collection during build time (requiring build-time ARGs for credentials). `start.sh` ensures migrations are run before starting `gunicorn`.
