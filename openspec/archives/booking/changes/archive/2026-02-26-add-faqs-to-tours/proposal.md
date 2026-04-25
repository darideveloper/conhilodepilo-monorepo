# Proposal: Add FAQs to Tours

## Why
Enhance the tour data structure by adding a `faqs` key to each tour in `src/data/tours.json`. This will provide users with quick answers to common questions specific to each tour, improving the user experience and potentially reducing direct inquiries for basic information.

## What Changes
- Modify `src/data/tours.json` to include a `faqs` array for each tour.
- Each `faqs` array will contain exactly 2 questions and answers related to the tour's content and logistics.
- All content will be in Spanish, following the project's primary language constraint.

## Objective
Enhance the tour data structure by adding a `faqs` key to each tour in `src/data/tours.json`.

## Scope
- Modify `src/data/tours.json` to include a `faqs` array for each tour.
- Each `faqs` array will contain exactly 2 questions and answers related to the tour's content and logistics.
- All content will be in Spanish, following the project's primary language constraint.

## Content Strategy
The FAQs will focus on:
1.  **Monumental/Religioso Tours:** Specifics about the monument, entry requirements (reminding about tickets), and what to expect from the historian's perspective.
2.  **Neighborhood Tours (Albaicín, Sacromonte, Centro):** Walking difficulty, best time for views, and cultural highlights.
3.  **Historical/Thematic Tours:** Context about the figure or period covered and the depth of the historical analysis.

## Requirements
- `faqs` must be an array of objects.
- Each object must have `question` (string) and `answer` (string) properties.
- Content must be specific to each tour's `id` and `title`.
