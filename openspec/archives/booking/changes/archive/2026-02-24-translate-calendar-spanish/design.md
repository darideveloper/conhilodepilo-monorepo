# Design: Spanish Translation and Language Standard

## Architectural Reasoning
The project is moving towards a Spanish-first user interface. This requires both a code-level change (translating strings) and a process-level change (updating specifications).

### Component Localization
We will utilize the built-in localization support of the shadcn/ui `Calendar` (which uses `react-day-picker`). By passing the `es` locale from `date-fns`, the calendar will automatically handle months and days of the week.

### String Mapping
| English | Spanish |
| :--- | :--- |
| Available | Disponible |
| Limited | Limitada |
| Full | Completo |
| Standard | Estándar |
| Selected Date | Fecha Seleccionada |

### Specification Formalization
We will add a new "Language" section to the project conventions to ensure all future features are developed with Spanish text by default.

## Implementation Details

### src/components/BookingCalendar.tsx
- Import `es` from `date-fns/locale`.
- Pass `locale={es}` to the `Calendar` component.
- Update JSX strings.

### openspec/project.md
- Update the "Multilingual Support" section to "Language Standard".
- Add a mandate: "All user-visible text MUST be in Spanish by default."

## Trade-offs
- **Hardcoded Strings**: For now, strings remain hardcoded in the components. If the project needs to scale to more languages later, an i18n library (like `astro-i18n` or `i18next`) will be considered. For the current scope, hardcoding Spanish is the simplest and most effective approach.
