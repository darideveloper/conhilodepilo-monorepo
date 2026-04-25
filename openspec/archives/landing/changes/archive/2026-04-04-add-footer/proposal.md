# Change: Add Footer Component

## Why
The website currently lacks a unified footer. Based on the reference design, a comprehensive footer is necessary for providing essential brand information, location details, direct booking links (WhatsApp), and copyright notices across all pages.

## What Changes
- Create a new comprehensive footer component adapted to our design system.
- Implement three column layout containing:
  - Brand identity: Logo, description, and social media links.
  - Location: Address and a map image snippet.
  - Direct Contact: Working hours and a WhatsApp reservation button.
- Bottom bar for copyright and legal links.
- Add the footer to the main application page or layout.

## Impact
- Affected specs: `footer` (new capability)
- Affected code: `src/components/Footer.astro`, target pages like `src/pages/index.astro`
