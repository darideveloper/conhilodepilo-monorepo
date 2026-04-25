# Proposal: Expose Tours API

Expose a public JSON API for tours data, sourced from an external project and mirrored locally for reliability and performance.

## Problem
The tour data is currently managed in an external project (`granada-go-custom-code`). This project (`granada-go-tours`) needs to serve this data via a public API endpoint to allow client-side components or third-party consumers to access it.

## Solution
1. Mirror the external `tours.json` into the local project at `src/data/tours.json`.
2. Implement an Astro API endpoint at `/api/tours.json` that serves this local data.
3. Ensure the local copy is easily updatable.

## Impact
- **New Capabilities**: Public GET endpoint for tour data.
- **Architectural Changes**: Introduction of a data mirroring pattern and an API route layer.
- **Dependencies**: Depends on the availability of `/mnt/hd/develop/vanilla/granada-go-custom-code/tours.json` during the initial setup/copy.
