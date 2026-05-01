## Context
The project is a monorepo where services are top-level directories. "Dashboard" is currently used for the Django admin/API.

## Goals
- Unified naming convention ("Dashboard").
- Zero broken links in documentation.
- Functional development scripts after rename.

## Decisions
- **Decision**: Use `dashboard/` as the new folder name.
- **Decision**: Rename OpenSpec capabilities `dashboard-host` and `dashboard-models` to `dashboard-host` and `dashboard-models` respectively.
- **Decision**: Update all occurrences of `dashboard/` in `openspec/` markdown files to ensure AI context remains accurate.

## Risks / Trade-offs
- **Risk**: External CI/CD or hosting provider settings might point to `dashboard/`.
  - **Mitigation**: This proposal focuses on codebase changes; manual platform updates are noted in the report.
- **Risk**: Broken references in un-archived changes.
  - **Mitigation**: A bulk update of the `openspec/` directory will be performed as part of the execution phase.
