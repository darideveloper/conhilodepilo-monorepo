---
change-id: fix-unfold-admin-ui-layout
title: Fix Unfold Admin UI Bottom Bar Positioning
status: draft
author: Gemini CLI
date: 2026-04-22
---

# Proposal: Fix Unfold Admin UI Bottom Bar Positioning

## Problem
The Unfold admin interface in the dashboard currently has issues with the "bottom bar" (the sticky container for action buttons like Save, Delete, etc.). The bar is either misplaced, lacks sticky behavior, or is missing essential Tailwind container classes. This is primarily caused by incorrect template inheritance and inconsistent `ModelAdmin` base class usage.

## Solution
1. **Restore Proper Template Inheritance**: Rename the custom `admin/base.html` to `admin/base_site.html` and update it to extend Unfold's `admin/base.html`. This ensures that Unfold's internal layout logic and container classes are correctly applied.
2. **Standardize Admin Base Class**: Update all application `ModelAdmin` classes to inherit from `ModelAdminUnfoldBase` (defined in `project/admin.py`) instead of the raw Unfold `ModelAdmin`. This ensures consistent UI behavior and features across all admin modules.
3. **Verify Layout Consistency**: Ensure that no conflicting custom CSS is fighting against Unfold's native sticky positioning.

## Impact
- **Improved UX**: The action bar will be consistently pinned to the bottom of the viewport as intended by the Unfold theme.
- **Consistency**: All admin pages will benefit from standardized Unfold features like unsaved form warnings and compressed fields.
- **Maintainability**: Proper template inheritance follows Django and Unfold best practices, making future updates easier.
