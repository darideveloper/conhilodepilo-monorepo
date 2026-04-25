import { useMemo } from "react";
import { useBookingStore } from "../../store/useBookingStore";
import { translations } from "./translations";

export function useTranslation() {
  const language = useBookingStore((state) => state.language);
  const config = useBookingStore((state) => state.config);
  
  const t = useMemo(() => {
    const baseT = translations[language] || translations.es;
    if (!config) return baseT;

    // Merge overrides
    return {
      ...baseT,
      calendar: { 
        ...baseT.calendar, 
        tourLabel: config.event_type_label || baseT.calendar.tourLabel,
        selectTour: config.event_label 
          ? (language === 'es' ? `Selecciona un ${config.event_label.toLowerCase()}` : `Select a ${config.event_label.toLowerCase()}`)
          : baseT.calendar.selectTour 
      },
      status: { 
        ...baseT.status,
        available: config.availability_free_label || baseT.status.available,
        standard: config.availability_regular_label || baseT.status.standard,
        booked: config.availability_no_free_label || baseT.status.booked
      },
      layout: { 
        ...baseT.layout,
        title: config.company_name || baseT.layout.title
      }
    };
  }, [language, config]);
  
  return { t, language };
}
