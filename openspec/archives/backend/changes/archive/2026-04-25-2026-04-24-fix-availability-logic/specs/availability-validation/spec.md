# Spec: Availability Validation

## ADDED Requirements

### Requirement: Availability Range Fallback
The system MUST validate dates against service-specific availability ranges, falling back to company-wide availability ranges if no service ranges are defined.
#### Scenario:
- Service A has an availability range defined (e.g., May 1st to May 31st).
- Service A availability for June 1st should be `False` (out of range).
- Company has an availability range defined (e.g., Jan 1st to Dec 31st).
- If Service B has *no* availability range defined, it should fallback to the Company range.

### Requirement: Weekday Slot Fallback
The system MUST validate weekdays against service-specific weekday slots, falling back to company-wide weekday slots.
#### Scenario:
- Service A has no weekday slots defined.
- Company has Monday slots defined.
- Service A should be available on Mondays.

### Requirement: Override Precedence
Overrides MUST apply at the end of the validation pipeline, with service overrides taking precedence over company overrides.
#### Scenario:
- Service A is normally available on Monday.
- Service A has an override setting that specific Monday to "Unavailable".
- Result should be "Unavailable".
