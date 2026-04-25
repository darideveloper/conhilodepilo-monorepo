import React from 'react';
import { Info, CheckCircle2, AlertCircle, XCircle } from 'lucide-react';

export type StatusKey = 'booked' | 'limited' | 'available' | 'standard';

export interface StatusConfigValue {
  i18nKey: keyof typeof import('../../lib/i18n/translations').translations.es.status;
  icon: React.ElementType;
  classes: {
    container: string;
    badge: string;
    icon: string;
    modifier?: string;
    legendMarker: string;
  };
}

export const STATUS_CONFIG: Record<StatusKey, StatusConfigValue> = {
  available: {
    i18nKey: 'available',
    icon: CheckCircle2,
    classes: {
      container: 'bg-emerald-500/10 border-emerald-500/20',
      badge: 'border-emerald-500 text-emerald-700 dark:text-emerald-400 bg-emerald-500/5',
      icon: 'text-emerald-600 dark:text-emerald-400',
      modifier: 'bg-emerald-500 text-white font-bold hover:bg-emerald-600! hover:text-white!',
      legendMarker: 'bg-emerald-500 border-emerald-600',
    }
  },
  limited: {
    i18nKey: 'limited',
    icon: AlertCircle,
    classes: {
      container: 'bg-amber-500/10 border-amber-500/20',
      badge: 'border-amber-500 text-amber-700 dark:text-amber-400 bg-amber-500/5',
      icon: 'text-amber-600 dark:text-amber-400',
      modifier: 'bg-amber-500 text-amber-950 font-medium hover:bg-amber-600! hover:text-amber-950!',
      legendMarker: 'bg-amber-500 border-amber-600',
    }
  },
  booked: {
    i18nKey: 'booked',
    icon: XCircle,
    classes: {
      container: 'bg-muted/30 border-border',
      badge: 'border-border text-muted-foreground bg-muted/20',
      icon: 'text-muted-foreground',
      modifier: 'bg-muted text-muted-foreground line-through opacity-50 cursor-not-allowed',
      legendMarker: 'bg-muted border-border opacity-50',
    }
  },
  standard: {
    i18nKey: 'standard',
    icon: Info,
    classes: {
      container: 'bg-accent/5 border-border',
      badge: 'border-border text-muted-foreground bg-muted/20',
      icon: 'text-muted-foreground',
      legendMarker: 'bg-accent border-border',
    }
  }
};
