# tours-data Specification Delta

## MODIFIED Requirements

### Requirement: Tour Availability Data
Every tour object in the catalog MUST provide accurate availability information for booking.

#### ADDED Scenario: Consistency in Availability Patterns
- **GIVEN** a tour object in `src/data/tours.json`
- **WHEN** availability arrays are populated
- **THEN** it MUST prioritize weekends (Saturdays and Sundays) as `limited`.
- **AND** it MUST keep the `booked` array empty for all tours.
- **AND** it MUST mark the majority of other weekdays as `available`.

#### ADDED Scenario: Visual Variety in Limited Status
- **GIVEN** the collection of all tours
- **WHEN** the `limited` arrays are defined
- **THEN** each tour SHOULD include 1-2 random weekdays in its `limited` array to avoid perfectly uniform availability patterns across the catalog.
