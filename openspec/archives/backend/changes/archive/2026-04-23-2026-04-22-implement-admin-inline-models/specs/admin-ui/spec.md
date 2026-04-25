# Capability: Admin UI

## ADDED Requirements

### Requirement: Tabbed Administrative Interface
The admin interface SHALL use a tabbed layout for complex models to reduce vertical scrolling and group related settings logically.

#### Scenario: Group Event Configuration in Tabs
- **Given** the `Event` ModelAdmin.
- **When** the admin page is rendered.
- **Then** fields and inlines must be organized into horizontal tabs.
- **And** the tabs must include: "General", "Date Ranges", "Business Hours", "Overrides", and "Bookings".

### Requirement: Weekday Slot Pre-population
Availability slot inlines SHALL automatically suggest all days of the week to ensure consistent schedule configuration.

#### Scenario: Auto-fill 7 Days on New Schedule
- **Given** an `Event` or `CompanyProfile` without existing `AvailabilitySlot` records.
- **When** a user views the inline formset for availability slots.
- **Then** the formset must be pre-populated with 7 rows, one for each day of the week (Monday-Sunday).

### Requirement: Read-Only Booking Summary
The service management interface SHALL show a non-editable summary of associated bookings.

#### Scenario: View Bookings within Event Admin
- **Given** an `Event` with existing `Booking` records.
- **When** viewing the "Bookings" tab in the `Event` admin.
- **Then** the bookings must be displayed in a read-only list using the `Booking.services.through` model.
- **And** each row must include a link/button to "Manage" the booking in its full edit form.
