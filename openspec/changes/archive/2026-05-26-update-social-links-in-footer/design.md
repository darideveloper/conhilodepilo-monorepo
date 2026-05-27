## Context

The landing page footer renders social links from `FooterData.socialLinks` — an array of `{ icon, url }` objects. Currently three items exist: `Globe` (`#`), `Mail` (`mailto:...`), and `Instagram` (`#`). The backend `CompanyProfile` model has no social media fields, so all links are hardcoded in the footer component.

The user has provided real Instagram (`https://www.instagram.com/conhilodepilospain`) and TikTok (`https://www.tiktok.com/@conhilodepilo`) URLs. The design must make these configurable via the Django admin (stored in the model) but also fallback to sensible defaults when the API is unavailable.

The `@lucide/astro` icon library does not include a TikTok icon, so a custom SVG approach is needed.

## Goals / Non-Goals

**Goals:**
- Replace Instagram `#` placeholder with the real URL
- Add TikTok icon + link to the footer social links row
- Store `instagram_url` and `tiktok_url` on `CompanyProfile` model (configurable via admin)
- Expose new fields through `/api/config/` endpoint
- Add TypeScript types and frontend fallback defaults
- Custom SVG icon for TikTok (not available in Lucide)

**Non-Goals:**
- Not adding other social platforms (Facebook, Twitter/X, YouTube, etc.)
- Not removing the existing `Globe` or `Mail` icons
- Not modifying the booking flow or any page beyond the landing footer
- Not adding social link management to any frontend admin panel — only Django admin

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **TikTok icon** | Integrated SVG in `Icon.astro` | Lucide has no TikTok icon. Adding it to the existing `Icon.astro` atom keeps the implementation consistent and avoids breaking the footer's icon loop |
| **Where to add social URLs** | Backend model + frontend fallback | API-driven for admin editability; fallback in `constants.ts` keeps the footer working when the API is down |
| **Field naming** | `instagram_url`, `tiktok_url` on `CompanyProfile` | Consistent with existing `contact_email`, `contact_phone` pattern — `_url` suffix makes the purpose clear |
| **Social link order** | Instagram → TikTok → Mail | Logical grouping: social platforms first, then contact. Globe remains first as a generic web link placeholder |
| **Migration strategy** | New nullable `URLField` with `blank=True, null=True` | No data migration needed; existing rows get `NULL` and the frontend falls back to constants |

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| TikTok branding may change (icon style) | The SVG is a simple, clean version. Easy to swap if needed |
| No admin UI awareness — staff may not know new fields exist | Fields are explicitly added to `CompanyProfileAdmin` fieldsets in `admin.py` |
| Instagram/TikTok URLs stored as plain text, no validation | `URLField` provides basic URL validation; no need for platform-specific validation |
