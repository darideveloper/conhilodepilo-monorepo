import React from 'react';
import { Badge } from '@/components/atoms/ui/badge';
import { cn } from "@/lib/utils";
import { STATUS_CONFIG, type StatusKey } from '@/components/organisms/types';
import { useTranslation } from '@/lib/i18n/useTranslation';

interface StatusDetailsProps {
  date: Date;
  statusKey: StatusKey;
}

export function StatusDetails({ date, statusKey }: StatusDetailsProps) {
  const { t, language } = useTranslation();
  const config = STATUS_CONFIG[statusKey];
  const Icon = config.icon;

  const dateObj = date instanceof Date ? date : new Date(date);
  const dateLocale = language === 'es' ? 'es-ES' : 'en-US';

  return (
    <div className={cn(
      "w-full p-4 rounded-lg flex items-center justify-between transition-all duration-300 border",
      config.classes.container
    )}>
      <div className="flex items-center gap-3">
        <Icon className={cn("w-5 h-5", config.classes.icon)} />
        <div>
          <p className="text-[10px] font-sans font-semibold text-foreground/60 uppercase tracking-widest">{t.calendar.selectedDate}</p>
          <p className="font-bold text-foreground font-sans">
            {dateObj.toLocaleDateString(dateLocale, { month: 'long', day: 'numeric', year: 'numeric' })}
          </p>
        </div>
      </div>
      
      <Badge variant="outline" className={cn("capitalize px-3 py-0.5 font-sans border", config.classes.badge)}>
        {t.status[config.i18nKey]}
      </Badge>
    </div>
  );
}
