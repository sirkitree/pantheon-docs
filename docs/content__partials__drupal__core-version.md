# content/partials/drupal/core-version.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/core-version.md
> **Generated**: 2025-11-01 06:08:49

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

Run the code below to set the Drupal core version to the latest version of Drupal:

  ```bash{promptUser: user}
  composer require --update-with-dependencies --no-update 'drupal/core-recommended:^10' 'drupal/core-composer-scaffold:^10'
  composer update drupal/core* -W
  git add composer.*
  git commit -m "upgrade to Drupal 10"
  ```

<Alert title="Note" type="info" >

If you receive the error message `Your requirements could not be resolved to an installable set of packages`, replace the `composer update drupal/core* -W` command with `composer update`

</Alert>
