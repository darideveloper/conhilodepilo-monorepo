# Change: Add Image to EventType

## Why
Currently, administrators cannot associate images with event types, which limits the visual richness of the service catalog in client-facing interfaces.

## What Changes
- Add an optional `image` field to the `EventType` model.
- Update the Django Admin to include the `image` field in the `EventType` editor.
- Update the `booking-models` specification to reflect this new capability.

## Impact
- **Affected specs:** `booking-models`
- **Affected code:** `booking/models.py`, `booking/admin.py`, `booking/tests.py`
