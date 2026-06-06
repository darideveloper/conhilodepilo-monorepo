## Context

The Booking model's Django admin list view currently shows: `client_name`, `start_time`, `end_time`, `status`, `google_sync_status_badge`. The admin team needs a more operationally useful view with services, total price, and Spanish column labels. No model changes are required — this is purely an admin configuration change.

## Goals / Non-Goals

**Goals:**
- Replace list_display columns with: `client_name`, `status`, `services`, `price`, `created_at`, `start_time`
- Show services as a comma-separated string of service names
- Show price as the sum of all related service prices
- Show `created_at` with the label "Fecha de compra"
- Show `start_time` with the label "Fecha del servicio"
- All column headers in Spanish: "Cliente", "Estado", "Servicios", "Precio", "Fecha de compra", "Fecha del servicio"
- Remove `end_time` and `google_sync_status_badge` from list view

**Non-Goals:**
- No model schema changes
- No database migrations
- No API or public-facing UI changes
- No changes to detail form view (fieldsets, tabs)
- No changes to inline admin classes
- No changes to list filtering or search

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Column computation approach | `@admin.display` methods on `BookingAdmin` | Existing pattern already used for `google_sync_status_badge`; no need for custom list display classes |
| Price computation | Sum of `service.price` on `booking.services.all()` via `annotate` or Python | Simple N+1 is acceptable for admin list (typically small result sets); can optimize with `prefetch_related` later if needed |
| Services string | `", ".join(...)` on `booking.services.all()` | Simplest approach; consistent with Django admin conventions |
| Spanish labels | `@admin.display(description=...)` decorator | Standard Django approach; no i18n machinery change needed |

## Risks / Trade-offs

- **[Performance]** Computed `services` and `price` fields cause N+1 queries if not optimized → Mitigation: Add `prefetch_related("services")` via `get_queryset()` override if list page is slow
- **[Sorting]** Computed columns (`services`, `price`) are not sortable by default → Acceptable trade-off: admin can sort by `start_time` or `created_at` which are real DB fields
