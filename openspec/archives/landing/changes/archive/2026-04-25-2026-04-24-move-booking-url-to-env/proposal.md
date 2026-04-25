# Proposal: Move Booking URL to Environment Variable

## Why
The booking URL base was hardcoded, making it difficult to change across environments without code modifications.

## What Changes
- Moved `BOOKING_BASE_URL` to `PUBLIC_BOOKING_URL` in `.env`.
- Updated `src/pages/booking/[id].astro` to consume the environment variable.
- Preserved dynamic `?service={id}` query string construction.

## Summary
The booking URL base is currently hardcoded in `src/pages/booking/[id].astro`. This proposal moves the `BOOKING_BASE_URL` to an environment variable for better configuration management across different environments (dev, staging, production).

## Objectives
- Extract `BOOKING_BASE_URL` from the Astro file to `.env`.
- Update `src/pages/booking/[id].astro` to consume the environment variable.
- Ensure the dynamic query string parameter (`?service={id}`) is preserved.
