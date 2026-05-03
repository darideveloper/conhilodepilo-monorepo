# Proposal: Privacy Policy and Terms of Service (ES)

## Problem Statement
To integrate Stripe payments and comply with local regulations (GDPR/LOPD), the platform needs a Privacy Policy and Terms of Service in Spanish. These documents must be easily accessible to users, especially during the booking and payment process.

## Proposed Solution
- Add `terms_and_conditions_url` to the `CompanyProfile` model in the dashboard to manage it from the dashboard.
- Create a new Content Collection in the `landing` app using MDX for legal documents.
- Store content in `landing/src/content/legal/politica-de-privacidad.mdx` and `landing/src/content/legal/terminos-y-condiciones.mdx`.
- Implement a **dynamic route** at `landing/src/pages/legal/[slug].astro` to automatically render all documents in the `legal` collection.
- Update footer links and the booking form to use the new `/legal/[slug]` URLs.
- Ensure the booking form requires explicit acceptance of both documents.

## Goals
- Comply with Stripe's requirement for clear terms and privacy policy.
- Provide transparency to users about data handling.
- Define clear rules for bookings and cancellations.

## Impact
- **Landing App**: Two new routes and footer updates.
- **Booking App**: Footer updates and link in the booking form.
- **Legal**: Compliance with Spanish and EU data protection laws.
