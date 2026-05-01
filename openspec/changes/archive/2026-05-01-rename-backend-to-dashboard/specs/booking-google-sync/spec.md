## MODIFIED Requirements
### Requirement: Automatic Sync via Django Signals
A `post_save` signal on `Booking` MUST automatically call `sync_booking_to_google` after every create or update. A `post_delete` signal MUST call `delete_google_calendar_event` when a booking is removed. Signals MUST be registered in `dashboard/booking/signals.py` and connected in `BookingConfig.ready()`.

#### Scenario: Booking created from admin
- **WHEN** a new booking is saved via the Django admin
- **THEN** `post_save` fires and `sync_booking_to_google` is called automatically

#### Scenario: Booking status updated from admin
- **WHEN** an admin changes a booking's status (e.g., PENDING → CONFIRMED) and saves
- **THEN** the corresponding Google Calendar event is patched with updated data

#### Scenario: Booking deleted from admin
- **WHEN** a booking is deleted from the Django admin
- **THEN** `post_delete` fires and the corresponding Google Calendar event is removed
