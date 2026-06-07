## 1. Template Modification

- [x] 1.1 Remove the logo image block `{% if logo_url %}...{% endif %}` from [booking_confirmation.html](file:///develop/monorepos/conhilorepilo/dashboard/project/templates/email/booking_confirmation.html).
- [x] 1.2 Verify that the company title remains centered in the email header layout.

## 2. Django Backend Modification

- [x] 2.1 Remove the `_build_logo_url` function and its imports/references in [utils/email.py](file:///develop/monorepos/conhilorepilo/dashboard/utils/email.py).
- [x] 2.2 Remove the `"logo_url"` key from the context dictionary in `_build_base_context` within [utils/email.py](file:///develop/monorepos/conhilorepilo/dashboard/utils/email.py).

## 3. Unit Test Updates & Verification

- [x] 3.1 Remove the `BuildLogoUrlTest` test class and its imports/references in [tests_email.py](file:///develop/monorepos/conhilorepilo/dashboard/booking/tests_email.py).
- [x] 3.2 Run Django tests using `python dashboard/manage.py test booking.tests_email` to verify everything works properly.
