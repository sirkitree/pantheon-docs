# content/partials/drupal/drupal-mariadb-considerations.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/drupal-mariadb-considerations.md
> **Generated**: 2025-08-20 15:06:45

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

The default database version for new sites is MariaDB 10.4.

If your site has any older contrib modules that are not compatible with MariaDB 10.4, set the MariaDB version of the new site to `10.3` in your `pantheon.yml` file.

The latest version of Drupal requires MariaDB 10.3 or later. If you have a site that you plan to upgrade, confirm that the database has been upgraded to MariaDB 10.3 or 10.4 in all environments before you begin the upgrade.
