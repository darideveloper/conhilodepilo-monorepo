# Proposal: Setup i18n Translations for Spanish UI

## Problem Statement
Despite `LANGUAGE_CODE` being set to `es` in `project/settings.py`, several UI elements in the Unfold admin interface (such as "No results found", search placeholders, and filters) remain in English. This is because these strings are not fully covered by Unfold's built-in Spanish translations or need to be explicitly overridden/defined in the project's local translation files.

## Proposed Solution
Implement a robust internationalization (i18n) workflow that allows for project-specific translation overrides. This involves:
1. Configuring `LOCALE_PATHS` in `project/settings.py`.
2. Initializing a `locale/` directory to house Spanish (`es`) translation files.
3. Generating the initial `.po` files using `makemessages`.
4. Manually adding the missing Unfold and Django admin translations to the local `.po` file.
5. Compiling the translations into `.mo` files for runtime use.

## Impact
- **User Experience:** Provides a fully localized Spanish interface for administrative users.
- **Consistency:** Ensures all "magic" strings from third-party libraries (Unfold, Django Admin) are consistent with the project's language settings.
- **Maintainability:** Establishes a standard process for adding future translations.
