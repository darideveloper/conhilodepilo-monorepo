## Why

The admin index page shows a list of all registered model groups, but the primary daily workflow is managing bookings. Every visit to `/admin/` requires an extra click to reach the booking changelist. Removing this intermediate step reduces friction for the main use case.

## What Changes

- `/admin/` now redirects (301) to `/admin/booking/booking/` instead of showing the admin index
- Django-unfold sidebar navigation remains unchanged — all models remain accessible from the sidebar
- The admin index page becomes unreachable (no route maps to it)

## Capabilities

### New Capabilities

- `admin-first-view`: Redirect the admin root URL to the booking changelist as the default landing page

### Modified Capabilities

*(None — no existing specs are being modified)*

## Impact

- **File changed**: `dashboard/project/urls.py` — add one `RedirectView` path before `admin.site.urls`
- **No dependencies added or removed**
- **No breaking changes** — existing URLs (`/admin/booking/booking/`, `/admin/booking/event/`, etc.) are unaffected
- **Admin index is inaccessible** — acceptable because the sidebar provides navigation to all models from any page
