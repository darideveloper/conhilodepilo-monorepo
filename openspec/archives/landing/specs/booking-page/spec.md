# booking-page Specification

## Purpose
TBD - created by archiving change add-booking-page. Update Purpose after archive.
## Requirements
### Requirement: Dynamic Booking Page
The system SHALL provide a dedicated page for service/course booking with dynamic content.

#### Scenario: Navigating to a service booking page
- **Given** a service ID "42" exists in the dashboard
- **When** I navigate to `/booking/42`
- **Then** I should see the service title "Service Name" as a big heading
- **And** I should see the service description on the left
- **And** I should see the service image (if provided) under the description
- **And** I should see a WhatsApp CTA button
- **And** I should see an iframe on the right pointing to `https://iframedummy.com?pre-selected=42`

#### Scenario: Navigating to a non-existent ID
- **Given** no service or course exists with ID "999"
- **When** I navigate to `/booking/999`
- **Then** I should be redirected to a 404 page or see a "Not Found" message

### Requirement: Unified Data Fetching
The API layer SHALL implement a utility to fetch both services and courses by a common ID.

#### Scenario: Fetching item by ID
- **Given** ID "10" belongs to a course
- **When** I call `getBookableItem(10)`
- **Then** It should return the course data
- **Given** ID "20" belongs to a service
- **When** I call `getBookableItem(20)`
- **Then** It should return the service data

