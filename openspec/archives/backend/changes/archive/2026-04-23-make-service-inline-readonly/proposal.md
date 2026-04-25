# Proposal: Make Service Inline Read-Only

## Problem Statement
In the **Service Type** (`EventType`) admin view, the **Services** (`Event`) inline currently allows administrators to create, edit, and delete services directly. This can lead to accidental modifications and bypasses the specialized management interface available in the **Service** (`Event`) admin, which includes tabs for availability, overrides, and bookings.

## Proposed Solution
Modify the `EventInline` in `booking/admin.py` to be strictly read-only within the `EventTypeAdmin`. This ensures that service management is centralized in the `EventAdmin`, while still providing visibility of associated services when viewing a service type.

## Success Criteria
- The "Add another Service" button is hidden in the `EventType` admin.
- All fields in the service inline are non-editable (text only).
- The delete checkbox is removed from the inline rows.
- Existing "Manage" links (if any) or "Change" links remain functional to navigate to the full edit form.
