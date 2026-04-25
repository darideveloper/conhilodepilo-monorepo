# Proposal: Use Dynamic CSS Variables for Markdown Preview

## Problem
The current CSS for the Markdown editor preview uses hardcoded hex values (e.g., `#e5e7eb`, `#f3f4f6`). This prevents the editor from automatically adapting to the brand colors configured in the `CompanyProfile` or the default Unfold theme colors, leading to potential visual inconsistencies if the theme is customized.

## Solution
Refactor `static/css/style.css` to use CSS variables provided by the Unfold theme and the project's branding context. Specifically, it will use:
- `var(--brand-primary-600)` for links and accents.
- `var(--color-base-100)` and `var(--color-base-200)` for backgrounds and borders (matching Unfold's neutral palette).
- `var(--color-font-subtle-light)` for secondary text in blockquotes.

## Scope
- **CSS**: Update `static/css/style.css`.
- **Documentation**: Update the code examples in `docs/django-unfold-admin.md`.

## Benefits
- Perfect alignment with the project's dynamic branding system.
- Improved consistency with the Unfold admin theme.
- Future-proof implementation that adapts to color changes without manual CSS edits.
