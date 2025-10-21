# content/partials/drupal/composer-config.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/composer-config.md
> **Generated**: 2025-10-21 21:06:38

---

---
contenttype: [partial]
categories: [update]
cms: [drupal9]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

Any additional Composer configuration that you have added to your site should be ported over to the new `composer.json` file. This can include configurations related to repositories, minimum-stability, or extra sections.

Use the diff command to get the information you need to copy:

```bash{promptUser:user}
diff -Nup --ignore-all-space $SOURCE/composer.json $DESTINATION/composer.json
```

Commit your changes as needed.
