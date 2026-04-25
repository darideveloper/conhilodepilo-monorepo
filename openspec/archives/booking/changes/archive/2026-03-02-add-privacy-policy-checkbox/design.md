# Design: Privacy Policy Checkbox Implementation

## Goals
Implement a required privacy policy consent field in the booking flow.

## Implementation Details

### State Management
Modify `src/store/useBookingStore.ts` to include `privacyAccepted: boolean` in the `formData` object. Initial value will be `false`.

```typescript
// useBookingStore.ts
formData: {
  // ... existing fields
  privacyAccepted: boolean;
}
```

### UI Component
The `BookingForm` will use a standard HTML checkbox input for simplicity, or a custom component if preferred. We'll use Tailwind classes to ensure it matches the brand aesthetic.

```jsx
<div className="flex items-start space-x-2 pt-2">
  <input
    type="checkbox"
    id="privacyAccepted"
    name="privacyAccepted"
    checked={formData.privacyAccepted}
    onChange={handleCheckboxChange}
    className="h-4 w-4 rounded border-gray-300 text-brand-red focus:ring-brand-red"
    required
  />
  <Label htmlFor="privacyAccepted" className="text-xs leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
    He leído y acepto la <a href="https://granadago.com/privacidad/" target="_blank" rel="noopener noreferrer" className="text-brand-red underline">política de privacidad</a>.
  </Label>
</div>
```

### Validation
Update `handleSubmit` to check `formData.privacyAccepted` even if the browser `required` attribute is present, to ensure robust validation.

```typescript
const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();
  if (!formData.privacyAccepted) {
    alert("Debes aceptar la política de privacidad para continuar.");
    return;
  }
  // ... existing logic
}
```

## Sequencing
1. Update store.
2. Update `BookingForm`.
3. Test locally.
