## ADDED Requirements

### Requirement: Booking list view shows configured columns
The Booking admin list view SHALL display exactly these columns in order: client name, status, services, price, created at, start time.

#### Scenario: List view renders all required columns
- **WHEN** an admin navigates to the Booking list view
- **THEN** the table SHALL display columns: "Cliente", "Estado", "Servicios", "Precio", "Fecha de compra", "Fecha del servicio"

### Requirement: Services column shows comma-separated names
The services column SHALL display the names of all services related to a booking, separated by commas.

#### Scenario: Booking with multiple services
- **WHEN** a booking has 3 related services named "Depilación facial", "Depilación corporal", "Cera"
- **THEN** the services column SHALL show "Depilación facial, Depilación corporal, Cera"

#### Scenario: Booking with single service
- **WHEN** a booking has 1 related service named "Depilación facial"
- **THEN** the services column SHALL show "Depilación facial"

#### Scenario: Booking with no services
- **WHEN** a booking has no related services
- **THEN** the services column SHALL show an empty string or dash

### Requirement: Price column shows total from services
The price column SHALL display the sum of all related service prices.

#### Scenario: Booking with multiple services of different prices
- **WHEN** a booking has services priced at 30.00, 45.00, and 25.00
- **THEN** the price column SHALL show "100.00" (or the locale-formatted equivalent)

#### Scenario: Booking with single service
- **WHEN** a booking has one service priced at 30.00
- **THEN** the price column SHALL show "30.00"

### Requirement: Created at column shows purchase date with Spanish label
The created at column SHALL display the booking's creation timestamp with the column header "Fecha de compra".

#### Scenario: Created at column header
- **WHEN** viewing the Booking list view
- **THEN** the column header for creation date SHALL read "Fecha de compra"

### Requirement: All column headers use Spanish labels
Every visible column header in the Booking list view SHALL use a Spanish label.

#### Scenario: Column header mapping
- **WHEN** viewing the Booking list view
- **THEN** the column headers SHALL be: "Cliente", "Estado", "Servicios", "Precio", "Fecha de compra", "Fecha del servicio"

### Requirement: Removed columns no longer appear
The end_time and Google sync status badge columns SHALL NOT appear in the Booking list view.

#### Scenario: Old columns hidden
- **WHEN** an admin views the Booking list view
- **THEN** the table SHALL NOT show an "End time" column or a "Google Sync" column
