## Context

The system sends confirmation emails using a single Django HTML template ([booking_confirmation.html](file:///develop/monorepos/conhilorepilo/dashboard/project/templates/email/booking_confirmation.html)). Currently, the template displays the company logo from the database (`CompanyProfile`). The backend dynamically builds an absolute logo URL to include in the email context. To simplify email formatting, we want to remove the logo from the email entirely while keeping the company name centered.

## Goals / Non-Goals

**Goals:**
- Remove the logo image element from the confirmation email template.
- Keep the company title text centered in the email header.
- Clean up unused Python helper functions (`_build_logo_url`) and context variables (`logo_url`) in the backend.
- Remove all tests related to email logo URL generation to avoid dead tests.

**Non-Goals:**
- Modifying the logo rendering on the landing page, booking widget, or django admin interface.
- Changing header text color or background styling.

## Decisions

### Decision 1: Template Modification & Layout Centering
- **Choice**: Remove the `{% if logo_url %}...{% endif %}` block from the header.
- **Rationale**: Since the header table cell already has `align="center"`, the `<h1>` company title remains centered automatically. No additional styling modifications are required.

### Decision 2: Backend Clean Sweep (Option 2)
- **Choice**: Delete `_build_logo_url` and its call in `_build_base_context`.
- **Rationale**: Keeps code maintenance simple by preventing unused helper functions and dead context parameters.

### Decision 3: Clean up Unit Tests
- **Choice**: Remove `BuildLogoUrlTest` class in `tests_email.py`.
- **Rationale**: The function it tests (`_build_logo_url`) will no longer exist.

## Risks / Trade-offs

- **Risk**: Other codebase modules or external views relying on `_build_logo_url` might break.
- **Mitigation**: We verified via search that `_build_logo_url` is only imported and used in [utils/email.py](file:///develop/monorepos/conhilorepilo/dashboard/utils/email.py) and [tests_email.py](file:///develop/monorepos/conhilorepilo/dashboard/booking/tests_email.py). Running Django tests after changes will guarantee correctness.
