# content/partials/drupal/troubleshooting-drush.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/troubleshooting-drush.md
> **Generated**: 2025-09-29 00:27:22

---

---
contenttype: [partial]
categories: [update]
cms: [drupal9]
product: [--]
integration: [drush]
tags: [--]
reviewed: ""
---

## Site-local Drush Is Required for Drupal Sites

Do not remove `drush/drush` from `composer.json`. If it is removed, `terminus drush` commands will fail with errors related to Twig.

