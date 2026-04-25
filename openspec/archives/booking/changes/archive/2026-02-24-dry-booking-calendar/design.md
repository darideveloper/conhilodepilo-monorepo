# Design: DRY Refactor for BookingCalendar

## Architectural Reasoning
The refactor adopts a **Configuration-Driven UI** pattern. By mapping semantic states ("Full", "Limited", "Available") to a rich configuration object, we decouple the *business logic* (availability state) from the *presentation logic* (icons, colors, Tailwind classes).

### Centralized Status Configuration
A `STATUS_CONFIG` object will hold:
- Display labels.
- Icon components.
- Tailwind class mappings for containers, badges, legend items, and **calendar modifiers**.

This allows the UI to be rendered via simple iterations or lookup operations, eliminating deeply nested ternary chains and unifying the styling logic for both the calendar and the status details.

### Data Structure Refinement
To align with the Unified Status Keys, `bookingData` will be refactored to use the same keys:
- `booked` (previously `fullyBooked`)
- `limited` (previously `limitedAvailability`)
- `available` (stays the same)

This ensures a direct 1-to-1 mapping between the data keys, the calendar modifiers, and the configuration object.

### Component Decomposition
To improve readability, the `BookingCalendar` will be decomposed:
1.  **`BookingCalendar` (Container)**: Manages state (`date`) and core configuration.
2.  **`StatusLegend`**: Pure presentation component iterating over the config.
3.  **`StatusDetails`**: Pure presentation component accepting the current status data.
4.  **`DateDisplay`**: A small helper for formatting the selected date correctly.

### Logic Optimization
The `getStatus` function will be refactored to use the Unified Status Keys and a more efficient lookup mechanism.

## Implementation Details

### Configuration Object Schema
```typescript
type StatusKey = 'booked' | 'limited' | 'available' | 'standard';

type StatusConfigValue = {
  label: string;
  icon: React.ElementType;
  classes: {
    container: string;
    badge: string;
    icon: string;
    modifier?: string; // Tailwind class for react-day-picker modifier
    legendMarker: string;
  }
};

type StatusConfig = Record<StatusKey, StatusConfigValue>;
```

### Dynamic Rendering
The Legend will use `Object.entries(STATUS_CONFIG).map(...)` to ensure consistency. The Details section will use `STATUS_CONFIG[status]` to retrieve all necessary visual assets in a single lookup.

## Trade-offs
- **Abstration Overhead**: Introducing sub-components and a config object adds a slight layer of abstraction. However, this is outweighed by the massive reduction in repetitive JSX and easier maintenance.
- **File Structure**: For now, sub-components will remain in the same file to keep the change focused, but they are designed to be easily moved to separate files if needed.
