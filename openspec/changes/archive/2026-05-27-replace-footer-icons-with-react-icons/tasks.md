## 1. Dependencies

- [x] 1.1 Install `react-icons` in the landing service
- [x] 1.2 Remove `@lucide/astro` from landing service dependencies

## 2. Create React Social Icons component

- [x] 2.1 Create `landing/src/components/molecules/SocialIcons.tsx` with `react-icons` imports (`FiGlobe`, `FiInstagram`, `SiTiktok`, `FiMail`)
- [x] 2.2 Export a `SocialIcons` component that renders the social links row with the same HTML structure and styling as the current Astro map

## 3. Update Footer.astro

- [x] 3.1 Import and render `<SocialIcons />` in place of the current `Icon.astro` social links map
- [x] 3.2 Replace MapPin and MessageCircle `Icon.astro` usage in the location and contact sections with `react-icons` components

## 4. Cleanup

- [x] 4.1 Delete `landing/src/components/atoms/Icon.astro` (refactored to use react-icons instead of @lucide/astro)
- [x] 4.2 Remove the `import Icon` line from `Footer.astro`
- [x] 4.3 Verify there are no remaining references to `@lucide/astro` or broken `Icon.astro` imports in the landing service

## 5. Verification

- [x] 5.1 Run `npm run build` to confirm no type/build errors
- [x] 5.2 Run `npm test` to confirm existing tests pass
- [x] 5.3 Visually verify footer renders all social icons correctly with no layout regressions
