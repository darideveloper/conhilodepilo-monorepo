# Proposal: Set Spanish Language

## Context
The website is currently configured with the default English language (`LANGUAGE_CODE = "en-us"`). To serve our target audience properly, the primary language of the application needs to be changed to Spanish.

## Goal
Update the main Django application language to Spanish.

## Proposed Solution
Modify `LANGUAGE_CODE` in `project/settings.py` to use an environment variable with a default value of `"es"`:
```python
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", "es")
```
Additionally, the `LANGUAGE_CODE` variable will be added to all environment configuration files:
- `.env.example`, `.env.dev.example`, `.env.prod.example`
- `.env`, `.env.dev`, `.env.prod` (where applicable)

This ensures the primary language is Spanish by default while maintaining the project's convention of being environment-variable-first. This will natively change the language of the Django application, including built-in translations for the admin interface and Unfold UI.