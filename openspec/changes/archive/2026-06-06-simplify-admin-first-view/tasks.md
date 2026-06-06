## 1. URL Redirect Implementation

- [x] 1.1 Add `RedirectView` path for `/admin/` before `admin.site.urls` in `dashboard/project/urls.py` that redirects to `/admin/booking/booking/`

## 2. Verify

- [x] 2.1 Run the Django dev server and confirm `/admin/` redirects (301) to `/admin/booking/booking/`
- [x] 2.2 Confirm `/admin/booking/booking/` renders the booking changelist normally
- [x] 2.3 Confirm `/admin/booking/event/` and other admin URLs are unaffected
