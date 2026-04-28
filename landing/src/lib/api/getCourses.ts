import type { Course } from "./types";
import { fetchCategories } from "./client";

export async function getCourses(): Promise<Course[]> {
  const categories = await fetchCategories();
  if (categories.length === 0) return [];

  const COURSES_GROUP_ID = Number(import.meta.env.PUBLIC_COURSES_GROUP_ID);
  const courseCategory = categories.find((cat) => cat.group_id === COURSES_GROUP_ID);

  if (!courseCategory) return [];

  return courseCategory.services.map((svc) => ({
    id: svc.id,
    title: svc.title,
    description: svc.description,
    price: svc.price,
    duration: svc.duration,
    image: svc.image,
  }));
}
