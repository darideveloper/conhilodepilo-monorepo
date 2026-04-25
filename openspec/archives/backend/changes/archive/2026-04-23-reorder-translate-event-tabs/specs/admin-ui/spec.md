# Spec Delta: Refined Event Admin Tabs

## MODIFIED Requirements

### Requirement: Tabbed Administrative Interface
The admin interface SHALL use a tabbed layout for complex models to reduce vertical scrolling and group related settings logically.

#### Scenario: Group Event Configuration in Tabs
- **Given** the `Event` ModelAdmin.
- **When** the admin page is rendered.
- **Then** fields and inlines must be organized into horizontal tabs in the following order:
    1. "General" (Fieldsets)
    2. "Service Week Slots" (Availability Slots)
    3. "Service Availability" (Date Ranges)
    4. "Service Date Overrides" (Holidays/Exceptions)
    5. "Booking" (Read-only summary)

### Requirement: Read-Only Booking Summary
The service management interface SHALL show a non-editable summary of associated bookings.

#### Scenario: View Bookings within Event Admin
- **Given** an `Event` with existing `Booking` records.
- **When** viewing the "Booking" tab in the `Event` admin.
- **Then** the bookings must be displayed in a read-only list using the `Booking.services.through` model.
- **And** the interface MUST NOT provide a button to add new bookings from this view.
- **And** each row must include a link/button to "Manage" the booking in its full edit form.
