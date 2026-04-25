# Tasks: Cleanup Administrative Consistency

## 1. Code Standardization
- [x] 1.1 Update `project/context_processors.py` to include `site_title` and `site_header`. <!-- id: 0 -->
- [x] 1.2 Update `project/settings.py` to use English `msgid`s for all sidebar items and headers. <!-- id: 1 -->

## 2. Localization Update
- [x] 2.1 Manually update `locale/es/LC_MESSAGES/django.po` with all missing and standardized Spanish translations. <!-- id: 2 -->
- [x] 2.2 Compile translation messages using `python manage.py compilemessages`. <!-- id: 3 -->

## 3. Validation
- [x] 3.1 Verify sidebar items are in Spanish. <!-- id: 4 -->
- [x] 3.2 Verify `EventTypeAdmin` tabs are in Spanish. <!-- id: 5 -->
- [x] 3.3 Verify `CompanyProfileAdmin` tabs are in Spanish. <!-- id: 6 -->
- [x] 3.4 Verify HTML `<title>` uses the dynamic company name globally. <!-- id: 7 -->
