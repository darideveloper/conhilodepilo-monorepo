# Architectural Design: Availability Intersection

## Overview
The availability logic needs to accurately calculate the intersection of open dates for any arbitrary combination of selected services within a 30-day window.

## Current State (The Problem)
The existing implementation relies on a loop structure to evaluate each date sequentially (`get_available_dates`). Within this loop, `_is_day_available` checks the availability for each service sequentially.
1.  **Intersection Failure:** The use of `return True` when a `DateOverride` allows a service on a given day prematurely terminates the evaluation. The check exits the `_is_day_available` function with a `True` value, thereby skipping all remaining services. For an intersection (`AND`) to be calculated correctly, every service must independently pass its availability test on that specific date.
2.  **N+1 Query Inefficiency:** The inner checks within `_is_day_available` query the database on every pass (e.g., `service.availabilities.all()`, `CompanyDateOverride.objects.filter(date=day)`). Over 30 days and with multiple services, this results in hundreds of individual SQL queries.

## Proposed State (The Solution)

### Correcting Intersection Logic
The logic in `_is_day_available` must be converted from an aggressive early return (`return True`) to an optimistic pass (`continue`). When a `DateOverride` explicitly allows the current service to be booked on the checked date, it implies this single service is available. To maintain intersection, we skip further checks for *this* service (like `CompanyWeekdaySlot`) and `continue` to the next service in the loop. Only if all services finish their loops without returning `False` should the date be deemed available.

### Resolving N+1 Queries
To resolve the inefficiency, the application will shift to an up-front Bulk Data Fetching approach:
1.  **Extract Data:** Execute a small, fixed number of queries (independent of the 30-day loop or the number of services) *before* the loop.
    -   Fetch `CompanyAvailability` and `EventAvailability` mapped for the requested services over the 30-day window.
    -   Fetch all `CompanyDateOverride` and `EventDateOverride` over the 30-day window.
    -   Fetch all relevant `CompanyWeekdaySlot` and `AvailabilitySlot`.
2.  **Build In-Memory Dictionaries:** Organize the fetched data into dictionaries keyed by date, service ID, or weekday for O(1) lookup times.
3.  **Perform In-Memory Checks:** The loop calculating the intersection will then evaluate the conditions using these dictionaries rather than querying the database.

## Trade-offs
- **Pros:** Massively improved performance; guarantees accurate logical intersection.
- **Cons:** Slightly increased code complexity in `get_available_dates` to handle the upfront data extraction and dictionary mapping. Memory usage increases marginally, but only proportional to a 30-day window of small models, making it insignificant.
