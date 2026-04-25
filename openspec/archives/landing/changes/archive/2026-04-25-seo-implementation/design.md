# SEO Spec Deltas

## MODIFIED Requirements
- **Requirement:** Dynamic Metadata Rendering
  - **Scenario:** When a user visits any page, the `<title>` and `meta[name="description"]` are populated based on the page's unique key or props, falling back to site defaults.
- **Requirement:** Structured Data (JSON-LD)
  - **Scenario:** The site provides `LocalBusiness` and `BreadcrumbList` schemas in the `<head>` to enhance SERP visibility.
- **Requirement:** PWA Readiness
  - **Scenario:** Browsers identify the site as installable via a generated `site.webmanifest` and high-resolution icons (192x192, 512x512).

## ADDED Requirements
- **Requirement:** SEO Asset Suite
  - **Scenario:** The `public/` directory contains `apple-touch-icon.png`, `site.webmanifest`, and icons at 192x192 and 512x512, derived from the project logo.
- **Requirement:** Environment Indexing Control
  - **Scenario:** Staging and development builds automatically include `<meta name="robots" content="noindex, nofollow" />`.
- **Requirement:** BaseSEO Component
  - **Scenario:** All pages utilize a shared `BaseSEO.astro` component to ensure consistent meta, canonical, and schema tags across the site.
