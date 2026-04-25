# Proposal: Simplify Availability System (Default Available)

## Problem
The current availability system explicitly lists every "available" day in `src/data/tours.json`. This leads to large, redundant data files that are hard to maintain. Furthermore, logically, most days are available by default unless specified otherwise (booked or limited).

## Proposed Solution
Refactor the availability system to assume all future days are **Available** by default. This involves:
- Migrating `tours.json` to an exclusion-based model.
- Updating the central store to infer availability.
- Adjusting UI logic to reflect these changes.

Detailed technical specifications and logic transitions are documented in the [Design Spec](./design.md).

## Impact
- **Data**: Significant reduction in `tours.json` file size.
- **Maintenance**: Easier to add or block dates as only exceptions need to be managed.
- **Performance**: Reduced payload size and simplified state initialization.
