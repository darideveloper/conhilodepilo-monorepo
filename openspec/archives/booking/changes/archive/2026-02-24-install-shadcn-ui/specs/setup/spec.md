# Spec: shadcn/ui Setup

This spec defines the installation and baseline configuration requirements for the **shadcn/ui** components.

## ADDED Requirements

### Requirement: Path Alias Configuration
The project SHALL support path aliases using `@/*` as the prefix to simplify imports and maintain component consistency.

#### Scenario: Verify Path Alias in tsconfig
- Given a `tsconfig.json` file.
- When `compilerOptions.paths["@/*"]` is defined to point to `./src/*`.
- Then the TypeScript compiler MUST resolve imports like `@/components/ui/button` to `src/components/ui/button.tsx`.

### Requirement: Essential Dependencies
The project SHALL include the core dependencies required for shadcn/ui components.

#### Scenario: Check Dependencies in package.json
- Given a `package.json` file.
- When `lucide-react`, `clsx`, `tailwind-merge`, and `tailwindcss-animate` are present in `dependencies`.
- Then the shadcn/ui components MUST be able to import these utilities.

### Requirement: shadcn/ui Initialization
The project SHALL have a valid `components.json` for managing components.

#### Scenario: Verify components.json Content
- Given a `components.json` file.
- When its configuration specifies `src/styles/global.css` and the path aliases `@/*`.
- Then the shadcn CLI MUST be able to add and update components in the project.

### Requirement: Utility Function
The project SHALL have a standard utility function for merging CSS classes.

#### Scenario: Verify cn utility
- Given a file `src/lib/utils.ts`.
- When the `cn` function is exported and uses `twMerge` with `clsx`.
- Then the components SHALL be able to handle conditional and complex Tailwind classes efficiently.
