## ADDED Requirements

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
