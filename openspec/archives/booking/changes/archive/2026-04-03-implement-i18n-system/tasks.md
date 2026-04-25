# Tasks: i18n Translation System

This document lists the tasks required to implement the i18n translation system.

## Setup & Infrastructure
- [x] Add `language` state ('es' | 'en') and `setLanguage` action to `src/store/useBookingStore.ts`, with `localStorage` persistence. <!-- id: 1 -->
- [x] Create `src/lib/i18n/translations.ts` with initial Spanish and English UI dictionaries. <!-- id: 2 -->
- [x] Implement a custom React hook `useTranslation()` or similar utility to easily access i18n strings in components. <!-- id: 3 -->

## UI Components
- [x] Implement `LanguageToggle.tsx` component to handle language switching. <!-- id: 4 -->
- [x] Update `src/components/organisms/BookingCalendar.tsx` to include the `LanguageToggle` next to the `ThemeToggle`. <!-- id: 5 -->
- [x] Update `BookingCalendar.tsx` to use `language` to switch between `date-fns` locales (`es` vs `enUS`). <!-- id: 6 -->

## Component Refactoring
- [x] Refactor `src/components/organisms/types.ts` to replace hardcoded labels in `STATUS_CONFIG` with i18n keys or logic. <!-- id: 7 -->
- [x] Refactor `src/components/molecules/StatusDetails.tsx` to use i18n strings and dynamic date locale. <!-- id: 8 -->
- [x] Refactor `src/components/organisms/BookingForm.tsx` to use i18n for all labels, placeholders, error messages, and the Stripe payload. <!-- id: 9 -->
- [x] Update `src/components/atoms/ui/ThemeToggle.tsx` to localize `aria-label`. <!-- id: 16 -->

## Layout & SEO
- [x] Refactor `src/layouts/Layout.astro` to dynamically set site title and HTML `lang` based on the store language. <!-- id: 17 -->

## Data Refactoring
- [x] Define the bilingual schema for `src/data/tours.json` including `title`, `subtitle`, `focus`, `introduction`, `discoveries`, `faqs`, `included`, `not_included`, `cancelation`, `disclaimer`, `meeting_point`, `historian_note`, `meta_title`, and `meta_description`. <!-- id: 10 -->
- [x] Update `tours.json` to include English translations for all the identified fields. <!-- id: 11 -->
- [x] Update components and asset scripts (e.g., `update-tour-data.js`) to correctly access the localized fields. <!-- id: 12 -->

## Validation
- [x] Verify that switching languages instantly updates all visible UI elements. <!-- id: 13 -->
- [x] Verify that the language preference persists after a page refresh. <!-- id: 14 -->
- [x] Ensure `tours.json` data is correctly localized in both steps of the booking flow. <!-- id: 15 -->
