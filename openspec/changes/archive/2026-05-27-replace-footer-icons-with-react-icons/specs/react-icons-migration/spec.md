## ADDED Requirements

### Requirement: Footer renders social icons via react-icons

The footer SHALL render social media icons using `react-icons` components instead of the `Icon.astro` wrapper. The following icon mappings SHALL apply:

| Link | react-icons component |
|------|----------------------|
| Globe | `FiGlobe` (feather) |
| Instagram | `FiInstagram` (feather) |
| TikTok | `SiTiktok` (simple-icons) |
| Mail | `FiMail` (feather) |
| MapPin | `FiMapPin` (feather) |
| MessageCircle | `FiMessageCircle` (feather) |

#### Scenario: Social links row renders React icons
- **WHEN** the footer renders the social links section
- **THEN** each link SHALL contain a `react-icons` component matching the mapping above

#### Scenario: TikTok icon renders without custom SVG
- **WHEN** the TikTok social link is rendered
- **THEN** it SHALL use `SiTiktok` from `react-icons/si` instead of the inline custom SVG

### Requirement: Icon.astro component removed

The `landing/src/components/atoms/Icon.astro` component SHALL be removed from the codebase.

#### Scenario: No remaining references to Icon.astro
- **WHEN** the migration is complete
- **THEN** there SHALL be no imports or references to `Icon.astro` in any file
- **AND** the `@lucide/astro` package SHALL be removed from `package.json`
