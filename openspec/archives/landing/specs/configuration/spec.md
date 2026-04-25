# Capability: configuration

## Purpose
Define the global configuration and environment setup for the project, including file exclusion rules and repository maintenance.
## Requirements
### Requirement: Git File Exclusion
The system SHALL exclude transient OpenSpec proposal files and temporary documentation from Git tracking while preserving archived history.

#### Scenario: Active proposals are ignored
- **WHEN** a new file is created in `openspec/changes/my-new-feature/`
- **THEN** Git MUST NOT track this file by default

#### Scenario: Archived proposals are tracked
- **WHEN** a file exists in `openspec/changes/archive/2026-01-01-my-feature/`
- **THEN** Git MUST track this file

#### Scenario: Docs directory is ignored
- **WHEN** a file is created in `docs/`
- **THEN** Git MUST NOT track this file

### Requirement: Environment Variable Support for Booking URL
- The system MUST support `PUBLIC_BOOKING_URL` via environment variables.
#### Scenario: Booking Iframe URL Configuration
- Given the need to configure the booking base URL, the system MUST support `PUBLIC_BOOKING_URL` via environment variables.

