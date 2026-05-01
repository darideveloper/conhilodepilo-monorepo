# Proposal: Migrate Booking to SSG and Simplify Routing

## Summary
Migrate the `@booking` application from Server-Side Rendering (SSR) to a single-page Static Site Generation (SSG) model. This involves removing the redundant `/[id]` subpages and relying entirely on the main entry point with query parameters for service selection.

## Problem Statement
The `@booking` app currently maintains two ways of selecting services: path-based routing (`/[id]`) and query parameters (`?service=ID`). 
1. **SSR Overhead:** Current SSR mode requires a Node.js server.
2. **Redundancy:** The Landing page primarily embeds the booking app via an iframe using query parameters, making the `/[id]` routes in the booking app redundant.
3. **Maintenance Burden:** Path-based SSG routes require a rebuild every time a new service is added to the backend.

## Proposed Solution
- Change Astro output to `static`.
- Remove the Node.js adapter and its dependencies.
- **Delete `src/pages/[id].astro`:** Streamline the app into a single-page static application.
- Use `index.astro` as the universal entry point. The existing logic in `BookingFlow.tsx` already handles service selection via the `?service` query parameter.
- This approach eliminates the need for rebuilds when adding new services in Django, as the single static page will fetch all data dynamically in the browser.

## Key Changes
- **Astro Config:** Update `booking/astro.config.mjs` to `output: 'static'`.
- **Dependencies:** Remove `@astrojs/node` from `booking/package.json`.
- **Cleanup:** Delete `booking/src/pages/[id].astro`.
- **Infrastructure:** The application becomes a pure static site (HTML/JS/CSS) that can be hosted anywhere without a Node runtime.

## Verification Plan
### Automated Tests
- Run `npm run build` and verify that only `index.html` (and static assets) are generated.
- Ensure no adapter errors occur during the build.
### Manual Verification
- Verify that `/?service=ID` correctly pre-selects the service in the `BookingFlow`.
- Confirm that availability and slot selection remain functional (client-side dynamic).
