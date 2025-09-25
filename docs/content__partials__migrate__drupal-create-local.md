# content/partials/migrate/drupal-create-local.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/migrate/drupal-create-local.md
> **Generated**: 2025-09-25 06:09:43

---

---
contenttype: [partial]
categories: [migrate]
cms: [--]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

1. Obtain a local copy of your old site's code.

  Your code includes all custom and contributed modules or plugins, themes, and libraries. The codebase should not include the `sites/default/files` directory, or any other static assets you do not want tracked by version control.

1. Export the database and media files (`sites/default/files`) from the old platform, but do not add them or upload any files to Pantheon.
