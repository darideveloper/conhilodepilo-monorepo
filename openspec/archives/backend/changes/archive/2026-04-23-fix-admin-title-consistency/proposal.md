# Proposal: Fix Admin Title Consistency

Restore the HTML `<title>` tag consistency across all admin pages by ensuring the `title` block is properly defined in base templates and fallback mechanisms are in place.

## Problem
Currently, the HTML `<title>` is correctly loaded on the admin home page but appears as `<title> </title>` (empty) on all other admin pages (changelists, change forms, etc.). This is due to:
1.  Missing `{% block title %}` in the custom `project/templates/admin/base_site.html`.
2.  Incomplete `<title>` implementation in `project/templates/unfold/layouts/skeleton.html` which lacks a global fallback.

## Solution
1.  Update `project/templates/admin/base_site.html` to define the `title` block, incorporating the page-specific title and the dynamic `site_title`.
2.  Update `project/templates/unfold/layouts/skeleton.html` to provide a robust `<title>` structure that includes the `site_title` as a fallback.
3.  Ensure the `site_title` and `site_header` are consistently available in the template context.

## Scope
-   `project/templates/admin/base_site.html`
-   `project/templates/unfold/layouts/skeleton.html`
-   `openspec/specs/admin-ui/spec.md`
