# content/partials/drupal-apply-upstream-updates.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal-apply-upstream-updates.md
> **Generated**: 2025-10-16 09:07:34

---

---
contenttype: [partial]
categories: [update, migrate]
cms: [drupal]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

1. Use Terminus to list all available updates:

  ```bash{outputLines:2}
  terminus upstream:updates:list $SITE.dev
  [warning] There are no available updates for this site.
  ```

1. Apply any available updates using the command line or the [Pantheon Dashboard](/core-updates#apply-upstream-updates-via-the-site-dashboard):

  ```bash{promptUser: user}
  terminus upstream:updates:apply $SITE.dev --updatedb
  ```
