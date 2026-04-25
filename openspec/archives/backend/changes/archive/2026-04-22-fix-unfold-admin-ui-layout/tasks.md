# Tasks: Fix Unfold Admin UI Bottom Bar Positioning

- [x] Restore proper template inheritance
    - [x] Rename `project/templates/admin/base.html` to `project/templates/admin/base_site.html`
    - [x] Update `project/templates/admin/base_site.html` to extend `"admin/base.html"`
- [x] Standardize admin base class usage
    - [x] Import `ModelAdminUnfoldBase` in `booking/admin.py`
    - [x] Update all admin classes in `booking/admin.py` to inherit from `ModelAdminUnfoldBase`
    - [x] Ensure `CompanyProfileAdmin` also inherits from `ModelAdminUnfoldBase` alongside `SingletonModelAdmin`
- [x] Verification
    - [x] Log in to admin and verify the sticky action bar is present on the Booking change form
    - [x] Verify that "Cancel" button is visible in the action bar
    - [x] Verify that unsaved change warnings are active
