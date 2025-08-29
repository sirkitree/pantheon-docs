# content/partials/drupal/troubleshooting-general.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/troubleshooting-general.md
> **Generated**: 2025-08-29 18:08:01

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

## Pantheon Launch Check Status Error: services.yml does not exist

After you set up Drupal, the following error might be displayed in the **Best practices** section of the Pantheon Launch Check:

> <span  style="color:red">x <strong>sites/default/services.yml:</strong></span> services.yml does not exist! Copy the default.service.yml to services.yml and refer to https://www.drupal.org/documentation/install/settings-file for details.
><br />
><br />
>
> *Create `services.yml` file inside `sites/default` directory by copying `default/services.yml` file. Refer to https://www.drupal.org/documentation/install/settings-file for details.*

Ensure your site's [Development Mode](/connection-modes/) is set to **Git**. Use the terminal on the local machine where you cloned the site, and from the project's root directory:

1. Copy `default.services.yml` to `services.yml`:

 ```bash{promptUser: user}
 cp web/sites/default/default.services.yml web/sites/default/services.yml
 ```

1. Commit and push:
<!-- need to provide example w/out web? -->
 ```bash{promptUser: user}
 git add web/sites/default/services.yml && git commit -m "init services.yml"
 git push origin master
  ```

Learn more about the [service configuration](/services-yml#create-and-modify-servicesyml) file.

## Where Can I Report an Issue?

[Contact support](/guides/support/contact-support) to report any issues that you encounter.
