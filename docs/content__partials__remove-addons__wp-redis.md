# content/partials/remove-addons/wp-redis.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/remove-addons/wp-redis.md
> **Generated**: 2025-09-04 21:06:19

---

---
contenttype: [partial]
categories: [cache]
cms: [wordpress]
product: [--]
integration: [plugins]
tags: [--]
reviewed: ""
---

1. Uninstall the [WP Redis](https://wordpress.org/plugins/wp-redis/) or Object Cache Pro plugin.

1. Delete the `wp-content/object-cache.php` file.

1. Commit and deploy these changes to the Live environment.

1. Go to <Icon icon="gear" /> **Settings**, select **Add Ons**, then click the **Remove** button for Redis.

1. Go to the Site Dashboard, and click <Icon icon="cleaning" /> **Clear Caches**.
