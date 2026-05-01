## Context
The application needs to support booking multiple services in a single transaction. Since the calendar only allows picking a single date for the entire booking, we need a robust approach to handle dates and payload submissions for multiple stacked services.

## Goals / Non-Goals
- **Goals**: Allow users to stack multiple services in Step 1; submit all services in one API call; persist the cart in local storage.
- **Non-Goals**: We are not allowing different dates for different services within the same booking (all stacked services will be booked for the single date selected in Step 2).

## Decisions
- **Decision: Intersection for Availability**
  We will calculate the available dates for the calendar based on the *intersection* of availability across all selected services. If Service A is only available on Mondays and Service B is only available on Tuesdays, selecting both will yield zero available dates.
  - *Alternatives considered*: Union (allowing booking if *any* service is available). This was rejected because users expect all stacked services to be provided on the date they choose.
- **Decision: Array Payload**
  The `BookingPayload` will switch from `serviceId: string | null` to `serviceIds: string[]`. This requires a dashboard update but is the cleanest way to represent a multi-service booking.

## Risks / Trade-offs
- **Zero Available Dates Risk** -> Users might select incompatible services and see an empty calendar. Mitigation: The UX should be clear, and potentially display a warning if intersection yields 0 days.
- **Dashboard Breaking Change** -> The Django dashboard will fail if it expects a single string and receives an array. Mitigation: Dashboard updates must be deployed simultaneously.

## Migration Plan
1. Update frontend state to support arrays, maintaining backward compatibility if possible during rehydration.
2. Update UI components.
3. Update API payload.
4. Update Django dashboard (requires coordination).

## Open Questions
- Should we actively warn users in Step 1 if the services they added have incompatible schedules before they proceed to Step 2?
