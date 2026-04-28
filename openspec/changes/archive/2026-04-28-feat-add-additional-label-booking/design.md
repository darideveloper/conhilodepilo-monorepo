# Design: Conditional Label for Service Type

## Component: `BookingServiceSelection.tsx`

The label for the service type category is currently:
```tsx
<Label htmlFor="serviceTypeId" className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground">
  {config?.event_type_label || "Tipo de Servicio"}
</Label>
```

We will modify it to:
```tsx
<Label htmlFor="serviceTypeId" className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground">
  {config?.event_type_label || "Tipo de Servicio"}
  {formData.selectedServices.length > 0 && ` ${t.form?.additional || "(adicional)"}`}
</Label>
```

## Localization: `translations.ts`

We will add the `additional` key to the `form` object:

```ts
// es
form: {
  // ...
  additional: "(adicional)",
}

// en
form: {
  // ...
  additional: "(additional)",
}
```
