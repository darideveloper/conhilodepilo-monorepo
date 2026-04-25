import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, Pagination } from 'swiper/modules';
import { cn } from '../../utils/cn';

// Swiper styles
import 'swiper/css';
import 'swiper/css/pagination';

import './HeroSlider.css';

interface CTA {
  label: string;
  href: string;
}

interface SlideData {
  badge?: string;
  title: string;
  titleAccent?: string;
  description: string;
  primaryCta: CTA;
  secondaryCta?: CTA;
  image: string;
  imageAlt: string;
}

interface HeroSliderProps {
  slides: SlideData[];
}

const Badge = ({ children, variant = 'primary', className }: { children: React.ReactNode; variant?: 'primary' | 'secondary'; className?: string }) => {
  const variants = {
    primary: "bg-brand-primary/15 text-ui-text-main border-brand-primary/30",
    secondary: "bg-brand-secondary/15 text-ui-text-main border-brand-secondary/30",
  };
  const baseClasses = "inline-flex items-center px-3 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase border";
  return (
    <span className={cn(baseClasses, variants[variant], className)}>
      {children}
    </span>
  );
};

const Button = ({ children, variant = 'primary', size = 'md', href, className }: { children: React.ReactNode; variant?: 'primary' | 'outline' | 'ghost'; size?: 'sm' | 'md' | 'lg'; href?: string; className?: string }) => {
  const variants = {
    primary: "bg-brand-primary text-ui-text-main hover:bg-brand-primary/90 shadow-sm",
    outline: "border-2 border-brand-primary text-ui-text-main hover:bg-brand-primary/10",
    ghost: "text-ui-text-main hover:bg-brand-primary/10",
  };
  const sizes = {
    sm: "px-4 py-2 text-sm",
    md: "px-6 py-3 text-base",
    lg: "px-8 py-4 text-lg",
  };
  const baseClasses = "inline-flex items-center justify-center rounded-lg font-bold transition-all hover:scale-[1.02] cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed";

  if (href) {
    return (
      <a href={href} className={cn(baseClasses, variants[variant], sizes[size], className)}>
        {children}
      </a>
    );
  }
  return (
    <button className={cn(baseClasses, variants[variant], sizes[size], className)}>
      {children}
    </button>
  );
};

export default function HeroSlider({ slides }: HeroSliderProps) {
  return (
    <div className="relative w-full overflow-hidden bg-ui-bg-light">
      <Swiper
        modules={[Autoplay, Pagination]}
        loop={true}
        speed={800}
        autoplay={{
          delay: 5000,
          disableOnInteraction: false,
        }}
        pagination={{
          el: '.hero-pagination',
          clickable: true,
          renderBullet: (_, className) => {
            return `<button class="${className} hero-slider-bullet" aria-label="Ir al slide"></button>`;
          },
        }}
        className="hero-swiper-main w-full"
      >
        {slides.map((slide, index) => (
          <SwiperSlide key={index}>
            <div className="container relative z-10 py-10 lg:py-16">
              <div className="grid min-h-[78vh] items-center gap-12 lg:grid-cols-[1.02fr_0.98fr] lg:gap-16">
                {/* Columna izquierda */}
                <div className="flex max-w-[34rem] mx-auto lg:mx-0 flex-col items-center text-center lg:items-start lg:text-left justify-center">
                  {slide.badge && (
                    <div className="mb-6">
                      <Badge variant="primary" className="text-brand-primary/70">
                        {slide.badge}
                      </Badge>
                    </div>
                  )}

                  <h1 className="text-ui-text-main text-[clamp(3.5rem,7vw,5.25rem)] font-black leading-[0.9] tracking-[-0.04em]">
                    {slide.title}
                    {slide.titleAccent && (
                      <>
                        <br />
                        <span className="font-black italic text-brand-primary">
                          {slide.titleAccent}
                        </span>
                      </>
                    )}
                  </h1>

                  <p className="mt-8 max-w-[31rem] text-[1.15rem] leading-[1.7] text-ui-text-muted">
                    {slide.description}
                  </p>

                  <div className="mt-8 flex flex-wrap justify-center lg:justify-start gap-4">
                    <Button size="md" href={slide.primaryCta.href}>
                      {slide.primaryCta.label}
                    </Button>

                    {slide.secondaryCta && (
                      <Button variant="outline" size="md" href={slide.secondaryCta.href}>
                        {slide.secondaryCta.label}
                      </Button>
                    )}
                  </div>
                </div>

                {/* Columna derecha */}
                <div className="flex flex-col items-center lg:items-start">
                  <div className="w-full max-w-[34rem]">
                    <div className="relative p-4 group">
                      <div className="absolute inset-0 rounded-2xl bg-brand-primary/20 -rotate-3 will-change-transform [backface-visibility:hidden] transition-all duration-[400ms] ease-[cubic-bezier(0.34,1.56,0.64,1)] group-hover:rotate-0 group-hover:translate-x-2 group-hover:-translate-y-2"></div>
                      <div className="absolute inset-4 rounded-2xl bg-brand-secondary/10 -rotate-3 will-change-transform [backface-visibility:hidden] transition-all duration-[400ms] ease-[cubic-bezier(0.34,1.56,0.64,1)] group-hover:rotate-0 group-hover:translate-x-2 group-hover:-translate-y-2"></div>

                      <div className="relative rounded-2xl overflow-hidden aspect-[4/5] shadow-image">
                        <img
                          src={slide.image}
                          alt={slide.imageAlt}
                          loading="eager"
                          decoding="async"
                          className="w-full h-full object-cover block"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>

      {/* Pagination Container - positioned absolute relative to the slider container */}
      <div className="absolute bottom-8 left-0 right-0 z-20">
        <div className="hero-pagination flex justify-center items-center gap-3"></div>
      </div>
    </div>
  );
}
