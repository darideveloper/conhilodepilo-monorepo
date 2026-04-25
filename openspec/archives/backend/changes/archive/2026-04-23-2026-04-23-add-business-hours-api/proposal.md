# Add Business Hours API

## Context
The application needs an endpoint to expose global operating hours to clients, which will constrain slot generation for scheduling. The documentation specifies a `GET /business-hours/` endpoint returning a list of available weekday slots.

## Proposed Changes
- Implement a `BusinessHoursView` endpoint that returns a list of configured `CompanyWeekdaySlot` items.
- Map the endpoint to `/api/business-hours/`.
- Create a `BusinessHoursSerializer` for serializing the slot data (`weekday`, `start_time`, `end_time`).
- Add tests to ensure the endpoint correctly returns business hours data and remains publicly accessible.
- Create a corresponding Bruno collection request file for the endpoint to support API exploration and manual testing.