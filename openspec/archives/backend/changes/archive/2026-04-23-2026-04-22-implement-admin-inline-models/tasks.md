# Tasks: Implement Admin Inline Models

## Phase 1: Model Enhancements
- [x] Add `__str__` methods to `BaseAvailabilityRange`, `BaseAvailabilitySlot`, and `BaseDateOverride` in `booking/models.py`.
- [x] Add `ForeignKey` to `CompanyProfile` in `CompanyAvailability`.
- [x] Add `ForeignKey` to `CompanyProfile` in `CompanyWeekdaySlot` (use `related_name="weekday_slots"`).
- [x] Add `ForeignKey` to `CompanyProfile` in `CompanyDateOverride`.
- [x] Generate and run migrations.
  - *Validation*: `python manage.py makemigrations` and `python manage.py migrate`.

## Phase 2: Base Admin Components
- [x] Create `BaseTabularInline` in `booking/admin.py` or use Unfold's directly.
- [x] Implement `AvailabilitySlotInline` with the 7-day pre-population logic (handle both `slots` and `weekday_slots` related names).
- [x] Implement `BookingInline` using `model = Booking.services.through`.
  - [x] Add methods for `client_name`, `status`, etc., to pull from the `booking` instance.
  - [x] Implement the `manage_booking` button logic.

## Phase 3: Event Admin Integration
- [x] Define inlines for `EventAvailability`, `AvailabilitySlot`, `EventDateOverride`, and `BookingInline`.
- [x] Configure `EventAdmin.tabs` and `EventAdmin.inlines`.
  - *Validation*: Verify tabs appear correctly in `/admin/booking/event/`.

## Phase 4: Company Profile Admin Integration
- [x] Define inlines for `CompanyAvailability`, `CompanyWeekdaySlot`, and `CompanyDateOverride`.
- [x] Configure `CompanyProfileAdmin.tabs` and `CompanyProfileAdmin.inlines`.
  - *Validation*: Verify tabs appear correctly in `/admin/booking/companyprofile/`.

## Phase 5: UI Refinement & Sidebar
- [x] Update `EventTypeAdmin` to include `EventInline`.
- [x] Update `UNFOLD["SIDEBAR"]` in `project/settings.py` to remove redundant "Disponibilidad" and secondary links.
- [x] Run `ruff check .` or `flake8` to ensure code quality.
