## Context

The landing page footer uses `Icon.astro` — a thin wrapper over `@lucide/astro` with a custom inline SVG fallback for TikTok (which Lucide doesn't ship). The project already has React 19 and `@astrojs/react` integrated. Standardising on React-based icons simplifies the component tree, reduces the number of icon strategies to one, and eliminates the need for `@lucide/astro`.

## Goals / Non-Goals

**Goals:**
- Replace all `Icon.astro` usage in `Footer.astro` with `react-icons`
- Remove the `@lucide/astro` dependency from the landing service
- Deprecate and delete the `Icon.astro` wrapper component
- Provide TikTok icon via `react-icons` (Simple Icons set) instead of a custom SVG

**Non-Goals:**
- Migrating other parts of the landing page beyond the footer (future work)
- Changing the visual appearance or layout of the footer
- Replacing the MapPin icon used in the location section (included since it's also rendered through Icon.astro)

## Decisions

1. **Use `react-icons` over `lucide-react`** — `react-icons` provides TikTok (`SiTiktok`) out of the box, eliminating the need for custom SVG assets. `lucide-react` has the same TikTok gap as `@lucide/astro`.

2. **Inline React icon components in `Footer.astro` via `client:only`** — Since `Footer.astro` is a static Astro component, React icons need to be rendered in a React island. The social links row will become a lightweight React component (`SocialIcons`) rendered with `client:only="react"`.

3. **Same icon mapping** — Globe → `FiGlobe`, Instagram → `FiInstagram`, TikTok → `SiTiktok`, Mail → `FiMail`, MapPin → `FiMapPin`, MessageCircle → `FiMessageCircle`.

## Risks / Trade-offs

- [**Bundle size**] `react-icons` is tree-shakeable with ESM, so importing only the needed icons will keep the footprint minimal.
- [**Waterfall**] Adding a handful of React islands for static components adds client-side JS. Mitigation: scope the React island to the smallest interactive unit (the social links row only).
