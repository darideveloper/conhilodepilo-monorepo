## Context

The monorepo has three projects — landing (`conhilodepilo.com`), booking (`booking.conhilodepilo`), and dashboard (`dashboard.conhilodepilo.apps.darideveloper.com`) — each with its own favicon file and setup:

| Project | Format | Reference method |
|---------|--------|-----------------|
| Landing | `favicon.ico` | `<link>` in Astro layout |
| Booking | `favicon.svg` + `favicon.ico` | Two `<link>` tags in Astro layout |
| Dashboard | `favicon.png` (32x32) | Django Unfold `SITE_FAVICONS` config |

Landing serves the canonical brand favicon at `https://conhilodepilo.com/favicon.ico`. Booking and dashboard currently maintain local copies that may diverge over time.

## Goals / Non-Goals

**Goals:**
- Centralize favicon source to `https://conhilodepilo.com/favicon.ico`
- Remove duplicate local favicon files from booking and dashboard
- Simplify booking's HTML (one `<link>` tag instead of two)
- Keep 100% backward-compatible behavior (same icon visible to users)

**Non-Goals:**
- Changing the favicon image itself (that's a brand decision, handled on landing)
- Adding SVG favicon support to landing or dashboard
- Changing the landing project's favicon setup
- Modifying the dashboard admin header icon (`SITE_ICON`) — that uses a different callback

## Decisions

| # | Decision | Rationale | Alternatives Considered |
|---|----------|-----------|------------------------|
| 1 | **External URL over local copy** | Single source of truth. Favicon changes only need deployment on landing; booking/dashboard pick it up immediately. | Local copy → three places to update, easy to desync |
| 2 | **Drop SVG favicon in booking** | The external URL only serves `.ico`. Keeping the SVG would either point nowhere or require a separate SVG URL on landing (not available). SVG favicons also have inconsistent browser support for the `type="image/svg+xml"` syntax. | Keep SVG + change ICO → mixed local/external setup, confusing |
| 3 | **Omit `type` attribute on dashboard** | ICO MIME type (`image/x-icon` or `image/vnd.microsoft.icon`) is not needed — browsers auto-detect from the response `Content-Type` header. Omitting it avoids incorrect metadata. | `type: "image/x-icon"` → correct but redundant; `type: "image/png"` → wrong for .ico |
| 4 | **Omit `type` attribute on booking** | Same reasoning as above. The `<link rel="icon" href="...">` without `type` works in every browser. |  |
| 5 | **Clean up stale files** | Dead code accumulates. Removing unused files keeps the repo clean and avoids confusion. | Leave them → no immediate harm, but clutter |

## Risks / Trade-offs

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Landing is down → booking/dashboard lose favicon | Low (landing is a static site, highly available) | The favicon is cosmetic. Browser tabs will show the default page icon — not a functional issue. |
| External URL adds a DNS lookup and HTTP request | Low | Favicon is ~1-15 KB. Browsers cache it aggressively. The performance impact is negligible vs the current local files. |
| CORS / mixed-content warnings | None | Favicon `<link>` tags are not subject to CORS. All URLs are HTTPS. |
| Future favicon format change on landing (e.g., SVG) | Low | If landing adds SVG support later, booking and dashboard can adopt it in a follow-up change. |
