# content/partials/drupal/deploy-using-launch.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/deploy-using-launch.md
> **Generated**: 2025-08-21 06:10:03

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

You should now have the three major components (contrib and custom code, database, and files) of your site imported to your Pantheon account. 

1. Clear your caches in the [Pantheon Dashboard](/clear-caches#pantheon-dashboard) or with Terminus by running the following command:

  ```bash{promptUser: user}
  terminus drush $SITE.dev cr
  ```

1. Review the site, then proceed to launch using the [Launch Essentials](/guides/launch) documentation.
