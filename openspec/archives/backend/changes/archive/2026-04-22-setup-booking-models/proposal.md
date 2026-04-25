# Proposal: Setup Booking Models

## Why
The system needs to replicate the scheduling logic from a multi-tenant legacy project but optimized for a single company. This requires removing tenant-related models, moving sensitive configurations to environment variables, and implementing a flexible multi-service booking system.

## What Changes
- Implement the following model structure in the `booking` app:
    1.  **Company Identity:** Use a singleton `CompanyProfile` (via `django-solo`) for branding and UI settings.
    2.  **Service Catalog:** Define `EventType` and `Event` models to categorize and describe bookable services.
    3.  **Availability Logic:** Implement a tiered availability system (Company-level and Event-level) using abstract base classes for ranges, slots, and overrides.
    4.  **Multi-Service Bookings:** Update the `Booking` model to support multiple services in a single time block using a `ManyToManyField` with an optimized Admin UI.
    5.  **Environment-Driven Config:** Move all sensitive integration keys (Stripe, Google Calendar) and core identity (Company Name, Site URL) to `.env` variables.

## Scope
- Implementation of core models in `booking/models.py`.
- Migration of sensitive configurations to environment variables.
- Configuration of `django-solo` for company-wide settings.
- Custom Admin configuration for multi-service selection using `filter_horizontal`.
- Integration logic for total duration calculation in the `Booking` model.

## Success Criteria
- All models are registered and accessible in the Django Admin.
- A single `CompanyProfile` can be managed via the UI.
- Multiple services can be selected for a single booking, and the total duration is correctly calculated.
- Sensitive keys are successfully loaded from `.env` instead of the database.
- Database constraints (uniqueness, indexing) match the optimized single-tenant requirements.
