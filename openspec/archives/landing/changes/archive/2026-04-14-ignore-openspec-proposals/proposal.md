# Change: Ignore OpenSpec Proposal Files

## Why
OpenSpec proposal files in `openspec/changes/` are transient drafts that shouldn't clutter the main repository's tracked history until they are finalized and archived. However, archived proposals in `openspec/changes/archive/` MUST be preserved to maintain a history of all changes. Additionally, the `docs/` directory should be ignored as it contains temporary documentation or generated assets not intended for source control.

## What Changes
- **MODIFIED** `.gitignore` to ignore all files and directories under `openspec/changes/` except for the `archive/` directory.
- **MODIFIED** `.gitignore` to ignore the `docs/` directory.

## Impact
- Affected specs: `configuration`
- Affected code: `.gitignore`
