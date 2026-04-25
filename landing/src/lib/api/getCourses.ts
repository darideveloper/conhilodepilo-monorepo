import type { Course } from "./types";
import { fetchCategories } from "./client";

export async function getCourses(): Promise<Course[]> {
  const categories = await fetchCategories();
  if (categories.length === 0) return [];

  return categories[0].services.map((svc) => ({
    id: svc.id,
    title: svc.title,
    description: svc.description,
    price: svc.price,
    duration: svc.duration,
    image: svc.image,
  }));
}
