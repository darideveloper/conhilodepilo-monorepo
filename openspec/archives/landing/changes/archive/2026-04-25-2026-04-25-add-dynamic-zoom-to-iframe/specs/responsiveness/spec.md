# Responsiveness Specification

## ADDED Requirements
### Requirement: Dynamic Iframe Zoom Logic
- The system MUST adjust the iframe URL zoom parameter dynamically based on the client viewport width.
#### Scenario: Mobile Viewport
- Given a viewport width < 768px, the system MUST ensure the iframe URL contains `&zoom=80`.
#### Scenario: Tablet/Laptop Viewport
- Given a viewport width >= 768px and < 1024px, the system MUST ensure the iframe URL contains `&zoom=100`.
#### Scenario: Desktop Viewport
- Given a viewport width >= 1024px, the system MUST ensure the iframe URL contains `&zoom=110`.
