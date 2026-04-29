# availability-cooldown Specification

## Purpose
TBD - created by archiving change add-booking-cooldown. Update Purpose after archive.
## Requirements
### Requirement: Cooldown Enforcement in Slots
The availability engine MUST subtract the global cooldown period from available time windows to prevent back-to-back bookings without a buffer.

#### Scenario: Booking with 15-minute cooldown
- **GIVEN** a company has a 15-minute cooldown configured.
- **GIVEN** an existing booking ends at 11:00 AM.
- **WHEN** a user checks for available slots.
- **THEN** the next available slot MUST NOT start before 11:15 AM.

#### Scenario: Booking before an existing appointment
- **GIVEN** a company has a 15-minute cooldown configured.
- **GIVEN** an existing booking starts at 12:30 PM.
- **WHEN** a user checks for available slots for a 60-minute service.
- **THEN** a slot at 11:15 AM MUST NOT be available (as it would end at 12:15, which is less than 15 mins before 12:30).
- **AND** a slot at 11:00 AM SHOULD be available (as it ends at 12:00, which is 30 mins before 12:30).

