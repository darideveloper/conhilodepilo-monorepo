## Why

The current Booking list view shows columns that are not optimized for daily admin operations. Admins need to quickly see the booked services and total price at a glance, and the date-oriented columns should use Spanish labels for a local admin audience.

## What Changes

- Replace the current `list_display` columns (`client_name`, `start_time`, `end_time`, `status`, `google_sync_status_badge`) with new columns: `client_name`, `status`, `services` (comma-separated service names), `price` (total from services), `created_at`, `start_time`
- Remove `end_time` and `google_sync_status_badge` from the list view
- Add `price` as a computed column (sum of all related service prices)
- Add `services` as a computed column (comma-separated names of related services)
- Add a custom admin method for `created_at` with `verbose_name` set to "Fecha de compra"
- All column headers in Spanish: "Cliente", "Estado", "Servicios", "Precio", "Fecha de compra", "Fecha del servicio"

## Capabilities

### New Capabilities
- `booking-admin-list-view`: Django admin list view configuration for Booking model - defines visible columns, their computed values, and Spanish labels.

### Modified Capabilities
None. No existing spec-level behavior is changing.

## Impact

- **Affected file**: `dashboard/booking/admin.py` - `BookingAdmin` class
- No model changes required
- No database migrations needed
- No API or public UI changes
