## Why

`info@conhilodepilo.com` still routes to the old Acens/Skynet mail host (`MX 10 mx.conhilodepilo.com` → `217.116.0.227`), which is being retired and is already failing (Skynet IMAP no longer reachable for re-import). Email must be fully operational on the existing Stalwart server (`mail.darideveloper.com`, VPS `5.78.126.131`) before the old MX records are removed and the Acens contract is cancelled.

## What Changes

- **DNS (Cloudflare, all DNS-only/grey):** publish SPF, DKIM (both selectors), DMARC `p=none`, TLS-RPT, and CAA for `conhilodepilo.com`; then swap `MX @` from `10 mx.conhilodepilo.com` to `10 mail.darideveloper.com.` and delete all old Skynet records (`A mx/imap/pop3/smtp/webmail` → `217.116.0.x`, old SPF `redirect=spf.dominioabsoluto.net`).
- **Stalwart:** add a dedicated `no-reply@conhilodepilo.com` sending account (aliases `postmaster@`/`abuse@` → `info@` already exist; `info@` mailbox already restored and verified: 4,147 emails).
- **Dashboard (Django):** point SMTP env vars at Stalwart (`mail.darideveloper.com:465`, SSL) so booking confirmation emails no longer depend on Skynet; verify via `/api/test-email/`. Update the dashboard `.env` files — committed examples (`.env.prod.example`, `.env.dev.example`) get generic dummy SMTP placeholders, and the gitignored real files (`.env.prod`, `.env.dev`) get the actual credentials.
- **Housekeeping:** re-enable Stalwart admin 2FA (top server security item; the admin UI is already in use for this migration) and run the optional cleanups (delete the `yourdomain.com` demo account, revert the temporarily-raised JMAP upload limits, disable Ed25519 DKIM signing).
- **Verification:** authenticated sending (SPF/DKIM/DMARC pass in Gmail headers, `mail-tester.com` ≥ 9/10) BEFORE the MX swap; inbound + outbound + web regression checks AFTER the swap.

## Capabilities

### New Capabilities
- `email-delivery`: Stalwart-hosted email service for `conhilodepilo.com` — account/alias provisioning, DNS authentication records (SPF/DKIM/DMARC/TLS-RPT/CAA), authenticated sending and receiving via `mail.darideveloper.com:465/993`, and the dashboard's SMTP integration with Stalwart.

### Modified Capabilities
<!-- No requirement changes: the `confirmation-email` spec already requires sending via SMTP env vars; only the deployed values change. -->

## Impact

- **DNS:** Cloudflare zone `conhilodepilo.com` (records changed in the safe order, MX last).
- **Email server:** Stalwart on `mail.darideveloper.com` — one new account; `info@conhilodepilo.com` already migrated.
- **Code:** `dashboard/project/settings.py` SMTP env vars (no code change required — values only); `dashboard/booking/views.py` `TestEmailView` (`/api/test-email/`) used for verification. `.env` file updates: `dashboard/.env.prod.example` + `.env.dev.example` (committed) and `dashboard/.env.prod` + `.env.dev` (gitignored, real credentials).
- **Deployment:** Coolify env vars for the dashboard service; container restart.
- **Docs:** `DNS-MIGRATION-PLAN.md` and the Obsidian `stalwart.md` onboarding status (incl. fixing `/debug-email` → `/api/test-email/`).
- **External systems:** old Skynet/Acens MX + `A` records removed; Acens contract kept alive for a 1–2 week grace window, then cancelled (registrar transfer is out of scope).

## Execution

- **Stalwart changes are agent-executed** via the admin JMAP Management API (`https://mail.darideveloper.com/jmap/`, RFC-8621 `Principal/*` methods under `urn:stalwart:jmap` + `urn:ietf:params:jmap:principals`), authenticated with the Stalwart **admin account supplied at runtime** (session/env) — **credentials are never stored in these artifacts or the repo**.
- Verified capability: `Principal/get` works; account/alias provisioning and verification use `Principal/set`/`Principal/get`.
- ⚠️ The management `/api` endpoint (config `x:*` methods) returns **404 on this build** — config-object changes (e.g., reverting the JMAP upload limits) must be done in the admin UI or via `stalwart-cli` on the host, not through the agent.
- **Cloudflare DNS** records are changed via the Cloudflare dashboard/API; **Coolify env** updates and **web/mail-client** test steps are operator-assisted (credentials for those live outside this repo).