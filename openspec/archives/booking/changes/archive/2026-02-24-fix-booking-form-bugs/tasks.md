# Tasks: Booking Calendar UI Fixes

- [x] **BookingCalendar Organism Fixes**
    - [x] Change initial `date` state from `today` to `undefined` in `src/components/organisms/BookingCalendar.tsx`.

- [x] **Calendar Atom Fixes**
    - [x] Update `CalendarDayButton` in `src/components/atoms/ui/calendar.tsx`:
        - [x] Change `data-[selected-single=true]:bg-primary` to `data-[selected-single=true]:bg-foreground`.
        - [x] Change `data-[selected-single=true]:text-primary-foreground` to `data-[selected-single=true]:text-background`.

- [x] **Validation**
    - [x] Run `npm run build` to ensure no build errors.
    - [x] Verify that the calendar widget shows no initial selection.
    - [x] Verify that selecting any date (available or limited) results in a black background.
    - [x] Verify that the hover state still works as expected.
    - [x] Run `openspec validate fix-booking-form-bugs`.
