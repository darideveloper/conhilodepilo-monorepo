# booking-models Specification Delta

## ADDED Requirements

### Requirement: Service Visualization
The `EventType` model MUST support an optional image for visual categorization in the service catalog.

#### Scenario: Adding an Image to Event Type
- GIVEN the Event Type admin interface
- WHEN an administrator uploads an image for the "General Consultation" event type
- THEN the system MUST store the image and associate it with that event type.
- AND the image MUST be optional.
