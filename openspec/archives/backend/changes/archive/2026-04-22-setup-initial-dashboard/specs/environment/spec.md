# Capability: Environment Setup

## ADDED Requirements

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
