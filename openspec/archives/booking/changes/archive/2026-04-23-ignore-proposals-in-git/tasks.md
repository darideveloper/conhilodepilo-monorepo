# Tasks: Ignore OpenSpec Proposals in Git

## Implementation
- [x] Add OpenSpec ignore patterns to `.gitignore` <!-- id: 0 -->
- [x] Add `docs/` ignore pattern to `.gitignore` <!-- id: 1 -->

## Validation
- [x] Verify `git status` does not show new files in `openspec/changes/non-existent-test/` <!-- id: 2 -->
- [x] Verify `git status` still shows (or doesn't ignore) `openspec/changes/archive/` <!-- id: 3 -->
- [x] Verify `docs/` is ignored <!-- id: 4 -->
