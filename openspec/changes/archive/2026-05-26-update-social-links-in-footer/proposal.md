## Why

The website currently has placeholder social media links (`#`) in the footer — Instagram is a dead link and TikTok is entirely absent. Real business accounts exist on both platforms (`@conhilodepilospain` on Instagram, `@conhilodepilo` on TikTok) and should be linked to drive traffic, improve brand credibility, and enable social proof.

## What Changes

- Replace the Instagram placeholder `#` with `https://www.instagram.com/conhilodepilospain`
- Add a new TikTok icon/link to `https://www.tiktok.com/@conhilodepilo`
- Add `instagram_url` and `tiktok_url` fields to the `CompanyProfile` Django model so links are editable via admin instead of hardcoded
- Expose the new fields through the `/api/config/` endpoint
- Add corresponding fields to the `AppConfig` TypeScript type on the landing side
- Add fallback defaults in `constants.ts` so the links work even when the API is unavailable
- The `Globe` placeholder icon (currently `#`) should remain as-is or be removed — no real website URL exists yet

## Capabilities

### New Capabilities
- `social-links-api`: API support for configurable social media URLs (Instagram, TikTok) on the `CompanyProfile` model, served via `/api/config/`

### Modified Capabilities
*(None — no existing capability specs change at the requirement level)*

## Impact

- **Backend** (`dashboard/`): `CompanyProfile` model gets 2 new fields; serializer and view update automatically; admin form includes the new fields; migration required
- **Frontend** (`landing/`): `AppConfig` TypeScript type gains 2 new optional fields; footer component uses them with fallback defaults; a TikTok icon needs to be rendered (Lucide may not have TikTok — may need a custom SVG or third-party icon)
- **Shared**: Booking app also uses `@lucide/astro` icons — verify TikTok icon availability across both landing and booking packages
- **No API breaking changes** — new fields are additive
