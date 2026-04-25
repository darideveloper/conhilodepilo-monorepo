# Proposal: Style Markdown Editor Preview

## Problem
The SimpleMDE Markdown editor preview in the Django admin is currently unstyled. Headings appear as plain text, and lists (bullets/numbers) lack indentation and markers. This is caused by Tailwind CSS's "Preflight" reset, which is part of the Unfold theme and strips default browser styles from these elements. This makes the "Preview" feature of the Markdown editor difficult to read and less useful for verifying content formatting.

## Solution
Implement targeted CSS rules in the project's global stylesheet (`static/css/style.css`) that specifically address the SimpleMDE preview containers (`.editor-preview` and `.editor-preview-side`). These rules will re-introduce standard typography styles (font sizes, weights, margins, and list markers) without affecting the rest of the Unfold admin interface.

## Scope
- **CSS**: Update `static/css/style.css` with typography rules.
- **Admin UI**: Affects all Markdown editors across the admin dashboard.

## Benefits
- Improved content verification before saving.
- Consistent visual feedback for Markdown formatting.
- Better readability for complex descriptions and notes.
