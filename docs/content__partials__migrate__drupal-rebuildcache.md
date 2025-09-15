# content/partials/migrate/drupal-rebuildcache.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/migrate/drupal-rebuildcache.md
> **Generated**: 2025-09-15 06:10:04

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

When you make changes to fix a problem, don't forget to rebuild the cache:

```bash{promptUser: user}
terminus drush $SITE.dev cr
```
