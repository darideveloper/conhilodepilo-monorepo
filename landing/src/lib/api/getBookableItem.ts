import type { Service, Course } from "./types";
import { getServices } from "./getServices";
import { getCourses } from "./getCourses";

export async function getBookableItem(id: number): Promise<Service | Course | null> {
  const [services, courses] = await Promise.all([getServices(), getCourses()]);
  
  const service = services.find(s => s.id === id);
  if (service) return service;
  
  const course = courses.find(c => c.id === id);
  if (course) return course;
  
  return null;
}
