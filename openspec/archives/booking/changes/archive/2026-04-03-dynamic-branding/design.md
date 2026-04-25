# Design: Dynamic Branding & Configuration

## Architecture

### 1. Dynamic Config State management
The `useBookingStore` will be updated to include a `config` object and an `isConfigLoaded` flag.

```typescript
interface AppConfig {
  brand_color: string;
  logo: string;
  currency: string;
  contact_email: string;
  contact_phone: string;
  company_name: string;
  timezone: string;
  event_type_label: string;
  event_label: string;
  availability_free_label: string;
  availability_regular_label: string;
  availability_no_free_label: string;
  extras_label: string;
}

interface BookingState {
  // ...
  config: AppConfig | null;
  isConfigLoading: boolean;
  fetchConfig: () => Promise<void>;
  // ...
}
```

### 2. Branding Injection Logic
To ensure that all UI elements use the `brand_color` from the API, we will dynamically update the CSS variables on the root element. Since Tailwind v4 uses standard CSS variables, updating `--color-brand-red` and `--primary` will propagate changes instantly.

```javascript
useEffect(() => {
  if (config?.brand_color) {
    document.documentElement.style.setProperty('--color-brand-red', config.brand_color);
    document.documentElement.style.setProperty('--primary', config.brand_color);
    // Optionally update other variables like rings or chart colors if they are tied to brand-red
  }
}, [config]);
```

### 3. Translation Overrides
The `useTranslation` hook will be refactored to merge the static translations with the dynamic config labels. To maintain performance and simplicity, we will perform a shallow merge of the relevant sections.

**Mapping:**
| API Config Key | Translation Path | Static Default (es) |
| --- | --- | --- |
| `event_type_label` | `calendar.tourLabel` | "Tour" |
| `event_label` | `calendar.selectTour` | "Selecciona un tour" |
| `availability_free_label` | `status.available` | "Disponible" |
| `availability_regular_label` | `status.standard` | "Estándar" |
| `availability_no_free_label` | `status.booked` | "Completo" |
| `company_name` | `layout.title` | "Granada Go Tours" |

**Implementation Strategy:**
The hook will derive a new translation object by overriding keys in the static `translations` map based on the active `config`.

```typescript
export function useTranslation() {
  const language = useBookingStore(s => s.language);
  const config = useBookingStore(s => s.config);
  
  const t = useMemo(() => {
    const baseT = translations[language] || translations.es;
    if (!config) return baseT;

    // Merge overrides
    return {
      ...baseT,
      calendar: { ...baseT.calendar, 
        tourLabel: config.event_type_label || baseT.calendar.tourLabel,
        selectTour: config.event_label || baseT.calendar.selectTour 
      },
      status: { ...baseT.status,
        available: config.availability_free_label || baseT.status.available,
        standard: config.availability_regular_label || baseT.status.standard,
        booked: config.availability_no_free_label || baseT.status.booked
      },
      layout: { ...baseT.layout,
        title: config.company_name || baseT.layout.title
      }
    };
  }, [language, config]);

  return { t, language };
}
```

### 4. Fetch Strategy & Dynamic Routing
...

### 5. Security & Error Handling
- **Color Validation:** The `brand_color` from the API MUST be validated as a valid CSS color string (hex, rgb, or oklch) before being applied to prevent layout breakage or XSS attempts through CSS injection.
- **Fallback Branding:** If the API fails or returns invalid branding, the application MUST use the hardcoded brand variables defined in `global.css`.
- **API Sanitization:** All labels from the API MUST be treated as untrusted and rendered using standard React escaping to prevent XSS.
All API calls (starting with `GET /config/`) will be made using a dynamic URL constructed from the `client` URL parameter and a base URL defined in the environment.

- **Environment Variable:** `PUBLIC_API_URL` (e.g., `http://localhost:8000/api/`)
- **URL Variable:** `client` (e.g., `?client=company1`)
- **Constructed URL Logic:** The `client` is injected as a subdomain into the host of the `PUBLIC_API_URL`.

**Example:**
- `PUBLIC_API_URL`: `https://services.darideveloper.com/api/`
- `client`: `granada-go`
- **Resulting Base URL**: `https://granada-go.services.darideveloper.com/api/`
- **Full Endpoint**: `https://granada-go.services.darideveloper.com/api/config/`

The `BookingFlow` component will extract the `client` parameter from the URL and trigger the configuration fetch. The store will use the `PUBLIC_API_URL` as the template for all requests.

## User-Visible Changes
- **Visuals:** Buttons, icons, and focus states will reflect the `brand_color`.
- **Content:** The logo in the header and the company name in the footer/title will be dynamic.
- **Terminology:** Status markers and dropdown labels may change based on the provider's specific configuration.
