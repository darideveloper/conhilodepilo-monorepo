# Design: Cursor Pointer and Booking Redirect

## Cursor Pointer
We will add `cursor-pointer` to all `<button>` elements in `CategoryCard.tsx`. Although some browsers default buttons to pointers, explicit inclusion ensures consistency across all platforms.

## Booking Redirect Logic
A new page `src/pages/booking.astro` will be created. 
- **Server-side Logic:** The page will extract the `id` from `Astro.url.searchParams`.
- **Validation:** If `id` is null or empty, it will use `Astro.redirect('/')` to send the user back to the landing page.
- **Service Validation:** (Optional but recommended) It should check if the `id` corresponds to a valid service before proceeding.
