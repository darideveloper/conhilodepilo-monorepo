import { apiClient } from "../client";

export interface BookingPayload {
  fullName: string;
  email: string;
  serviceIds: string[];
  guests: number;
  specialRequests: string;
}

export async function submitBooking(payload: BookingPayload): Promise<void> {
  await apiClient<void>("bookings/", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}
