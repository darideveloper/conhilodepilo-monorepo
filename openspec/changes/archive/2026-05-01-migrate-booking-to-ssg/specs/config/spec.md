# spec Delta: Static Output Configuration

## ADDED Requirements

### Requirement: Application Output Mode
The build configuration for the booking application MUST explicitly define its output as static to prevent accidental SSR deployment.

#### Scenario: Astro Configuration
- **GIVEN** the `booking/astro.config.mjs` file
- **WHEN** the `defineConfig` object is evaluated
- **THEN** the `output` property MUST be set to `'static'`.
