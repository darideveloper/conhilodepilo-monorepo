import type { ServiceCategory } from "./types";

let cachedData: ServiceCategory[] | null = null;

export async function fetchCategories(): Promise<ServiceCategory[]> {
  if (cachedData) {
    return cachedData;
  }

  const apiUrl = import.meta.env.PUBLIC_API_URL || "http://localhost:8000";
  
  try {
    const response = await fetch(`${apiUrl}/api/services/`);
    if (!response.ok) {
      throw new Error(`Failed to fetch services: ${response.statusText}`);
    }
    
    const data: ServiceCategory[] = await response.json();
    cachedData = data;
    return data;
  } catch (error) {
    console.error("Error fetching services:", error);
    return [];
  }
}
