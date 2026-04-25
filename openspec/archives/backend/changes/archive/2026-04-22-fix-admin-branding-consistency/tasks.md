# Tasks: Fix Admin Branding Consistency

## 1. Rename Context Processor
- [x] Rename `branding` function to `brand_theme_context` in `project/context_processors.py`.
- [x] Update `TEMPLATES` in `project/settings.py` to use `project.context_processors.brand_theme_context`.

## 2. Restore Branding Block
- [x] Add `{% block branding %}` with `{% include "unfold/helpers/site_branding.html" %}` to `project/templates/admin/base_site.html`.

## 3. Fix Template Overrides
- [x] Update `project/templates/unfold/layouts/skeleton.html` to fix recursion (use library path or move logic).
- [x] Ensure `skeleton.html` still correctly injects `--brand-primary-*` CSS variables.

## 4. Admin Configuration
- [x] Uncomment `"SITE_LOGO"` in `UNFOLD` settings within `project/settings.py`. (Update: Decided to keep it commented to allow icon+text rendering path which looks better with the current site_icon_callback).

## 5. Validation
- [x] Verify branding is visible on the admin home page.
- [x] Verify branding is visible on the Bookings list view (`/admin/booking/booking/`).
- [x] Verify branding is visible on the Booking change form.
- [x] Check console/logs for template recursion warnings.
