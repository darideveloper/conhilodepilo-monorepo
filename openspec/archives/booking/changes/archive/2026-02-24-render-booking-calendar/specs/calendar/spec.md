# Spec: Booking Calendar

This spec defines the requirements for the interactive **Booking Calendar** component.

## ADDED Requirements

### Requirement: Visual Status Representation
The calendar SHALL visually distinguish between dates based on their availability status using brand-aligned colors.

#### Scenario: Verify Availability Coloring
- Given a `bookingData` object with different statuses.
- When the calendar is rendered.
- Then "Available" dates MUST show green accents, "Limited" MUST show gold accents, and "Full" MUST show red accents.

### Requirement: Interactive Date Selection
The component SHALL allow users to select a single date and display its detailed status.

#### Scenario: Update Status on Selection
- Given the Booking Calendar is displayed.
- When a user clicks on an "Available" date.
- Then the status display area MUST update to show "Available" and include the correct icon (CheckCircle2).

### Requirement: Data Structure Compatibility
The component SHALL consume a standardized availability data structure.

#### Scenario: Mock Data Integration
- Given the component uses a `bookingData` structure with `fullyBooked`, `limitedAvailability`, and `available` arrays of `Date` objects.
- When the component is initialized.
- Then all specified dates MUST be correctly mapped to their respective modifiers.
