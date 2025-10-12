# content/partials/migrate/drupal-modules-themes.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/migrate/drupal-modules-themes.md
> **Generated**: 2025-10-12 06:08:07

---

---
contenttype: [partial]
categories: [migrate]
cms: [--]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

Follow the steps below if you want to move modules and themes to your new site.

1. Navigate to the Pantheon site directory.

1. Copy modules from the local directory of the old platform site:

    ```bash{promptUser: user}
    cp -R ../FORMER-PLATFORM/modules/custom web/modules
    git add web/modules/custom
    git commit -m "Copy custom modules"
    ```

1. Copy themes from the local directory of the old platform site:

    ```bash{promptUser:user}
    cp -R ../FORMER-PLATFORM/themes/custom web/themes
    git add web/themes/custom
    git commit -m "Copy custom themes"
    ```

1. Copy any other custom code you need from your old platform site.
