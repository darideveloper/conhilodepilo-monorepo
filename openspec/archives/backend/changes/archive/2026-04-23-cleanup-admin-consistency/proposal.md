# Proposal: Cleanup Administrative Consistency

This proposal addresses remaining inconsistencies in the administrative interface regarding site identity and translations. While previous efforts improved the UI, several gaps exist where English strings persist or where site-wide identity falls back to hardcoded values.

## Problem Statement
1. **Mixed Translation IDs:** Some parts of the codebase use Spanish strings as `msgid` (e.g., `_("Servicios")` in `settings.py`) while others use English (e.g., `_("Services")` in `admin.py`). This duplicates effort and leads to inconsistent UI state if one is translated and the other is not.
2. **Missing Spanish Translations:** Numerous administrative strings (tabs, fieldsets, actions) in the `.po` file are missing translations.
3. **Site Identity Fragmentation:** Global site identity variables (`site_title`, `site_header`) are not consistently available in all templates, leading to hardcoded fallback usage.
4. **Hardcoded Subheader:** The sidebar subheader "Dashboard" is hardcoded and not translatable.

## Proposed Solution
- **Standardize msgids:** Convert all translatable strings in the codebase to English `msgid` format.
- **Complete Localization:** Populate all missing Spanish translations in `locale/es/LC_MESSAGES/django.po`.
- **Inject Global Context:** Update `project/context_processors.py` to globally provide `site_title` and `site_header`.
- **Refine Settings:** Update `UNFOLD` settings to use translatable labels for all sidebar items and headers.

## Impact
- **Consistency:** Uniform translation strategy across the entire application.
- **Identity:** Dynamic and consistent branding across all admin views.
- **Professionalism:** A fully localized Spanish interface for the end-user.
