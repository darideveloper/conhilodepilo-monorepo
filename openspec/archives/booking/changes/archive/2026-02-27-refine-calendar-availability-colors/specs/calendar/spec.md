# calendar Specification Delta

## MODIFIED Requirements

### Requirement: Visual Status Representation
The calendar SHALL visually distinguish between dates based on their availability status using intuitive colors (e.g. Green = Available, Amber = Limited).

#### Scenario: Verify Availability Coloring
- **GIVEN** a `bookingData` object with different statuses.
- **WHEN** the calendar is rendered.
- **THEN** "Available" dates MUST show **emerald/green** accents, "Limited" MUST show **amber/gold** accents, and "Full" MUST show **slate/gray** accents with a strike-through.

## NEW Requirements

### Requirement: Hover State Consistency
The component SHALL provide clear visual feedback when a user hovers over a date, while maintaining the visibility of its current status.

#### Scenario: Hover Feedback on Status Dates
- **GIVEN** an "Available" (Green) or "Limited" (Amber) date.
- **WHEN** the user hovers over that date.
- **THEN** the background color MUST subtly change (e.g., to a darker or lighter shade of the status color) to provide interaction feedback, instead of reverting to the generic hover style.
