## Context

The landing page footer renders social links in `Footer.astro` from a `socialLinks` array, each `{ icon, url }` object mapped to a `react-icons` component in `SocialIcons.tsx`. URLs are sourced from the Django `/api/config/` endpoint (backed by `CompanyProfile` model) with hardcoded fallbacks in `landing/src/lib/constants.ts`.

Currently three social links exist: Globe, Instagram, TikTok, Mail. The proposal adds Facebook between Instagram and TikTok, following the exact same 8-layer flow as the existing social links.

## Goals / Non-Goals

**Goals:**
- Add `facebook_url` field on `CompanyProfile` model, configurable via Django admin
- Expose `facebook_url` through `/api/config/` API
- Render a Facebook icon in the footer, placed between Instagram and TikTok
- Use placeholder URL `#` by default (configurable via admin later)

**Non-Goals:**
- No changes to existing social link behavior or ordering (beyond inserting Facebook)
- No new UI patterns or components — reuse existing `SocialIcons` infrastructure
- No Facebook-specific validation on the URL field

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Icon library | `SiFacebook` from `react-icons/si` | Consistent with `SiTiktok` already in use; Simple Icons has a clean branded Facebook icon |
| Field name | `facebook_url` | Follows the `instagram_url` / `tiktok_url` naming convention |
| Default/fallback | `"#"` (placeholder) | Same pattern as the Globe link; will be replaced with real URL when available |
| Link order | Instagram → **Facebook** → TikTok | As requested — Facebook sits between Instagram and TikTok in the social links row |
| Admin placement | "Contact Information" fieldset, after `tiktok_url` | Keeps all social links grouped together |

## Risks / Trade-offs

- **[Low] Icon consistency**: `SiFacebook` is a filled-brand icon while `FiInstagram` is a Feather outline icon. This visual inconsistency already exists with `SiTiktok` next to `FiInstagram`. Acceptable as-is.
- **[Low] Placeholder dead link**: `"#"` will be a no-op link until admin sets a real URL. Same behavior as the Globe link.
