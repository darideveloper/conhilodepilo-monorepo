# Proposal: Unify Phone Configuration

## Why
The `landing` project currently has hardcoded phone numbers and WhatsApp links scattered across multiple components (`Footer.astro`, `WhatsAppButton.astro`, and `booking/[id].astro`). These numbers are inconsistent and do not match the source of truth managed in the dashboard `CompanyProfile`.

## What Changes
Refactor the landing project to fetch the company configuration from the `/api/config/` endpoint and use the `contact_phone` field for all phone-related UI elements. This ensures consistency and allows the company to update their contact information via the Django admin without code changes.

### Key Changes
1.  **API Integration:** Create a `getConfig` utility in `landing/src/lib/api/` to fetch the `CompanyProfile` data. This utility will implement a **module-level cache** to ensure only one API call is made per build/session, regardless of how many components request the data.
2.  **Dynamic UI:**
    *   Update `Footer.astro` to display the dynamic `contact_phone` and fix language inconsistencies (Spanish locale).
    *   Update `WhatsAppButton.astro` to use the dynamic phone for the `wa.me` link.
    *   Update the "Help" CTA in `booking/[id].astro` to use the dynamic phone.
3.  **Formatting & Robustness:** 
    *   Implement a utility to format raw phone numbers for display (e.g., `+34 ...`) and for WhatsApp links (stripping non-numeric characters).
    *   **Unified Fallbacks:** Create a `constants.ts` file to manage default contact information consistently across the app if the API is unavailable.
    *   **Testing:** Implement unit tests using Vitest to ensure formatting logic is accurate and regression-free.

## Impact
*   **Consistency:** All contact points will show the same number.
*   **Maintainability:** Contact info is managed in one place (dashboard).
*   **Accuracy:** Users will always reach the correct contact.
