## Context

The admin is a Django project using `django-unfold` for theming. URL routing is defined in `dashboard/project/urls.py` using Django's standard `path()` patterns. The root `/admin/` maps to `admin.site.urls`, which renders the admin index page listing all registered models.

The booking changelist at `/admin/booking/booking/` is the most-used page — it's already the first item in the unfold sidebar navigation. The admin index is purely decorative for this workflow.

## Goals / Non-Goals

**Goals:**
- `/admin/` redirects to `/admin/booking/booking/`
- All other admin URLs (`/admin/booking/event/`, `/admin/auth/user/`, etc.) remain unchanged
- Zero runtime overhead beyond the redirect

**Non-Goals:**
- No changes to admin view logic, templates, or sidebar configuration
- No custom AdminSite subclass
- No conditional redirects (all users, all the time)

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Approach** | URL-level `RedirectView` in `project/urls.py` | Simplest option (1 line). Django path matching is exact — `/admin/` matches only the literal path `/admin/`, so `/admin/booking/booking/` falls through to `admin.site.urls`. No new classes, no template changes, trivially reversible. |
| **Alternatives considered** | Custom `AdminSite` with `index()` override | More boilerplate — requires subclassing, re-registering all models, and updating `project/admin.py`. Adds maintenance surface for zero functional gain over the URL approach. |
| **Alternatives considered** | Template override of `admin/index.html` | Fragile (JS redirect) or retains the index page. Neither satisfies the goal. |
| **Redirect status** | 301 (permanent) via `RedirectView` | Correct semantic for a permanent routing change. Browsers will cache it, reducing latency on repeat visits. If rollback is needed, deploy the revert and users' cached 301 will clear on the next visit (or use a 302 if preferred). |

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| **Admin index lost** — no way to see all models at a glance | Sidebar provides navigation to every model from any page. The index had no unique content — it just listed what's in the sidebar. |
| **Cached 301 on rollback** — if we revert, browsers may still redirect from cache | Use 302 (temporary) during initial rollout, or instruct users to clear browser cache on revert. Acceptable risk for an internal admin tool. |
| **Path ordering** — new path must come before `admin.site.urls` | Straightforward in `urlpatterns`. Django resolves top-to-bottom. The new `/admin/` path is exact, so it won't interfere with longer paths. |
