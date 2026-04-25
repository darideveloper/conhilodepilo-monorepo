import React from 'react';
import { useBookingStore } from '../../../store/useBookingStore';
import { Button } from './button';
import { Globe } from 'lucide-react';

export function LanguageToggle() {
  const language = useBookingStore((state) => state.language);
  const setLanguage = useBookingStore((state) => state.setLanguage);

  const toggleLanguage = () => {
    setLanguage(language === 'es' ? 'en' : 'es');
  };

  return (
    <Button
      variant="outline"
      size="sm"
      onClick={toggleLanguage}
      className="rounded-full px-3 h-10 transition-colors bg-background border-border shadow-sm hover:bg-accent/20 flex items-center gap-2 font-medium"
      aria-label={language === 'es' ? 'Switch to English' : 'Cambiar a Español'}
    >
      <Globe className="h-4 w-4" />
      <span className="uppercase text-xs">{language}</span>
    </Button>
  );
}
