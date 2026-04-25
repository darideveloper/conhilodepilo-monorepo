# Design: Unify Tours Date Patterns

## Date Distribution Strategy

To ensure consistency while maintaining a "random" feel for limited days, the following logic will be applied to each tour in `src/data/tours.json`:

### 1. The Timeframe
The availability data currently covers **March 1, 2026** to **April 30, 2026**.

### 2. Status Mapping
- **`booked`**: Always `[]`.
- **`limited`**:
    - **All Saturdays and Sundays** in March and April 2026.
    - **1-2 random weekdays** per tour. These should vary between tours to avoid a perfectly uniform look across the entire catalog.
- **`available`**:
    - **All other weekdays** (Monday through Friday) in March and April 2026 that are not selected as "limited".

### 3. Verification of Weekends (2026)
- **March**: 1, 7-8, 14-15, 21-22, 28-29.
- **April**: 4-5, 11-12, 18-19, 25-26.

### 4. Special Case: Palacios Nazaríes
This tour currently has all dates as `limited`. It will be refactored to follow the standard pattern, making most of its weekdays `available`.

## Implementation Details
The changes will be applied directly to `src/data/tours.json`. Since this file is the source of truth for the API and the frontend components, no code changes in `src/components` or `src/store` are required.
