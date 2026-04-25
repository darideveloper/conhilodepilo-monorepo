# Requirement: Local Development Orchestration

## ADDED Requirements

### Requirement: Local dev.sh script
The system SHALL provide a shell script `dev.sh` in the project root to start all development services, use `tmux` to multiplex the terminal session, and automatically activate the backend virtual environment.

#### Scenario: Running `dev.sh`
- Given the user is in the project root.
- When they run `./dev.sh`.
- Then the `tmux` session `conhilorepilo_dev` is created or attached.
- And the backend, booking, and landing services are started in separate panes.
