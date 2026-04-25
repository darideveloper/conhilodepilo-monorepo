# Proposal: Reorder and Translate Event Admin Tabs

## Problem
The `Event` (Service) admin interface currently has tabs in a suboptimal order for the user workflow. Additionally, some tab labels are not translated to Spanish or use inconsistent terminology. The "Bookings" tab also allows adding new bookings, which should be restricted to a read-only summary in this context.

## Proposed Solution
- Reorder the tabs in `EventAdmin` to follow the requested sequence: General, Service Week Slots, Service Availability, Service Date Overrides, and Booking.
- Update the labels to be more descriptive and ensure they are properly translated to Spanish in the `.po` files.
- Restrict the `BookingInline` to be read-only by removing the "Add" button (disabling add permission).

## Impact
- **Admin UI:** Improved user experience with a more logical flow of configuration.
- **I18n:** Complete translation of the Service administration interface.
- **Security/Data Integrity:** Prevents accidental creation of bookings directly from the Service detail page, enforcing management through the dedicated Booking module.
