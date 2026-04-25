# Design: Read-Only Service Inline

## Overview
The goal is to restrict the `EventInline` to a read-only state when displayed inside `EventTypeAdmin`.

## Implementation Strategy
We will follow the pattern established by `BookingInline` in `booking/admin.py` to ensure a consistent administrative experience.

### Key Components
1. **`readonly_fields`**: All fields displayed in the inline (`name`, `price`, `duration_minutes`) will be added to `readonly_fields`. This renders them as static text instead of editable inputs.
2. **`can_delete`**: Set to `False` to remove the deletion checkbox from each row.
3. **`has_add_permission`**: Overridden to return `False`, which hides the "Add another..." button.

## Architectural Reasoning
- **Centralized Management**: By making the inline read-only, we encourage users to use the `Event` admin for modifications. The `Event` admin is feature-rich, offering tabbed navigation for availability, overrides, and bookings, which are not suitable for a simple inline view.
- **Consistency**: This approach mirrors the `BookingInline` implementation, providing a predictable UX for administrators across different models.
- **Safety**: Prevents accidental data loss or corruption while viewing service categories.
