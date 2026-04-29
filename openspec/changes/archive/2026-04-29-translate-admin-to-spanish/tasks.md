# Tasks: Translate Admin Interface to Spanish

## 1. Research & Preparation
- [x] 1.1 Verify all visible strings in `backend/booking/models.py` are wrapped in `_()`.
- [x] 1.2 Verify all visible strings in `backend/booking/admin.py` are wrapped in `_()`.
- [x] 1.3 Verify all visible strings in `backend/project/settings.py` (UNFOLD settings) are wrapped in `_()`.
- [x] 1.4 Identify any hardcoded English strings in `utils/callbacks.py` or `apps.py` that need wrapping.

## 2. Source Code Updates
- [x] 2.1 Wrap any missing strings identified in phase 1 with `gettext_lazy` or `gettext`.
- [x] 2.2 Wrap environment names in `backend/utils/callbacks.py` with `gettext_lazy`.
- [x] 2.3 Standardize existing English source strings if they are inconsistent (e.g., "Event type" vs "Service type").

## 3. Translation Catalog Updates
- [x] 3.1 Run `python manage.py makemessages -l es` to sync all strings to the `.po` file.
- [x] 3.2 Update `backend/locale/es/LC_MESSAGES/django.po` with Spanish translations for all `msgstr ""`.
- [x] 3.3 Verify existing translations are not "broken" or unintentionally modified.

## 4. Verification
- [x] 4.1 Compile messages using `python manage.py compilemessages`.
- [x] 4.2 Start the backend server and manually verify the admin interface in Spanish.
- [x] 4.3 Check specifically for:
    - [x] Model names and plurals.
    - [x] Field labels in forms.
    - [x] List filter titles.
    - [x] Navigation sidebar titles and items.
    - [x] Success/error messages and validation warnings.
