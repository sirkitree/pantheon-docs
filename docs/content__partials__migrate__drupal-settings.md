# content/partials/migrate/drupal-settings.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/migrate/drupal-settings.md
> **Generated**: 2025-11-05 00:28:22

---

---
contenttype: [partial]
categories: [migrate]
cms: [drupal]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

Your existing site may have customizations to `settings.php` or other configuration files.

1. Copy the existing `settings.php` to the Pantheon site and remove the `$databases` array if it exists.

1. Ensure that everything in the [Pantheon settings.php](https://github.com/pantheon-upstreams/drupal-composer-managed/blob/master/web/sites/default/settings.php) is included.

1. Confirm that the `settings.php` file on the Pantheon D9 site:

   - Has one `$settings['container_yamls'][]`
   - Contains no duplicates
   - Contains `include __DIR__ . "/settings.pantheon.php";`
