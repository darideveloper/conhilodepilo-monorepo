# Design: Legal Documents Architecture

## Dashboard Configuration
To allow dynamic management of the legal document URLs, the `CompanyProfile` model will be extended:
- `terms_and_conditions_url`: A new `URLField` to store the link to the Terms of Service.
- Existing `privacy_policy_url` will be used for the Privacy Policy link.

## Content Management (MDX)
The legal documents will be managed using **Astro Content Collections** and **MDX**. This allows non-technical users (or AI) to easily update the legal text in a structured way without touching the page logic.

- **Storage**: `landing/src/content/legal/*.mdx`
- **Format**: MDX allows combining standard Markdown with React components if needed (e.g., for highlighted warnings or dynamic dates).
- **Collection Config**: A `legal` collection will be defined in `src/content/config.ts` with a Zod schema for metadata (title, last updated).

## Hosting & Rendering (Dynamic)
- **Dynamic Route**: `src/pages/legal/[slug].astro` will use Astro's `getStaticPaths` to generate a static page for every entry in the `legal` collection.
- **Benefits**: This ensures that any new document added to `src/content/legal/` is automatically available at `/legal/{filename}` without further code changes.
- **Rendering**: The dynamic page will fetch the collection entry, extract the title for SEO, and render the MDX body using the `<Content />` component.

## Structure
Both pages will use a shared `Layout` to maintain consistency with the rest of the site. The MDX content will follow standard Markdown headers for semantic structure.

## Content Strategy
- **Privacy Policy**: 
    - Owner: Con Hilo Depilo.
    - Data: Name, email, phone, appointment details.
    - Processors: Stripe (Payments), Google (Calendar).
    - Rights: ARCO (Access, Rectification, Cancellation, Opposition).
- **Terms of Service**:
    - Service: Beauty treatments.
    - Booking: Real-time confirmation or payment-first.
    - Cancellation: Specific rules (e.g., 24h notice).
    - Payments: Secure processing via Stripe.

## Integration in Booking Flow
The `booking` app's `BookingForm` will include a checkbox requiring acceptance of both the Privacy Policy and the Terms of Service.
- The label will dynamically link to the URLs provided by the dashboard config.
- Links will use `target="_blank"` to ensure the booking flow is not interrupted, especially when the app is embedded in an iframe.
