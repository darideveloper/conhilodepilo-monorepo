# Spec: Tours API

Expose a JSON API for tours data, sourced from a local mirror of the external `tours.json`.

## ADDED Requirements

### Requirement: Serve tour data as JSON
The application SHALL provide a GET endpoint at `/api/tours.json` that returns a JSON array of tours.

#### Scenario: Requesting all tours
- **GIVEN**: The tour data is copied to `src/data/tours.json`
- **WHEN**: A client makes a GET request to `/api/tours.json`
- **THEN**: The response status is 200
- **AND**: The response content type is `application/json`
- **AND**: The response body contains the JSON array from `src/data/tours.json`

### Requirement: Local data mirror
The application SHALL store a local copy of the external tour data at `src/data/tours.json` for reliable serving.

#### Scenario: Local data exists
- **GIVEN**: The external file `/mnt/hd/develop/vanilla/granada-go-custom-code/tours.json` is accessible
- **WHEN**: The data is copied to the project
- **THEN**: The file `src/data/tours.json` should exist in the project structure
