# booking-models Specification

## ADDED Requirements

### Requirement: Company Branding Fields
The `CompanyProfile` model MUST include fields for the company's public identity.

#### Scenario: Adding Branding Information
- GIVEN the Company Profile admin
- WHEN an administrator sets the `name` to "My Company"
- THEN the system MUST store this name to be used across the interface.

### Requirement: Color Format Validation
The `brand_color` field MUST support both HEX and OKLCH color formats.

#### Scenario: Validating Color Format
- GIVEN the Company Profile admin
- WHEN an administrator enters `oklch(0.68 0.28 296)`
- THEN the system MUST accept the value.
- WHEN an administrator enters `invalid-color`
- THEN the system MUST raise a validation error.
