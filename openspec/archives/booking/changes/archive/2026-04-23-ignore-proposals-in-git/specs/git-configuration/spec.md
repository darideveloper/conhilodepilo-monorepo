# Git Configuration Specification

## Purpose
Define the standard git ignore rules for the project to ensure a clean repository state and historical integrity.

## ADDED Requirements

### Requirement: Ignore Active Proposals
The project MUST ignore active OpenSpec proposals to prevent draft files from cluttering the repository history.

#### Scenario: Verify active proposals are ignored
- **GIVEN** a directory `openspec/changes/my-new-proposal/`.
- **WHEN** checking `git status`.
- **THEN** files inside `openspec/changes/my-new-proposal/` MUST NOT be tracked by default.

### Requirement: Preserve Archive History
The project MUST NOT ignore the `openspec/changes/archive/` directory to ensure all finalized changes are versioned.

#### Scenario: Verify archive is tracked
- **GIVEN** a file in `openspec/changes/archive/2026-01-01-my-change/proposal.md`.
- **WHEN** checking `git status` or `git check-ignore`.
- **THEN** the file MUST NOT be ignored.

### Requirement: Ignore Documentation Directory
The project SHALL ignore the `docs/` directory.

#### Scenario: Verify docs are ignored
- **GIVEN** a file in `docs/notes.md`.
- **WHEN** checking `git status`.
- **THEN** the file MUST NOT be tracked by default.
