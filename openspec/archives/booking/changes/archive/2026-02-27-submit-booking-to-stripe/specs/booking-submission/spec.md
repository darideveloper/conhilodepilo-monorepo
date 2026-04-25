# Booking Submission Specification

## Purpose
Integrate the booking form with an external Stripe API to process payments and handle the transition from form data to successful redirect.

## ADDED Requirements
### Requirement: API Integration and Payload
The booking form SHALL send the data to the configured Stripe API endpoint with a specific payload structure.

#### Scenario: Verify API Payload Structure
- **GIVEN** the environment variables are correctly set.
- **AND** the user has filled in their name, email, and selected a tour with a date and guests.
- **WHEN** the form is submitted.
- **THEN** the `fetch` request MUST contain the following structure:
  - `url`, `url_success`, `user` from environment variables.
  - `currency` set to `eur`.
  - `products` mapping the tour title to a product object.
  - `description` containing a formatted string of all booking details.

### Requirement: User Feedback and Loading State
The application SHALL provide clear visual feedback during the asynchronous submission process.

#### Scenario: Loading Indicator Visibility
- **GIVEN** the user clicks "Solicitar Reserva".
- **WHEN** the API request is pending.
- **THEN** the submit button MUST display a loading spinner.
- **AND** both the "Volver" and "Solicitar Reserva" buttons MUST be disabled.

#### Scenario: Submission Success Redirection
- **GIVEN** the API returns a `200 OK` with a `url`.
- **WHEN** the response is processed.
- **THEN** the user MUST be automatically redirected to the provided URL.

#### Scenario: API Error Handling
- **GIVEN** the API call fails or returns an error.
- **WHEN** the booking form is submitted.
- **THEN** the loader SHOULD disappear.
- **AND** a user-friendly error message SHOULD be displayed (basic alert).
