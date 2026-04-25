# Design: Initialize OpenSpec Infrastructure

## Architectural Approach
The current state of the monorepo is "documentation-light" at the implementation level. To rectify this without introducing unnecessary overhead:

1. **Hierarchy:** We will enforce a clear separation:
   - `openspec/specs/` for cross-service API contracts and global architectural invariants.
   - `<service>/openspec/` for local task tracking and service-specific requirements.
2. **Bootstrapping:** We will start with a "skeleton" approach. Existing code (e.g., Bruno collections, existing Astro pages) will serve as the ground truth for populating the initial contracts.
3. **Validation:** All new specifications must adhere to the OpenSpec standard to facilitate future automation.

## Trade-offs
- **Minimal vs. Exhaustive:** We are prioritizing *establishing the structure* over documenting every single existing endpoint immediately. This prevents the "documentation trap" where the effort to document consumes the time for development.
- **Maintainability:** By using Markdown for specs, we ensure that engineers are likely to keep them updated via PRs, rather than opaque configuration files.
