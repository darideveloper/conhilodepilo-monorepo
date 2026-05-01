# Proposal: Refine Booking SSG Implementation

## Summary
Document and formalize the final state of the `@booking` SSG migration, including the single-page routing architecture and the client-side zoom scaling fix.

## Why
The initial SSG migration proposal was partially implemented before discovering nuances about URL parameter handling and routing redundancy. The system was subsequently refined to:
1. Use a single-page static architecture (removing `[id].astro`).
2. Fix the zoom feature using client-side style injection.
3. Align dependencies for a static build environment.

This proposal retroactively documents these already-implemented changes to ensure the project specifications match the actual codebase.

## What Changes
- **Astro Config:** Formalized `output: 'static'` and removal of the Node adapter.
- **Routing:** Formalized the removal of `src/pages/[id].astro`.
- **UI Logic:** Added requirements for client-side zoom handling via dynamic style injection.
- **Dependencies:** Formalized the removal of `@astrojs/node` and the addition of `@types/node`.

## Verification Plan
- **Build:** Run `npm run build` and verify `dist/index.html` is generated.
- **Zoom:** Verify `?zoom=X` correctly scales the page in the browser.
- **Routing:** Verify `/?service=ID` correctly selects the service.
