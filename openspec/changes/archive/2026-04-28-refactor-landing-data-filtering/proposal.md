# Proposal: Refactor Landing Data Filtering to use Group ID

## Why
The landing page currently distinguishes between "Courses" and "Services" using hardcoded array indices from the API response (e.g., `categories[0]` for courses and `categories.slice(1)` for services). This approach is fragile and breaks if the category order changes or if new categories are added in the dashboard.

## What Changes

### landing-ui: update
Refactor the data fetching logic in the `landing` service to use the `group_id` field provided by the API. The specific IDs used for filtering will be configurable via environment variables to avoid hardcoding logic that depends on dashboard database IDs.

- Update `ServiceCategory` interface to include the `group_id` property.
- Add `PUBLIC_COURSES_GROUP_ID` and `PUBLIC_SERVICES_GROUP_ID` to `.env` files.
- **getCourses.ts**: Use `.find()` or `.filter()` based on `group_id === Number(import.meta.env.PUBLIC_COURSES_GROUP_ID)`.
- **getServices.ts**: Use `.filter()` to include categories matching `PUBLIC_SERVICES_GROUP_ID` or exclude those matching `PUBLIC_COURSES_GROUP_ID`.

## Architectural Reasoning
- **Robustness**: Using explicit identifiers is less prone to errors than relying on delivery order.
- **Alignment**: This aligns the landing page with the filtering logic already implemented or planned for the booking widget.
- **Dashboard-Driven**: Allows the dashboard to control what is considered a "Course" or a "Service" via the `EventTypeGroup` model.