# Proposal: Document Development Admin User Credentials

## Problem
Future proposals and development workflows need a reliable and documented set of administrative credentials for testing and dashboard access. Currently, there is no formal specification stating that a default `admin`/`admin` user should exist in the development environment.

## Proposed Change
Instead of implementing a management command, we will formally define a requirement in the project specifications that the development environment MUST be initialized with a superuser account (`admin`/`admin`). This ensures that all future automation, tests, and proposals can assume these credentials are available.

## Impact
- **Clarity:** Provides a single source of truth for development credentials.
- **Interoperability:** Allows future OpenSpec proposals (e.g., for E2E testing) to reference these credentials.
- **Simplicity:** Avoids adding unnecessary code to the application.

## Proposed Capabilities
- **environment**: Add a requirement for standard development administrator credentials.
