## 1. Implementation
- [x] 1.1 Add `<link rel="sitemap" href="/sitemap-index.xml" />` to `src/layouts/Layout.astro`.
- [x] 1.2 Create `src/pages/robots.txt.ts` with dynamic content generation.

## 2. Validation
- [x] 2.1 Verify that `npm run build` generates `dist/sitemap-index.xml` and `dist/robots.txt`.
- [x] 2.2 Verify that `dist/layouts/Layout.html` (if built) or the final index has the sitemap link in `<head>`.
- [x] 2.3 Verify that `dist/robots.txt` contains the correct `Sitemap:` URL pointing to `https://conhilodepilo.com/sitemap-index.xml`.
