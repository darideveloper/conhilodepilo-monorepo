## ADDED Requirements

### Requirement: Categories and Services Discovery API
The system MUST provide a public API endpoint to retrieve all available service categories (`EventType`) and their associated services (`Event`).
- The response MUST include a top-level array of categories.
- Each category MUST include its main data (`id`, `name`, `description`, `image`).
- Each category MUST include a nested `services` array containing its associated services.
- Each service MUST include its main data (`id`, `title` (mapping to name), `description`, `price`, `duration` (mapping to duration_minutes), `image`).
- The response MUST explicitly EXCLUDE any availability data (e.g., date overrides, slots).

#### Scenario: Retrieving categories and services successfully
- GIVEN the database contains `EventType` and `Event` records
- WHEN a client sends a `GET` request to `/api/services/`
- THEN the system MUST return a `200 OK` status
- AND the JSON response MUST contain a list of categories
- AND each category object MUST contain the fields: `id`, `name`, `description`, `image`, and `services`
- AND the `services` array MUST contain service objects with the fields: `id`, `title`, `description`, `price`, `duration`, and `image`.
- AND the response MUST NOT contain any slots or availability configurations.

### Requirement: Categories Bruno Collection Synchronization
All API endpoints MUST have a corresponding request defined in the Bruno collection.

#### Scenario: Exploring Categories API
- GIVEN the Bruno collection in `bruno/`
- WHEN a developer inspects the "Booking" folder
- THEN there MUST be a "Get Services" request file configured to query `/api/services/`.
