# Capability: admin-ui

## ADDED Requirements

### Requirement: Admin Color Picker
The `brand_color` field in the `CompanyProfile` admin interface MUST be rendered using a visual color picker.

#### Scenario: Selecting a new brand color
- GIVEN the user is on the `CompanyProfile` change page in the admin
- AND the user is logged in as the development admin (`admin` / `admin`)
- WHEN the user clicks the `brand_color` input
- THEN a visual color picker MUST be displayed
- AND selecting a color MUST update the field value with a HEX code
- AND saving the profile MUST successfully update the `brand_color` and trigger the regeneration of the dashboard theme colors.

### Requirement: Color Restoration
After verification, the system MUST be restored to its original brand color to maintain design consistency.

#### Scenario: Restoring original color
- GIVEN the verification of the color picker is complete
- WHEN the `brand_color` is reset to `#ee5837`
- THEN the system MUST function exactly as it did prior to the change.

### Requirement: Color Math Preservation
The system MUST continue to derive a full color palette from the `brand_color`, even when it is provided in HEX format by the picker.

#### Scenario: Verifying derived shades
- GIVEN a `CompanyProfile` with `brand_color` set to `#682896`
- WHEN `get_brand_config()` is called
- THEN it MUST return a dictionary of 11 shades (50-950)
- AND the `500` shade MUST match `#682896`.
