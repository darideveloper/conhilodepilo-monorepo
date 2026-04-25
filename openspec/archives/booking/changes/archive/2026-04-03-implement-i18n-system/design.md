# Design: i18n Translation System

This document outlines the architectural approach for implementing a bilingual (Spanish/English) translation system for the Granada Go Tours project.

## Overview
The goal is to provide a unified way to manage all user-visible strings, including UI labels and tour data, allowing users to toggle between Spanish and English.

## Components

### 1. State Management (`useBookingStore.ts`)
We will extend the existing `useBookingStore` to include the global language state.

```typescript
type Language = 'es' | 'en';

interface BookingState {
  // ... existing fields
  language: Language;
  setLanguage: (lang: Language) => void;
}
```

- **Persistence**: The language preference will be persisted in `localStorage`.
- **Default**: The default language will be 'es' (Spanish).

### 2. UI Translation Dictionary (`src/lib/i18n/translations.ts`)
A centralized dictionary will store UI-related strings for both languages.

```typescript
export const translations = {
  es: {
    calendar: {
      tourLabel: "Tour",
      selectTour: "Selecciona un tour",
      continue: "Continuar con la reserva",
      availabilityUpdate: "La disponibilidad se actualiza diariamente.",
      // ...
    },
    // ...
  },
  en: {
    calendar: {
      tourLabel: "Tour",
      selectTour: "Select a tour",
      continue: "Continue with booking",
      availabilityUpdate: "Availability is updated daily.",
      // ...
    },
    // ...
  }
};
```

### 3. Tour Data Localization (`src/data/tours.json`)
The `tours.json` file will be modified to support bilingual fields for all user-visible text.

**Current Structure**:
```json
{
  "title": "Alhambra Completa",
  "introduction": "..."
}
```

**Proposed Structure**:
```json
{
  "title": {
    "es": "Alhambra Completa",
    "en": "Complete Alhambra"
  },
  "introduction": {
    "es": "...",
    "en": "..."
  }
}
```

A utility function or hook will be provided to select the correct string based on the current language.

### 4. Language Toggle Component (`LanguageToggle.tsx`)
A new React component will be created to allow users to switch languages. It will be placed next to the `ThemeToggle` component in `BookingCalendar.tsx`.

## Technical Decisions

### Custom Solution vs. Library
Given the project's relatively small scale and the existing use of Zustand for state management, a custom i18n implementation is preferred over heavy libraries like `react-i18next`. This keeps the bundle size small and the implementation "minimal" and straightforward.

### Date Localization
The project currently uses `date-fns` with the `es` locale in `BookingCalendar.tsx`. This will be updated to dynamically switch between `es` and `en-US` locales based on the current language.

## Trade-offs
- **Data Duplication**: `tours.json` will grow in size due to bilingual content. However, since it's a static file loaded by the client, the impact is manageable compared to the benefit of full localization.
- **Manual Translation**: All existing strings in `tours.json` must be manually translated to English.
