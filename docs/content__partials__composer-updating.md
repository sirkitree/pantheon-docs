# content/partials/composer-updating.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/composer-updating.md
> **Generated**: 2025-10-01 03:25:42

---

---
contenttype: [partial]
categories: [dependencies]
cms: [drupal9, drupal8]
product: [--]
integration: [composer]
tags: [--]
reviewed: ""
---

Version compatibility issues can occur when packages pulled by Composer are updated along with their dependencies. If this happens, you will need to manually alter the version constraints on a given package in the `require` or `require-dev` section of `composer.json` to update the packages. Refer to the [updating dependencies](https://getcomposer.org/doc/01-basic-usage.md#updating-dependencies-to-their-latest-versions) section of the Composer documentation for more information.

Troubleshoot package updates by running `composer update`. This updates `composer.lock` to the latest available packages. Package updates are constrained by version requirements in `composer.json`.
