# Proposal: Render Booking Calendar

This proposal outlines the implementation of an interactive **Booking Calendar** component for **Granada Go Tours**, allowing users to visualize tour availability for specific dates.

## Why
A visual calendar improves the user experience by providing immediate feedback on available dates, reducing frustration and streamline the booking flow towards the contact form or WhatsApp.

## What Changes
- Install additional shadcn/ui components: `calendar`, `card`, `badge`.
- Install `date-fns` for robust date manipulation.
- Create `src/components/BookingCalendar.tsx`, a React component implementing the calendar with custom availability modifiers.
- Integrate the `BookingCalendar` into the home page or a dedicated booking section.
- Customize the calendar styles in `src/styles/global.css` to match the brand color palette (#A62C2B, #F9F7F2, #2D2D2D) and Mediterranean aesthetic.

## Goals
- Provide a clear, accessible visual representation of tour availability.
- Align the calendar styling with the "Authority, Tradition, and Elegance" brand personality.
- Ensure smooth interactive feedback when a date is selected.

## Scope
- UI Components: `Calendar`, `Card`, `Badge`, `BookingCalendar`.
- Styling: `src/styles/global.css` for custom status colors.
- Integration: Home page component update.

## Success Criteria
- The calendar renders correctly as an Astro island.
- Different statuses (Available, Limited, Full) are visually distinguishable using brand-appropriate colors.
- Selecting a date updates the status display area.
- `openspec validate` passes.
