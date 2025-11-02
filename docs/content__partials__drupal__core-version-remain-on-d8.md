# content/partials/drupal/core-version-remain-on-d8.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/core-version-remain-on-d8.md
> **Generated**: 2025-11-02 12:09:31

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
  composer require --no-update drupal/core-recommended:^9
  composer require --no-update drush/drush:"^10 || ^11 || ^12"
  composer require --dev drupal/core-dev:^9
  git add composer.*
  git commit -m "Remain on Current Version"
  ```
