import type { Service, ServiceCategory } from "./types";
import { fetchCategories } from "./client";

export async function getServices(): Promise<Service[]> {
  const categories = await fetchCategories();
  if (categories.length === 0) return [];

  // Flatten categories 1+ into a single services array
  return categories.slice(1).flatMap((cat) =>
    cat.services.map((svc) => ({
      ...svc,
      category: cat.name,
      image: svc.image || cat.image,
    }))
  );
}

export async function getServiceCategories(): Promise<ServiceCategory[]> {
  const categories = await fetchCategories();
  if (categories.length === 0) return [];

  // Return categories 1+ (excluding courses)
  return categories.slice(1);
}
