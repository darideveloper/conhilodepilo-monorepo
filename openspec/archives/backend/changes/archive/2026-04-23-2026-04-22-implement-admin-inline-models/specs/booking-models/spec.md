# Capability: Booking Models

## ADDED Requirements

### Requirement: Global Availability Linkage
Global availability models MUST be linked to the `CompanyProfile` singleton to support administrative inlines.

#### Scenario: Relate Company Availability to Profile
- **Given** an existing `CompanyProfile` singleton instance.
- **When** defining `CompanyAvailability`, `CompanyWeekdaySlot`, and `CompanyDateOverride` models.
- **Then** each model must include a `ForeignKey` to `CompanyProfile`.
- **And** `CompanyWeekdaySlot` MUST use `related_name="weekday_slots"`.
- **And** the relationship must be mandatory (null=False) with a default value pointing to the singleton instance.
