# content/guides/drupal/drupal-hosted-createempty-md/07-contrib-custom.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/drupal/drupal-hosted-createempty-md/07-contrib-custom.md
> **Generated**: 2025-09-18 12:10:15

---

---
title: Upgrade a Site That Was Created With an Empty Upstream to the Latest Version of Drupal
subtitle: Add Contrib and Custom Code
description: 
tags: [code, launch, migrate, site, updates]
contributors: [wordsmither]
showtoc: true
permalink: docs/guides/drupal-hosted-createempty-md/contrib-custom
editpath: drupal/drupal-hosted-createempty-md/07-contrib-custom.md
reviewed: "2022-12-13"
contenttype: [guide]
innav: [false]
categories: [overview, migrate]
cms: [drupal, drupal8, drupal9, druapl10]
audience: [agency, development]
product: [--]
integration: [--]
---

This section describes how to replicate your selection of contributed modules and themes, and any custom modules or themes your development team has created in your new project structure.

## Contributed Code

### Modules and Themes

The goal of this process is to have Composer manage all the site's contrib modules, contrib themes, core upgrades, and libraries (we'll call this *contributed code*). The only things that should be migrated from the existing site are custom code, custom themes, and custom modules that are specific to the existing site.

The steps here ensure that any modules and themes from [drupal.org](https://drupal.org) are in the `composer.json` `require` list.

Once Composer is aware of all the contributed code, you'll be able to run `composer update` from within the directory to have Composer upgrade all the contributed code automatically.

Begin by reviewing the existing site's code. Check for contributed modules in `/modules`, `/modules/contrib`, `/sites/all/modules`, and `/sites/all/modules/contrib`.

1. Review the site and make a list of the exact versions of modules and themes you depend on.

  One way to do this is to run the `pm:list` Drush command from within a contributed module's folder (e.g. `/modules`, `/themes`, `/themes/contrib`, `/sites/all/themes`, `/sites/all/themes/contrib`, etc.).

  This will list each module, followed by which version of that module is installed:

  ```bash{promptUser:user}
  terminus drush $SITE.dev pm:list -- --no-core --fields=name,version --format=table
  ```

  If you are already using Composer to manage your site dependencies, you can go to `composer.json` in your source site to get the package names and versions.

1. Add these modules to your new codebase using Composer by running the following for each module in the `$SITE` directory:

  ```bash{promptUser:user}
  composer require drupal/MODULE_NAME:^VERSION
  ```

  <Partial file="module-name.md" />

  Some modules use different version formats.

   - For older Drupal version strings:

   ```none
   Chaos Tools (ctools)  8.x-3.4
   ```

    Replace the `8.x-` with a `^` to convert it into `^3.4`.

   - Semantic Versioning version strings:

   ```none
   Devel (devel)  4.1.1
   ```

    Use the version directly, e.g. `^4.1.1`.

### Libraries

Libraries are handled similarly to modules, but the specifics depend on how your library code was included in the source site. If you're using a library's API, you may have to do additional work to ensure that library functions properly.

## Custom Code

Next, manually copy custom code from the existing site repository to the Composer-managed directory.

### Modules and Themes

<Partial file="drupal/custom-modules-themes.md" />

### settings.php

<Partial file="drupal/custom-settings.md" />
