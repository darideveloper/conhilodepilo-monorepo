# Tasks: Install and Setup shadcn/ui

- [x] **Infrastructure Setup**
    - [x] Update `tsconfig.json` to include path aliases and React JSX settings.
    - [x] Install dependencies: `lucide-react`, `clsx`, `tailwind-merge`, `tailwindcss-animate`, `class-variance-authority`.
    - [x] Add and configure `@astrojs/react` integration.

- [x] **Initialize shadcn/ui**
    - [x] Create `components.json` with correct paths and styles.
    - [x] Create `src/lib/utils.ts` with the `cn` utility.

- [x] **Styling Integration**
    - [x] Update `src/styles/global.css` with brand-aligned shadcn/ui variables.

- [x] **Verification**
    - [x] Add the Button component: `npx shadcn@latest add button`.
    - [x] Render the Button component in `src/pages/index.astro`.
    - [x] Successfully build the project with `npm run build`.
    - [x] Run `openspec validate install-shadcn-ui`.
