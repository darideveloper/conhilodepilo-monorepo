# Design: Unfold Admin UI Layout Fix

## Architectural Context
The Django Unfold theme relies on a specific template hierarchy to inject its responsive grid and sticky footer logic. By overriding `admin/base.html` and extending `unfold/layouts/base.html` directly, the project was bypassing the "glue" layer that Unfold provides.

### Template Hierarchy Change
- **Current**: `project/templates/admin/base.html` -> `unfold/layouts/base.html` (Bypasses Unfold's admin logic)
- **Target**: `project/templates/admin/base_site.html` -> `admin/base.html` (Provided by Unfold) -> `unfold/layouts/base.html`

By extending `admin/base.html`, we ensure that the following blocks and containers from Unfold are preserved:
- `@container px-4 pb-4 grow`: The main container that allows the sticky footer to position itself relative to the viewport.
- Internal Unfold blocks that handle sidebars and headers.

### Base Admin Class Strategy
Instead of manually configuring every `ModelAdmin`, we use a project-wide `ModelAdminUnfoldBase`. This centralizes common UI configurations:
- `compressed_fields = True`: Better use of horizontal space.
- `warn_unsaved_form = True`: Prevents accidental data loss.
- `change_form_show_cancel_button = True`: Standardizes the action bar buttons.

## Trade-offs
- **Renaming `base.html` to `base_site.html`**: While `base.html` is the most common override point for the global admin, Unfold's architecture specifically expects the app-level `admin/base.html` to remain intact or be extended carefully. Renaming to `base_site.html` (a standard Django override point) is cleaner and avoids shadowing Unfold's own base template while still achieving global coverage.
