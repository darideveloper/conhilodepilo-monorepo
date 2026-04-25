# Proposal: Implement Service Availability API

## Summary
Add a new API endpoint to calculate and return available dates (next 30 days) for one or more selected services.

## Problem
The current API lacks the ability to check availability for specific services. Users can only fetch general business hours, which do not account for booking collisions or service-specific availability rules.

## Proposed Solution
Introduce a `GET /api/availability/days/` endpoint that:
1. Accepts `service_ids` (list) and optionally a `start_date`.
2. Validates the request.
3. Computes free days by checking:
    - Company-wide overrides/hours.
    - Service-specific overrides/slots.
    - Existing bookings (respecting `allow_overlap` of service categories).
4. Returns a list of available dates (next 30 days).

## Benefits
- Enables frontend to display a calendar with enabled/disabled dates.
- Improves user experience by showing accurate availability before booking.
