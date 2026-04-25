# Proposal: Refactor Layout Structure

## Goal
Standardize the HTML structure of the project by moving the `<main>` tag and `<Footer />` component into the `Layout.astro` file. This ensures semantic consistency across all pages and reduces boilerplate in individual page components.

## Scope
- **Modified**: `src/layouts/Layout.astro` to include `<main>` and `<Footer />`.
- **Modified**: `src/pages/index.astro` to remove redundant `<main>` and `<Footer />`.
- **Modified**: `src/pages/design-system.astro` to remove redundant `<main>`.
- **New Spec**: `openspec/specs/layout/spec.md` (via delta).

## Rational
Currently, the `<Footer />` is manually included in `index.astro` but missing in `design-system.astro`. Additionally, the `<main>` tag is being used inconsistently across pages. Centralizing these in the layout ensures that every page follows the same semantic structure:
1. Header
2. Main (Content)
3. Footer

## Risks
- **CSS Selectors**: If there are CSS rules targeting `main` specific to a page, they might need adjustment.
- **Full-height sections**: Pages that previously didn't use `main` or used different wrappers might have layout shifts. (Not an issue here as both existing pages use `main`).
