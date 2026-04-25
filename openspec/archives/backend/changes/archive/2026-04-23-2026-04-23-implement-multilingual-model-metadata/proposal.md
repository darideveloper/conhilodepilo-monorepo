---
change-id: 2026-04-23-implement-multilingual-model-metadata
title: Implement Multilingual Model Metadata
description: Update models, admin, and app configuration to support full translation of metadata, field names, and verbose names for both English and Spanish.
tags: [i18n, models, admin, translations]
---

# Proposal: Implement Multilingual Model Metadata

## Problem Statement
Currently, while the application supports i18n, several model-level metadata (verbose names, plural names) and field labels are either hardcoded in Spanish or rely on Django's default auto-generated labels, which are not explicitly marked for translation. This results in a fragmented user experience in the admin dashboard when switching between English and Spanish.

## Proposed Solution
We will systematically update the `booking` application to ensure all user-facing strings in the data layer are translatable. This includes:
1. Updating `booking/apps.py` to include a translatable `verbose_name`.
2. Adding `verbose_name` and `verbose_name_plural` to all models in `booking/models.py`.
3. Explicitly defining `verbose_name` for all fields in `booking/models.py`.
4. Ensuring all custom labels in `booking/admin.py` are wrapped in translation hooks.
5. Updating translation files for both `es` and `en`.

## Impact
- **Consistency**: The Admin UI will be fully localized regardless of the selected language.
- **Maintainability**: Explicitly defining translatable strings makes it easier to manage future translations.
- **User Experience**: Improved experience for English-speaking administrators.
