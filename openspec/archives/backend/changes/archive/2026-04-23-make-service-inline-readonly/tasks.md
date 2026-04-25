# Tasks: Make Service Inline Read-Only

## Implementation

### Task: Update EventInline in booking/admin.py
- [x] Modify `EventInline` to set `readonly_fields` to include all displayed fields.
- [x] Set `can_delete = False` in `EventInline`.
- [x] Override `has_add_permission` to return `False` in `EventInline`.

## Validation

### Task: Manual Verification in Admin UI
- [ ] Log in to the admin dashboard.
- [ ] Navigate to "Service Types" (`EventType`).
- [ ] Select an existing service type.
- [ ] Click on the "Services" tab.
- [ ] Verify that no "Add another Service" button is present.
- [ ] Verify that fields (`name`, `price`, `duration_minutes`) are read-only.
- [ ] Verify that no delete checkboxes are present.
- [ ] Verify that the "View" or "Change" link (icon) is present to navigate to the `Event` admin.
