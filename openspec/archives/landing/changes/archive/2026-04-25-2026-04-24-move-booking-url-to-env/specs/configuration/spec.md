# Configuration Specification

## ADDED Requirements
### Requirement: Environment Variable Support for Booking URL
- The system MUST support `PUBLIC_BOOKING_URL` via environment variables.
#### Scenario: Booking Iframe URL Configuration
- Given the need to configure the booking base URL, the system MUST support `PUBLIC_BOOKING_URL` via environment variables.

## MODIFIED Requirements
#### Requirement: Dynamic Booking URL Construction
- The system MUST construct the iframe `src` using the `PUBLIC_BOOKING_URL` environment variable.
#### Scenario: Dynamic Booking URL Construction
- Given an `id`, the system MUST construct the iframe `src` using the `PUBLIC_BOOKING_URL` environment variable followed by `?service={id}`.
