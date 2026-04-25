# Proposal: Setup Bruno API Collection (v3)

This proposal outlines the integration of **Bruno** into the project using the modern **Bruno v3 (OpenCollection YAML)** format.

## Problem Statement
Currently, there is no shared repository for API requests and environments. Developers must manually configure their testing tools, leading to duplication of effort and potential inconsistencies.

## Proposed Solution
We will implement a Bruno collection following the v3 standard:
1.  **OpenCollection YAML Format:** Use `opencollection.yml` and `.yml` request files for better Git compatibility and standard YAML tooling.
2.  **Standardize Environments:** Provide pre-configured YAML environments for `Local`, `Development`, and `Production`.
3.  **Initial Coverage:** Include the `CompanyConfig` endpoint as a reference request.
4.  **Security:** Ensure local secrets in `bruno/.env` are ignored by Git.

## Impact
- **Productivity:** Developers can use modern YAML-based workflows for API testing.
- **Consistency:** Aligns the project with the latest Bruno standards.
- **Future-Proof:** Using an open standard (OpenCollection) ensures long-term portability and tool compatibility.
