# Design: Business Hours API

## Overview
The requirement is to expose global operating hours for the company so frontend applications can render constrained scheduling logic. The underlying model is `CompanyWeekdaySlot`, which is tied to the `CompanyProfile` singleton.

## Architecture
- **Endpoint Structure:** Instead of exposing a complex nested structure within the `config` endpoint, separating `/business-hours/` provides a cleaner, purpose-built API matching the OpenSpec documentation.
- **Serialization:** Only `weekday`, `start_time`, and `end_time` are needed for client-side processing. The internal ID and company reference are irrelevant to external consumers.
- **Query Strategy:** The view will retrieve the singleton `CompanyProfile` and fetch its `weekday_slots`. This ensures it gracefully handles an empty database state by fetching or creating the singleton profile first.
- **Testing and Verification:** Tests must validate that the `CompanyWeekdaySlot` elements are accurately exposed and publicly accessible, simulating external client behavior without an authorization token.