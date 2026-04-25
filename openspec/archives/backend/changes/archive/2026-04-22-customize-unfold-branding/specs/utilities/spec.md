# utilities Specification

## ADDED Requirements

### Requirement: Dynamic Branding Callbacks
The project SHALL include callback functions to resolve site title, header, and icon from the current company profile.

#### Scenario: Resolve Dynamic Header
- GIVEN a `CompanyProfile` with name "Custom Brand"
- WHEN `site_header_callback(request)` is called
- THEN it returns "Custom Brand".

### Requirement: Brand Color Derivation
The project SHALL include a utility to derive a full 11-step palette (50-950) from a base primary color.

#### Scenario: Exact Color Matching
- GIVEN a base color `#ee5837`
- WHEN `get_brand_config()` is called
- THEN the returned dictionary MUST map the exact base color to the `500` and `600` shades.

#### Scenario: Derive OKLCH Shades
- GIVEN a base color `oklch(0.68 0.28 296)`
- WHEN `get_brand_config()` is called
- THEN it returns a dictionary with adjusted luminance values for the remaining shades (e.g., 50, 400, 900).
