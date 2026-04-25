# Proposal: Render all textarea fields as Markdown editors

## Problem
Currently, the Markdown editor (SimpleMDE) is only applied to a subset of `textarea` fields in the Django admin. Specifically, fields with IDs like `description` are explicitly excluded. This leads to an inconsistent user experience where some long-text fields have rich editing capabilities while others do not, even when Markdown content is intended.

## Solution
Modify the Markdown loading logic in the admin interface to remove the blacklist of excluded field IDs. This will ensure that all `textarea` fields rendered within the standard admin layout are enhanced with the SimpleMDE editor.

## Scope
- **Frontend**: Update `static/js/load_markdown.js`.
- **Admin UI**: Affects all models in the Django admin that use `TextField`.

## Benefits
- Consistent editing experience across the entire dashboard.
- Enables rich formatting (bold, links, lists) for all description fields.
- Simplifies the maintenance of the Markdown loading script.
