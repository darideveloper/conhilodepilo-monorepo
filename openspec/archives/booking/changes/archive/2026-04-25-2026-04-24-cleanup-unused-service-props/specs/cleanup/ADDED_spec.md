# cleanup-unused-props Specification

## Purpose
Clean up unused `initialServiceId` property to reduce code complexity, as pre-selection is handled exclusively via client-side URL parameter parsing.

## ADDED Requirements

### Requirement: Improved codebase maintainability by removing unused prop
- **Given** `src/components/pages/index.astro` and `src/components/organisms/BookingFlow.tsx` defined an `initialServiceId` prop
- **When** it is removed
- **Then** the components MUST function without it

#### Scenario: Verify component rendering
- **Given** the component prop is removed
- **When** the booking page is rendered
- **Then** it MUST load the `BookingFlow` component without error

### Requirement: Simplified service selection logic
- **Given** `src/components/organisms/BookingFlow.tsx` used `initialServiceId`
- **When** it is removed
- **Then** the component SHALL handle service selection solely through URL parameters
- **And** no compile errors SHALL be generated

#### Scenario: Verify service pre-selection
- **Given** the component prop is removed
- **When** a user navigates with `?service=alhambra-completa`
- **Then** the service MUST be correctly selected from the URL
