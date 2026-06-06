## 1. Backend — Model & Admin

- [x] 1.1 Add `facebook_url = models.URLField(_("Facebook URL"), null=True, blank=True)` to `CompanyProfile` in `dashboard/booking/models.py`
- [x] 1.2 Generate migration: `python manage.py makemigrations`
- [x] 1.3 Add `"facebook_url"` to `CompanyProfileAdmin` fieldset in `dashboard/booking/admin.py` (under "Contact Information", after `tiktok_url`)
- [x] 1.4 Add `'facebook_url'` to `CompanyProfileSerializer` fields in `dashboard/booking/serializers.py`

## 2. Frontend — Types & Constants

- [x] 2.1 Add `facebook_url: string | null` to `AppConfig` interface in `landing/src/lib/api/types.ts`
- [x] 2.2 Add `facebook_url: "#"` to `DEFAULT_CONTACT` in `landing/src/lib/constants.ts`

## 3. Frontend — Footer & Icons

- [x] 3.1 Resolve Facebook URL in `Footer.astro`: `const facebookUrl = config?.facebook_url || DEFAULT_CONTACT.facebook_url;`
- [x] 3.2 Insert `{ icon: "Facebook", url: facebookUrl }` in `socialLinks` array between Instagram and TikTok
- [x] 3.3 Import `SiFacebook` from `react-icons/si` and add `Facebook: SiFacebook` to `iconMap` in `SocialIcons.tsx`

## 4. Verify

- [x] 4.1 Run Django migrations (auto-generated `0015_companyprofile_facebook_url.py`)
- [x] 4.2 Start landing dev server and confirm Facebook icon renders between Instagram and TikTok in the footer
- [x] 4.3 Confirm placeholder link `"#"` is used when no Facebook URL is configured
