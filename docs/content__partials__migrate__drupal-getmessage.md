# content/partials/migrate/drupal-getmessage.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/migrate/drupal-getmessage.md
> **Generated**: 2025-11-09 06:08:59

---

---
contenttype: [partial]
categories: [migrate]
cms: [drupal]
product: [--]
integration: [--]
tags: [--]
reviewed: "2022-11-03"
---

When there are problems, you can sometimes get helpful messages about what's wrong with the following command if you have dblog module enabled:

```bash{promptUser: user}
terminus drush $SITE.dev watchdog:show
```
