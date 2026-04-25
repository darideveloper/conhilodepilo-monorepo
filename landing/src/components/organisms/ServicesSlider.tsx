import { useState, useMemo } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Pagination, Navigation } from "swiper/modules";
import { ServiceCard } from "../molecules/ServiceCard";
import { ReactIcon } from "../atoms/ReactIcon";
import { cn } from "../../utils/cn";

// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
import "./ServicesSlider.css";

import type { Service } from "../../lib/api/types";

interface Props {
  services: Service[];
  className?: string;
}

export function ServicesSlider({ services, className }: Props) {
  const [activeCategory, setActiveCategory] = useState<string>("all");

  // Extract unique categories
  const categories = useMemo(() => {
    const cats = new Set(services.map((s) => s.category));
    return ["all", ...Array.from(cats)];
  }, [services]);

  // Filter services based on active category
  const filteredServices = useMemo(() => {
    if (activeCategory === "all") return services;
    return services.filter((s) => s.category === activeCategory);
  }, [services, activeCategory]);

  return (
    <div className={cn("flex flex-col gap-8 w-full", className)}>
      {/* Category Filter */}
      <div className="flex flex-wrap justify-center gap-2">
        {categories.map((category) => (
          <button
            key={category}
            onClick={() => setActiveCategory(category)}
            className={cn(
              "px-4 py-2 rounded-full text-sm font-bold uppercase tracking-widest transition-all border",
              activeCategory === category
                ? "bg-brand-primary text-ui-text-main border-brand-primary"
                : "bg-transparent text-ui-text-muted border-brand-primary/20 hover:border-brand-primary"
            )}
          >
            {category === "all" ? "Todos" : category}
          </button>
        ))}
      </div>

      {/* Swiper Slider */}
      <div className="w-full relative px-4 md:px-12 group">
        {/* Custom Navigation Buttons */}
        <button className="swiper-button-prev-custom absolute left-0 top-[40%] -translate-y-1/2 z-10 w-10 h-10 flex items-center justify-center bg-white rounded-full border border-brand-primary/20 shadow-sm text-ui-text-main hover:bg-brand-primary/10 transition-all disabled:opacity-50 disabled:cursor-not-allowed">
          <ReactIcon name="LuChevronLeft" size={24} />
        </button>
        <button className="swiper-button-next-custom absolute right-0 top-[40%] -translate-y-1/2 z-10 w-10 h-10 flex items-center justify-center bg-white rounded-full border border-brand-primary/20 shadow-sm text-ui-text-main hover:bg-brand-primary/10 transition-all disabled:opacity-50 disabled:cursor-not-allowed">
          <ReactIcon name="LuChevronRight" size={24} />
        </button>

        <Swiper
          modules={[Pagination, Navigation]}
          spaceBetween={24}
          slidesPerView={1}
          loop={true}
          navigation={{
            prevEl: '.swiper-button-prev-custom',
            nextEl: '.swiper-button-next-custom',
          }}
          pagination={{ clickable: true, dynamicBullets: true }}
          breakpoints={{
            640: {
              slidesPerView: 2,
            },
            1024: {
              slidesPerView: 3,
            },
            1280: {
              slidesPerView: 4,
            },
          }}
          className="w-full !pb-12"
        >
          {filteredServices.map((service) => (
            <SwiperSlide key={service.id} className="!h-auto flex">
              <ServiceCard
                className="w-full"
                title={service.title}
                price={service.price}
                duration={service.duration}
                description={service.description}
                image={service.image}
                category={service.category}
                variant="outline"
              />
            </SwiperSlide>
          ))}
        </Swiper>
      </div>
    </div>
  );
}
