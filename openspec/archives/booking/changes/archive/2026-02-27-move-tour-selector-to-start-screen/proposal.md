# Proposal: Move Tour Selector to Start Screen

## Problem
Currently, the tour selection is located on the second screen (Step 2: Personal Details), which causes a logical disconnect: the user picks a date on the calendar first without being clearly informed that availability is tour-specific, or they find out only after moving to the second screen.

## Proposed Solution
Move the **Tour Selection** dropdown from Step 2 to **Step 1 (Start Screen)**. This will allow the user to select their desired experience *before* picking a date, ensuring the calendar instantly reflects the correct availability for that specific tour.

## User-Visible Changes
- **Step 1 (Calendar Screen)**:
  - A new "Selecciona tu Tour" dropdown will appear at the top of the card.
  - The calendar will reactively update its availability markers as the user switches tours.
  - Initial tour pre-selection (from URL) will be handled here instead of the form.
- **Step 2 (Personal Details)**:
  - The "Tour" dropdown will be removed.
  - The "Número de personas" field will be repositioned to maintain a compact grid layout.

## Related Capabilities
- `booking-flow`: Centralizes the initialization and transition logic.
- `calendar`: Integrates the tour selection into the first interaction step.
- `booking-form`: Simplifies the form by removing the tour selection.
