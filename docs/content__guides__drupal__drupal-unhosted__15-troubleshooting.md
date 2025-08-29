# content/guides/drupal/drupal-unhosted/15-troubleshooting.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/drupal/drupal-unhosted/15-troubleshooting.md
> **Generated**: 2025-08-29 15:05:25

---

---
title: Migrate a Drupal Site from Another Platform
subtitle: Troubleshooting
description: Troubleshoot common issues when migrating.
tags: [code, launch, migrate, site, updates]
contributors: [wordsmither]
showtoc: true
permalink: docs/guides/drupal-unhosted/troubleshooting
editpath: drupal/drupal-unhosted/15-troubleshooting.md
contenttype: [guide]
innav: [false]
categories: [migrate, troubleshooting]
cms: [drupal9, drupal8, drupal10, drupal]
audience: [development]
product: [--]
integration: [--]
reviewed: "2022-12-13"
---

This section covers common troubleshooting scenarios when migrating a Drupal site from another host to Pantheon's platform.

## Provided host name not valid

If you receive the error message "The provided host name is not valid for this server.", then update your `settings.php` file with a trusted host setting. Refer to the [Trusted Host Setting](/guides/php/settings-php#trusted-host-setting) documentation for more information.

<Partial file="drupal/troubleshooting-drush.md" />

<Partial file="drupal/troubleshooting-general.md" />

