## 1. Directory Structure Setup
- [x] 1.1 Create `atoms`, `molecules`, and `organisms` subdirectories in `src/components`.

## 2. Component Migration
- [x] 2.1 Categorize and move components to their respective newly created subdirectories based on their functional complexity.
- [x] 2.2 Fix all internal import paths referencing the moved components.

## 3. Styling Refactor
- [x] 3.1 Migrate custom vanilla styling in `atoms` components to Tailwind CSS utility classes.
- [x] 3.2 Migrate custom vanilla styling in `molecules` components to Tailwind CSS utility classes.
- [x] 3.3 Migrate custom vanilla styling in `organisms` components to Tailwind CSS utility classes.
- [x] 3.4 Verify clean-up of unnecessary `<style>` tags directly impacted by the Tailwind conversion.

## 4. Quality Assurance
- [x] 4.1 Perform sanity checks across main pages confirming paths are working.
- [x] 4.2 Validate styles remain visually congruent while purely adopting Tailwind.
