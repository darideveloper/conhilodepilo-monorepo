import { cn } from "../../utils/cn";
import { ReactIcon } from "../atoms/ReactIcon";

interface Props {
  title: string;
  price?: string;
  duration?: number;
  description?: React.ReactNode;
  image: string | null;
  category?: string;
  className?: string;
  variant?: "primary" | "outline" | "ghost";
}

export function ServiceCard({
  title,
  price,
  duration,
  description,
  image,
  category,
  className,
  variant = "outline",
}: Props) {
  const imgSrc = image || "";

  // Badge styles mapping
  const badgeVariants = {
    primary: "bg-brand-primary/15 text-ui-text-main border-brand-primary/30",
    secondary: "bg-brand-secondary/15 text-ui-text-main border-brand-secondary/30",
  };
  const badgeBaseClasses =
    "inline-flex items-center px-3 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase border";

  // Button styles mapping
  const buttonVariants = {
    primary: "bg-brand-primary text-ui-text-main hover:bg-brand-primary/90 shadow-sm",
    outline: "border-2 border-brand-primary text-ui-text-main hover:bg-brand-primary/10",
    ghost: "text-ui-text-main hover:bg-brand-primary/10",
  };
  const buttonSizes = {
    sm: "px-4 py-2 text-sm",
    md: "px-6 py-3 text-base",
    lg: "px-8 py-4 text-lg",
  };
  const buttonBaseClasses =
    "inline-flex items-center justify-center rounded-lg font-bold transition-all hover:scale-[1.02] cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed";

  return (
    <article
      className={cn(
        "group/card flex flex-col bg-white border border-brand-primary/10 overflow-hidden transition-all rounded-2xl shadow-sm hover:shadow-lg cursor-pointer h-full",
        className,
      )}
    >
      <div className="relative overflow-hidden aspect-[4/3]">
        {price && (
          <span
            className={cn(
              badgeBaseClasses,
              badgeVariants.primary,
              "absolute top-4 right-4 z-20 bg-white border-brand-primary/50"
            )}
          >
            {price}
          </span>
        )}
        {imgSrc ? (
          <img
            src={imgSrc}
            alt={title}
            className="w-full h-full object-cover transition-transform duration-500 group-hover/card:scale-105"
            loading="lazy"
          />
        ) : (
          <div className="w-full h-full bg-gray-100 flex items-center justify-center">
            <ReactIcon name="LuImage" size={32} className="text-gray-300" />
          </div>
        )}
      </div>

      <div className="flex flex-col flex-1 gap-3 p-6">
        <div className="flex flex-col gap-1">
          <h3 className="text-bold">{title}</h3>
          {duration ? (
            <small className="flex items-center gap-1 text-ui-text-muted">
              <ReactIcon name="LuClock" size={14} />
              {duration} min
            </small>
          ) : null}
        </div>

        <p className="text-ui-text-muted flex-1">{description}</p>

        <button
          className={cn(
            buttonBaseClasses,
            buttonVariants[variant],
            buttonSizes.sm,
            "w-full mt-auto uppercase"
          )}
        >
          Reservar ahora
        </button>
      </div>
    </article>
  );
}