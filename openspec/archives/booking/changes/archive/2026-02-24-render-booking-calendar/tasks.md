# Tasks: Render Booking Calendar

- [x] **Infrastructure Setup**
    - [x] Install dependencies: `npm install date-fns`.
    - [x] Install shadcn components: `npx -y shadcn@latest add calendar card badge`.

- [x] **Styling Configuration**
    - [x] Update `src/styles/global.css` with status color variables:
      ```css
      --color-status-available: #2E7D32;
      --color-status-limited: #D4A017;
      ```

- [x] **Component Implementation**
    - [x] Create `src/components/BookingCalendar.tsx` based on the provided base code.
    - [x] Refactor styles to use brand variables and the new status variables.
    - [x] Ensure the component uses `font-serif` for titles.

- [x] **Page Integration**
    - [x] Add `BookingCalendar` to `src/pages/index.astro`.
    - [x] Position it appropriately within the layout.

- [x] **Validation**
    - [x] Verify that selecting a date correctly displays its status.
    - [x] Confirm colors match the brand analysis and Mediterranean aesthetic.
    - [x] Run `openspec validate render-booking-calendar`.
