# Proposal: Fix and Enhance Service Availability Validation Logic

## Summary
The current availability logic is a placeholder. This proposal introduces a full hierarchical validation engine (Service > Company) for ranges, slots, and overrides to accurately determine service availability.

## Problem
1. **Incomplete Logic**: The current `utils/availability.py` returns `True` for everything, ignoring model configurations.
2. **Missing Hierarchy**: The system doesn't implement the Service-level vs. Company-level fallback logic for ranges and slots.
3. **Invalid Ordering**: Validation steps (Availability Ranges -> Weekday Slots -> Overrides) are not correctly sequenced as required by business rules.

## Proposed Solution
Implement the 7-step validation logic:
1. **Availability Ranges**: Check Service; fallback to Company.
2. **Weekday Slots**: Filter by Service slots; fallback to Company slots.
3. **Overrides**: Apply Service overrides first, then Company overrides (adding/removing specific slots).

## Ambiguity / Questions
- **Multi-service Constraint**: If multiple services are requested, should the API return only dates where *all* services are available simultaneously, or the union of all available dates? (Proposal assumes intersection: date is available only if *all* selected services can be booked on that day).
