# Change: Update Tours Availability 2026

## Why
The current tour availability data in `src/data/tours.json` contains placeholder values. This change provides the **final and real** availability for March and April 2026, including the high-demand "Semana Santa" period, ensuring the booking system reflects actual operational capacity.

## What Changes
- Update `dates` object for all 14 tours in `src/data/tours.json`.
- Populate `available` and `limited` arrays with real dates for March and April 2026 based on official schedules.
- Ensure that the peak "Semana Santa" dates (late March to early April) are accurately categorized as "Limited" where appropriate.
- Align `calendar` and `tours-data` specifications with the actual data structure and implementation.

## Impact
- Affected specs: `tours-data`, `calendar`.
- Affected code: `src/data/tours.json`.
