# Proposal: Unify Tours Date Patterns

## Problem
The current date availability in `src/data/tours.json` is inconsistent across different tours. Some tours have empty `limited` arrays, while others have excessive `limited` days (or only `limited` days). Additionally, some tours contain `booked` dates, which contradicts the goal of having no "completed" days in any tour.

## Solution
Standardize the `dates` object for all tours in `src/data/tours.json` to follow a consistent pattern:
1.  **Empty `booked` list**: Ensure no tour has dates in the `booked` array.
2.  **Weekend-focused `limited` status**: All weekends in March and April 2026 should be marked as `limited`.
3.  **Randomized weekday `limited` status**: Add 1-2 random weekdays as `limited` for each tour to provide visual variety and reflect real-world constraints.
4.  **Weekday-focused `available` status**: All other weekdays in the specified period should be marked as `available`.

## Impact
- **Consistency**: All tours will show a similar level of availability, providing a more professional and predictable user experience.
- **Visual Polish**: The calendar will display a balanced mix of "Available" (green) and "Limited" (yellow) statuses, primarily highlighting weekends as higher-demand days.
- **Clarity**: Removing `booked` dates ensures users don't encounter "Sold Out" dates during this phase of the project.
