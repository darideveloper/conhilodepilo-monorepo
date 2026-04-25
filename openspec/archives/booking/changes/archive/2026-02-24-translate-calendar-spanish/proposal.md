# Proposal: Translate Booking Calendar to Spanish

This proposal outlines the translation of all user-visible text in the `BookingCalendar` component to Spanish and the formalization of Spanish as the primary language for the project's user interface.

## Why
Granada Go Tours is based in Granada, Spain, and primarily targets Spanish-speaking visitors or those interested in Spanish culture. Establishing Spanish as the main language ensures consistency and better serves the core demographic.

## What Changes
- **Component Translation**: Translate all labels, statuses, and descriptive text in `src/components/BookingCalendar.tsx` to Spanish.
- **Calendar Localization**: 
    - Configure the shadcn/ui `Calendar` component to use the Spanish locale (days of week, months) via `date-fns/locale/es`.
    - Update `toLocaleDateString` to use `es-ES`.
- **Project Specifications**: 
    - Update `openspec/project.md` by renaming "Multilingual Support" to "Language Standard" and mandating Spanish as the primary language.
    - Create a new specification file at `openspec/specs/language/spec.md`.

### String Mapping
| English | Spanish |
| :--- | :--- |
| Available | Disponible |
| Limited | Disponibilidad Limitada |
| Full | Completo |
| Standard | Estándar |
| Selected Date | Fecha Seleccionada |
| Availability is updated daily... | La disponibilidad se actualiza diariamente. Seleccione una fecha para ver los detalles y proceder con su consulta de reserva. |

## Goals
- Provide a fully localized experience for Spanish speakers.
- Ensure all calendar elements (including the date picker itself) are in Spanish.
- Set a clear standard for language in the project's specifications.

## Scope
- Component: `src/components/BookingCalendar.tsx`.
- Localization: `date-fns/locale/es` and `es-ES` locale strings.
- Specs: `openspec/project.md` and `openspec/specs/language/spec.md`.

## Success Criteria
- All text in the Booking Calendar is in Spanish.
- The calendar widget displays months and days in Spanish.
- The project specifications explicitly state that Spanish is the primary language.
- `openspec validate` passes.
