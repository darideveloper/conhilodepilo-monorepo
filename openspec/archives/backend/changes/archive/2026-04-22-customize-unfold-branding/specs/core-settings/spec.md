# core-settings Specification

## ADDED Requirements

### Requirement: Branding Context Processor
 the project SHALL include a context processor to provide derived brand colors to all templates.

#### Scenario: Inject Brand Colors
- GIVEN the `branding` context processor is registered
- WHEN any template is rendered
- THEN `brand_colors` (containing 400, 500, 600 shades) MUST be available in the context.
