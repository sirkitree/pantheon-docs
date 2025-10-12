# content/guides/drupal/drupal-hosted-btworkflow/13-restore-token.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/drupal/drupal-hosted-btworkflow/13-restore-token.md
> **Generated**: 2025-10-12 00:27:30

---

---
title: Upgrade a Drupal Site Created With the Pantheon Dashboard to the Latest Version of Drupal + Build Tools
subtitle: Restore the tokens.json File
description: 
tags: [code, launch, migrate, site, updates]
contributors: [wordsmither]
permalink: docs/guides/drupal-hosted-btworkflow/restore-token
editpath: drupal/drupal-hosted-btworkflow/13-restore-token.md
reviewed: "2022-12-12"
contenttype: [guide]
innav: [false]
categories: [migrate, sftp]
cms: [drupal8, drupal9, drupal10]
audience: [development]
product: [dashboard]
integration: [--]
---

1. Connect to your site using SFTP command or credentials from your dashboard to restore the backup of the `tokens.json` file:

  ```bash
  files/private/.build-secrets/tokens.json
  ```

1. Use the SFTP `put` command to upload the file from your local directory (only if using the SFTP command line):

 <Alert title="Note"  type="info" >

 You must run this from the directory where the `tokens.json` backup was downloaded.

 </Alert>

  ```bash{promptUser:user}
  echo "put files/private/.build-secrets/tokens.json" | $(terminus connection:info $DESTINATION_SITE_NAME.dev --format=string --field=sftp_command)
  ```
