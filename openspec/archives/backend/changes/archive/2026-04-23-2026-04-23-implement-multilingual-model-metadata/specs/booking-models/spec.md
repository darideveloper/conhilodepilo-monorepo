# booking-models Specification Delta

## ADDED Requirements

### Requirement: Multilingual Metadata
All models and fields within the `booking` application MUST have translatable labels.

#### Scenario: Translating Model Names
- GIVEN the Django Admin in English
- WHEN viewing the "booking" app section
- THEN "Booking" MUST be displayed.
- WHEN switching the Admin to Spanish
- THEN "Reserva" MUST be displayed.

#### Scenario: Translating Field Labels
- GIVEN the Booking model in the Admin
- WHEN viewing the "client_name" field in English
- THEN "Client name" MUST be displayed.
- WHEN switching to Spanish
- THEN "Nombre del cliente" MUST be displayed.
