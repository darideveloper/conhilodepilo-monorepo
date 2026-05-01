# Design: Integrate Services API

## Architectural Shift
Moving from `src/data/booking.json` to a dynamic dashboard API (`/api/services/`) introduces architectural challenges regarding state initialization, data availability, and data typing.

### Synchronous vs Asynchronous
- **Current State:** The application expects `booking.json` to be available immediately upon application load. Functions like `getInitialAvailability` within `useBookingStore.ts` execute synchronously.
- **Proposed State:** Services will be fetched asynchronously on application mount via `fetchServices()`. 
- **Decision:** We will migrate the `services` data directly into the global `useBookingStore` Zustand state. This allows components to dynamically react when the services load, decoupling the UI from static imports and allowing easy loading-state implementations.

### Data Mapping & UI Compatibility
- **Problem:** The new `/api/services/` endpoint schema differs from the mock data in two critical ways:
  1. It does not include a `dates` object (with `limited` and `booked` arrays), which the calendar relies upon.
  2. It returns IDs as `number` values, whereas the UI components and Zustand store strictly use `string` values for form selection (`s.id === serviceId`).
- **Decision:** The API mapping layer inside `src/lib/api/endpoints/services.ts` will aggressively enforce schema resilience to prevent UI refactoring:
  - If `dates` is undefined, the mapping layer will inject a fallback `{ limited: [], booked: [] }`.
  - All category and service `id` fields will be explicitly coerced to strings (`String(id)`). This eliminates the need to recursively update types and strict equality checks across all React components.

### I18n Compatibility
- **Observation:** The dashboard returns flat strings for `name` and `title`, whereas the UI mock data used localized objects (e.g., `{ es: "...", en: "..." }`).
- **Decision:** No action required. The UI codebase already safely handles this via fallbacks (`typeof category.name === 'string' ? category.name : ...`), meaning the dashboard strings will naturally and safely replace the localized mock objects without any component changes.
