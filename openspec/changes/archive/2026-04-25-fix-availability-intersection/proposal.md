# Proposal: Fix Availability Intersection and Query Performance

## Problem Statement
The current logic in `dashboard/utils/availability.py` for calculating available booking dates (`get_available_dates`) has two major issues:
1.  **Logical Flaw in Intersection:** The algorithm attempts to find the intersection of available dates for multiple selected services. However, if a service has a specific `DateOverride` making it available on a certain day, the logic immediately returns `True` and short-circuits. This skips evaluating the other services in the request, incorrectly marking the day as available for the entire intersection, even if another selected service is explicitly unavailable on that day.
2.  **Performance Bottleneck (N+1 Queries):** The `get_available_dates` function loops over a 30-day window and checks availability for each service per day, performing multiple database queries within each iteration. This results in dozens to hundreds of queries for a single API request, severely degrading performance.

## Proposed Solution
1.  **Correct the Override Logic:** Change the early `return True` for DateOverrides to `continue`. This ensures that an explicit override makes the current service available for that day but still requires the remaining services to be checked to satisfy the overall intersection requirement.
2.  **Bulk Data Pre-fetching:** Restructure `get_available_dates` to query all relevant availability ranges, slots, and overrides for the requested services and the company over the entire 30-day window upfront in single bulk queries. The daily availability checks will then be performed against this pre-fetched, structured data in memory, reducing the database query count to a small constant number (O(1) with respect to the number of days).

## Impact
- **Accuracy:** The available days endpoint will accurately return only the dates where *all* requested services are mutually available.
- **Performance:** Significant reduction in database load and API response time due to the elimination of N+1 queries.
