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
        "grid grid-cols-1 md:grid-cols-2 gap-8 w-full px-4",
        className
      )}
    >
      {categories.map((category, index) => (
        <CategoryCard
          key={category.id}
          category={category}
          isLast={index === categories.length - 1}
        />
      ))}
    </div>
  );
}
