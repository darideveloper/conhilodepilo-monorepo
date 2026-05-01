import { apiClient } from "../client";

export interface DashboardService {
  id: number;
  title: string;
  description: string;
  price: string;
  duration: number;
  image: string;
}

export interface DashboardServiceCategory {
  id: number;
  name: string;
  description: string;
  image: string;
  services: DashboardService[];
  group_id: number | null;
}

export interface ServiceDates {
  limited: string[];
  booked: string[];
}

export interface Service {
  id: string;
  title: string;
  description: string;
  price: string;
  duration: number;
  image: string;
  dates: ServiceDates;
}

export interface ServiceCategory {
  id: string;
  name: string;
  description: string;
  image: string;
  services: Service[];
  group_id: string | null;
}

export async function fetchServices(): Promise<ServiceCategory[]> {
  const data = await apiClient<DashboardServiceCategory[]>("services/");
  
  return data.map((category) => ({
    ...category,
    id: String(category.id),
    group_id: category.group_id ? String(category.group_id) : null,
    services: category.services.map((service) => ({
      ...service,
      id: String(service.id),
      dates: { limited: [], booked: [] } // Fallback defaults
    }))
  }));
}
