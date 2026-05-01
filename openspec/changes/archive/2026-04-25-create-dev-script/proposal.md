# Proposal: Create Development Orchestration Script

## Summary
To improve developer productivity by providing a single, consistent entry point to start the dashboard and frontend subprojects simultaneously using `tmux`.

## Why
Currently, the repository requires manually navigating to multiple directories and starting processes individually, which is inefficient and prone to environmental inconsistencies.

## What Changes
- Create a `dev.sh` script in the root directory.
- Configure the script to manage `dashboard`, `booking`, and `landing` services.
- Leverage `tmux` for terminal multiplexing to manage logs and interactive sessions.

## Impact
- Simplifies local development setup.
- Standardizes the startup process across all contributors.
