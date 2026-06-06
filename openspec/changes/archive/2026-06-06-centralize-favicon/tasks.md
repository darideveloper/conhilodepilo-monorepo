## 1. Booking — Update favicon reference

- [x] 1.1 Replace the two `<link>` tags in `booking/src/layouts/Layout.astro` (lines 22-23) with a single external URL reference: `<link rel="icon" href="https://conhilodepilo.com/favicon.ico" />`

## 2. Dashboard — Update favicon config and callback

- [x] 2.1 Replace the `SITE_FAVICONS` entry in `dashboard/project/settings.py` (lines 286-293) to use the external URL instead of the static file lambda
- [x] 2.2 Update `site_icon_callback` fallback in `dashboard/utils/callbacks.py` (line 31) from `static("favicon.png")` to `"https://conhilodepilo.com/favicon.ico"`

## 3. Cleanup — Remove stale favicon files

- [x] 3.1 Delete `booking/public/favicon.ico`
- [x] 3.2 Delete `booking/public/favicon.svg`
- [x] 3.3 Delete `dashboard/static/favicon.png`

## 4. Verification

- [x] 4.1 Run `npm run dev` (or equivalent) for booking and confirm no broken asset warnings
- [x] 4.2 Run the dashboard dev server and confirm no static file errors
- [x] 4.3 Verify there are no remaining references to the local favicon files in the codebase
