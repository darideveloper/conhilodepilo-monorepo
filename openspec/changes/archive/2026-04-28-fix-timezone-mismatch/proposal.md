# Proposal: Fix Timezone Mismatch and Align with Madrid Time

The current system defaults to `America/Mexico_City` timezone in the dashboard, and the frontend parsing of availability dates (which are returned as "YYYY-MM-DD" strings) leads to a 1-day shift in negative timezones because `new Date(string)` treats that format as UTC. This proposal aligns the entire system to the `Europe/Madrid` (Madrid, Spain) timezone as requested and fixes the date parsing logic to ensure consistent display across all client locations.

## Goals
- Align dashboard `TIME_ZONE` to `Europe/Madrid`.
- Fix the frontend 1-day shift bug in availability calendar.
- Ensure the booking UI consistently displays dates relative to the business's operating timezone.

## Scope
- **Dashboard:** Update `TIME_ZONE` in the dashboard `.env` configuration.
- **Frontend:** Update `fetchAvailability` to parse date strings as local/timezone-aware dates to prevent shifts.
