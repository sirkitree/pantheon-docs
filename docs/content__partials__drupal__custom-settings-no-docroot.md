# content/partials/drupal/custom-settings-no-docroot.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/custom-settings-no-docroot.md
> **Generated**: 2025-09-09 03:19:28

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
git status # Ensure working tree is clean
git show master:sites/default/settings.php > web/sites/default/original-settings.php
diff -Nup --ignore-all-space web/sites/default/settings.php web/sites/default/original-settings.php
# edit web/sites/default/settings.php and commit as needed
rm web/sites/default/original-settings.php
```
