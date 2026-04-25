# Proposal: Add Dynamic Zoom Parameter to Booking Iframe

## Why
The booking iframe requires different zoom levels based on the user's viewport width to ensure optimal display across mobile, tablet/laptop, and desktop devices.

## What Changes
- Implement client-side logic to detect viewport width.
- Append a dynamic `zoom` query parameter to the iframe `src` URL.
- Logic:
  - Mobile (< 768px): `zoom=80`
  - Tablet/Laptop (768px - 1023px): `zoom=100`
  - Desktop (>= 1024px): `zoom=110`

## Summary
Currently, the iframe URL is constructed entirely on the server. To support responsive design for the third-party booking system, we will inject a `zoom` parameter on the client-side based on viewport dimensions.

## Objectives
- Add an identifier to the booking iframe in `src/pages/booking/[id].astro`.
- Create a client-side script to update the iframe URL upon page load.
- Ensure the initial load is performant and responsive to the user's device.
