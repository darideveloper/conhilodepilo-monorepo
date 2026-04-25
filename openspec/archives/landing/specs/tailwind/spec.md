# tailwind Specification

## Purpose
TBD - created by archiving change install-tailwind-v4. Update Purpose after archive.
## Requirements
### Requirement: Install Tailwind CSS v4

The project MUST have Tailwind CSS v4 installed using the official Astro CLI integration command.

#### Scenario: Running `npx astro add tailwind`
- Run `npx astro add tailwind`.
- Verify `package.json` contains `@tailwindcss/vite` and `tailwindcss` (version 4).
- Verify `astro.config.mjs` is updated with the Tailwind integration or Vite plugin.

### Requirement: Set up global styles

A global CSS file SHALL contain Tailwind v4's `@import "tailwindcss";` directive.

#### Scenario: Create `src/styles/global.css`
- If `src/styles/global.css` does not exist, create it.
- Ensure `@import "tailwindcss";` is at the top of the file.

### Requirement: Load Tailwind in layout

The `src/layouts/Layout.astro` MUST import the global CSS file to provide Tailwind styles to all pages.

#### Scenario: Update `Layout.astro`
- Add `import "../styles/global.css";` to the frontmatter of `src/layouts/Layout.astro`.

