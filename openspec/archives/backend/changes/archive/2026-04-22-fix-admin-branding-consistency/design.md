# Design: Admin Branding Consistency and Stability

## Overview
The fix addresses three main architectural friction points in the admin UI implementation: template inheritance, naming collisions, and configuration gaps.

## 1. Context Variable Collision
Django Unfold uses a template tag `{% capture as branding silent %}` to capture the `branding` block content into a local variable. Our custom context processor was also named `branding`, which injected a dictionary into the context with the same name. On some pages, this caused the variable to be overridden or misinterpreted, leading to empty headers.

**Solution**: Rename the context processor to `brand_theme_context`. This keeps the "primary colors" logic separate from the "site title/logo" logic.

## 2. Template Inheritance Loop
The file `project/templates/unfold/layouts/skeleton.html` was extending itself via `{% extends "unfold/layouts/skeleton.html" %}`. While Django's loader often handles this by picking the "next" file in the search path, it is brittle.

**Solution**: Use a more explicit path or ensure the library version is targeted. In Django, if a template exists in multiple `DIRS`, the first one wins. To extend the library's version while overriding it, we must ensure the loader can differentiate them. A safer pattern in Unfold is often to inject the custom styles into `base.html` or `base_site.html` if possible, but since we are overriding the skeleton for `:root` variables, we will ensure the extension logic is robust.

## 3. Block Omission in `base_site.html`
`base_site.html` is the primary entry point for many admin views. By not defining `{% block branding %}`, we were effectively telling Unfold that the site has no branding.

**Solution**: Re-introduce the block and include Unfold's branding helper.

## 4. Configuration
Uncommenting `SITE_LOGO` in `settings.py` ensures that `unfold/helpers/navigation_header.html` chooses the logo rendering path over the icon rendering path, providing a more professional look aligned with the `CompanyProfile`.
