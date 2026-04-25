# Design: URL Parameter Handling and Internal Naming Standardization

## Problem
The language and theme selectors are currently always visible, and the internal naming `tourId` doesn't fully align with the more general "service" concept when dealing with URL parameters like `?service=ID`.

## Solution Architecture

### 1. Store Updates (`useBookingStore.ts`)
- **Rename `tourId` to `serviceId`** in the `formData` object and associated logic.
- Add `theme: 'light' | 'dark'` to the store for state synchronization.
- Add `visibility: { lang: boolean, theme: boolean, service: boolean }` to the store.
- Add `serviceGroup: string | null` to the store state.

### 2. URL Processing (`BookingFlow.tsx`)
- In the `useEffect` of `BookingFlow`, we will use `URLSearchParams` to:
  - Check for `lang`, `theme`, `service` (mapped internally to `serviceId`), and `service_group`.
  - Set the store values if found.
  - Set visibility flags to `false` if `lang`, `theme`, or `service` are provided.

### 3. Codebase-wide Refactor
- Search and replace all instances of `tourId` with `serviceId`.
- Update components, stores, and any other logic where `tourId` is referenced.

### 4. Documentation (`docs/url-variables.md`)
- Create a markdown file documenting:
  - `lang`: Values (`es`, `en`).
  - `theme`: Values (`light`, `dark`).
  - `service`: Service IDs.
  - `service_group`: Optional group identifier.

## Considerations
- **Internal Naming consistency**: Transitioning to `serviceId` internally makes it clearer when interacting with the `?service=` URL parameter.
- **Backwards Compatibility**: Ensure that the `tour` URL parameter (if it was used before) can still be handled or is clearly replaced by `service`.
- **Persistence**: Visibility flags should not be persisted.
