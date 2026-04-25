## 1. Implementation
- [x] 1.1 Create `BusinessHoursSerializer` in `booking/serializers.py` mapping `CompanyWeekdaySlot` to fields `weekday`, `start_time`, and `end_time`.
- [x] 1.2 Create `BusinessHoursView` in `booking/views.py` subclassing `APIView` with `AllowAny` permissions and fetching all `CompanyWeekdaySlot` records associated with the singleton.
- [x] 1.3 Add `path("api/business-hours/", BusinessHoursView.as_view(), name="api-business-hours")` to `project/urls.py`.
- [x] 1.4 Add a test class for `/api/business-hours/` in `booking/tests_api.py` verifying proper serialization and `200 OK` unauthenticated access.
- [x] 1.5 Create `bruno/Booking/Get Business Hours.yml` that performs a `GET` on `{{base_url}}/api/business-hours/`.