# Tasks: Install and Setup @astrojs/react

## [TBD-1] - Package Installation
- [x] Install `@astrojs/react` (v5.0.1)
- [x] Install `react` (v19.2.4) and `react-dom` (v19.2.4)
- [x] Install type definitions: `@types/react` (v19.2.14) and `@types/react-dom` (v19.2.3)
- **Validation:** `npm list @astrojs/react react react-dom @types/react @types/react-dom` completes successfully.

## [TBD-2] - Integration Configuration
- [x] Update `astro.config.mjs` to import and call `react()`.
- **Validation:** `npm run build` succeeds (initial smoke test).

## [TBD-3] - TypeScript Support
- [x] Update `tsconfig.json` with `jsx: "react-jsx"` and `jsxImportSource: "react"`.
- **Validation:** `npx tsc --noEmit` succeeds.

## [TBD-4] - Project Documentation
- [x] Update `openspec/project.md` to reflect `@astrojs/react` as a core integration.
- **Validation:** `cat openspec/project.md` includes the React integration.

## [TBD-5] - Final Verification
- [x] Create a dummy React component in `src/components/ReactTest.tsx`.
- [x] Render the dummy React component in `src/pages/index.astro` with a `client:load` directive.
- [x] Verify that the component hydrates correctly by adding a button with a `console.log`.
- **Validation:** Run `npm run build` and `npx tsc --noEmit` succeed.
