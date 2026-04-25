# booking-models Specification

## Purpose
TBD - created by archiving change setup-booking-models. Update Purpose after archive.
## Requirements
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

### Requirement: Company Branding Fields
The `CompanyProfile` model MUST include fields for the company's public identity.

#### Scenario: Adding Branding Information
- GIVEN the Company Profile admin
- WHEN an administrator sets the `name` to "My Company"
- THEN the system MUST store this name to be used across the interface.

### Requirement: Color Format Validation
The `brand_color` field MUST support both HEX and OKLCH color formats.

#### Scenario: Validating Color Format
- GIVEN the Company Profile admin
- WHEN an administrator enters `oklch(0.68 0.28 296)`
- THEN the system MUST accept the value.
- WHEN an administrator enters `invalid-color`
- THEN the system MUST raise a validation error.

### Requirement: Global Availability Linkage
Global availability models MUST be linked to the `CompanyProfile` singleton to support administrative inlines.

#### Scenario: Relate Company Availability to Profile
- **Given** an existing `CompanyProfile` singleton instance.
- **When** defining `CompanyAvailability`, `CompanyWeekdaySlot`, and `CompanyDateOverride` models.
- **Then** each model must include a `ForeignKey` to `CompanyProfile`.
- **And** `CompanyWeekdaySlot` MUST use `related_name="weekday_slots"`.
- **And** the relationship must be mandatory (null=False) with a default value pointing to the singleton instance.

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

### Requirement: Service Visualization
The `EventType` model MUST support an optional image for visual categorization in the service catalog.

#### Scenario: Adding an Image to Event Type
- GIVEN the Event Type admin interface
- WHEN an administrator uploads an image for the "General Consultation" event type
- THEN the system MUST store the image and associate it with that event type.
- AND the image MUST be optional.

