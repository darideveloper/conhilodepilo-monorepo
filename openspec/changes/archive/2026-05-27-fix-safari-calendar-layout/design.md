## Context

The booking calendar uses `react-day-picker` v9. In Safari on macOS, the month container (with classes `rdp-month`) sometimes fails to render as a proper grid when conflicting flexbox classes are present. The user has identified that the element has classes `flex flex-col w-full gap-4 rdp-month grid` but needs explicit `display: grid` enforcement to fix layout breakage.

## Goals / Non-Goals

**Goals:**
- Fix the calendar month layout specifically for Safari/macOS.
- Maintain existing styling and functionality for other browsers.

**Non-Goals:**
- Redesigning the calendar component.
- Changing `react-day-picker` version.

## Decisions

### 1. Explicitly apply `display: grid` to the month container
Instead of relying solely on the `grid` utility class which might be conflicting with `flex`, we will ensure that the `month` element in `Calendar` component correctly uses the grid layout.
**Rationale:** Safari can be sensitive to conflicting display properties. Ensuring a clean grid setup for the month container is the most direct fix.

### 2. Update `calendar.tsx` class application
Modify the `month` class in `classNames` prop of `DayPicker` to use `grid` instead of `flex flex-col` for the month container, or ensure they don't conflict.
**Rationale:** The calendar content is inherently grid-based (days in a week).

## Risks / Trade-offs

- [Risk] → Changes might affect layout on other browsers.
- [Mitigation] → Use standard Tailwind grid classes that are well-supported and test on Chrome/Firefox.
