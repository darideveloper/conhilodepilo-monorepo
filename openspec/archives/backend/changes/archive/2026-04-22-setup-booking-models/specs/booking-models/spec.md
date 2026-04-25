# Spec Delta: Booking Models

## ADDED Requirements

### Requirement: Singleton Configuration
The system MUST maintain a single instance of company-wide settings using `django-solo`.

#### Scenario: Managing Profile
- GIVEN the Django Admin
- WHEN the administrator navigates to the Company Profile
- THEN they MUST only be able to edit a single, global configuration record.

### Requirement: Multi-Service Structure
The system MUST group services into types and allow specific descriptions and durations.

#### Scenario: Creating a Service
- GIVEN an EventType "Consultations"
- WHEN an administrator creates an Event "First Meeting" with a duration of 30 minutes
- THEN the service MUST be available for selection in the Booking model.

### Requirement: Tiered Overrides
The system MUST support both global and service-specific availability rules.

#### Scenario: Overriding Global Hours
- GIVEN a global business hour of 9:00 - 17:00
- WHEN a specific Event is configured with an AvailabilitySlot of 10:00 - 12:00
- THEN the system MUST prioritize the Event's slot for that service's availability checks.

### Requirement: Configuration Integrity
The system MUST prevent overlapping availability slots at the same level.

#### Scenario: Preventing Duplicates
- GIVEN a Slot for Monday 09:00-10:00
- WHEN an administrator tries to create another Slot for Monday 09:00-10:00
- THEN the system MUST raise a validation error.

### Requirement: Multi-Service Selection
The system MUST allow selecting multiple services for a single booking instance.

#### Scenario: Scheduling Multiple Services
- GIVEN a client wanting Service A (20m) and Service B (40m)
- WHEN the administrator creates a booking starting at 10:00
- THEN the system MUST calculate the total duration as 60 minutes
- AND the `end_time` MUST be set to 11:00.

### Requirement: Admin Experience (Unfold)
The admin interface MUST provide a high-quality, organized interface for managing bookings.

#### Scenario: Using Filter Horizontal
- GIVEN a Booking creation form in Unfold Admin
- WHEN the administrator views the Services field
- THEN they MUST see a searchable `filter_horizontal` interface to select multiple events.
