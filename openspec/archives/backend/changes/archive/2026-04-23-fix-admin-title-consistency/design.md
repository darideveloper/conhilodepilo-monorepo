# Design: Fix Admin Title Consistency

## Architectural Reasoning
The Django admin interface relies on a hierarchical template structure. `admin/base_site.html` is the primary entry point for customization of the branding and titles. 

Unfold further abstracts this into its own layouts, specifically `skeleton.html`, which handles the HTML `<head>` section. 

The disconnect occurred because:
1.  **Block Shadowing:** By overriding `base_site.html` without providing a `title` block, we effectively "muted" the default Django behavior for page titles on any view using that template.
2.  **Context Variable Dependency:** Unfold's `SITE_TITLE` setting uses a callback that populates the `site_title` context variable. However, the `skeleton.html` was not leveraging this variable correctly as a fallback.

## Proposed Changes

### 1. Template Inheritance Correction
In `base_site.html`, we will re-introduce the `title` block. This block is standard in Django admin and is expected by most views to set the browser tab title.
-   Format: `[Page Title] | [Site Title]`

### 2. Layout Robustness
In `skeleton.html`, we will modify the `<title>` tag to be more defensive.
-   Instead of just `{% block title %}{% endblock %}`, it will use a combination of the block and the `site_title` variable to ensure that even if a block is empty, the company name is present.

### 3. Context Availability
Since `UNFOLD["SITE_TITLE"]` is already a callback, the `site_title` variable should be available in admin views. No changes to context processors are strictly required if Unfold is working as expected, but verifying this availability is part of the task.
