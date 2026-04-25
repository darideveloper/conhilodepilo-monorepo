# environment Specification

## Purpose
TBD - created by archiving change setup-initial-dashboard. Update Purpose after archive.
## Requirements
### Requirement: Dependency Management
The project MUST use a `requirements.txt` file for dependency management, including Django 5.2, Unfold, DRF, and storage adapters.

#### Scenario: Install Dependencies
- Given a `requirements.txt` file with specified versions.
- When running `pip install -r requirements.txt`.
- Then all necessary packages are installed in the virtual environment.

### Requirement: Environment Configuration
The project MUST use environment variables for configuration, loaded via `python-dotenv` from `.env`, `.env.dev`, and `.env.prod`.

#### Scenario: Load Environment Variables
- Given `.env` files with configuration values.
- When the Django application starts.
- Then the variables are correctly loaded into `os.environ`.

### Requirement: Source Control Strategy
The project SHALL use a `.gitignore` file that ignores active OpenSpec proposals in `openspec/changes/` while preserving the `archive/` directory.

#### Scenario: Ignore Active Proposals
- When checking the git status.
- Then files under `openspec/changes/` (except for `archive/`) are not tracked by Git.

### Requirement: Standard Development Administrator
The development environment MUST be configured with a standard superuser account to facilitate consistent testing and dashboard access across all development instances. This requirement is strictly limited to non-production environments.

#### Scenario: Verify Development Credentials
- GIVEN a development environment.
- THEN a superuser with the following credentials MUST exist:
    - **Username:** `admin`
    - **Password:** `admin`
    - **Email:** `admin@example.com`
    - **Status:** `is_superuser=True`, `is_staff=True`

### Requirement: Production Credential Security
The project MUST NOT use default or predictable credentials in production environments.

#### Scenario: Prevent Default Admin in Production
- GIVEN a production environment (where `ENV=prod` or `DEBUG=False`).
- THEN the "Standard Development Administrator" credentials (admin/admin) MUST NOT be present or usable.

