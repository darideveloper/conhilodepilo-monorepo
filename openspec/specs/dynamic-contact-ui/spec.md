# dynamic-contact-ui Specification

## Purpose
TBD - created by archiving change unify-phone-configuration. Update Purpose after archive.
## Requirements
### Requirement: Dynamic Footer Contact Info
The `Footer` component MUST display contact information fetched from the configuration API.

#### Scenario: Footer renders dynamic contact details
1.  **Given** the configuration API returns phone `4493402622` and email `Test@test.test`.
2.  **When** the Footer component is rendered.
3.  **Then** it should show the formatted phone number and the correct email address.

### Requirement: Dynamic WhatsApp Links
All WhatsApp buttons and links MUST point to the phone number defined in the configuration API.

#### Scenario: WhatsApp floating button uses dynamic phone
1.  **Given** the configuration API returns phone `4493402622`.
2.  **When** the user clicks the floating WhatsApp button.
3.  **Then** they should be redirected to `https://wa.me/4493402622`.

#### Scenario: Booking detail page WhatsApp CTA uses dynamic phone
1.  **Given** the configuration API returns phone `4493402622`.
2.  **When** the user views a service detail page and clicks the WhatsApp help button.
3.  **Then** they should be redirected to `https://wa.me/4493402622`.

