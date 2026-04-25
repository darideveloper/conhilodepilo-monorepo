# Proposal: Fix Admin Branding Consistency

## Problem
The admin interface branding (logo and site name) is inconsistent: it works on the home page (`/admin/`) but disappears on all subpages (e.g., list views, change forms). This is caused by a missing template block in the custom `base_site.html` override and a naming collision between a custom context processor and Unfold's internal variables. Additionally, the `skeleton.html` override contains a recursive extension loop that could cause instability.

## Proposed Change
1.  **Rename Context Processor**: Rename the `branding` context processor to `brand_theme_context` to avoid clashing with Unfold's `branding` template variable.
2.  **Restore Branding Block**: Update the `base_site.html` override to include the `branding` block required by Unfold to render the sidebar header.
3.  **Fix Template Recursion**: Update the `skeleton.html` override to correctly extend the library's base template without recursion.
4.  **Enforce Logo usage**: Explicitly enable `SITE_LOGO` in settings to ensure the brand logo is prioritized in the UI.

## Impact
- **Consistency**: Branding will be visible on every page of the admin interface.
- **Stability**: Removing template recursion and variable collisions prevents future rendering bugs.
- **Maintainability**: Clearer naming for custom context variables.

## Proposed Capabilities
- **admin-ui**: Restore branding block and fix skeleton inheritance.
- **core-settings**: Rename branding context processor to prevent naming collisions.
