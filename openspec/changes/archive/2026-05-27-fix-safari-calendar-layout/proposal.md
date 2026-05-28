## Why

In Safari on macOS, the booking calendar month container does not render correctly, leading to layout breakage. This is caused by a missing or overwritten `display: grid` property on the element that handles the calendar layout.

## What Changes

- Update `booking/src/components/atoms/ui/calendar.tsx` to ensure the `month` container explicitly uses `grid` layout when needed or through custom CSS to fix Safari rendering issues.
- Specifically, ensure the element with classes `flex flex-col w-full gap-4 rdp-month` correctly applies grid properties.

## Capabilities

### New Capabilities
- `safari-calendar-fix`: Explicit grid layout enforcement for the calendar month container to ensure cross-browser compatibility.

### Modified Capabilities
- `booking-ui`: Requirements for the booking UI now include specific Safari/macOS layout compatibility for the calendar.

## Impact

- `booking/src/components/atoms/ui/calendar.tsx`: Component styling.
- Booking form UX on macOS/Safari.
