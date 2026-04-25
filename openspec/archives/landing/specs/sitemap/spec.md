# sitemap Specification

## Purpose
TBD - created by archiving change configure-sitemap-discovery. Update Purpose after archive.
## Requirements
### Requirement: Sitemap Discovery via Layout
The base Layout SHALL include a reference to the sitemap index in its head section to enable discovery by search engine crawlers.

#### Scenario: Layout head has sitemap link
- **WHEN** the `Layout.astro` component is rendered
- **THEN** it contains a `<link rel="sitemap" href="/sitemap-index.xml" />` element in the `<head>`

### Requirement: Dynamic Robots.txt Generation
The system SHALL dynamically generate a `robots.txt` file at the root of the site that includes the correct Sitemap URL.

#### Scenario: Robots.txt contains sitemap URL
- **WHEN** the site is built
- **THEN** `robots.txt` is created with `Sitemap: <SITE_URL>/sitemap-index.xml`

