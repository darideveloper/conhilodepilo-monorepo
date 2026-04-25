# Spec: Centralized State Management

## ADDED Requirements
### Requirement: API State Integration
The centralized store SHALL encapsulate methods that interact with the **API Service Layer**, ensuring a clean separation between state management and network implementation.

#### Scenario: Dispatch fetchConfig
- **GIVEN** the `useBookingStore` is initialized.
- **WHEN** the `fetchConfig` dispatch action is called.
- **THEN** it MUST invoke the corresponding `api/config` service and update the store's `config` state.
