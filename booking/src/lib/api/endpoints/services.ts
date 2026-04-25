import { apiClient } from "../client";

export interface BackendService {
  id: number;
  title: string;
  description: string;
  price: string;
  duration: number;
  image: string;
}

export interface BackendServiceCategory {
  id: number;
  name: string;
  description: string;
  image: string;
  services: BackendService[];
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
}

export async function fetchServices(): Promise<ServiceCategory[]> {
  const data = await apiClient<BackendServiceCategory[]>("services/");
  
  return data.map((category) => ({
    ...category,
    id: String(category.id),
    services: category.services.map((service) => ({
      ...service,
      id: String(service.id),
      dates: { limited: [], booked: [] } // Fallback defaults
    }))
  }));
}
