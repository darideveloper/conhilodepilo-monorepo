# Design: Booking Submission Logic

This specification details how the `BookingForm.tsx` component will interact with the external Stripe API.

## API Integration Architecture

The client-side React component `BookingForm.tsx` will perform an asynchronous `fetch` call to the Stripe-backed service endpoint.

### Required Environment Variables
The following `PUBLIC_` environment variables must be defined in Astro for client-side access:
- `PUBLIC_STRIPE_API_URL`: The base URL of the Stripe API.
- `PUBLIC_RETURN_URL`: Error/Back URL.
- `PUBLIC_SUCCESS_URL`: Success URL.
- `PUBLIC_STRIPE_USER`: API user identifier.
- `PUBLIC_STRIPE_IMAGE_URL`: Image URL for the product in the Stripe session.

### Payload Construction logic
The payload will be constructed by pulling data from the `useBookingStore`. 

```typescript
const payload = {
  url: import.meta.env.PUBLIC_RETURN_URL,
  url_success: import.meta.env.PUBLIC_SUCCESS_URL,
  user: import.meta.env.PUBLIC_STRIPE_USER,
  currency: "eur",
  products: {
    [selectedTour.title]: {
      description: `
        Nombre: ${formData.fullName}
        Email: ${formData.email}
        Tour: ${selectedTour.title}
        Fecha: ${selectedDate?.toLocaleDateString() || "No especificada"}
        Invitados: ${formData.guests}
        Peticiones: ${formData.specialRequests || "Ninguna"}
      `.trim(),
      image_url: import.meta.env.PUBLIC_STRIPE_IMAGE_URL,
      price: selectedTour.price,
      amount: 1
    }
  }
};
```

## Component State & UI Feedback

### Loading State
- Use `useState<boolean>(false)` to track the submission status.
- Disable the "Solicitar Reserva" and "Volver" buttons while `isLoading` is true.
- Show a loading spinner inside the submit button.

### Redirection & Success Handling
On a successful `200 OK` response, the API is expected to return a JSON object containing a `url` property. The client will then redirect the user using `window.location.href = data.url;`.

### Error Handling
If the fetch fails (e.g., non-200 response or network error), the `isLoading` state will be reset to `false`, and a basic `window.alert` will be used to notify the user.

## Implementation Details
- Component: `src/components/organisms/BookingForm.tsx`
- Form wrapper: Wrap the current layout in a `<form onSubmit={handleSubmit}>` tag.
- Tour Data: Import `tours.json` to look up the selected tour's price and title using `formData.tourId`.
