import React, { useEffect } from 'react';
import { Sun, Moon } from 'lucide-react';
import { Button } from './button';
import { useTranslation } from '@/lib/i18n/useTranslation';
import { useBookingStore } from '@/store/useBookingStore';

export function ThemeToggle() {
  const { t } = useTranslation();
  const theme = useBookingStore((state: any) => state.theme);
  const setTheme = useBookingStore((state: any) => state.setTheme);

  useEffect(() => {
    // Check localStorage first as Layout.astro script might have set it
    const savedTheme = localStorage.getItem('theme') as 'light' | 'dark' | null;
    
    // If store is still default light but localStorage says otherwise, update store
    if (savedTheme && savedTheme !== theme) {
      setTheme(savedTheme);
      applyTheme(savedTheme);
    } else {
      // Otherwise just ensure store theme is applied to document
      applyTheme(theme);
    }
  }, [theme, setTheme]);

  const applyTheme = (newTheme: 'light' | 'dark') => {
    if (newTheme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  };

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    applyTheme(newTheme);
  };

  return (
    <Button
      variant="outline"
      size="icon"
      onClick={toggleTheme}
      className="rounded-full w-10 h-10 transition-colors bg-background border-border shadow-sm hover:bg-accent/20"
      aria-label={t.accessibility.toggleTheme}
    >
      {theme === 'light' ? (
        <Moon className="h-5 w-5 text-foreground" />
      ) : (
        <Sun className="h-5 w-5 text-foreground" />
      )}
    </Button>
  );
}
