# Proposal: i18n Translation System

## Why
The project's user interface and tour data are currently hardcoded in Spanish. To reach a broader audience, specifically international tourists visiting Granada, we need to support English as a secondary language.

## What Changes
We propose a custom i18n system integrated with the existing Zustand state management, coupled with a bilingual refactor of the tour data source.

### Key Features
- **Global Language State**: Managed via `useBookingStore.ts` and persisted in `localStorage`.
- **Language Toggle**: A UI component next to the `ThemeToggle` to switch between ES and EN.
- **Bilingual Tour Data**: Support for both Spanish and English descriptions, titles, and metadata in `tours.json`.
- **Dynamic Date Localization**: Calendars and date pickers will automatically adjust their locale.

## Detailed Text Mapping
The following strings have been identified for externalization and translation:

### 1. Availability Status
- **Disponible** → **Available**
- **Pocas plazas** → **Limited availability**
- **Completo** → **Full**
- **Estándar** → **Standard**

### 2. Calendar UI
- **Tour** (Label)
- **Selecciona un tour** → **Select a tour**
- **Continuar con la reserva** → **Continue with booking**
- **La disponibilidad se actualiza diariamente.** → **Availability is updated daily.**
- **Fecha Seleccionada** → **Selected Date**

### 3. Booking Form & Stripe Payload
- **Datos de la reserva** → **Booking details**
- **Completa tus datos para finalizar la solicitud.** → **Complete your details to finalize the request.**
- **Nombre Completo** → **Full Name**
- **Tu nombre** → **Your name** (placeholder)
- **tu@email.com** (placeholder)
- **Personas (máximo 30)** → **Guests (max 30)**
- **Peticiones especiales (opcional)** → **Special requests (optional)**
- **Cuéntanos si necesitas algo especial...** → **Tell us if you need anything special...** (placeholder)
- **He leído y acepto la política de privacidad.** → **I have read and accept the privacy policy.**
- **Volver** → **Back**
- **Solicitar Reserva** → **Request Booking**
- **Procesando...** → **Processing...**
- **Todos los campos marcados son obligatorios...** → **All marked fields are required...**
- **Stripe Receipt Labels**:
    - **Nombre**, **Email**, **Tour**, **Fecha**, **Invitados**, **Peticiones**
    - **No especificada** → **Not specified**
    - **Ninguna** → **None**

### 4. Layout, SEO & Accessibility
- **Granada Go Tours** (Site Title)
- **HTML lang attribute** ('es' vs 'en')
- **Toggle theme** (aria-label in ThemeToggle)

### 5. Tour Data (tours.json)
All user-facing fields will be bilingual:
- `title`, `subtitle`, `focus`, `introduction`, `historian_note`, `meeting_point`, `cancelation`, `disclaimer`
- `meta_title`, `meta_description`
- `discoveries`: `title`, `description`
- `faqs`: `question`, `answer`
- `included`, `not_included` (arrays of strings)

### 6. Asset Scripts (WordPress Integration)
Hardcoded strings in `src/assets/wordpress/update-tour-data.js`:
- Currency prefix (`€ `)
- Suffixes (` / grupo`, ` hrs`)
- Icons (`✅ `, `❌ `)

## Proposed Changes

### Infrastructure
- `src/store/useBookingStore.ts`: Add `language` state and `setLanguage` action.
- `src/lib/i18n/`: Create a new directory for translation dictionaries and utilities.

### Components
- `src/components/atoms/ui/LanguageToggle.tsx`: New component for language switching.
- `src/components/organisms/BookingCalendar.tsx`: Refactor to use i18n strings and dynamic date locale (date-fns).
- `src/components/organisms/BookingForm.tsx`: Refactor to use i18n strings for all labels, placeholders, errors, and the Stripe payload.
- `src/components/molecules/StatusDetails.tsx`: Refactor to use i18n strings and `toLocaleDateString` with dynamic locale.
- `src/components/organisms/types.ts`: Update `STATUS_CONFIG` to use i18n keys.
- `src/components/atoms/ui/ThemeToggle.tsx`: Localize `aria-label`.

### Layout & Pages
- `src/layouts/Layout.astro`: Localize site title and HTML `lang` attribute.
- `src/pages/[id].astro` & `src/pages/index.astro`: Ensure language state is accessible.

### Data
- `src/data/tours.json`: Update the schema to support bilingual fields (`{ es: string, en: string }`).

## Out of Scope
- Automatic translation of tour descriptions (must be done manually).
- Support for more than two languages (ES/EN) for now.
