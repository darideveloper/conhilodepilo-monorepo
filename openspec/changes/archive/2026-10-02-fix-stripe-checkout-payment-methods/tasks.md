## 1. Code fix

- [x] 1.1 In `dashboard/utils/stripe_utils.py`, remove the `payment_method_types=['card']` argument from `stripe.checkout.Session.create`.
- [x] 1.2 Confirm the remaining arguments (`line_items`, `mode='payment'`, `success_url`, `cancel_url`, `metadata`) are unchanged.
- [x] 1.3 In `dashboard/requirements.txt`, pin `stripe==16.0.0` (was `stripe>=11.4.0`).
- [x] 1.4 Keep the detailed `StripeError` logging added in `ddb10c9` (no change).

## 2. Regression tests

- [x] 2.1 In `dashboard/booking/tests_stripe.py::test_create_booking_with_stripe_redirect`, assert `'payment_method_types' not in kwargs`.
- [x] 2.2 In `dashboard/booking/tests_stripe.py::test_create_checkout_session_product_name`, assert `'payment_method_types' not in kwargs`.

## 3. Verify

- [x] 3.1 `python -m py_compile dashboard/utils/stripe_utils.py` passes.
- [ ] 3.2 Confirm Card is enabled in Stripe Dashboard → Settings → Payment methods.
- [ ] 3.3 Deploy and place a live `PRE-PAID` booking; expect `201` with `checkout_url`.
- [ ] 3.4 Confirm `Stripe session creation failed` is absent from production logs after the fix.

## 4. Housekeeping

- [x] 4.1 Note the remaining unpinned dependencies as a follow-up (out of scope for this change).
