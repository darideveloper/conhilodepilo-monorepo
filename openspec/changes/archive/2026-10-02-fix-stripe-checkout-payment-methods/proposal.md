## Why

After a production redeploy, every `PRE-PAID` booking failed with `503 {"error": "Payment service is currently unavailable."}`. The container rebuilt with `stripe==16.0.0` because `dashboard/requirements.txt` declared `stripe>=11.4.0` (unbounded), and the new SDK/API rejects the `payment_method_types` parameter on Checkout Session creation:

```
InvalidRequestError code=None param=payment_method_types http_status=400
"The `payment_method_types` parameter is no longer supported when creating a Checkout Session.
 Payment methods are now managed from your Dashboard settings."
```

The same credentials worked minutes earlier; the only change was the freshly resolved SDK major. The bug is a regression against the existing `payment-flow` requirement ("At least one service is PRE-PAID → create a Stripe Checkout Session and return a `checkout_url`"), not a new capability.

## What Changes

- Stop sending the deprecated `payment_method_types=['card']` parameter from `create_checkout_session`; payment methods are now dynamic and configured in the Stripe Dashboard.
- Pin the Stripe Python SDK to the version production actually runs (`stripe==16.0.0`) so an image rebuild cannot silently pull a new breaking major.
- Add regression assertions ensuring `payment_method_types` is never passed again.
- Keep the detailed `StripeError` logging added in `ddb10c9` (it surfaced the real error).

No API contract, data-model, or frontend changes.

## Capabilities

### New Capabilities
<!-- None -->

### Modified Capabilities
- `payment-flow`: Checkout Sessions must be created without `payment_method_types`; payment methods come from the Stripe Dashboard's dynamic configuration. The Stripe SDK must be pinned to a tested version.

## Impact

- `dashboard/utils/stripe_utils.py` — remove `payment_method_types`.
- `dashboard/requirements.txt` — `stripe>=11.4.0` → `stripe==16.0.0`.
- `dashboard/booking/tests_stripe.py` — assert the parameter is absent.
- No changes to `dashboard/booking/views.py` response contract, the webhook, the database, or the booking/landing frontends.
