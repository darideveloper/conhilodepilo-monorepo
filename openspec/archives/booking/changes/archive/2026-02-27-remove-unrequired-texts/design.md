# Design: Remove Unrequired UI Texts

## Components to Modify
- `src/components/organisms/BookingCalendar.tsx`
- `src/components/organisms/BookingForm.tsx`

## Changes in `BookingCalendar.tsx`
- Remove the `<CardHeader>` component entirely, including the step indicator, title, and description.
- Update the `<CardContent>` component by removing the `pt-0` class to allow for standard top padding, ensuring the layout remains balanced.
- Ensure the `<Card>` component maintains its structure with the remaining children.

## Changes in `BookingForm.tsx`
- Remove the `<div className="flex justify-between items-center mb-1">` block containing the "Paso 2 de 2" indicator within the `<CardHeader>`.
- Maintain the `<CardTitle>` and `<CardDescription>` to provide context for the form fields.

## Architectural Reasoning
These changes are purely visual and do not affect the functionality of the booking flow. By removing these texts, we create a more streamlined experience, especially for users who are already familiar with the flow or are accessing it through a tour-specific landing page where the context is already established.
