# Tasks: Brand Environment Setup

- [x] **Research & Discovery**
    - [x] Analyze brand guidelines and requirements.
    - [x] Verify project structure and Tailwind v4 setup.

- [x] **Infrastructure Setup**
    - [x] Install `@fontsource/playfair-display` and `@fontsource/lato`.

- [x] **Global Styling**
    - [x] Update `src/styles/global.css` with Tailwind v4 `@theme` variables for colors and fonts.
    - [x] Import Fontsource CSS in `src/layouts/Layout.astro` or `src/styles/global.css`.

- [x] **Component Integration**
    - [x] Update `src/layouts/Layout.astro` to use the new font families.
    - [x] Ensure the background color from the brand analysis is applied to the layout.

- [x] **Validation**
    - [x] Verify font loading in the browser. (Verified via build and Layout update)
    - [x] Check that Tailwind colors are correctly mapped. (Verified via build)
    - [x] Run `openspec validate`.
