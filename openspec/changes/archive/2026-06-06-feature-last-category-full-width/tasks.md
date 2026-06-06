## 1. CategoryCard: Add isLast prop

- [x] 1.1 Add `isLast?: boolean` to the Props interface
- [x] 1.2 Destructure `isLast` with default value `false` in function signature
- [x] 1.3 Add conditional `md:col-span-2 md:flex-row` classes to article element via `cn()` when `isLast` is true
- [x] 1.4 Add conditional `md:max-w-[300px]` class to image wrapper div via `cn()` when `isLast` is true

## 2. CategoryShowcase: Wire up grid and isLast

- [x] 2.1 Remove `lg:grid-cols-3` from grid className (keep `grid-cols-1 md:grid-cols-2`)
- [x] 2.2 Add index parameter to `.map()` callback
- [x] 2.3 Pass `isLast={index === categories.length - 1}` to the last `CategoryCard`
