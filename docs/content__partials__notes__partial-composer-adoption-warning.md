# content/partials/notes/partial-composer-adoption-warning.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/notes/partial-composer-adoption-warning.md
> **Generated**: 2025-11-01 18:07:39

---

---
contenttype: [partial]
categories: [dependencies]
cms: [drupal]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

<alert type="danger" title="Warning">

Partial Composer adoption for Drupal sites is not supported since Composer is used by core, meaning any change to `composer.json` or the `vendor` directory would result in massive merge conflicts when trying to update core via one-click updates in the Pantheon Site Dashboard. Composer with Drupal is an all or nothing proposition. To use Composer to manage Drupal sites, use the [Build Tools](/guides/build-tools) or [convert an existing Drupal site to Integrated Composer](/guides/composer-convert) on Pantheon methods.

</alert>
