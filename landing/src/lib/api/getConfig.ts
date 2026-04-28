import type { AppConfig } from "./types";

let cachedConfig: AppConfig | null = null;

export async function getConfig(): Promise<AppConfig | null> {
  if (cachedConfig) {
    return cachedConfig;
  }

  const apiUrl = import.meta.env.PUBLIC_API_URL || "http://localhost:8000";
  
  try {
    const response = await fetch(`${apiUrl}/api/config/`);
    if (!response.ok) {
      throw new Error(`Failed to fetch config: ${response.statusText}`);
    }
    
    const data: AppConfig = await response.json();
    cachedConfig = data;
    return data;
  } catch (error) {
    console.error("Error fetching config:", error);
    return null;
  }
}
