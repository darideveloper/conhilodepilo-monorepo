# Design: Categorized Service Selection

The service selection process requires restructuring the data and introducing a new dedicated screen at the beginning of the booking flow.

## Data Structure Refactor

The current flat list in `src/data/booking.json` will be refactored into a categorized structure. Each "Service Type" (category) will contain its own list of services.

```json
[
  {
    "id": "tours",
    "name": { "es": "Tours", "en": "Tours" },
    "services": [
      { "id": "tour-1", "title": { "es": "Tour 1", "en": "Tour 1" }, ... },
      { "id": "tour-2", "title": { "es": "Tour 2", "en": "Tour 2" }, ... }
    ]
  },
  {
    "id": "events",
    "name": { "es": "Eventos", "en": "Events" },
    "services": [
      { "id": "event-1", "title": { "es": "Evento 1", "en": "Event 1" }, ... }
    ]
  }
]
```

## State Management (`useBookingStore.ts`)

The `formData` in `useBookingStore.ts` will be updated to include `serviceTypeId`.

```typescript
formData: {
  serviceId: string | null;
  serviceTypeId: string | null;
  ...
}
```

The availability lookup logic (`getInitialAvailability`) must be updated to search for the service within the new nested structure.

## New Flow Architecture (3 Steps)

The flow will be expanded from 2 steps to 3 steps in `BookingFlow.tsx`.

1.  **Step 1: `BookingServiceSelection.tsx` (NEW)**
    *   Replaces the service selection dropdown previously inside the Calendar.
    *   Features two dependent `<Select>` components: Category Select and Service Select.
    *   Uses API labels (`event_type_label` and `event_label`) for the dropdowns.
    *   Has a "Continue" button that unlocks only when both are selected.
2.  **Step 2: `BookingCalendar.tsx` (MODIFIED)**
    *   The service selection dropdown is removed.
    *   Now solely focused on date selection.
3.  **Step 3: `BookingForm.tsx` (MODIFIED)**
    *   Updates logic to lookup the selected service from the nested `booking.json` structure for the summary display.

## Routing (`[id].astro`)

`getStaticPaths` will now `flatMap` all categories' services to generate the correct paths for each service.

## Legacy API Removal

The existing API endpoint at `src/pages/api/tours.ts` was previously used by the now-removed WordPress integration scripts. This file will be deleted. All internal dependencies on `tours.json` will be updated to import `booking.json` directly.