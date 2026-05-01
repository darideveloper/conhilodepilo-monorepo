# Design: Booking Calendar Component

## Architectural Reasoning
The **Booking Calendar** is an interactive React component rendered as an **Astro Island** (`client:load`). This allows for dynamic client-side state management (date selection, status updates) while keeping the rest of the site static.

### Availability Modifiers
We will use `react-day-picker` modifiers to apply specific styles to dates based on their availability status:
- **Available**: High availability. Deep Green accents.
- **Limited**: Low availability. Ochre/Gold accents (complementary to the Mediterranean palette).
- **Full**: No availability. Pomegranate Red (#A62C2B) accents with reduced opacity or strikethrough.

### Brand Alignment
- **Typography**: Headings will use `font-serif` (Playfair Display) to maintain authority and elegance.
- **Colors**:
    - Primary accent: `--color-brand-red` (#A62C2B).
    - Background: `--color-brand-cream` (#F9F7F2).
    - Text: `--color-brand-charcoal` (#2D2D2D).
- **UI Components**: shadcn/ui `Card` for the container and `Badge` for status labeling.

## Implementation Details

### Data Structure
The component will accept a `bookingData` object (initially mocked, but designed to be easily linked to a future API):
```typescript
const bookingData = {
  fullyBooked: Date[],
  limitedAvailability: Date[],
  available: Date[]
};
```

### CSS Variables for Statuses
New theme variables will be added to `src/styles/global.css` to handle status colors consistently:
- `--color-status-available`: `#2E7D32` (Mediterranean Olive/Green)
- `--color-status-limited`: `#D4A017` (Ochre/Gold)
- `--color-status-full`: `var(--color-brand-red)`

### Accessibility
- Use `aria-label` for status descriptions.
- Ensure keyboard navigation support (native to `react-day-picker`).
- High contrast for readability.

## Trade-offs
- **Mocked Data**: The current proposal uses mock data for availability. This simplifies the initial UI implementation but will require integration with a dashboard or static data source later.
- **Client-side Rendering**: Using a React island increases the JS bundle size slightly for this component, but is necessary for the interactivity required by a calendar.
