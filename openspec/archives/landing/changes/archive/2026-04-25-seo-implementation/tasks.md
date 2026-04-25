# Tasks

- [x] Create missing icons and manifest:
  - [x] Use `logo.webp` to generate `apple-touch-icon.png` (180x180).
  - [x] Generate `android-chrome-192x192.png` and `android-chrome-512x512.png`.
  - [x] Create `site.webmanifest` with correct references and theme colors.
- [x] Develop `src/components/atoms/BaseSEO.astro`:
  - [x] Implement logic for title and description.
  - [x] Add JSON-LD schema (LocalBusiness).
  - [x] Add canonical link tag.
- [x] Refactor `src/layouts/Layout.astro`:
  - [x] Remove hardcoded meta tags.
  - [x] Integrate `BaseSEO` component.
  - [x] Add environment-based robot tag logic.
- [x] Verify SEO implementation:
  - [x] Check console for 404s on icons/manifest.
  - [x] Validate JSON-LD schema with browser tool/validator.
  - [x] Inspect source code to confirm robots tag in non-prod.
