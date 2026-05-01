# Tasks: SSG Refinements

- [x] **Routing Simplification**
    - [x] Removed `booking/src/pages/[id].astro`.
    - [x] Verified `index.astro` as the sole entry point.
    - [x] Validation: Build generates only `index.html`.

- [x] **Zoom Fix**
    - [x] Implemented client-side `zoom` parameter handling in `Layout.astro`.
    - [x] Replaced server-side `Astro.url.searchParams` with dynamic style injection in the `<head>`.
    - [x] Validation: `?zoom=50` scales the page in the browser.

- [x] **Dependency & Config Alignment**
    - [x] Uninstalled `@astrojs/node`.
    - [x] Set `output: 'static'` in `astro.config.mjs`.
    - [x] Added `@types/node` for config type safety.
    - [x] Validation: `npm run build` completes successfully.
