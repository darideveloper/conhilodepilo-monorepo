# core-settings Specification

## MODIFIED Requirements

### Requirement: Branding Context Processor
The project SHALL include a context processor to provide derived brand colors to all templates without colliding with system variables.

#### Scenario: Inject Brand Colors via Unique Variable
- GIVEN the `brand_theme_context` context processor is registered.
- WHEN any template is rendered.
- THEN the context variable `brand_colors` (containing 400, 500, 600 shades) MUST be available.
- AND the context processor function MUST NOT be named `branding` to avoid collisions.
