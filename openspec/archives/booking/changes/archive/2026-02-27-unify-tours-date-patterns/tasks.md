# Tasks: Unify Tours Date Patterns

## Data Modification
- [x] Reset `booked` dates to `[]` for all tours in `src/data/tours.json`. <!-- id: 0 -->
- [x] Standardize `limited` dates for all tours to include all weekends in March and April 2026. <!-- id: 1 -->
- [x] Distribute 1-2 random weekdays as `limited` for each tour. <!-- id: 2 -->
- [x] Set all remaining weekdays in March and April 2026 as `available`. <!-- id: 3 -->
- [x] Special attention to `palacios-nazaries` to move the majority of its dates from `limited` to `available`. <!-- id: 4 -->

## Validation
- [x] Verify that no date appears in more than one array for any tour. <!-- id: 5 -->
- [x] Verify that all tours have a non-empty `available` and `limited` list. <!-- id: 6 -->
- [x] Verify that `booked` is empty for all tours. <!-- id: 7 -->
