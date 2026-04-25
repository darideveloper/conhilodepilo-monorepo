# Tasks: Add Image to EventType

## 1. Implementation
- [x] 1.1 Add `image` field to `EventType` model in `booking/models.py` <!-- id: 0 -->
- [x] 1.2 Generate database migration for the new field <!-- id: 1 -->
- [x] 1.3 Apply database migration <!-- id: 2 -->
- [x] 1.4 Add `image` field to `EventTypeAdmin` in `booking/admin.py` <!-- id: 3 -->

## 2. Validation
- [x] 2.1 Add unit test in `booking/tests.py` to verify the `image` field is optional <!-- id: 4 -->
- [x] 2.2 Run Django tests to verify model integrity <!-- id: 5 -->
- [x] 2.3 Manually verify image upload and display in Admin <!-- id: 6 -->

## 3. Localization
- [x] 3.1 Update Spanish translation catalog with `makemessages` <!-- id: 7 -->
- [x] 3.2 Translate the new "Image" string in `django.po` <!-- id: 8 -->
- [x] 3.3 Compile translation messages <!-- id: 9 -->
