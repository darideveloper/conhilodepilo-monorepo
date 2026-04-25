# tours-data Specification Delta

## MODIFIED Requirements
### Requirement: Tour Availability Data
Every tour object in the catalog MUST provide accurate availability information for booking using an exclusion-based model.

#### MODIFIED Scenario: Consistency in Availability Patterns
- **GIVEN** a tour object in `src/data/tours.json`
- **WHEN** availability arrays are populated
- **THEN** it MUST prioritize weekends (Saturdays and Sundays) as `limited`.
- **AND** it MUST keep the `booked` array empty for all tours.
- **AND** it MUST NOT include an `available` property, as all future dates are available by default.
