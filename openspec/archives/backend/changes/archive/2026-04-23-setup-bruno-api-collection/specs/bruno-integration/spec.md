# Capability: Bruno API Integration

Integrates the Bruno API client into the repository to provide a shared, versioned environment for API development and testing, following the **Bruno v3 (OpenCollection YAML)** standard.

## ADDED Requirements

### API Collection Structure
The project must include a standardized Bruno collection to ensure consistency across the development team.

#### Scenario: Bruno Directory Layout
- **Given** a developer clones the repository
- **Then** they should see a `bruno/` directory at the project root
- **And** it must contain an `opencollection.yml` configuration file
- **And** it must contain an `environments/` directory for configuration profiles
- **And** it must contain folders organized by feature (e.g., `Booking/`) for individual API requests using the `.yml` extension.

### Environment Management
The API client must support multiple environments to facilitate testing across local and remote instances.

#### Scenario: Pre-configured Environments
- **Given** the `bruno/environments/` directory
- **Then** it must include a `Local.yml` file
- **And** `Local.yml` must define a `base_url` variable pointing to the local Django server.

### Security and Privacy
Sensitive credentials must never be committed to the repository.

#### Scenario: Git-Ignored Bruno Secrets
- **Given** the project's `.gitignore` file
- **Then** it must contain an entry for `bruno/.env` to prevent local secrets from being tracked by Git.

### Initial Endpoint Coverage
The collection must provide immediate value by including critical system endpoints.

#### Scenario: Company Configuration Endpoint
- **Given** the `bruno/Booking/` directory
- **Then** it must contain a request named `Get Company Config` in `Get Company Config.yml`
- **And** the request must target `{{base_url}}/api/config/`
- **And** the request must include an assertion verifying a `200 OK` status.
