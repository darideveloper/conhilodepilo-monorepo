# Tasks: Refine Calendar Availability Colors

## 1. Research and Alignment
- [x] Confirm the exact hex codes for brand red (primary) to avoid clashes with amber. <!-- id: task-confirm-hex -->
- [x] Verify `shadcn/ui` calendar default hover behaviors. <!-- id: task-verify-hover -->

## 2. Implementation
- [x] Update `available` status in `src/components/organisms/types.ts` to `emerald-500`. <!-- id: task-update-available -->
- [x] Update `limited` status in `src/components/organisms/types.ts` to `amber-500`. <!-- id: task-update-limited -->
- [x] Update `booked` status in `src/components/organisms/types.ts` to `slate-100` / `line-through`. <!-- id: task-update-booked -->
- [x] Ensure hover states (`hover:bg-emerald-600` etc.) are added to the `modifier` classes. <!-- id: task-add-hovers -->

## 3. Validation
- [x] Verify visual alignment in the `BookingCalendar` component. <!-- id: task-verify-calendar-ui -->
- [x] Ensure the `StatusLegend` reflects the new colors. <!-- id: task-verify-legend -->
- [x] Confirm no regressions in the `BookingForm` transition. <!-- id: task-verify-form-transition -->
