# content/partials/migrate/drupal-config.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/migrate/drupal-config.md
> **Generated**: 2025-11-03 15:07:08

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

Complete the steps in this section to copy exported configuration settings from the original site to your new Pantheon site.

1. Navigate to your Pantheon site.

1. Run the following commands:

  ```bash{promptUser: user}
  mkdir config
  cp -R ../FORMER-PLATFORM/<config folder location> config/
  git commit -m "Add site configuration."
  ```
