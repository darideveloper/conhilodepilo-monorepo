# Proposal: Setup Initial Dashboard

This proposal outlines the steps to initialize and configure the `con hilo depilo` dashboard project from scratch, following the provided documentation for project setup and Django Unfold integration.

## Problem Statement
The project needs a modern, robust, and environment-driven Django dashboard with a customized administrative interface and integrated API capabilities.

## Proposed Solution
We will scaffold a Django 5.2 project with a "booking" application, integrate `django-unfold` for the admin UI, and establish an environment-variable-first configuration for database, storage, and security. The project will be configured for the `Europe/Madrid` timezone and will include full email functionality.

## Scope
- Initial project scaffolding and dependency management.
- Environment infrastructure (.env, .env.dev, .env.prod).
- Refactored `settings.py` for dynamic behavior.
- Core project wiring (pagination, storage backends, exception handlers).
- Modern Admin UI with `django-unfold` and custom enhancements.
- Deployment configuration (Dockerfile, start.sh).

## Success Criteria
- Django project starts without errors.
- Admin interface is accessible and styled with Unfold.
- Environment variables correctly drive the configuration.
- API endpoints (pagination, error handling) follow the specified standards.
- Docker image can be built and run.
