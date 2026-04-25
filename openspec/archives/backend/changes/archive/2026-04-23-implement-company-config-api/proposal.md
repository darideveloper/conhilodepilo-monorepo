# Proposal: Implement Company Configuration API

This proposal outlines the implementation of a public API endpoint to expose company branding and configuration settings. This endpoint is essential for front-end applications to dynamically adapt their UI based on the company's profile.

## Problem Statement
The current system stores company configuration (branding, contact info, labels) in a `CompanyProfile` singleton model, but this data is only accessible via the Django Admin. Front-end integrations (like the booking widget or landing page) need a public, standardized way to fetch these settings.

## Proposed Solution
- Implement a `GET /api/config/` endpoint using Django REST Framework.
- Expand the `CompanyProfile` model to include configurable UI labels.
- Create a serializer to transform the singleton data into the format expected by the frontend.
- Ensure the endpoint is public and includes necessary CORS headers (already configured in the project).

## Impact
- **Public API:** New `GET /api/config/` endpoint.
- **Models:** `CompanyProfile` will have new fields for UI labels.
- **Admin:** The Unfold dashboard will show new fields for customizing labels.
