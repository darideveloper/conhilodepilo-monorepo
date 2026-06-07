## MODIFIED Requirements

### Requirement: Email uses company branding from CompanyProfile
The email SHALL use the company name, brand color, and social media URLs from `CompanyProfile`. The company logo SHALL NOT be displayed in the email template.

#### Scenario: Company name appears in email header
- **WHEN** a confirmation email is sent
- **THEN** the email header displays the company name from `CompanyProfile`
- **AND** the company logo is not included or rendered

#### Scenario: Social links rendered in email footer
- **WHEN** a confirmation email is sent
- **THEN** the email footer contains links to Instagram, TikTok, and Facebook from `CompanyProfile`
