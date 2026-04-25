# calendar Specification Delta

## ADDED Requirements
### Requirement: Dynamic Limited Window
The calendar SHALL automatically mark the 10 days immediately following "Today" as "Limited" unless they are explicitly marked as "Booked".

#### Scenario: Verify Rolling 10-Day Window
- **GIVEN** "Today" is February 27, 2026.
- **WHEN** the calendar is rendered for any tour.
- **THEN** dates from February 28 to March 9 MUST be displayed with the "Limited" visual status (Amber).
- **AND** if March 1 was explicitly marked as "Booked" in the data, it MUST remain "Booked" (Slate).
