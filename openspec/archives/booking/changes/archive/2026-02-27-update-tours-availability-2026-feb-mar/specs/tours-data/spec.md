# tours-data Specification Delta

## MODIFIED Requirements

### Requirement: Tour Availability Data
Every tour object in the catalog MUST provide accurate availability information for booking.

#### Scenario: Date Structure Definition
- **GIVEN** a tour object in `src/data/tours.json`
- **WHEN** the `dates` property is present
- **THEN** it MUST contain three arrays: `available`, `limited`, and `booked`.

#### Scenario: Date Format Compliance
- **GIVEN** the `dates` property
- **WHEN** populating the availability arrays
- **THEN** all entries MUST be strings in the `YYYY-MM-DD` format.

#### Scenario: Logical Date Separation
- **GIVEN** a tour's availability arrays
- **WHEN** checking for date occurrences
- **THEN** a single date MUST NOT appear in more than one of the `available`, `limited`, or `booked` arrays for that tour.
