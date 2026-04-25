# Proposal: Remove Unrequired UI Texts

## Problem
The booking flow currently displays several redundant or unrequired texts that clutter the UI:
1. "Paso 1 de 2" / "Paso 2 de 2" (Stepper indicators)
2. "Selecciona tu Tour y Fecha" (Redundant title in BookingCalendar)
3. "Elige el tour que deseas realizar y busca un día disponible." (Redundant description in BookingCalendar)

These texts take up vertical space and don't add significant value to the user experience, especially in a compact or embedded context.

## Proposed Solution
- Remove the step indicators from both `BookingCalendar` and `BookingForm`.
- Remove the main `CardTitle` and `CardDescription` from `BookingCalendar`.
- Adjust padding/spacing if necessary to maintain a clean layout.

## Goals
- Simplify the UI.
- Reduce vertical space consumption.
- Remove redundant instructions.
