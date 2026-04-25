# Design: Availability System Migration

## Problem
The current availability system relies on static data embedded in the service files and complex client-side intersection logic. This is inflexible and prone to inconsistencies with real-time server-side availability.

## Solution
Transition to an asynchronous fetching strategy. 
1. **API First:** All availability decisions are delegated to a dedicated API endpoint (`/api/availability`).
2. **Asynchronous Store:** The `useBookingStore` will treat availability as a transient, fetchable state rather than a derived local state.
3. **Decoupling:** By removing `getIntersectedAvailability`, we decouple the booking UI from the underlying business rules (which now live on the server).

## Trade-offs
- **Complexity:** Moving to async fetching requires managing loading/error states in the UI.
- **Latency:** User might experience slight delays during service selection while availability is fetched. This will be mitigated by optimistic UI transitions if necessary in the future.
- **Network Dependency:** Offline usage (if relevant) will be impacted. Current requirements prioritize server consistency over offline availability.
