## Why

The favicon is currently duplicated across three projects (landing, booking, dashboard) in different formats (ICO, SVG, PNG) with no guarantee they stay in sync. Landing (`conhilodepilo.com`) already hosts the canonical favicon — booking and dashboard should reference it directly rather than maintaining their own copies.

## What Changes

- **Booking**: Replace the two local favicon `<link>` tags (SVG + ICO) with a single external reference to `https://conhilodepilo.com/favicon.ico`
- **Dashboard**: Replace the local static file favicon config (`static/favicon.png`) with an external URL reference in `SITE_FAVICONS` settings
- **Dashboard callback** (optional): Update the `site_icon_callback` fallback to use the external URL
- **Cleanup**: Remove stale favicon files from booking (`public/favicon.ico`, `public/favicon.svg`) and dashboard (`static/favicon.png`)

## Capabilities

### New Capabilities

*(none — this is a configuration change, not a new capability)*

### Modified Capabilities

*(none — no spec-level behavior changes)*

## Impact

| File | Change |
|------|--------|
| `booking/src/layouts/Layout.astro:22-23` | Replace 2 `<link>` tags with 1 external URL |
| `dashboard/project/settings.py:286-293` | Replace `SITE_FAVICONS` href lambda with external URL |
| `dashboard/utils/callbacks.py:31` | (optional) Update `static("favicon.png")` fallback |
| `booking/public/favicon.ico` | Remove (unused) |
| `booking/public/favicon.svg` | Remove (unused) |
| `dashboard/static/favicon.png` | Remove (unused) |
