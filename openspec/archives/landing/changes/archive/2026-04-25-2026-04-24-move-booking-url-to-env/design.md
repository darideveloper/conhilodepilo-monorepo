# Design: Configuration Management

## Overview
Moving configuration constants like service booking endpoints into environment variables allows for flexible deployment configurations without requiring code changes for URL updates.

## Patterns
- Use Astro's `import.meta.env` to access variables.
- Maintain the current logic of constructing the full URL: `${PUBLIC_BOOKING_URL}/?service=${id}`.
- Ensure `.env.example` is updated to reflect the new variable.

## Trade-offs
- Slight increase in complexity by requiring environment variable setup, but standard for modern web development.
