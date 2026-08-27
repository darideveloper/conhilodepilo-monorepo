# email-delivery Specification

## Purpose
TBD - created by archiving change onboard-conhilodepilo-email. Update Purpose after archive.
## Requirements
### Requirement: Inbound email routes to Stalwart via MX
The system SHALL deliver inbound email for `conhilodepilo.com` to the Stalwart server by publishing `MX @ → 10 mail.darideveloper.com.` in the Cloudflare zone, replacing the old Skynet MX (`10 mx.conhilodepilo.com`).

#### Scenario: MX record points at Stalwart
- **WHEN** the MX swap has been performed
- **THEN** `dig MX conhilodepilo.com` returns `10 mail.darideveloper.com.`
- **AND** no old Skynet MX or `mx/imap/pop3/smtp/webmail` `A` records remain in the zone

#### Scenario: Email to info@ is delivered to Stalwart
- **WHEN** an external sender sends to `info@conhilodepilo.com` after the swap
- **THEN** the message arrives in the `info@conhilodepilo.com` mailbox on `mail.darideveloper.com` (IMAP :993)

#### Scenario: Cloudflare Email Routing remains disabled
- **WHEN** the Cloudflare zone is managed for this domain's email
- **THEN** Cloudflare "Email Routing" is NOT enabled
- **AND** no `_dc-mx` rewrite is injected into the zone

### Requirement: Stalwart accounts and aliases provisioned for conhilodepilo.com
The system SHALL have a `no-reply@conhilodepilo.com` user account and SHALL retain `info@conhilodepilo.com` with aliases `postmaster@conhilodepilo.com` and `abuse@conhilodepilo.com` forwarding to it, all on the Stalwart server.

#### Scenario: Required addresses resolve to real mailboxes
- **WHEN** mail is sent to `postmaster@conhilodepilo.com` or `abuse@conhilodepilo.com`
- **THEN** it is delivered to `info@conhilodepilo.com`

#### Scenario: Dedicated dashboard sender exists
- **WHEN** the dashboard authenticates to SMTP
- **THEN** it uses the `no-reply@conhilodepilo.com` account on `mail.darideveloper.com:465`

### Requirement: Published DNS authentication records for conhilodepilo.com
The Cloudflare zone SHALL publish SPF, DKIM (both `v1-rsa-20260823` and `v1-ed25519-20260823` selectors), DMARC (`p=none`), TLS-RPT, and CAA (allowing `letsencrypt.org` and `zerossl.com`) records, all DNS-only (grey-cloud).

#### Scenario: SPF authorizes only the Stalwart host
- **WHEN** `dig TXT conhilodepilo.com` is run
- **THEN** it returns a single SPF record `v=spf1 mx a:mail.darideveloper.com -all`
- **AND** no old `redirect=spf.dominioabsoluto.net` record remains

#### Scenario: DKIM keys are published under the generated selectors
- **WHEN** `dig TXT v1-rsa-20260823._domainkey.conhilodepilo.com` and `v1-ed25519-20260823._domainkey.conhilodepilo.com` are run
- **THEN** each returns a `v=DKIM1; p=<key>` TXT record matching Stalwart's generated public keys

#### Scenario: DMARC and TLS-RPT published
- **WHEN** `dig TXT _dmarc.conhilodepilo.com` and `_smtp._tls.conhilodepilo.com` are run
- **THEN** they return `v=DMARC1; p=none; rua=mailto:postmaster@conhilodepilo.com` and `v=TLSRPTv1; rua=mailto:postmaster@conhilodepilo.com` respectively

#### Scenario: CAA allows both certificate authorities in use
- **WHEN** `dig CAA conhilodepilo.com` is run
- **THEN** it returns `0 issue "letsencrypt.org"` and `0 issue "zerossl.com"`

### Requirement: Authenticated sending via Stalwart
Outbound mail sent as `info@conhilodepilo.com` or `no-reply@conhilodepilo.com` SHALL pass SPF, DKIM, and DMARC validation at the receiving side before the MX swap is performed.

#### Scenario: Gmail receives an authenticated test message
- **WHEN** a message is sent from `info@conhilodepilo.com` via `mail.darideveloper.com:465` to a Gmail address
- **THEN** the original headers show `spf=pass`, `dkim=pass`, and `dmarc=pass`
- **AND** the DKIM signature selector matches `v1-rsa-20260823`

#### Scenario: mail-tester score is clean
- **WHEN** a message is sent from `info@conhilodepilo.com` to the `mail-tester.com` check address
- **THEN** the score is at least 9/10

### Requirement: Dashboard booking email sends via Stalwart
The Django dashboard SHALL send booking confirmation email through `mail.darideveloper.com:465` using the `no-reply@conhilodepilo.com` credentials configured via the `EMAIL_*` environment variables, with no dependency on Skynet.

#### Scenario: Test email sent through Stalwart
- **WHEN** `GET /api/test-email/?to=<recipient>` is called on the dashboard
- **THEN** it responds `{"message":"Test email sent successfully", "to":[...]}`
- **AND** the message is transmitted to the recipient via the Stalwart SMTP server

#### Scenario: Booking confirmation uses Stalwart SMTP
- **WHEN** a booking is confirmed (non-gift) on the dashboard
- **THEN** the confirmation email is sent via the `EMAIL_HOST`/`EMAIL_PORT` configuration pointing at `mail.darideveloper.com:465`

#### Scenario: Example env files use generic placeholders
- **WHEN** a developer reads `dashboard/.env.prod.example` or `dashboard/.env.dev.example`
- **THEN** the `EMAIL_*` values are generic dummy placeholders (`smtp.example.com`, `sender@example.com`, `change-me`) with no real production host, account, or secret
- **AND** they contain no references to the production mail host or this domain

### Requirement: Web and dashboard regressions prevented
The email cutover SHALL NOT break the existing `conhilodepilo.com`, `www`, `dashboard`, or `booking` web properties.

#### Scenario: Web properties resolve after MX swap
- **WHEN** the MX swap and record cleanup have been performed
- **THEN** `conhilodepilo.com`, `www.conhilodepilo.com`, `dashboard.conhilodepilo.com`, and `booking.conhilodepilo.com` still resolve to `5.78.126.131` and serve their applications

