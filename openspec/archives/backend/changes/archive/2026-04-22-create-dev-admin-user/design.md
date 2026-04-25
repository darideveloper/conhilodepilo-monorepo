# Design: Development Admin User Specification

## Overview
We are shifting from an implementation-based approach to a specification-based approach. The existence of a standard admin user is a prerequisite for a consistent development experience.

## Security & Environment Isolation
To prevent security issues, this specification explicitly partitions requirements by environment:

1.  **Scope:** The `admin`/`admin` user is defined exclusively for the **Development Environment**.
2.  **Constraint:** A new requirement, **Production Credential Security**, is added to mandate that these credentials MUST NOT exist in production.
3.  **Validation:** Any future proposal involving automation or testing MUST check the environment state before attempting to use these credentials.

## Specification Strategy
The requirement is added to the `environment` specification to serve as a contract for project setup.

## Usage in Future Proposals
Future proposals (e.g., E2E testing) will reference the `environment` specification. They will be required to check if the environment is `dev` before assuming the existence of the `admin` user.

## Verification
Verification involves:
1.  Manually creating the user in `dev`.
2.  Ensuring the `openspec` validation passes.
3.  Confirming that no production deployment scripts or instructions reference these credentials.
