# Specification: Landing Data Fetching

## ADDED Requirements

### Requirement: Service Category Filtering
The landing page MUST identify and separate "Courses" from "Salon Services" using the `group_id` field provided by the backend API. The specific IDs used for filtering MUST be configurable via environment variables.

#### Scenario: Identifying Courses
- **Given** a list of service categories from the API
- **And** the `PUBLIC_COURSES_GROUP_ID` environment variable
- **When** filtering for courses
- **Then** the application MUST select categories where `group_id` matches the value of `PUBLIC_COURSES_GROUP_ID`
- **And** map their services to the `Course` type

#### Scenario: Identifying Salon Services
- **Given** a list of service categories from the API
- **And** the `PUBLIC_COURSES_GROUP_ID` environment variable
- **When** filtering for regular services
- **Then** the application MUST exclude all categories where `group_id` matches `PUBLIC_COURSES_GROUP_ID`
- **And** maintain their `ServiceCategory` structure