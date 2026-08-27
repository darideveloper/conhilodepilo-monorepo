## Context

`conhilodepilo.com` DNS is already on Cloudflare (Phase 1 done, all records DNS-only), and the domain was renewed at Acens to 2027-08-24. The mailbox backup `info-conhilodepilo.sqlite` (4,147 emails) has been restored into Stalwart and verified (INBOX 3,285 · Sent 551 · Deleted 305 · Junk 5 · Drafts 1). Stalwart has the `conhilodepilo.com` domain added with DKIM keys generated (`v1-rsa-20260823`, `v1-ed25519-20260823`), plus accounts `info@` and aliases `postmaster@`/`abuse@`. The old Skynet MX (`10 mx.conhilodepilo.com` → `217.116.0.227`) is still authoritative for inbound, and the Django dashboard still sends via the old provider's SMTP.

The remaining work is the email cutover in the safe order — **accounts → non-MX DNS → send tests → MX swap last** — so delivery never stops and booking email stays functional.

## Goals / Non-Goals

**Goals:**
- Zero mail loss and zero inbound downtime during cutover.
- `info@conhilodepilo.com` sending and receiving fully on Stalwart with authenticated delivery (SPF/DKIM/DMARC pass).
- Dashboard booking confirmation email sending via Stalwart, independent of Skynet.
- Remove every Skynet/Acens dependency from the Cloudflare zone.

**Non-Goals:**
- Registrar transfer to Cloudflare and Acens contract cancellation (time-gated ≈ 2026-10-08; separate effort).
- MTA-STS enforcement, webmail UI, DMARC escalation (`p=none` → `quarantine` → `reject`).
- Re-importing new Skynet mail (provider unreachable; the 2026-08-25 backup is the source of truth).

## Decisions

1. **Dashboard sender = dedicated `no-reply@conhilodepilo.com` account.** Keeps `info@`'s Sent folder clean and isolates app credentials. *Alternative considered:* reuse `info@` / an app password on it — simpler but pollutes Sent and shares the client account's secret with the app.
2. **SPF = single `@` TXT `v=spf1 mx a:mail.darideveloper.com -all`**, replacing `v=spf1 redirect=spf.dominioabsoluto.net`. `a:mail.darideveloper.com` authorizes the VPS IP (covers Stalwart and the dashboard). Exactly one `@` TXT (SPF allows only one).
3. **Publish both DKIM selectors.** RSA is the deliverability-relevant key; Ed25519 may show `dkim=neutral` in Gmail (cosmetic, accepted — optional to disable signing later).
4. **DMARC starts at `p=none`** (report-only) at cutover; escalation deferred to post-cutover hardening.
5. **CAA includes both `letsencrypt.org` and `zerossl.com`** (merge, never overwrite) — the web proxy uses Let's Encrypt, the mail cert is ZeroSSL.
6. **All mail-affecting records DNS-only (grey).** Cloudflare cannot proxy SMTP/IMAP and injects a `_dc-mx` rewrite (incident precedent 2026-08-25). MX is external (`mail.darideveloper.com`), so there is no same-domain MX↔A trap.
7. **No MTA-STS for this client domain** — the policy file needs a cert for `mta-sts.conhilodepilo.com`, which Stalwart doesn't serve. `autodiscover`/`autoconfig` CNAMEs optional; skipped initially.
8. **MX swap is done exactly once.** TTLs are fixed (~6h for A/MX from the old provider); old MX + Skynet `A` values are recorded for rollback before deletion.
9. **Stalwart changes are executed via the admin JMAP Management API** (`/jmap/`, `urn:stalwart:jmap`, **`x:Account/get` / `x:Account/set`** — verified on this build; RFC-8621 `Principal/set` returns `notRequest`), authenticated as the Stalwart admin with credentials provided at runtime — **never stored in artifacts/repo**. Account creation (`x:Account/set` create), alias provisioning (account `aliases` field), and mailbox checks (`x:Account/get`, IMAP) are agent-executable. The `/api` management endpoint is unavailable on this build (404), so config-object edits (e.g., JMAP limits revert) remain admin-UI/`stalwart-cli` actions.

## Risks / Trade-offs

- [**MX swapped before accounts/mail ready**] → Accounts, restore, and send tests all complete first (mail already restored and verified).
- [**Dashboard still on Skynet when `smtp` `A` record is deleted → booking email breaks**] → Step T2 (dashboard → Stalwart, `/api/test-email/`) is a gate before the MX swap.
- [**New Skynet mail lost**] → Provider unreachable; last backup restored; keep Acens mailbox alive 1–2 weeks as a grace window before cancelling.
- [**Slow rollback (6h TTL)**] → Do the swap once; old values documented for a clean restore.
- [**Ed25519 `dkim=neutral` in Gmail**] → Cosmetic; RSA selector passes; optional disable later.
- [**Dashboard email lands in spam during IP warm-up**] → Cold-IP reputation; Stalwart warm-up already ongoing; monitor mail-tester score.
- [**Cloudflare "Email Routing" accidentally enabled**] → It intercepts `info@` and injects a `_dc-mx` rewrite. Never enable it; keep the MX record DNS-only and pointing externally (trap documented in `DNS-MIGRATION-PLAN.md` §9).

## Migration Plan

1. **Pre-flight (done):** Cloudflare DNS Phase 1, domain renewal, mailbox backup + restore, domain/account/aliases in Stalwart, JMAP upload limits raised for the restore.
2. **T1** — Create `no-reply@conhilodepilo.com` in Stalwart (strong password, quota ~1 GB).
3. **T2** — Update Coolify env for the dashboard to `mail.darideveloper.com:465` (SSL) with `no-reply@` credentials; update the dashboard `.env` files (committed examples + gitignored real files); redeploy; verify `/api/test-email/`.
4. **T3** — Publish non-MX DNS: SPF, DKIM ×2, DMARC, TLS-RPT, CAA (all DNS-only). No delivery impact.
5. **T4** — Send tests: `info@` → Gmail (headers `spf=pass`/`dkim=pass`/`dmarc=pass`), `mail-tester.com` ≥ 9/10.
6. **T5** — MX swap last: delete `MX 10 mx.conhilodepilo.com`, Skynet `A` records, old SPF; add `MX @ → 10 mail.darideveloper.com.`
7. **T6** — Post-swap verify: external → `info@` arrives; `info@` → Gmail inbox (not spam); `dig -x` PTR; web regression.
8. **Rollback:** within the first days, flip MX back to `10 mx.conhilodepilo.com` + restore Skynet `A` records while Acens still hosts the mailbox.

## Open Questions

- None blocking. (Post-cutover hardening items — DMARC escalation, optional Ed25519 disable, JMAP limit revert — are tracked in T7 housekeeping, not required for cutover.)