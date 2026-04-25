# Change: Configure Sitemap Discovery

## Why
Search engine crawlers (like Googlebot) need to find the sitemap to crawl the site efficiently. Currently, `@astrojs/sitemap` is integrated but not discoverable by default.

## What Changes
- **MODIFIED**: `src/layouts/Layout.astro` to add `<link rel="sitemap" href="/sitemap-index.xml" />` in the `<head>`.
- **ADDED**: `src/pages/robots.txt.ts` to dynamically generate a `robots.txt` file that includes the sitemap URL from the site's configuration.

## Impact
- Affected specs: `sitemap` (new capability)
- Affected code: `src/layouts/Layout.astro`, `src/pages/robots.txt.ts`
