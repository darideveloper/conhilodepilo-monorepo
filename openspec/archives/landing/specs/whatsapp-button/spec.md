# whatsapp-button Specification

## Purpose
TBD - created by archiving change 2026-04-24-add-whatsapp-button. Update Purpose after archive.
## Requirements
### Requirement: Floating Contact Action
The application MUST display a floating button in the bottom-right corner of the viewport on all pages.

#### Scenario: User visits homepage
1. Given the user is on the home page.
2. When the page loads.
3. Then the user should see a WhatsApp button fixed in the bottom-right corner.

#### Scenario: User clicks WhatsApp button
1. Given the user sees the WhatsApp button.
2. When the user clicks the button.
3. Then the user should be redirected to the WhatsApp service in a new tab.

### Requirement: Accessible Contact Action
The floating button MUST be accessible and clearly indicate its purpose.

#### Scenario: Verify accessibility
1. Given the WhatsApp button is rendered.
2. Then it should have an `aria-label` describing its function (e.g., "Contactar por WhatsApp").
3. And it should open in a new tab (`target="_blank"`).

