# calendar Specification Delta

## ADDED Requirements

### Requirement: Show Current Month Dates Only
The `BookingCalendar` SHALL only display and allow the selection of dates that fall within the month currently being viewed. Dates from the previous or next month (outside days) MUST be hidden from the calendar grid.

#### Scenario: Verify Hidden Outside Days
- **GIVEN** the calendar is displaying "May 2026".
- **WHEN** the calendar grid is rendered.
- **THEN** any dates from April or June that would normally complete the first or last week of the grid MUST be hidden (not visible and not selectable).
