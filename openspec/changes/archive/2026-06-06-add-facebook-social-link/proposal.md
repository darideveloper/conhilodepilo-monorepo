## Why

The landing page footer currently renders Instagram and TikTok social links but has no Facebook link. Adding Facebook gives customers another familiar channel to follow the business, increasing brand touchpoints and social proof.

## What Changes

- Add `facebook_url` field to `CompanyProfile` Django model (nullable, configurable via admin)
- Expose `facebook_url` via `/api/config/` endpoint
- Add `facebook_url` to frontend TypeScript types and hardcoded fallback constant (placeholder `#`)
- Resolve Facebook URL in `Footer.astro` (API first, fallback to default)
- Insert Facebook icon/link in the social links row **between** Instagram and TikTok
- Import and map `SiFacebook` (Simple Icons via `react-icons/si`) in `SocialIcons.tsx`

## Capabilities

### New Capabilities
- `facebook-social-link`: Store, serve, and render a Facebook URL in the landing page footer, matching the existing Instagram/TikTok pattern across all layers (model → admin → serializer → API → types → fallback → footer → icon).

### Modified Capabilities
*(none — no existing specs are changing)*

## Impact

- **`dashboard/booking/models.py`**: New `facebook_url` field on `CompanyProfile`
- **`dashboard/booking/migrations/`**: New auto-generated migration
- **`dashboard/booking/admin.py`**: Add field to "Contact Information" fieldset
- **`dashboard/booking/serializers.py`**: Add to serializer fields
- **`landing/src/lib/api/types.ts`**: Add `facebook_url: string | null` to `AppConfig`
- **`landing/src/lib/constants.ts`**: Add `facebook_url: "#"` fallback to `DEFAULT_CONTACT`
- **`landing/src/components/organisms/Footer.astro`**: Resolve URL, insert into `socialLinks` array
- **`landing/src/components/molecules/SocialIcons.tsx`**: Import `SiFacebook`, add to `iconMap`
