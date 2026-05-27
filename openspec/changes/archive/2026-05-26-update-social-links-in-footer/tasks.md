## 1. Backend — Model & API

- [x] 1.1 Add `instagram_url` and `tiktok_url` URLField columns to `CompanyProfile` model in `dashboard/booking/models.py`
- [x] 1.2 Generate and apply Django migration for the new fields
- [x] 1.3 Add the new fields to `CompanyProfileSerializer.fields` in `dashboard/booking/serializers.py`
- [x] 1.4 Add `instagram_url` and `tiktok_url` to `CompanyProfileAdmin` fieldsets in `dashboard/booking/admin.py`

## 2. Frontend — Types & Constants

- [x] 2.1 Add `instagram_url` and `tiktok_url` optional fields to `AppConfig` interface in `landing/src/lib/api/types.ts`
- [x] 2.2 Add default Instagram and TikTok URL fallbacks to `DEFAULT_CONTACT` in `landing/src/lib/constants.ts`

## 3. Frontend — Icons

- [x] 3.1 Update `landing/src/components/atoms/Icon.astro` to support a custom TikTok SVG when `name="TikTok"` is passed

## 4. Frontend — Footer Update

- [x] 4.1 Update `Footer.astro` frontmatter to derive `instagramUrl` and `tiktokUrl` from `config` (API) with fallbacks to `DEFAULT_CONTACT`
- [x] 4.2 Update `defaultFooterData.socialLinks` to use the derived URLs and reorder to: Globe, Instagram, TikTok, Mail
- [x] 4.3 Add `target="_blank"` and `rel="noopener noreferrer"` to the social link `<a>` tags in `Footer.astro`

## 5. Verify

- [x] 5.1 Run Django migration and confirm `/api/config/` returns the new fields
- [x] 5.2 Run landing dev server and visually verify footer icons render and link to the correct URLs
- [x] 5.3 Run `npm run lint` and `npm run typecheck` on the landing project
