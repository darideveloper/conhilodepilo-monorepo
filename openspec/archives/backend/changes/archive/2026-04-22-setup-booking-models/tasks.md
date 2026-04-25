# Tasks: Setup Booking Models

## Phase 1: Environment & Dependencies
- [x] Add `django-solo` to `requirements.txt`.
- [x] Update `.env` with core identity and integration placeholders:
    - `COMPANY_NAME`
    - `SITE_URL`
    - `STRIPE_PUBLIC_KEY`
    - `STRIPE_SECRET_KEY`
    - `GOOGLE_CALENDAR_ID`
- [x] Verify environment loading in `project/settings.py`.

## Phase 2: Base Models & Catalog
- [x] Implement Abstract Bases in `booking/models.py`:
    - `BaseAvailabilityRange`
    - `BaseAvailabilitySlot`
    - `BaseDateOverride`
- [x] Implement `CompanyProfile` using `SingletonModel`.
- [x] Implement `EventType` and `Event` models.
- [x] Implement Company-level availability models:
    - `CompanyAvailability`
    - `CompanyWeekdaySlot` (with `unique_together`)
    - `CompanyDateOverride`
- [x] Implement Event-level availability models:
    - `EventAvailability`, `AvailabilitySlot` (with `unique_together`), `EventDateOverride`.

## Phase 3: Booking Implementation
- [x] Implement `Booking` model:
    - `services`: `ManyToManyField` to `Event`.
    - `start_time`, `end_time`, `client_name`, `client_email`, `status`.
    - `db_index=True` on `start_time` and `status`.
- [x] Implement `m2m_changed` signal logic to calculate `end_time` based on the sum of service durations.

## Phase 4: Admin UI (Unfold)
- [x] Register all models in `booking/admin.py` using `unfold.admin.ModelAdmin`.
- [x] Configure `BookingAdmin` with:
    - `filter_horizontal = ('services',)`
    - `fieldsets` for information grouping.
    - `list_filter` for status and date.
- [x] Configure `CompanyProfileAdmin` with `SingletonModelAdmin`.

## Phase 5: Validation
- [x] Create basic unit tests in `booking/tests.py` to verify:
    - Singleton behavior of `CompanyProfile`.
    - Total duration calculation via the `m2m_changed` signal.
    - Uniqueness constraints for slots.
- [x] Run `python manage.py makemigrations` and `python manage.py migrate`.
