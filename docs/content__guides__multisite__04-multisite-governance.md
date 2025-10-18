# content/guides/multisite/04-multisite-governance.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/multisite/04-multisite-governance.md
> **Generated**: 2025-10-18 18:07:44

---

---
title: WordPress Multisite
subtitle: Multisite Governance
description: Learn more about governance with WordPress Multisites.
type: guide
contenttype: [guide]
innav: [false]
categories: [cms]
cms: [wordpress]
audience: [development]
product: [--]
integration: [--]
tags: [multisite]
permalink: docs/guides/multisite/multisite-governance/
editpath: multisite/04-multisite-governance.md
---

This section provides information on Multisite governance on Pantheon.

## Multisite on Pantheon

There are two primary layers involved in the governance system when you own a multisite on Pantheon.

**Pantheon**

- Workspace admin (full portfolio)

    - Site owner (specific WP site)

**WordPress**

- Network site admin (all sites)

    - Site admin (individual site)

This means that both Pantheon and your team manage different aspects of your multisite.

Pantheon's responsibilities include:

- Managing themes
- Administration
- Other technical aspects

Your team's responsibilities include:

- Content creation and editing
- Content accessibility
- Creating pages (site administrator)
- Managing site settings (site administrator)
- Managing pages and posts
- Uploading media
- Editing menus

## Multiple, Single Site Governance

Each WordPress site is owned or maintained by a different group at the Pantheon level. There is a management difference between who owns the Pantheon account and can update code versus who manages the application with content and site-specific configuration. For example:

- Site Owner US owns the US Pantheon site

    - Manager X manages WordPress

- Site Owner UK owns UK the Pantheon site

    - Manger Y manages WordPress

![Site Governance](../../../images/site-governance-multisite2.png)

## Multisite Governance

A multisite setup can be more efficient for teams as long as roles and responsibilities are defined.

**Pantheon Owner**
- 1 person in this role
- Pays for account
- Manages users who manage the platform, such as adding plugins, running backups, etc.

**WordPress Network Administrator**

- 2 people in this role
- Manages the core WP site
- Assigns users to country-specific subsites

**Individual Network Site Owners**

- 3 - 5 people in this role
- Manages content and plugin settings for an individual multisite

![Multisite Governance Example](../../../images/multisite-governance-example2.png)

## More Resources

- [WordPress on Pantheon Quick Start Guide](/guides/wordpress-pantheon/)

