# Proposal: Implement Admin Inline Models

## Problem
The current Django admin interface for the booking system requires users to navigate between multiple separate pages to configure a single service or global availability. This leads to "vertical fatigue" and a fragmented user experience. Additionally, global availability models (`CompanyAvailability`, `CompanyWeekdaySlot`, etc.) are not linked to the `CompanyProfile`, preventing them from being managed as inlines.

## Solution
Implement a centralized administrative interface using `django-unfold` inline patterns. This includes:
1.  **Refactoring Models**: Adding `ForeignKey` relationships to `CompanyProfile` for global availability models.
2.  **Tabbed Inlines**: Organizing `Event` and `CompanyProfile` configurations into logical horizontal tabs.
3.  **7-Day Pre-population**: Automatically creating 7 weekday rows for new availability slots.
4.  **Read-Only Summaries**: Adding a read-only booking list to the `Event` admin for quick status checks.
5.  **Sidebar Optimization**: Hiding secondary models from the main navigation to reduce clutter.

## Impact
- **Improved UX**: Users can configure services and company settings from a single view.
- **Data Integrity**: Enforces relationships between company settings and the singleton profile.
- **Clarity**: A cleaner sidebar makes the most important management tasks (Bookings, Services) more prominent.
