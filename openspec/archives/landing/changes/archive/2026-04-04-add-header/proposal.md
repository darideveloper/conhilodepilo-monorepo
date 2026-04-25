# Change: Add Header Component

## Why
The website lacks a global site header/navigation bar. Based on the reference design, a sticky, responsive header is needed to allow users to navigate between sections (Tratamientos, Cursos, etc.) and access the primary booking action at any time.

## What Changes
- Create a new `Header.astro` component following the reference design.
- Adapt the design to use the existing design system tokens (e.g., `bg-ui-bg-light`, `border-brand-primary`).
- Add navigation links: Tratamientos, Cursos, Resultados, Sobre mí, Contacto.
- Implement a responsive mobile menu (hamburger toggle) since the desktop menu is hidden on smaller screens.
- Integrate the `Header.astro` component into the global layout layout or pages.

## Impact
- Affected specs: `header` (new capability)
- Affected code: `src/components/Header.astro`, `src/layouts/Layout.astro`
