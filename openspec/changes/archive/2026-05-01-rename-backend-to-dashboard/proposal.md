# Change: Rename dashboard to dashboard

## Why
The term "dashboard" is generic and describes the technical layer, while "dashboard" better reflects the primary purpose of the Django application as the administrative hub for the ecosystem. Aligning the directory name with its role improves codebase clarity and developer onboarding.

## What Changes
- Rename the root directory `dashboard/` to `dashboard/`.
- Update `dev.sh` to use the new directory and update tmux window names.
- Update `README.md` and `openspec/project.md` to reflect the new structure.
- Update all path references in `openspec/` documentation and archived tasks.
- **BREAKING**: Local development environments will need to be restarted. External deployment configurations (e.g., Dockerfile paths in PaaS) must be updated manually.

## Impact
- Affected specs: `dashboard-host`, `dashboard-models`, `dev-orchestration`.
- Affected code: `dev.sh`, `README.md`, `dashboard/scripts/migrate_db.sh`.
