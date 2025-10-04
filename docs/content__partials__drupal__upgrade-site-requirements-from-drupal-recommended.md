# content/partials/drupal/upgrade-site-requirements-from-drupal-recommended.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/upgrade-site-requirements-from-drupal-recommended.md
> **Generated**: 2025-10-04 03:12:01

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

Confirm that your site meets the following requirements before you continue:

- Ensure your site has the [Pantheon `drupal-composer-managed` repository](https://github.com/pantheon-upstreams/drupal-composer-managed) in its upstream.

   - Use Terminus to confirm the `drupal-composer-managed` Upstream

     Run the command `terminus site:info $SITE` to display the site's basic information and properties.

     The following is an abridged example of the output for a site upstream set to `drupal-composer-managed`:

     ```bash{outputLines:2-18}
     terminus site:info $SITE

     ------------------ -------------------------------------------------------------------------------------
     ID                 abdc3ea1-fe0b-1234-9c9f-3cxeAA123f88
     Name               anita-drupal
     Label              AnitaDrupal
     Created            2019-12-02 18:28:14
     Framework          drupal8
     ...
     //highlight-start
     Upstream           897fdf15-992e-4fa1-beab-89e2b5027e03: https://github.com/pantheon-upstreams/drupal-composer-managed.git
     //highlight-end
     ...
     ------------------ -------------------------------------------------------------------------------------
     ```

    The following values indicate that a site is using a `drupal-composer-managed` upstream:

     - The `Framework` is `drupal8`

     - The `Upstream` includes `https://github.com/pantheon-upstreams/drupal-composer-managed.git`
