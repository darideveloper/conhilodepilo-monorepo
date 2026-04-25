# Tasks: Setup Bruno API Collection

## Infrastructure
- [x] Create the `bruno/` directory and subdirectories (`environments/`, `Booking/`).
- [x] Initialize `opencollection.yml` with project name and Bruno configuration.
- [x] Update `.gitignore` to exclude `bruno/.env`.

## Environments
- [x] Create `bruno/environments/Local.yml` with `base_url` set to `http://localhost:8000`.
- [x] Create `bruno/environments/Development.yml` with a placeholder for the dev server URL.
- [x] Create `bruno/environments/Production.yml` with a placeholder for the production server URL.

## Requests
- [x] Create `bruno/Booking/Get Company Config.yml` for the `GET /api/config/` endpoint using OpenCollection YAML format.
- [x] Add an assertion to `Get Company Config.yml` to verify a `200 OK` response.

## Validation
- [x] Verify that the collection can be opened in Bruno v3+.
- [x] Verify that the `Local` environment correctly resolves the `base_url`.
- [x] Verify that `bruno/.env` is ignored by Git.
