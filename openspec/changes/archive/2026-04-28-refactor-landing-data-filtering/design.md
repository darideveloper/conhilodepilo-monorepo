# Design: Landing Data Filtering Refactor

## Data Model Update
The `ServiceCategory` interface in the landing application needs to match the actual API response from the backend.

```typescript
export interface ServiceCategory {
  id: number;
  name: string;
  description: string | null;
  image: string | null;
  services: Service[];
  group_id: number; // Added field
}
```

## Filtering Strategy

### Environment Variables
The following variables must be defined in the `.env` files:
- `PUBLIC_COURSES_GROUP_ID`: The ID of the group representing Courses (e.g., `2`).
- `PUBLIC_SERVICES_GROUP_ID`: The ID of the group representing regular Services (e.g., `1`).

### Courses
Instead of `categories[0]`, we will look for categories belonging to the group defined by `PUBLIC_COURSES_GROUP_ID`.
Note: Since there might be multiple categories in the "Courses" group in the future, `getCourses` should ideally handle multiple categories or continue to pick the first one matching the group if that's the current UI requirement. Based on `CoursesSection.astro`, it expects an array of courses.

### Services
Instead of `categories.slice(1)`, we will filter categories based on the `PUBLIC_SERVICES_GROUP_ID`. Alternatively, we can filter out any category that belongs to the "Courses" group.

## Implementation Details

### getCourses.ts
Currently:
```typescript
return categories[0].services.map(...)
```
Proposed:
```typescript
const COURSES_GROUP_ID = Number(import.meta.env.PUBLIC_COURSES_GROUP_ID);
const courseCategory = categories.find(cat => cat.group_id === COURSES_GROUP_ID);
if (!courseCategory) return [];
return courseCategory.services.map(...)
```

### getServices.ts
Currently:
```typescript
return categories.slice(1);
```
Proposed:
```typescript
const COURSES_GROUP_ID = Number(import.meta.env.PUBLIC_COURSES_GROUP_ID);
return categories.filter(cat => cat.group_id !== COURSES_GROUP_ID);
```

