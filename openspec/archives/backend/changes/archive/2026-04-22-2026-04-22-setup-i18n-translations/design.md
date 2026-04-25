# Design: i18n Translation Workflow

## Architecture Overview
The solution leverages Django's built-in internationalization system. By defining `LOCALE_PATHS`, we tell Django to look for translation files in a local directory before searching in application-specific directories. This allows us to "shadow" or override strings from third-party apps like `django-unfold`.

## Components

### 1. Configuration (`project/settings.py`)
- Add `LOCALE_PATHS` pointing to `BASE_DIR / 'locale'`.
- Define `LANGUAGES` to explicitly support Spanish and English (even if Spanish is the default).
- Ensure `USE_I18N = True` and `LANGUAGE_CODE = 'es'`.

### 2. Storage (`locale/`)
- A new top-level directory `locale/es/LC_MESSAGES/` will contain:
    - `django.po`: The human-readable translation source file.
    - `django.mo`: The compiled binary file used by Django.

### 3. Tooling
- `python manage.py makemessages -l es`: Scans the codebase for `_()` or `gettext` calls.
- `python manage.py makemessages -l es --ignore=venv`: Standard scan.
- **Tip from Documentation:** To capture strings from Unfold templates directly, the scan can be extended to `venv` if necessary, though manual override in `django.po` is preferred for stability.
- `python manage.py compilemessages`: Compiles `.po` files to `.mo`.

## Workflow for Overriding Third-Party Strings
Since `makemessages` only scans local project files, it won't pick up strings from `unfold` inside the virtual environment by default. To override these:
1. Identify the English `msgid` from the UI (e.g., "No results found").
2. Manually append these entries to `locale/es/LC_MESSAGES/django.po`.
3. Ensure no `#, fuzzy` tags are present for these entries.
4. Run `compilemessages`.

## Constraints & Considerations
- **System Dependencies:** `gettext` must be installed on the environment where `makemessages` and `compilemessages` are run.
- **Performance:** `.mo` files are cached by Django. Changes require a server restart in some environments (though usually not in development).
