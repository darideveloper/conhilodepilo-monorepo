## ADDED Requirements

### Requirement: Environment Configuration Strictness
The environment files MUST separate the declaration of the environment from the environment's configuration values. The root `.env` MUST be restricted to defining the environment context, while `.env.{dev|prod}` provides the actual key-value pairs.

#### Scenario: Developer clones the repository
**Given** a developer sets up any application (`dashboard`, `landing`, or `booking`)
**When** they initialize their environment files
**Then** the `.env` file MUST ONLY contain the `ENV` declaration (e.g., `ENV=dev`).

#### Scenario: Loading Application Context
**Given** the application starts up
**When** the environment variables are loaded
**Then** the system MUST read `ENV` from `.env`, and subsequently load all configuration overrides and secrets exclusively from `.env.${ENV}`.

#### Scenario: Example Template Integrity
**Given** the committed repository state
**When** examining the source control
**Then** there MUST exist `.env.example`, `.env.dev.example`, and `.env.prod.example` for all apps, AND they must contain placeholder strings completely devoid of sensitive production or development secrets.