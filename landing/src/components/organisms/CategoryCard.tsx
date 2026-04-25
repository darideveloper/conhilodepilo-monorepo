import { useState } from "react";
import { cn } from "../../utils/cn";
import { ReactIcon } from "../atoms/ReactIcon";
import { marked } from "marked";
import type { ServiceCategory, Service } from "../../lib/api/types";

interface Props {
  category: ServiceCategory;
  className?: string;
}

export function CategoryCard({ category, className }: Props) {
  const [selectedService, setSelectedService] = useState<Service | null>(
    category.services[0] || null
  );

  const imgSrc = category.image || "";

  return (
    <article
      className={cn(
        "group/card flex flex-col bg-white border border-brand-primary/10 overflow-hidden transition-all rounded-2xl shadow-sm hover:shadow-lg h-full",
        className,
      )}
    >
      {/* Category Image */}
      <div className="relative overflow-hidden aspect-[4/3]">
        {imgSrc ? (
          <img
            src={imgSrc}
            alt={category.name}
            className="w-full h-full object-cover transition-transform duration-500 group-hover/card:scale-105"
            loading="lazy"
          />
        ) : (
          <div className="w-full h-full bg-gray-100 flex items-center justify-center">
            <ReactIcon name="LuImage" size={32} className="text-gray-300" />
          </div>
        )}
      </div>

      <div className="flex flex-col flex-1 gap-5 p-6">
        {/* Category Header */}
        <div className="flex flex-col gap-2">
          <h3 className="text-xl font-bold text-ui-text-main">{category.name}</h3>
          <div 
            className="text-sm text-ui-text-muted leading-relaxed line-clamp-3 prose prose-sm prose-p:my-0 prose-ul:my-0 prose-li:list-disc prose-li:ml-4"
            dangerouslySetInnerHTML={{ __html: category.description ? marked.parse(category.description) as string : "" }}
          />
        </div>

        {/* Service Selection */}
        <div className="flex flex-col gap-3">
          <p className="text-[10px] font-bold text-brand-secondary uppercase tracking-widest">
            Servicios disponibles
          </p>
          <div className="flex flex-wrap gap-2">
            {category.services.map((service) => (
              <button
                key={service.id}
                onClick={() => setSelectedService(service)}
                className={cn(
                  "px-3 py-2 rounded-xl text-[11px] font-bold uppercase tracking-wider transition-all border cursor-pointer",
                  selectedService?.id === service.id
                    ? "bg-brand-primary text-ui-text-main border-brand-primary shadow-sm"
                    : "bg-ui-bg-light text-ui-text-muted border-brand-primary/10 hover:border-brand-primary/40"
                )}
              >
                {service.title}
              </button>
            ))}
          </div>
        </div>

        {/* Selected Service Details & CTA */}
        {selectedService && (
          <div className="mt-auto pt-5 border-t border-brand-primary/10 flex items-center justify-between">
            <div className="flex flex-col gap-0.5">
              <span className="text-xl font-bold text-ui-text-main">
                {selectedService.price}
              </span>
              <small className="flex items-center gap-1.5 text-[10px] text-ui-text-muted uppercase font-bold tracking-wider">
                <ReactIcon name="LuClock" size={14} className="text-brand-primary" />
                {selectedService.duration} min
              </small>
            </div>
            <button
              onClick={() => {
                if (selectedService) {
                  window.location.href = `/booking/${selectedService.id}`;
                }
              }}
              className="bg-brand-primary text-ui-text-main px-5 py-2.5 rounded-xl text-xs font-bold uppercase tracking-widest hover:bg-brand-primary/90 transition-all hover:scale-[1.03] active:scale-95 shadow-sm cursor-pointer"
            >
              Reservar
            </button>
          </div>
        )}
      </div>
    </article>
  );
}
