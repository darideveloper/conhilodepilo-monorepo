# core-settings Specification Delta

## ADDED Requirements

### Requirement: Global App Translation
Application-level configurations (like `AppConfig`) MUST have translatable labels to support consistent multi-language dashboard interfaces.

#### Scenario: Translating App Labels
- GIVEN the Django Admin
- WHEN viewing the application list in English
- THEN the "booking" app MUST be labeled "Booking Management" (or similar).
- WHEN switching to Spanish
- THEN the "booking" app MUST be labeled "Gestión de Reservas" (or similar).
