# Tasks: Render all textarea fields as Markdown editors

- [x] Remove field exclusions in `static/js/load_markdown.js` <!-- id: 0 -->
    - Update the script to target all `div > textarea` elements without using the `noMarkdownIds` blacklist.
- [x] Verify SimpleMDE initialization in Admin <!-- id: 1 -->
    - Log in to the admin.
    - Navigate to an `Event` or `EventType` change page.
    - Confirm the `description` field has the Markdown toolbar.
- [x] Update documentation <!-- id: 2 -->
    - Update `docs/django-unfold-admin.md` to reflect that all text areas now use Markdown by default.
