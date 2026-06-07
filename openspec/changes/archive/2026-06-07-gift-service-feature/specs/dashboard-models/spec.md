# dashboard-models Specification

## Purpose
Defines application data model requirements. This delta adds gift-related fields to the Booking model and a migration strategy for existing records.

## ADDED Requirements

### Requirement: Gift fields on Booking model
The `Booking` model SHALL have the following additional fields to support gift bookings:

- `is_gift`: `BooleanField(default=False)` — whether this booking is a gift
- `buyer_name`: `CharField(max_length=255)` — the name of the person who submitted the form (always filled)
- `buyer_email`: `EmailField()` — the email of the person who submitted the form (always filled)
- `recipient_name`: `CharField(max_length=255, blank=True, null=True)` — the gift recipient name (null when not a gift)
- `recipient_email`: `EmailField(blank=True, null=True)` — the gift recipient email (null when not a gift)

The existing `client_name` and `client_email` fields SHALL continue to represent the final service recipient:
- When `is_gift=False`: `client_name=buyer_name`, `client_email=buyer_email`
- When `is_gift=True`: `client_name=recipient_name`, `client_email=recipient_email`

#### Scenario: New gift booking stored correctly
- **WHEN** a gift booking is created with buyer name "Alice" and recipient name "Bob"
- **THEN** `is_gift` SHALL be `True`
- **AND** `buyer_name` SHALL be "Alice"
- **AND** `client_name` SHALL be "Bob" (the recipient)
- **AND** `recipient_name` SHALL be "Bob"

#### Scenario: New non-gift booking stored correctly
- **WHEN** a non-gift booking is created with buyer name "Alice"
- **THEN** `is_gift` SHALL be `False`
- **AND** `buyer_name` SHALL be "Alice"
- **AND** `client_name` SHALL be "Alice"
- **AND** `recipient_name` SHALL be `None`

### Requirement: Migration populates buyer fields for existing records
A data migration SHALL set `is_gift=False`, `buyer_name=client_name`, and `buyer_email=client_email` for all existing Booking records where these fields are null.

#### Scenario: Existing booking migration
- **WHEN** the migration runs against an existing booking with `client_name="Alice"`, `client_email="alice@test.com"`
- **THEN** the booking SHALL have `is_gift=False`, `buyer_name="Alice"`, `buyer_email="alice@test.com"`
