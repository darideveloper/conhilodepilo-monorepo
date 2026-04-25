import React from 'react';
import { useBookingStore } from '../../store/useBookingStore';
import { ThemeToggle } from '../atoms/ui/ThemeToggle';
import { LanguageToggle } from '../atoms/ui/LanguageToggle';
import { Button } from '@/components/atoms/ui/button';
import { ArrowLeft } from 'lucide-react';

interface BookingHeaderProps {
  showBack?: boolean;
  onBack?: () => void;
  showStep?: boolean;
  stepText?: string;
}

export function BookingHeader({ showBack, onBack, showStep, stepText }: BookingHeaderProps) {
  const visibility = useBookingStore((state: any) => state.visibility);
  const config = useBookingStore((state: any) => state.config);

  return (
    <div className="flex items-center justify-between w-full px-4 pt-4 pb-2">
      <div className="flex items-center gap-2">
        {showBack && (
          <Button 
            variant="ghost" 
            size="icon" 
            className="rounded-full h-8 w-8 hover:bg-primary/10 hover:text-primary transition-colors"
            onClick={onBack}
          >
            <ArrowLeft className="w-4 h-4" />
          </Button>
        )}
        {showStep && stepText && (
          <div className="px-3 py-1 bg-primary/10 rounded-full">
            <span className="text-[10px] font-bold uppercase tracking-widest text-primary leading-none">
              {stepText}
            </span>
          </div>
        )}
      </div>

      <div className="flex items-center gap-3">
        {visibility.lang && (
          <div className="scale-75 lg:scale-90 origin-right">
            <LanguageToggle />
          </div>
        )}
        {visibility.theme && (
          <div className="scale-75 lg:scale-90 origin-right">
            <ThemeToggle />
          </div>
        )}
        {config?.logo && (
          <img 
            src={config.logo} 
            alt={config.company_name || "Logo"} 
            className="h-7 w-auto object-contain" 
          />
        )}
      </div>
    </div>
  );
}
