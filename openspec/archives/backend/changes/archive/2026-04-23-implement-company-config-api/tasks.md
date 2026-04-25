# Tasks: Implement Company Configuration API

## Implementation

### Models & Admin
- [x] Add label fields to `CompanyProfile` in `booking/models.py`.
- [x] Create and apply migrations: `python manage.py makemigrations` and `python manage.py migrate`.
- [x] (Verification) Verify new fields are visible in the Unfold admin dashboard.

### API Logic
- [x] Create `booking/serializers.py` with `CompanyProfileSerializer`.
- [x] Implement `CompanyConfigView` in `booking/views.py`.
- [x] Register the `/api/config/` path in `project/urls.py`.

## Validation

### Automated Tests
- [x] Create a new test file `booking/tests_api.py`.
- [x] Implement a test case to verify `GET /api/config/` returns `200 OK`.
- [x] Verify the response JSON structure matches the requirements in the spec.
- [x] Verify unauthenticated access is permitted.

### Manual Verification
- [x] Start the development server and run `curl -X GET http://localhost:8000/api/config/`.
- [x] Confirm `logo` URL is absolute (if logo is present).
