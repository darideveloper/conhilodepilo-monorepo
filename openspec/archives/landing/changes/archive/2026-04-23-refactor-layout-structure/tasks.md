# Tasks: Refactor Layout Structure

- [x] **Research & Prep**
  - [x] Verify if other pages (besides `index.astro` and `design-system.astro`) use `Layout.astro`.
  - [x] Check for any global CSS targeting `main` that might be affected.

- [x] **Implement Layout Changes**
  - [x] Modify `src/layouts/Layout.astro`:
    - [x] Import `Footer` from `../components/organisms/Footer.astro`.
    - [x] Wrap `<slot />` in a `<main>` tag.
    - [x] Apply the `className` prop (or a dedicated `mainClass` prop) to the `<main>` tag.
    - [x] Place `<Footer />` after the `<main>` tag.

- [x] **Refactor Page Components**
  - [x] Modify `src/pages/index.astro`:
    - [x] Remove `<main>` and its closing tag.
    - [x] Remove `<Footer />` and its import.
  - [x] Modify `src/pages/design-system.astro`:
    - [x] Remove `<main>` and its closing tag.
    - [x] Pass `class="py-20"` to the `Layout` component if needed to maintain padding.

- [x] **Validation**
  - [x] Build the project (`npm run build`) to ensure no breaking changes.
  - [x] Visually verify `index.astro` and `design-system.astro` to ensure the footer is present and the layout is correct.
  - [x] Check HTML structure in the browser to confirm: `<header>` -> `<main>` -> `<footer>`.
