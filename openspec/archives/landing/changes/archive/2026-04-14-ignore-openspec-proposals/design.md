## Context
The project uses OpenSpec for change management. Active proposals are stored in `openspec/changes/<change-id>/`. Once applied, they are moved to `openspec/changes/archive/<date>-<change-id>/`. 

## Goals / Non-Goals
- Goals:
    - Automatically exclude active proposals from Git to avoid unnecessary commits of WIP drafts.
    - Ensure archived proposals are always tracked and versioned.
    - Exclude `docs/` from Git.
- Non-Goals:
    - Ignoring the `openspec/specs/` directory (these are the source of truth).
    - Ignoring `openspec/project.md` or `openspec/AGENTS.md`.

## Decisions
- Decision: Use a combination of a broad ignore pattern and a specific "unignore" pattern in `.gitignore`.
    - `openspec/changes/*`: Ignores everything under changes.
    - `!openspec/changes/archive/`: Negates the ignore for the archive folder, ensuring its contents are tracked.
- Decision: Explicitly ignore `docs/`.

## Risks / Trade-offs
- Risk: Developers might forget that their active proposals aren't being tracked and could lose work if not careful.
- Mitigation: The tool used to manage proposals (OpenSpec) should handle the lifecycle, and developers are encouraged to use the archive feature once work is complete.
