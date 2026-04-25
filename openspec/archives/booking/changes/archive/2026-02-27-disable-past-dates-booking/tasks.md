# Tasks: Disable Past Dates

## 1. Preparation
- [x] Define `today` constant in `BookingCalendar.tsx` using `useMemo`. <!-- id: task-define-today -->

## 2. Implementation
- [x] Update `disabled` prop in `Calendar` to include dates `<= today`. <!-- id: task-update-disabled-prop -->
- [x] Update `modifiers` logic to only highlight dates `> today`. <!-- id: task-update-modifiers-logic -->
- [x] Update `getStatus` helper to respect the "future only" rule. <!-- id: task-update-getstatus-logic -->

## 3. Validation
- [x] Verify that today's date is greyed out and unclickable. <!-- id: task-verify-today-disabled -->
- [x] Verify that yesterday's date is greyed out and unclickable. <!-- id: task-verify-yesterday-disabled -->
- [x] Verify that tomorrow's date remains selectable (if available). <!-- id: task-verify-tomorrow-enabled -->
