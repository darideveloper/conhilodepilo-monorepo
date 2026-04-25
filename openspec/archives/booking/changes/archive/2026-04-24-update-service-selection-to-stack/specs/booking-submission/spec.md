## MODIFIED Requirements
### Requirement: API Integration and Payload
The booking form SHALL send the data to the configured Stripe API endpoint with a specific payload structure **using the centralized API service layer**.

#### Scenario: Verify API Payload Structure
- **GIVEN** the environment variables are correctly set.
- **AND** the user has filled in their name, email, and stacked tours with a date and guests.
- **WHEN** the form is submitted via the `submitBooking` service.
- **THEN** the `fetch` request MUST contain the following structure:
  - `url`, `url_success`, `user` from environment variables.
  - `currency` set to `eur`.
  - `products` mapping the array of selected tours to products.
  - `description` containing a formatted string of all booking details, including all selected tours.
  - `client` subdomain prepended if applicable.
  - **AND** the payload MUST submit an array of `serviceIds` corresponding to the stacked services.

#### Scenario: Real API Call Replace
- **GIVEN** the booking form is currently simulating submission via `setTimeout`.
- **WHEN** the submission logic is refactored.
- **THEN** it MUST perform a real `POST` request using the centralized `api/booking` service.
- **AND** it MUST handle both successful redirection and failure states visually.
