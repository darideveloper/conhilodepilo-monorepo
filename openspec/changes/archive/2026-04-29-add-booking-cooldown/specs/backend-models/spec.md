## ADDED Requirements

### Requirement: Global Booking Cooldown
The system MUST allow an administrator to define a global "cool down" period (in minutes) that is enforced between consecutive bookings.

#### Scenario: Configuring cooldown
- **WHEN** the administrator updates the Company Profile with a `booking_cooldown_minutes` value of `15`.
- **THEN** all subsequent availability calculations MUST ensure at least a 15-minute gap exists between the end of one booking and the start of the next.
