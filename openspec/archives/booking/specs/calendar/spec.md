# calendar Specification

## Purpose
TBD - created by archiving change render-booking-calendar. Update Purpose after archive.
## Requirements
### Requirement: Visual Status Representation
The calendar SHALL visually distinguish between dates based on their availability status using brand-consistent colors that maintain semantic clarity.

#### Scenario: Verify Branded Availability Coloring
- **GIVEN** the unified brand color system.
- **WHEN** the calendar is rendered.
- **THEN** "Available" dates MUST show green-ish tones (OKLCH).
- **AND** "Limited" dates MUST show amber/gold tones (OKLCH).
- **AND** "Full" dates MUST show muted/slate tones (OKLCH) with a strike-through.
- **AND** all colors MUST be consistent with the brand's primary hue where appropriate.

### Requirement: Interactive Date Selection
The component SHALL allow users to select a single date and display its detailed status, restricted to future dates only.

#### Scenario: Prevent Past Date Selection
- **GIVEN** the current date is "Today"
- **WHEN** the calendar is displayed
- **THEN** all dates before and including "Today" MUST be disabled and non-selectable.

#### Scenario: Hide Availability for Past Dates
- **GIVEN** a date that is in the past but marked as "Available" in the data source
- **WHEN** the calendar renders
- **THEN** that date MUST NOT show the green availability accent and MUST be disabled.

### Requirement: Data Structure Compatibility
The component SHALL consume a simplified availability data structure where availability is inferred.

#### MODIFIED Scenario: Mock Data Integration
- **GIVEN** a `bookingData` structure (e.g. from `useBookingStore`)
- **WHEN** it contains `booked` and `limited` arrays of `Date` objects
- **THEN** any future date not present in these arrays MUST be treated as "available".
- **AND** the availability arrays MUST represent the intersected availability across all stacked services.

### Requirement: Hover State Consistency
The component SHALL provide clear visual feedback when a user hovers over a date, while maintaining the visibility of its current status.

#### Scenario: Hover Feedback on Status Dates
- **GIVEN** an "Available" (Green) or "Limited" (Amber) date.
- **WHEN** the user hovers over that date.
- **THEN** the background color MUST subtly change (e.g., to a darker or lighter shade of the status color) to provide interaction feedback, instead of reverting to the generic hover style.

### Requirement: UI Simplification
The `BookingCalendar` SHALL NOT display redundant header titles, descriptions, or step indicators.

#### Scenario: No Header in BookingCalendar
- **Given** the user is on the `BookingCalendar`
- **Then** the text "Selecciona tu Tour y Fecha" MUST NOT be visible.
- **And** the text "Elige el tour que deseas realizar y busca un día disponible." MUST NOT be visible.

#### Scenario: No Step Indicator in Step 1
- **Given** the user is on the `BookingCalendar`
- **Then** the text "Paso 1 de 2" MUST NOT be visible.

### Requirement: Dynamic Limited Window
The calendar SHALL automatically mark the 10 days immediately following "Today" as "Limited" unless they are explicitly marked as "Booked".

#### Scenario: Verify Rolling 10-Day Window
- **GIVEN** "Today" is February 27, 2026.
- **WHEN** the calendar is rendered for any tour.
- **THEN** dates from February 28 to March 9 MUST be displayed with the "Limited" visual status (Amber).
- **AND** if March 1 was explicitly marked as "Booked" in the data, it MUST remain "Booked" (Slate).

### Requirement: Show Current Month Dates Only
The `BookingCalendar` SHALL only display and allow the selection of dates that fall within the month currently being viewed. Dates from the previous or next month (outside days) MUST be hidden from the calendar grid.

#### Scenario: Verify Hidden Outside Days
- **GIVEN** the calendar is displaying "May 2026".
- **WHEN** the calendar grid is rendered.
- **THEN** any dates from April or June that would normally complete the first or last week of the grid MUST be hidden (not visible and not selectable).

