# admin-ui Specification

## Purpose
TBD - created by archiving change setup-initial-dashboard. Update Purpose after archive.
## Requirements
### Requirement: Modern Admin Interface
The project SHALL use `django-unfold` to provide a modern, Tailwind-based administrative interface with a functional sticky action bar.

#### Scenario: Branding Visibility on Subpages
- GIVEN the superuser is on a model list view (e.g., Bookings) or a change form.
- WHEN the page is rendered.
- THEN the sidebar MUST display the brand logo and site name.
- AND the `branding` template block MUST be explicitly defined in `base_site.html`.

### Requirement: Markdown Support in Admin
All text areas in the admin interface SHALL support Markdown editing via SimpleMDE. The editor MUST provide a theme-aware preview that adapts to the project's dynamic branding.

#### Scenario: Global Markdown Application
- **Given** any model with a `TextField` (rendered as a `textarea`) in the Django admin (e.g., `Event.description`).
- **When** the change form is rendered.
- **Then** the field MUST be automatically enhanced with a SimpleMDE editor.
- **And** no `textarea` fields SHALL be excluded by default.

#### Scenario: Styled and Theme-Aware Preview
- **Given** a user is viewing the Markdown preview for a field.
- **Then** the preview MUST render headings, lists, and blockquotes with distinct typography.
- **And** the preview MUST use the project's dynamic CSS variables (e.g., `--brand-primary-600`) for links and accents.
- **And** the styles MUST NOT leak into the surrounding admin interface.

### Requirement: Environment Badges
The admin interface SHALL display a badge indicating the current environment (Production, Development, etc.).

#### Scenario: Display Environment Badge
- Given `ENV=prod`.
- When accessing the admin.
- Then a "Production" badge is visible in the header.

### Requirement: Template-based CSS Variable Injection
The admin interface SHALL inject dynamic primary color shades into the document `:root` using a template override.

#### Scenario: Apply Dynamic Colors without Recursion
- GIVEN the `skeleton.html` override is active.
- WHEN the admin dashboard is loaded.
- THEN the template MUST NOT cause a recursion error during extension.
- AND the `--brand-primary-500` CSS variable MUST match the value provided by the `brand_theme_context`.

### Requirement: Admin Color Picker
The `brand_color` field in the `CompanyProfile` admin interface MUST be rendered using a visual color picker.

#### Scenario: Selecting a new brand color
- GIVEN the user is on the `CompanyProfile` change page in the admin
- AND the user is logged in as the development admin (`admin` / `admin`)
- WHEN the user clicks the `brand_color` input
- THEN a visual color picker MUST be displayed
- AND selecting a color MUST update the field value with a HEX code
- AND saving the profile MUST successfully update the `brand_color` and trigger the regeneration of the dashboard theme colors.

### Requirement: Color Restoration
After verification, the system MUST be restored to its original brand color to maintain design consistency.

#### Scenario: Restoring original color
- GIVEN the verification of the color picker is complete
- WHEN the `brand_color` is reset to `#ee5837`
- THEN the system MUST function exactly as it did prior to the change.

### Requirement: Color Math Preservation
The system MUST continue to derive a full color palette from the `brand_color`, even when it is provided in HEX format by the picker.

#### Scenario: Verifying derived shades
- GIVEN a `CompanyProfile` with `brand_color` set to `#682896`
- WHEN `get_brand_config()` is called
- THEN it MUST return a dictionary of 11 shades (50-950)
- AND the `500` shade MUST match `#682896`.

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
- **When** viewing the "Booking" tab in the `Event` admin.
- **Then** the bookings must be displayed in a read-only list using the `Booking.services.through` model.
- **And** the interface MUST NOT provide a button to add new bookings from this view.
- **And** each row must include a link/button to "Manage" the booking in its full edit form.

### Requirement: Read-Only Service Summary
The service type management interface SHALL show a non-editable summary of associated services.

#### Scenario: Read-only Services within Service Type Admin
- **Given** the `EventType` ModelAdmin.
- **When** viewing the "Services" tab.
- **Then** the list of services MUST be read-only.
- **And** the interface MUST NOT provide a button to add new services from this view.
- **And** the interface MUST NOT allow deleting services from this view.
- **And** each service MUST display its name, price, and duration as non-editable text.
- **And** each row MUST include a link/icon to navigate to the full service details.

### Requirement: Dynamic Admin Page Titles
The admin interface MUST consistently display the company name in the HTML `<title>` tag across all pages, incorporating specific page titles when available.

#### Scenario: Navigating to a Change List
- GIVEN a user is logged into the admin dashboard
- WHEN they navigate to the "Reservas" changelist
- THEN the browser tab title MUST show "Seleccione Reserva a cambiar | [Company Name]"
- AND the HTML `<title>` tag MUST NOT be empty.

#### Scenario: Fallback Site Title
- GIVEN an admin page that does not explicitly set a page-specific title
- WHEN the page is rendered
- THEN the browser tab title MUST show at least the site title from `CompanyProfile`.

