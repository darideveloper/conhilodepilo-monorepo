# Proposal: Ignore OpenSpec Proposals in Git

## Problem
Currently, all OpenSpec proposal files (under `openspec/changes/`) are tracked by git. This can lead to a cluttered git history with work-in-progress proposals that are not yet approved or finalized. Additionally, the `docs/` directory is being tracked but should likely be ignored if it contains generated or transient documentation.

## Proposed Solution
Update `.gitignore` to:
1. Ignore all active proposals under `openspec/changes/`.
2. Explicitly include (un-ignore) the `openspec/changes/archive/` directory to ensure finalized proposals are preserved in history.
3. Ignore the `docs/` directory.

## Impact
- **Developer Experience:** Cleaner `git status` output by hiding in-progress proposals.
- **Repository Health:** Prevents accidental commits of draft specs while ensuring historical records of completed changes remain available.
- **Documentation:** Decouples documentation artifacts from the core source control if they are not intended to be versioned.
