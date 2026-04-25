# Design: Setup Booking Models

This document outlines the architectural decisions for the single-company scheduling system.

## Architectural Patterns

### 1. Singleton Company Configuration
We use `django-solo` for the `CompanyProfile` model. This ensures that only one record exists in the database, simplifying access throughout the application (e.g., `CompanyProfile.get_solo()`). 

### 2. Tiered Availability System
The availability logic follows a hierarchical override pattern:
- **Global Level:** `CompanyAvailability`, `CompanyWeekdaySlot`, `CompanyDateOverride`.
- **Service Level:** `EventAvailability`, `AvailabilitySlot`, `EventDateOverride`.

**Constraints:** All slot models will use `unique_together = ('day', 'start_time', 'end_time')` (or equivalent) to prevent overlapping configuration at the same level.

### 3. Multi-Service Scheduling (Many-to-Many)
To support scheduling multiple services in a single block:
- **Model:** `Booking` contains a `ManyToManyField` to `Event`.
- **Total Duration Calculation:** Since M2M relationships are saved after the model instance in the Django Admin, we will use a **`m2m_changed` signal** on the `Booking.services` field. This signal will trigger a recalculation of `end_time` whenever services are modified.
- **Admin UI:** We utilize `unfold.admin.ModelAdmin` with `filter_horizontal = ('services',)` and organized `fieldsets` for a premium user experience.

### 4. Environment-Driven Settings
All sensitive data and fixed company metadata are moved to `.env`.

| Key | Usage |
| :--- | :--- |
| `COMPANY_NAME` | Global display name for emails and titles. |
| `SITE_URL` | Base URL for absolute links (invites, webhooks). |
| `STRIPE_SECRET_KEY` | Payment processing. |
| `GOOGLE_CALENDAR_ID` | Integration with Google Calendar. |
| `TIME_ZONE` | Default timezone for the application (Europe/Madrid). |

## Database Optimizations
- **Indexing:** `Booking.start_time` and `Booking.status` will have `db_index=True`.
- **Integrity:** `Event.duration` will be a `PositiveIntegerField` to ensure valid math for total duration.
