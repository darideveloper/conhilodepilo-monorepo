import { cn } from "../../utils/cn";
import { CategoryCard } from "./CategoryCard";
import type { ServiceCategory } from "../../lib/api/types";

interface Props {
  categories: ServiceCategory[];
  className?: string;
}

export function CategoryShowcase({ categories, className }: Props) {
  return (
    <div
      className={cn(
        "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 w-full px-4",
        className
      )}
    >
      {categories.map((category) => (
        <CategoryCard key={category.id} category={category} />
      ))}
    </div>
  );
}
