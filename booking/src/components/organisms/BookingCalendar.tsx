import React, { useMemo } from 'react';
import { Calendar } from '@/components/atoms/ui/calendar';
import { Card, CardContent } from '@/components/atoms/ui/card';
import { Button } from '@/components/atoms/ui/button';
import { Label } from '@/components/atoms/ui/label';
import { Select } from '@/components/atoms/ui/select';
import { cn } from "@/lib/utils";
import { es, enUS } from 'date-fns/locale';
import { STATUS_CONFIG, type StatusKey } from './types';
import { StatusLegend } from '@/components/molecules/StatusLegend';
import { StatusDetails } from '@/components/molecules/StatusDetails';
import { BookingHeader } from '@/components/molecules/BookingHeader';
import { useBookingStore } from '../../store/useBookingStore';
import { useTranslation } from '@/lib/i18n/useTranslation';
import { AlertCircle } from 'lucide-react';


/**
 * MAIN COMPONENT
 */
export function BookingCalendar() {
  const { t, language } = useTranslation();
  const selectedDate = useBookingStore((state: any) => state.selectedDate);
  const setSelectedDate = useBookingStore((state: any) => state.setSelectedDate);
  const availability = useBookingStore((state: any) => state.availability);
  const isAvailabilityLoading = useBookingStore((state: any) => state.isAvailabilityLoading);
  const availabilityError = useBookingStore((state: any) => state.availabilityError);
  const nextStep = useBookingStore((state: any) => state.nextStep);
  const formData = useBookingStore((state: any) => state.formData);
  const updateFormData = useBookingStore((state: any) => state.updateFormData);
  const visibility = useBookingStore((state: any) => state.visibility);
  const config = useBookingStore((state: any) => state.config);
  const prevStep = useBookingStore((state: any) => state.prevStep);

  const dateLocale = language === 'es' ? es : enUS;

  const today = useMemo(() => {
    const d = new Date();
    d.setHours(0, 0, 0, 0);
    return d;
  }, []);

  const modifiers = useMemo(() => ({
    isAvailable: (d: Date) => {
      const dateObj = d instanceof Date ? d : new Date(d);
      return dateObj > today && availability.available.some((availableDate: Date) => {
        const a = availableDate instanceof Date ? availableDate : new Date(availableDate);
        return a.toDateString() === dateObj.toDateString();
      });
    },
  }), [availability, today]);

  const modifiersClassNames = useMemo(() => {
    return {
      isAvailable: STATUS_CONFIG.available.classes.modifier,
    };
  }, []);

  const getStatus = (d: Date | undefined): StatusKey => {
    if (!d) return 'standard';
    const dateObj = d instanceof Date ? d : new Date(d);
    if (dateObj <= today) return 'standard';
    
    const dateStr = dateObj.toDateString();
    
    const isAvailable = availability.available.some((availableDate: Date) => {
      const a = availableDate instanceof Date ? availableDate : new Date(availableDate);
      return a.toDateString() === dateStr;
    });
    
    return isAvailable ? 'available' : 'booked';
  };

  const statusKey = getStatus(selectedDate);

  return (
    <>
      <Card className="w-full max-w-md shadow-xl border-none bg-background relative overflow-hidden">
        <BookingHeader 
          showBack={true}
          onBack={prevStep}
          showStep={true} 
          stepText={t.form?.step2Of3 || "Step 2 of 3"} 
        />
        <CardContent className="flex flex-col items-center gap-4 h-full justify-center">

          <StatusLegend />

          {formData.selectedServices.length > 1 && (
            <div className="w-full p-3 bg-amber-50 border border-amber-200 rounded-xl flex items-start gap-3 animate-in fade-in slide-in-from-top-2 duration-300">
              <div className="w-5 h-5 rounded-full bg-amber-100 flex items-center justify-center shrink-0 mt-0.5">
                <AlertCircle className="w-3.5 h-3.5 text-amber-600" />
              </div>
              <div className="space-y-1">
                <p className="text-[11px] font-bold text-amber-900 leading-tight">
                  {language === 'es' ? 'Combinando disponibilidades' : 'Combining availabilities'}
                </p>
                <p className="text-[10px] text-amber-700 leading-snug">
                  {language === 'es' 
                    ? 'Mostrando solo los días donde TODOS los servicios seleccionados están disponibles simultáneamente.' 
                    : 'Showing only days where ALL selected services are available simultaneously.'}
                </p>
              </div>
            </div>
          )}

          <div className="p-2 bg-background rounded-xl border border-border shadow-sm w-full relative">
            {isAvailabilityLoading && (
              <div className="absolute inset-0 z-10 flex items-center justify-center bg-background/80 backdrop-blur-sm rounded-xl">
                <p className="text-xs">{language === 'es' ? 'Cargando disponibilidad...' : 'Loading availability...'}</p>
              </div>
            )}
            {availabilityError && (
              <div className="absolute inset-0 z-10 flex items-center justify-center bg-background/90 p-4 text-center rounded-xl">
                <p className="text-xs text-destructive">{availabilityError}</p>
              </div>
            )}
            <Calendar
              mode="single"
              selected={selectedDate}
              onSelect={setSelectedDate}
              locale={dateLocale}
              showOutsideDays={false}
              className="rounded-md border-none w-full"
              classNames={{
                day: cn(
                  "relative w-full h-full p-0 text-center [&:last-child[data-selected=true]_button]:rounded-r-md group/day aspect-square select-none",
                  "hover:bg-foreground hover:text-background rounded-md transition-colors"
                ),
                disabled: "hover:bg-transparent hover:text-muted-foreground",
                ...modifiersClassNames,
              }}
              modifiers={modifiers}
              disabled={(d: Date) => {
                const dateObj = d instanceof Date ? d : new Date(d);
                if (dateObj <= today) return true;
                const isAvailable = availability.available.some((availableDate: Date) => {
                  const a = availableDate instanceof Date ? availableDate : new Date(availableDate);
                  return a.toDateString() === dateObj.toDateString();
                });
                return !isAvailable;
              }}
            />
          </div>

          <div className="w-full space-y-4">
            {selectedDate && <StatusDetails date={selectedDate} statusKey={statusKey} />}
            
            <Button 
              className="w-full py-6 text-lg font-serif rounded-xl"
              disabled={!selectedDate || formData.selectedServices.length === 0}
              onClick={nextStep}
            >
              {t.calendar.continue}
            </Button>
          </div>
        </CardContent>
      </Card>
      
      <div className="max-w-md text-center text-muted-foreground text-[10px] font-sans italic mt-2">
        <p>{t.calendar.availabilityUpdate}</p>
      </div>
    </>
  );
}

