# Design: Git Ignore Strategy for OpenSpec

## Architectural Reasoning
The OpenSpec workflow involves creating proposals in `openspec/changes/<id>/`. These files are often experimental and change frequently before being merged/archived. By ignoring them in git, we maintain a cleaner main branch and avoid noise in PRs.

The `archive/` directory, however, represents the historical record of *applied* changes. These MUST be tracked to maintain the project's evolution history.

The `docs/` directory often contains generated files or notes that are secondary to the codebase. Following the user's preference to skip it aligns with keeping the repository focused on source code.

## Implementation Details
The `.gitignore` file uses pattern matching. The `!` prefix allows us to white-list a directory that would otherwise be caught by a broader ignore pattern.

### Patterns:
- `openspec/changes/*`: Catch-all for proposals.
- `!openspec/changes/archive/`: Exception for the archive.
- `docs/`: Standard directory ignore.
