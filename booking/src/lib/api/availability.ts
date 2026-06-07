export interface Availability {
  available: Date[];
}

export const fetchAvailability = async (serviceIds: string[], signal: AbortSignal, quantities?: string[]): Promise<Availability> => {
  let url = `${import.meta.env.PUBLIC_API_URL}availability/days/?service_ids=${serviceIds.join(',')}`;
  if (quantities && quantities.length > 0) {
    url += `&quantities=${quantities.join(',')}`;
  }
  const response = await fetch(url, { signal });

  if (!response.ok) {
    throw new Error('Failed to fetch availability');
  }

  const availableDates: string[] = await response.json();

  return {
    available: availableDates.map((d: string) => {
      const [year, month, day] = d.split('-').map(Number);
      return new Date(year, month - 1, day);
    }),
  };
};

export const fetchSlots = async (serviceIds: string[], date: string, signal?: AbortSignal, quantities?: string[]): Promise<string[]> => {
  let url = `${import.meta.env.PUBLIC_API_URL}availability/slots/?service_ids=${serviceIds.join(',')}&date=${date}`;
  if (quantities && quantities.length > 0) {
    url += `&quantities=${quantities.join(',')}`;
  }
  const response = await fetch(url, { signal });

  if (!response.ok) {
    throw new Error('Failed to fetch slots');
  }

  return await response.json();
};
