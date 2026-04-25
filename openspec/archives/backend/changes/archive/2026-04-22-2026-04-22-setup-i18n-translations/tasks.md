# Tasks: Setup i18n Translations

- [x] **Infrastructure: Setup Locale Directory**
    - [x] Verify `gettext` is installed on the system (run `xgettext --version`).
    - [x] Create `locale/` directory in the project root.
    - [x] Ensure the directory is excluded from unnecessary scans but tracked in git (except for compiled files if preferred, though usually `.mo` are ignored).

- [x] **Configuration: Update Django Settings**
    - [x] Add `LOCALE_PATHS` to `project/settings.py`.
    - [x] Define `LANGUAGES = [("es", _("Spanish")), ("en", _("English"))]` in `project/settings.py`.
    - [x] Verify `LANGUAGE_CODE = 'es'` and `USE_I18N = True`.

- [x] **Generation: Initialize Translation Files**
    - [x] Run `python manage.py makemessages -l es`.
    - [x] Verify `locale/es/LC_MESSAGES/django.po` is created.

- [x] **Implementation: Add Missing Translations**
    - [x] Identify key missing strings: "No results found", "Search", "Filters", etc.
    - [x] Add entries to `django.po` for these strings.
    - [x] **Check for fuzzy tags:** Ensure no entries are marked as `#, fuzzy`.
    - [x] Example entry:
        ```po
        msgid "No results found"
        msgstr "No se encontraron resultados"
        ```

- [x] **Compilation: Build Binary Files**
    - [x] Run `python manage.py compilemessages`.
    - [x] Verify `.mo` files are generated.

- [x] **Validation: UI Check**
    - [x] Restart the development server.
    - [x] Verify that the English strings in the Admin UI are now displayed in Spanish.
