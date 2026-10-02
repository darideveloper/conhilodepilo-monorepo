## Context

`dashboard/utils/stripe_utils.py::create_checkout_session` builds the Checkout Session with:

```python
stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[...],
    mode='payment',
    success_url=...,
    cancel_url=...,
    metadata={'booking_id': str(booking.id)},
)
```

`dashboard/requirements.txt` declared `stripe>=11.4.0` with no upper bound, and `dashboard/Dockerfile` runs a fresh `pip install --no-cache-dir -r requirements.txt` on every build with no lockfile. A production rebuild therefore resolved `stripe==16.0.0`, whose API version rejects `payment_method_types` for Checkout Sessions (dynamic payment methods are now configured in the Dashboard). The Stripe API returned `InvalidRequestError` (`param=payment_method_types`, `http_status=400`), which `views.py` wrapped into the generic `503`. The same `sk_live` key had processed a payment minutes earlier on the previous image, confirming the regression is SDK-driven, not credential-driven.

## Goals / Non-Goals

**Goals:**
- Restore successful Checkout Session creation for `PRE-PAID` bookings.
- Remove dependence on a parameter the current Stripe API no longer accepts.
- Make the build deterministic for the payment-critical dependency.

**Non-Goals:**
- Enforcing card-only at the code level. Payment methods are now a Dashboard concern.
- Pinning every other dependency or introducing a full lockfile (noted as follow-up).
- Changing the booking API contract, webhook handling, pricing, or templates.
- Migrating the webhook event type.

## Decisions

**Decision: remove `payment_method_types` entirely rather than downgrade the SDK.**
- Rationale: the parameter is deprecated server-side by the account's API/dynamic payment methods. Downgrading would re-pin the build to a dead API shape and re-break on the next upgrade.
- Alternative considered: pin `stripe<16` to keep the parameter. Rejected — temporary, and future upgrades fail the same way.

**Decision: accept dynamic payment methods; verify Card is enabled in the Stripe Dashboard.**
- Rationale: dynamic methods are the supported path; with only Card enabled in the Dashboard the customer-facing behavior is unchanged.
- Alternative considered: enforce card-only in code. No longer possible via `payment_method_types`; would require Dashboard configuration anyway.

**Decision: pin `stripe==16.0.0` exactly.**
- Rationale: deterministic rebuilds; the version already validated in production. Upgrades become intentional.
- Alternative considered: `stripe>=16.0.0,<17.0.0`. Rejected — a minor could still change Checkout behavior.

## Risks / Trade-offs

- [The Dashboard might have additional payment methods enabled, changing what customers see] → Mitigation: confirm Card (and only the methods you want) in Stripe Dashboard → Settings → Payment methods.
- [Card disabled in the Dashboard would still break checkout differently] → Mitigation: the verification step confirms Card is enabled before closing the change.
- [Other unpinned dependencies remain a latent rebuild risk] → Mitigation: out of scope here; tracked as a follow-up.
- [Local test suite cannot run due to an unrelated `django-unfold` import error] → Mitigation: verify with `py_compile` and a live production booking; the mock-based Stripe tests are updated regardless.

## Migration Plan

Code-only, backward compatible. Deploy the dashboard service; no database migration. Rollback is the previous image. Post-deploy verification: place a live `PRE-PAID` booking and confirm `201` with a `checkout_url`, and that `Stripe session creation failed` no longer appears in logs.

## Open Questions

None blocking.
