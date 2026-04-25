# calendar Spec Delta

## MODIFIED Requirements

### Requirement: Visual Status Representation
The calendar SHALL visually distinguish between dates based on their availability status using brand-consistent colors that maintain semantic clarity.

#### Scenario: Verify Branded Availability Coloring
- **GIVEN** the unified brand color system.
- **WHEN** the calendar is rendered.
- **THEN** "Available" dates MUST show green-ish tones (OKLCH).
- **AND** "Limited" dates MUST show amber/gold tones (OKLCH).
- **AND** "Full" dates MUST show muted/slate tones (OKLCH) with a strike-through.
- **AND** all colors MUST be consistent with the brand's primary hue where appropriate.
