## Why

The landing page hero section currently uses lower resolution JPEG/WebP images that do not reflect the high-quality, premium aesthetic desired for the brand. Replacing these assets with the new, uniformly sized, and high-fidelity WebP images (hero-1.webp, hero-2.webp, and hero-3.webp) will significantly improve visual appeal and consistency on the landing page.

## What Changes

- Update `HeroSection.astro` to import the new high-quality images.
- Map the slider items to use the new images:
  - Slide 1 (Tratamientos de Autor) -> `hero-1.webp`
  - Slide 2 (Formación Exclusiva) -> `hero-2.webp`
  - Slide 3 (Diseña tu Mirada) -> `hero-3.webp`
- Remove unused imports of the previous hero images (`hero-treatments.webp`, `hero-academy.webp`, `hero-experience.webp`).

## Capabilities

### New Capabilities

- None

### Modified Capabilities

- None

## Impact

- **Affected Code**: `landing/src/components/organisms/HeroSection.astro`
- **Impacted Systems**: Landing page frontend.
