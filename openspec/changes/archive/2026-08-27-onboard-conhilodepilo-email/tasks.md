> **Execution notes:** Stalwart account/alias/verification tasks are executed via the admin JMAP Management API (`mail.darideveloper.com/jmap/`, **`x:Account/get` / `x:Account/set`** under `urn:stalwart:jmap` — the verified-working methods on this build; RFC-8621 `Principal/*` returns `notRequest`). Admin and account credentials are supplied at runtime (session/env) and **never stored in these artifacts**. The `/api` config endpoint is 404 on this build → config-object edits (7.3 JMAP limits revert) and 2FA (7.4) are admin-UI / host `stalwart-cli` actions.

## 1. Stalwart Accounts

- [x] 1.1 Create `no-reply@conhilodepilo.com` account via admin `Principal/set` (strong password, quota ~1 GB)
- [x] 1.2 Verify `info@conhilodepilo.com` exists and aliases `postmaster@` / `abuse@` forward to it (`Principal/get` / `Principal/query`)
- [x] 1.3 Confirm `info@` mailbox holds 4,147 restored emails (INBOX 3,285 · Sent 551 · Deleted 305 · Junk 5 · Drafts 1) via IMAP :993
- [x] 1.4 Store the `no-reply@` password in the password manager

## 2. Dashboard SMTP → Stalwart

- [x] 2.1 Update Coolify env for the dashboard: `EMAIL_HOST=mail.darideveloper.com`, `EMAIL_PORT=465`, `EMAIL_USE_SSL=True`, `EMAIL_HOST_USER=no-reply@conhilodepilo.com`, `EMAIL_HOST_PASSWORD=<pw>`
- [x] 2.2 Redeploy/restart the dashboard service
- [x] 2.3 Verify send via `GET https://dashboard.conhilodepilo.com/api/test-email/?to=<email>` → success (SPF/DKIM not expected to pass until 3.x)
- [x] 2.4 Update committed example env files (`dashboard/.env.prod.example`, `dashboard/.env.dev.example`) with generic dummy SMTP values (`EMAIL_HOST=smtp.example.com`, `EMAIL_PORT=465`, `EMAIL_USE_SSL=True`, `EMAIL_HOST_USER=sender@example.com`, `EMAIL_HOST_PASSWORD=change-me`) — no real hosts/users/secrets
- [x] 2.5 Update gitignored real env files (`dashboard/.env.prod`, `dashboard/.env.dev`) with the actual `no-reply@` credentials (password from the password manager; never commit)

## 3. Publish non-MX DNS Records (Cloudflare, DNS-only)

- [x] 3.1 Replace `TXT @`: delete old `v=spf1 redirect=spf.dominioabsoluto.net`, add `v=spf1 mx a:mail.darideveloper.com -all`
- [x] 3.2 Add `TXT v1-rsa-20260823._domainkey` → `v=DKIM1; p=<RSA key from Stalwart>`
- [x] 3.3 Add `TXT v1-ed25519-20260823._domainkey` → `v=DKIM1; p=<Ed25519 key from Stalwart>`
- [x] 3.4 Add `TXT _dmarc` → `v=DMARC1; p=none; rua=mailto:postmaster@conhilodepilo.com`
- [x] 3.5 Add `TXT _smtp._tls` → `v=TLSRPTv1; rua=mailto:postmaster@conhilodepilo.com`
- [x] 3.6 Add `CAA @` → `0 issue "letsencrypt.org"` and `0 issue "zerossl.com"` (merge, keep both)
- [x] 3.7 Verify all records with `dig`; confirm all are DNS-only (grey-cloud), nothing proxied

## 4. Pre-swap Sending Verification

- [x] 4.1 Send from `info@conhilodepilo.com` (IMAP :993 SSL / SMTP :465 SSL) to a Gmail you control
- [x] 4.2 Inspect original headers: `spf=pass`, `dkim=pass`, `dmarc=pass`; DKIM selector matches `v1-rsa-20260823`
- [x] 4.3 Send a dashboard test mail from `no-reply@` and confirm authenticated delivery
- [x] 4.4 Run `mail-tester.com` from `info@` → ✅ **9.5/10** (realistic message; SPF/DKIM pass, "properly authenticated"; 1 blocklist hit = cold-IP warm-up)

## 5. MX Swap + Cleanup (LAST)

- [x] 5.1 Confirm dashboard test email sent via Stalwart (2.3) — gate before deleting the `smtp` `A` record
- [x] 5.2 Delete `MX 10 mx.conhilodepilo.com`
- [x] 5.3 Delete `A mx/imap/pop3/smtp/webmail` (`217.116.0.x`)
- [x] 5.4 Add `MX @ → 10 mail.darideveloper.com.`
- [x] 5.5 Record old MX + Skynet `A` values in `DNS-MIGRATION-PLAN.md` §2 for rollback
- [x] 5.6 Verify `dig MX` → `10 mail.darideveloper.com.` and `dig TXT` shows new SPF/DKIM/DMARC

## 6. Post-swap Verification

- [x] 6.1 Send from an external address to `info@` → arrives in Stalwart (IMAP :993) — SMTP :25 accepted + queued `486a514dd001400` (2026-08-26); operator confirms mailbox arrival
- [x] 6.2 Send `info@` → Gmail → lands in **inbox**, not spam
- [x] 6.3 `dig -x 5.78.126.131` → `mail.darideveloper.com` (PTR) ✅ re-checked after swap 2026-08-26
- [x] 6.4 Regression: `https://conhilodepilo.com`, `www`, `dashboard.conhilodepilo.com`, `booking.conhilodepilo.com` → all 200 ✅ (2026-08-26 after swap)
- [x] 6.5 Confirm dashboard `/api/test-email/` still succeeds after the swap

## 7. Documentation & Housekeeping

- [x] 7.1 Update `DNS-MIGRATION-PLAN.md`: mark Phase 2 steps complete, record MX swap date, fix `/debug-email` → `/api/test-email/` (`dashboard/project/urls.py:37`)
- [x] 7.2 Update `stalwart.md` "Onboarded clients → conhilodepilo.com": status → LIVE, MX swap date + verified counts
- [x] 7.3 Optional: delete `yourdomain.com` demo account via admin `Principal/set destroy` (moot — **no such account exists**); revert JMAP upload limits (✅ done via `x:Jmap/set`); disable Ed25519 DKIM signing (✅ done via `x:Domain/set`, RSA only)
- [x] 7.4 Re-enable Stalwart admin 2FA (currently off)