# tours-api Specification

## Purpose
TBD - created by archiving change expose-tours-api. Update Purpose after archive.
## Requirements
### Requirement: Local data mirror
The application SHALL store a local copy of the external tour data at `src/data/tours.json` for reliable serving.

#### Scenario: Local data exists
- **GIVEN**: The external file `/mnt/hd/develop/vanilla/granada-go-custom-code/tours.json` is accessible
- **WHEN**: The data is copied to the project
- **THEN**: The file `src/data/tours.json` should exist in the project structure

