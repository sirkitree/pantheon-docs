# content/partials/drupal/custom-modules-themes-no-docroot.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/custom-modules-themes-no-docroot.md
> **Generated**: 2025-08-19 00:27:48

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

```bash{promptUser:user}
git checkout master modules/custom
git mv modules/custom web/modules/
git commit -m "Copy custom modules"
```
