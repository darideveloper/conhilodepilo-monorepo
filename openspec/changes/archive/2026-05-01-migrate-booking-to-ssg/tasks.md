# Tasks: Single-Page SSG Migration

- [x] **Cleanup & Dependencies**
    - [x] Delete `booking/src/pages/[id].astro`.
    - [x] Remove `@astrojs/node` from `booking/package.json`.
    - [x] Run `npm install` (to update lockfile).
    - [x] Validation: Ensure the `[id].astro` file is gone and `package.json` is clean.

- [x] **Astro Configuration**
    - [x] Set `output: 'static'` in `booking/astro.config.mjs`.
    - [x] Remove the `adapter` property.
    - [x] Validation: Run `npx astro check`.

- [x] **Routing Validation**
    - [x] Verify that `booking/src/pages/index.astro` is correctly set up as the only entry point.
    - [x] Double-check `BookingFlow.tsx` to ensure it correctly handles the `?service=` parameter without needing the `initialServiceId` prop from the SSR route.
    - [x] Validation: Manually test `/?service=ID` in a dev server.

- [x] **Build & Verification**
    - [x] Run `npm run build` in the `booking` directory.
    - [x] Verify that the `dist/` directory contains only `index.html` and assets.
    - [x] Validation: Serve the `dist` folder and confirm that query parameters still trigger the correct service selection.
