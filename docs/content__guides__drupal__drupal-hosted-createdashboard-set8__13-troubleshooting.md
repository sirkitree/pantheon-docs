# content/guides/drupal/drupal-hosted-createdashboard-set8/13-troubleshooting.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/drupal/drupal-hosted-createdashboard-set8/13-troubleshooting.md
> **Generated**: 2025-09-11 15:06:45

---

---
title: Upgrade a Site Created With the Pantheon Dashboard to the Latest Version of Drupal
subtitle: Troubleshooting
description: Troubleshoot common issues when migrating.
tags: [code, launch, migrate, site, updates, composer]
contributors: [wordsmither]
reviewed: "2022-12-13"
showtoc: true
permalink: docs/guides/drupal-hosted-createdashboard-set8/troubleshooting
editpath: drupal-hosted-createdashboard-set8/13-troubleshooting.md
contenttype: [guide]
innav: [false]
categories: [migrate, troubleshooting]
cms: [drupal8, drupal9, drupal10]
audience: [development]
product: [dashboard]
integration: [--]
---

## Your Requirements Could Not Be Resolved to an Installable Set of Packages

When setting the Drupal core version, use the command `composer update` instead of `composer update drupal/core* -W` if you receive the error message `Your requirements could not be resolved to an installable set of packages.`

## Working With Dependency Versions

<Partial file="composer-updating.md" />

<Partial file="drupal/troubleshooting-drush.md" />

<Partial file="drupal/troubleshooting-general.md" />
