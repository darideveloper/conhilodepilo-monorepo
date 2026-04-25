# Proposal: Hide UI elements via URL variables

This proposal introduces the ability to hide the language, theme, and service selectors through URL parameters. This is useful for embedded or pre-configured booking flows where these settings should be fixed and not changeable by the user.

As part of this change, we will also rename the internal `tourId` to `serviceId` throughout the codebase to align with the new nomenclature.

## Goals
- Allow setting the language via `?lang=es|en` and hiding the language toggle.
- Allow setting the theme via `?theme=light|dark` and hiding the theme toggle.
- Allow setting the service via `?service=ID` and hiding the service selector.
- Support a new `service_group` parameter (for future use).
- Rename internal `tourId` to `serviceId` for consistency.
- Create a comprehensive documentation of all available URL parameters in `docs/url-variables.md`.

## Key Changes
- Update `useBookingStore.ts` to rename `tourId` to `serviceId`, include visibility states for UI elements, and support `service_group`.
- Update `BookingFlow.tsx` to process URL parameters (`lang`, `theme`, `service`, `service_group`) and update the store.
- Update `BookingCalendar.tsx` and `BookingForm.tsx` to conditionally render toggles and the service selector, and use `serviceId`.
- Update `ThemeToggle.tsx` to synchronize with the store's theme state.
- Update `Layout.astro` inline scripts to handle URL-based theme and language initialization.
- Refactor all other occurrences of `tourId` to `serviceId` in the codebase.
- Create `docs/url-variables.md`.
