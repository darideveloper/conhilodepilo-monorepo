# Tasks: Hide UI via URL Parameters and Internal Refactor

- [x] Rename `tourId` to `serviceId` throughout the codebase:
    - [x] `useBookingStore.ts`: update state and logic.
    - [x] `BookingCalendar.tsx`: update props and state usage.
    - [x] `BookingForm.tsx`: update props and state usage.
    - [x] `BookingFlow.tsx`: update props and state usage.
    - [x] `pages/api/tours.ts`: update response or params if needed. (No changes needed)
    - [x] Any other components or files using `tourId`.
- [x] Update `useBookingStore.ts` to include `theme`, `serviceGroup`, and visibility flags in the state.
- [x] Implement visibility control logic in `BookingFlow.tsx` by processing URL parameters (`lang`, `theme`, `service`, `service_group`).
- [x] Ensure the internal `serviceId` is set when either the `service` or the `tour` URL parameter is provided (for compatibility).
- [x] Update `Layout.astro` inline script to handle URL-based language and theme initialization.
- [x] Conditionally render `LanguageToggle` and `ThemeToggle` in `BookingCalendar.tsx` and `BookingForm.tsx`.
- [x] Update `ThemeToggle.tsx` to use the global theme state from the store.
- [x] Conditionally render the service selector in `BookingCalendar.tsx` based on the visibility flag.
- [x] Create `docs/url-variables.md` with complete documentation for `lang`, `theme`, `service`, and `service_group`.
- [x] Validate changes by testing with various URL parameters and ensuring no regressions from the renaming.
