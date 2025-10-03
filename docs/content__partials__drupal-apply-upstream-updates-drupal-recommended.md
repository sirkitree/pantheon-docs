# content/partials/drupal-apply-upstream-updates-drupal-recommended.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal-apply-upstream-updates-drupal-recommended.md
> **Generated**: 2025-10-03 18:08:24

---

---
contenttype: [partial]
categories: [update, migrate]
cms: [--]
product: [dashboard, terminus]
integration: [--]
tags: [--]
reviewed: "2022-11-04"
---

[Update the site](/core-updates) to the latest [Pantheon Drupal Composer Managed](https://github.com/pantheon-upstreams/drupal-composer-managed) Upstream and apply all available updates.

1. Use Terminus to list all available updates:

  ```bash{outputLines:2}
  terminus upstream:updates:list $SITE.dev
  [warning] There are no available updates for this site.
  ```

1. Run the following code to apply available updates:

  ```bash{promptUser: user}
  terminus upstream:updates:apply $SITE.dev --updatedb
  ```

You can also use the [Pantheon Dashboard](/core-updates#apply-upstream-updates-via-the-site-dashboard) to apply upstream updates.
