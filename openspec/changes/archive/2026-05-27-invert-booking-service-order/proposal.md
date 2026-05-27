## Why

On Step 1 of the booking wizard (Service Selection), the selected-services cart appears below the service dropdowns. Users must scroll past the selection area to see what they've added, making the feedback loop sluggish. Inverting the visual order — cart above the dropdowns — lets users see their selections immediately, improving the UX without any behavioral changes.

## What Changes

- Visually reorder the **Stack/Cart Area** above the **Selection Area** on Step 1 of the booking flow
- Pure CSS change using `order` flexbox property — no DOM restructuring, no JS logic changes
- Tab order and accessibility remain unchanged

## Capabilities

### New Capabilities

None — this is a visual-only change within the existing booking UI.

### Modified Capabilities

None — no spec-level requirements are changing. This is purely an implementation/design change.

## Impact

- **Single file**: `booking/src/components/organisms/BookingServiceSelection.tsx`
- **3 CSS class additions**: `order-1`, `order-2`, `order-3` on the three flex children
- No API, dependency, or behavioral impact
