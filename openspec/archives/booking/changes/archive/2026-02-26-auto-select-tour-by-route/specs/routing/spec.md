# Routing Specification

## ADDED Requirements

### Requirement: Tour Specific Routes
The application MUST provide dedicated routes for each tour defined in the system.

#### Scenario: Visit Tour Page
- **Given** a tour with ID "alhambra-completa" exists in `tours.json`
- **When** the user navigates to `/alhambra-completa`
- **Then** the page MUST render the booking interface.

#### Scenario: Dynamic Path Generation
- **Given** a new tour with ID "new-tour-id" is added to `tours.json`
- **When** the application is built
- **Then** the route `/new-tour-id` MUST be available.

### Requirement: Auto-selection by Route
The booking form MUST automatically select the tour corresponding to the current URL path.

#### Scenario: Auto-select from URL
- **Given** the user is on the page `/alhambra-completa`
- **When** the booking form is loaded
- **Then** the "Tour" field MUST be pre-selected with "Alhambra Completa".
- **And** the `formData.tourId` in the Zustand store MUST be set to "alhambra-completa".
