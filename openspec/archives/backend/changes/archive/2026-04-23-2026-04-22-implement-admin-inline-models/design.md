# Design: Admin Inline Patterns and Model Linking

## Architectural Overview
This change transitions the admin interface from a flat, model-per-page structure to a hierarchical, hub-based structure.

### 1. Model Linking (The "Company Hub")
Currently, `CompanyAvailability`, `CompanyWeekdaySlot`, and `CompanyDateOverride` are standalone models. To implement the "Global Configuration Hub" pattern described in `docs/inline-models.md`, these models will be updated with a `ForeignKey` to `CompanyProfile`.

- **Requirement**: `CompanyWeekdaySlot` MUST use `related_name="weekday_slots"` to ensure compatibility with the 7-day pre-population logic.
- **Base Models**: Add `__str__` methods to `BaseAvailabilityRange`, `BaseAvailabilitySlot`, and `BaseDateOverride` to ensure meaningful labels in the tabbed interface.

### 2. Tabbed Layout Pattern
We will use Unfold's `tab = True` on Inline classes and the `tabs` attribute on `ModelAdmin`.
- **Event Admin**: [General, Date Ranges, Weekday Slots, Overrides, Bookings]
- **Company Profile Admin**: [General, Global Availability, Business Hours, Holidays]

### 3. Smart Formsets (7-Day Pattern)
To reduce manual entry, the `AvailabilitySlotInline` (both for Events and Company) will override `get_formset` to provide initial data for all 7 days of the week (Monday-Sunday) when no slots exist. The implementation must use the `weekday_slots` related name.

### 4. Read-Only Booking Summary
The `Event` admin will include a `BookingInline`. 
- **M2M Logic**: Since `Booking` relates to `Event` via a `ManyToManyField`, the inline MUST use `model = Booking.services.through`.
- **Fields**: Read-only fields (client name, status, etc.) must be implemented as methods on the inline class that retrieve data from the associated `booking` instance.
- **Actions**: Include a custom `manage_booking` method that renders a "Manage" button linking to the full Booking change form.

### 5. Sidebar Navigation
The `UNFOLD["SIDEBAR"]` in `settings.py` will be streamlined. Specifically, the "Disponibilidad" link will be removed, as global availability is now managed within the "Perfil de Empresa" (Company Profile) hub.
