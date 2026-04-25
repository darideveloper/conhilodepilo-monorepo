# Tasks: Auto-select Tour by Route

## Implementation

- [x] Update `BookingForm.tsx` to handle `initialTourId` prop <!-- id: 0 -->
    - Add `initialTourId` to component props.
    - Use `useEffect` to call `updateFormData` if `initialTourId` is provided.
- [x] Create dynamic route `src/pages/[id].astro` <!-- id: 1 -->
    - Implement `getStaticPaths` using `src/data/tours.json`.
    - Render `Layout`, `BookingForm` (passing `id`), and `BookingCalendar`.
- [x] (Optional) Update `index.astro` to support query params <!-- id: 2 -->
    - Extract `tour` query param and pass it to `BookingForm`.

## Validation

- [x] Verify dynamic routing <!-- id: 3 -->
    - Navigate to `/alhambra-completa` and check if it loads.
    - Navigate to a non-existent tour and check if it 404s.
- [x] Verify auto-selection <!-- id: 4 -->
    - Visit `/alhambra-completa` and verify the "Tour" field is set to "Alhambra Completa".
    - Visit `/palacios-nazaries` and verify the "Tour" field is set to "Palacios Nazaríes".
- [x] Verify home page behavior <!-- id: 5 -->
    - Visit `/` and verify the "Tour" field is empty/default.
