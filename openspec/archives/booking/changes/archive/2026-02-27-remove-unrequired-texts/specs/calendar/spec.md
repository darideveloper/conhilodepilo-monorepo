# calendar Specification Delta

## ADDED Requirements
### Requirement: UI Simplification
The `BookingCalendar` SHALL NOT display redundant header titles, descriptions, or step indicators.

#### Scenario: No Header in BookingCalendar
- **Given** the user is on the `BookingCalendar`
- **Then** the text "Selecciona tu Tour y Fecha" MUST NOT be visible.
- **And** the text "Elige el tour que deseas realizar y busca un día disponible." MUST NOT be visible.

#### Scenario: No Step Indicator in Step 1
- **Given** the user is on the `BookingCalendar`
- **Then** the text "Paso 1 de 2" MUST NOT be visible.
