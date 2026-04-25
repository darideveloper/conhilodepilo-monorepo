# Design: Booking Page Architecture

## Overview
The booking page will be a server-rendered (or statically generated) Astro page that consumes the existing backend API.

## Data Flow
1. User navigates to `/booking/123`.
2. Astro `getStaticPaths` (or server-side logic) fetches all services and courses to validate the ID.
3. `getBookableItem(id)` helper is used to find the specific item.
4. The page renders with the item's data.

## Layout Structure
```html
<Layout>
  <main class="container py-24">
    <!-- Big Title -->
    <h1 class="text-display mb-12">Service Title</h1>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
      <!-- Left Column -->
      <div class="flex flex-col gap-8">
        <p class="text-body text-ui-text-muted">Description...</p>
        <img src="..." alt="..." class="rounded-2xl shadow-image" />
        <div class="flex gap-4">
          <!-- WhatsApp CTA -->
          <Button variant="primary" href="...">WhatsApp Reservas</Button>
        </div>
      </div>
      
      <!-- Right Column -->
      <div class="h-[600px] bg-white rounded-2xl shadow-card overflow-hidden">
        <iframe 
          src="https://iframedummy.com?pre-selected=123" 
          class="w-full h-full border-0"
        ></iframe>
      </div>
    </div>
  </main>
</Layout>
```

## API Extension
A new utility `src/lib/api/getBookableItem.ts` will be created:
```typescript
import { getServices } from "./getServices";
import { getCourses } from "./getCourses";

export async function getBookableItem(id: string | number) {
  const services = await getServices();
  const courses = await getCourses();
  
  const idNum = Number(id);
  const item = services.find(s => s.id === idNum) || courses.find(c => c.id === idNum);
  
  return item;
}
```

## Branding & Styling
- Use `--color-brand-primary` and `--color-brand-secondary` for accents.
- Use `text-display` utility for the main title.
- Use `container` utility for layout.
- Reuse `Button` atom for CTAs.
