# content/guides/drupal/drupal-hosted-createcustom/03-new-branch.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/drupal/drupal-hosted-createcustom/03-new-branch.md
> **Generated**: 2025-08-20 09:07:27

---

---
title: Upgrade a Custom Upstream to the Latest Version of Drupal
subtitle: Create a New Branch with Integrated Composer Code
description: 
tags: [code, launch, migrate, site, updates]
contributors: [wordsmither, michellecolon-pantheon]
permalink: docs/guides/drupal-hosted-createcustom/new-branch
editpath: drupal/drupal-hosted-createcustom/03-new-branch.md
reviewed: "2022-12-12"
contenttype: [guide]
innav: [false]
categories: [update, custom-upstreams]
cms: [drupal9, drupal10, drupal8, drupal]
audience: [agency, development]
product: [terminus, custom-upstreams]
integration: [--]
---

The first step in the migration process is to create a new branch with Integrated Composer.

1. Create a local clone of the Custom Upstream repository using the SSH URL and change the directory into the cloned repository:

  ```bash{promptUser:user}
  git clone $SSH_URL
  cd $REPOSITORY_NAME
  ```

1. Add the Integrated Composer upstream as a second remote and fetch:

  ```bash{promptUser:user}
  git remote add ic https://github.com/pantheon-upstreams/drupal-composer-managed.git && git fetch ic
  ```

1. Create a new `composerify` branch to work in:

   ```bash{promptUser:user}
   git checkout -b composerify
   ```

1. On the `composerify` branch, use Git to remove all the files in the directory and commit the change. This is because you are going to completely replace the file structure and re-add customizations:

   ```bash{promptUser:user}
    git rm -rf * && git commit -m "Removing all files"
    ```

1. Add and commit files from the Integrated Composer upstream:

   ```bash{promptUser:user}
   git checkout ic/main .
   git add $FILE_NAME
   git commit -m "Add and commit Integrated Composer files"
   ```

1. Navigate to `composer.json` in your text editor and change the `drupal/core-recommended` version to the version of Drupal you are currently on:

  ```json:title=upstream-configuration/composer.json
  "drupal/core-recommended": "^9"
  ```

1. Commit the change:

  ```bash{promptUser:user}
  git commit -am "Setting Drupal core version to ^9"
  ```
