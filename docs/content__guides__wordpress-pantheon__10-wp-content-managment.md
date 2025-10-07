# content/guides/wordpress-pantheon/10-wp-content-managment.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/wordpress-pantheon/10-wp-content-managment.md
> **Generated**: 2025-10-07 18:08:54

---

---
title: WordPress on Pantheon Quick Start Guide
subtitle: WordPress Content Management
description: Learn how to manage your WordPress content efficiently.
contenttype: [guide]
innav: [false]
categories: [cms]
cms: [wordpress]
audience: [development]
product: [--]
integration: [--]
tags: [wordpress, webops]
contributors: [whitneymeredith]
reviewed: "2022-05-09"
showtoc: true
permalink: docs/guides/wordpress-pantheon/wp-content-management
---

This section provides information to make managing content and tasks in your WordPress site easier.

## Content Staging

Review our [Content Staging](/content-staging) doc to learn how to successfully stage and move content between environments in your WordPress site.

## WordPress Configuration Management (WP-CFM)

The [WP-CFM plugin](/guides/wordpress-configurations/wp-cfm) provides an elegant mechanism for enabling developers to practice configuration management in code. The plugin exports WordPress site configuration from the SQL database's wp_options table to a .json file stored in private/config. After deploying the file to a new environment for the same site, it can then import the configuration from the .json file into the second wp_options table.

## Cron for WordPress

Review our [Cron for WordPress](/guides/wordpress-developer/wordpress-cron) doc to learn how to create and run jobs using Pantheon Cron or WordPress's WP-Cron feature on your Pantheon site.

## WordPress Multisite

WordPress Multisite lets you create a network of sites using a single copy of the WordPress codebase and a common database. For those responsible for maintaining several or dozens of similar sites, WordPress Multisites can make it much easier to fix bugs and deploy new features across all of those sites. Review our guide to learn how Pantheon supports [WordPress Multisite](/guides/multisite/).
