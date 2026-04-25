# Availability Data Mapping Design

## Data Translation Strategy

The high-level table provided by the user will be mapped to the `dates` object within `src/data/tours.json`.

### Date Ranges for March/April 2026

- **March 2026:**
  - **Standard Mon-Fri:** 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27.
  - **Weekends:** 1, 7, 8, 14, 15, 21, 22, 28. (Note: March 1st is a Sunday)
  - **Semana Santa (Mar):** 29 (Palm Sunday), 30, 31.
- **April 2026:**
  - **Easter Week (Semana Santa):** 1, 2, 3, 4, 5 (Easter Sunday).
  - **Weekends:** 11, 12, 18, 19, 25, 26.
  - **Standard Mon-Fri (Rest):** 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 20, 21, 22, 23, 24, 27, 28, 29, 30.

### Mapping Rule

- `Available` status will be mapped to the `available` array.
- `Limited` status will be mapped to the `limited` array.
- For "Available" Mon-Fri, all dates in that range will be added to `available`.
- For "Limited" Weekends, the specific weekend dates (7-8, 14-15, 21-22) will be added to `limited`.
- For "Limited" Semana Santa, the specific dates (Mar 29-31, Apr 1-5) will be added to `limited`.

### Tour-Specific Mapping Table (Detailed)

| Tour ID | Mar Mon-Fri | Mar Wknds | Mar SS | Apr Easter | Apr Wknds | Apr Mon-Fri |
| --- | --- | --- | --- | --- | --- | --- |
| alhambra-completa | Avail | Limited | Limited | Limited | Limited | Avail |
| alhambra-sin-tickets | Avail | Avail | Limited | Limited | Avail | Avail |
| palacios-nazaries | Limited | Limited | Limited | Limited | Limited | Limited |
| catedral-granada | Avail | Limited | Avail | Limited | Avail | Avail |
| capilla-real | Avail | Avail | Limited | Limited | Limited | Avail |
| monasterio-san-jeronimo | Avail | Avail | Avail | Avail | Avail | Avail |
| monasterio-cartuja | Avail | Avail | Avail | Avail | Avail | Avail |
| ruta-fray-leopoldo | Avail | Limited | Limited | Limited | Limited | Avail |
| ruta-gran-capitan | Avail | Avail | Avail | Avail | Avail | Avail |
| ruta-san-juan-de-dios | Avail | Avail | Avail | Avail | Avail | Avail |
| basilica-san-juan-de-dios | Avail | Limited | Limited | Limited | Avail | Avail |
| albaicin-misterios | Avail | Limited | Limited | Limited | Limited | Avail |
| sacromonte | Avail | Avail | Limited | Limited | Avail | Avail |
| centro-ciudad | Avail | Avail | Avail | Limited | Avail | Avail |

## Verification Plan

- After the update, the `src/data/tours.json` file will be validated for JSON syntax.
- The `BookingCalendar.tsx` component should correctly display these dates (can be verified visually or through component testing if available).
- Ensure no duplicate dates exist across `available`, `limited`, and `booked` arrays for a single tour.
