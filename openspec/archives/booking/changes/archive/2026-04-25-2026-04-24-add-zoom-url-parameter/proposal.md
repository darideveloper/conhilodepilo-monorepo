# Proposal: Add `zoom` URL Parameter

## Change ID
2026-04-24-add-zoom-url-parameter

## Why
The current booking interface has a hardcoded zoom level of 80% which lacks flexibility for different displays or user preferences.

## What Changes
Add support for a `zoom` URL query parameter to dynamically control the body scaling of the booking interface. This replaces the hardcoded `zoom` in `global.css` with a flexible, parameter-driven approach.

## Objectives
- Enable URL-based scaling for the booking application.
- Decouple scaling from the base stylesheet.
- Document the new capability.
