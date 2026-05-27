## Why

The "Sobre mí" navigation option in the landing header no longer aligns with the site's content strategy. Removing it from the header streamlines navigation and reduces clutter, while the `InfoCardSection` and other links to `#info` (e.g., hero CTAs) remain intact and accessible from elsewhere on the page.

## What Changes

- Remove the "Sobre mí" link (`{ label: "Sobre mí", href: "/#info" }`) from the Header navigation array in `Header.astro`
- The `InfoCardSection` and its `<section id="info">` anchor remain on the page — reachable via hero CTAs and direct URL
- Hero CTA buttons linking to `#info` are unchanged

## Capabilities

### New Capabilities

_(None — this is a removal-only change.)_

### Modified Capabilities

- `landing-ui-components`: Header navigation link set is reduced (5 links → 4); the absolute-path requirement still applies but the item list no longer includes "Sobre mí"

## Impact

- **`landing/src/components/organisms/Header.astro`** — remove one entry from the `navLinks` array