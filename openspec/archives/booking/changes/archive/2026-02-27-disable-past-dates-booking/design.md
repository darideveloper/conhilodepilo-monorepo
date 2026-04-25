# Disable Past Dates Design

## Strategy
We will use the `disabled` prop of the `react-day-picker` (via our `Calendar` atom) to prevent selection of dates on or before today.

### Today's Definition
"Today" will be defined as the start of the current calendar day in the user's local timezone (00:00:00.000).

### Logic Adjustments
1. **Disabled Matcher**: The `Calendar` component's `disabled` prop will accept an array containing a function `(date) => date <= today` and the existing `availability.booked` array.
2. **Modifier Filtering**: To prevent past dates from showing green/amber highlights (which might happen if the `tours.json` contains past dates or if a recurring pattern is used), the `modifiers` logic will be updated to check `d > today`.
3. **Status Consistency**: The `getStatus` helper will also check if a date is in the future before returning a specific availability status.

## Alternative Considerations
- **Server-side check**: While this change is UI-only, any real backend implementation should also validate the date. For this prototype, the UI constraint is sufficient.
