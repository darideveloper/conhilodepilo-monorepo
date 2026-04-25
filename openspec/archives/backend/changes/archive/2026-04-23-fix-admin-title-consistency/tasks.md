# Tasks: Fix Admin Title Consistency

## Setup & Verification
- [x] Reproduce the empty title issue by visiting a changelist page (e.g., `/admin/booking/booking/`) and inspecting the `<title>` tag. <!-- id: 0 -->

## Template Implementation
- [x] Update `project/templates/admin/base_site.html` to include the `title` block with a dynamic site title fallback. <!-- id: 1 -->
- [x] Update `project/templates/unfold/layouts/skeleton.html` to use a more robust `<title>` tag structure that includes `site_title`. <!-- id: 2 -->

## Validation
- [x] Verify that the admin index page still displays the correct title. <!-- id: 3 -->
- [x] Verify that the Booking changelist page displays "[Title] | [Company Name]". <!-- id: 4 -->
- [x] Verify that the User change form page displays "[Title] | [Company Name]". <!-- id: 5 -->
