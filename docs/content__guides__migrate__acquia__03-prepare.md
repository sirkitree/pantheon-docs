# content/guides/migrate/acquia/03-prepare.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/migrate/acquia/03-prepare.md
> **Generated**: 2025-09-07 12:09:29

---

---
title: Migrate a Site From Acquia to Pantheon Using Guided Migration
subtitle: Prepare
description: Get your site ready for migration.
contenttype: [guide]
innav: [false]
categories: [migrate]
cms: [drupal]
audience: [development]
product: [--]
integration: [--]
tags: [code, launch, migrate, site, updates]
contributors: [wordsmither]
permalink: docs/guides/acquia/prepare
editpath: migrate/acquia/03-prepare.md
reviewed: "2022-12-13"
---

<Partial file="migrate/prepare.md" />

8. Choose to either move the contents of Aquia's nested directory `docroot` up and remove the folder, or rename the folder to `web` and set `web_docroot: true` in your `pantheon.yml` file. For more information on nested docroots, see [Serving Sites from the Web Subdirectory](/nested-docroot).

9. Navigate to your Acquia dashboard > click **Manage** > click **Extend**. Click **Uninstall** to uninstall Acquia-specific modules.

10. Adjust any special Acquia configurations related to `env` to ensure compatibility with Pantheon's platform. 

11. Uninstall any Acquia Search modules and the default Drupal core Search module (if still enabled for your site) by navigating to `admin/modules/uninstall` if you plan on using [Pantheon Search](/solr).

<Alert title="Note" type="info">

If `query cache` is turned on within the MySQL service (an obsolete setting), you may notice a severe performance drop on Pantheon during the User Acceptance Testing stage of an active migration from Acquia. We recommend that you move to a modern service to avoid this issue.

If you would like to confirm that your performance drop is caused by the obsolete `query cache` MySQL service setting, connect to the MySQL service in Acquia’s production environment and run the following:

```sql{promptUser: sql}
SHOW VARIABLES LIKE 'query_cache_%';
```

High values for the `query_cache_limit` and `query_cache_size` variables will confirm that performance degradation is related to the MySQL `query cache` service setting.

</Alert>
