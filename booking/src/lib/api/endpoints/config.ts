import { apiClient } from "../client";
import type { AppConfig } from "../../../store/useBookingStore";

export async function fetchConfig(): Promise<AppConfig> {
  return apiClient<AppConfig>("config/");
}
