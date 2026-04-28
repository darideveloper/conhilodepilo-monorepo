import type { Service, ServiceCategory } from "./types";
import { fetchCategories } from "./client";

export async function getServices(): Promise<Service[]> {
  const categories = await fetchCategories();
  if (categories.length === 0) return [];

  const COURSES_GROUP_ID = Number(import.meta.env.PUBLIC_COURSES_GROUP_ID);

  // Flatten categories (excluding courses) into a single services array
  return categories
    .filter((cat) => cat.group_id !== COURSES_GROUP_ID)
    .flatMap((cat) =>
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

  const COURSES_GROUP_ID = Number(import.meta.env.PUBLIC_COURSES_GROUP_ID);

  // Return categories (excluding courses)
  return categories.filter((cat) => cat.group_id !== COURSES_GROUP_ID);
}
