# Change: Add Gallery Section

## Why
The website needs a visual portfolio to showcase the high-quality services provided by Con Hilo Depilo. By adapting the new design provided in `.themes/code.html`, we build trust with potential customers by providing visual evidence in a cohesive, aesthetically pleasing layout.

## What Changes
- Add a new Gallery capability to the project configuration.
- Implement the 'Resultados Reales' gallery mosaic layout provided in `.themes/code.html`.
- Adapt the `.themes/code.html` layout into `Gallery.astro`, replacing custom hard-coded classes with existing design system components (`SectionHeader`) and design tokens (`bg-brand-primary`, `text-brand-secondary`, etc.).
- Download the initial gallery images to `src/assets/images/gallery/` for local usage instead of external hot-linking, and build the component so it anticipates data coming from an API in the future.
- Integrate the gallery section into the homepage (`src/pages/index.astro`).

## Impact
- Affected specs: `gallery`
- Affected code: `src/pages/index.astro`, `src/components/Gallery.astro`
