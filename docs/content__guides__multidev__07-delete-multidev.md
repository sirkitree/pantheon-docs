# content/guides/multidev/07-delete-multidev.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/multidev/07-delete-multidev.md
> **Generated**: 2025-08-27 03:20:53

---

---
title: Multidev
subtitle: Delete Branch Environments and Branches
description: Learn how to delete branch environments and branches in Multidev.
contenttype: [guide]
innav: [false]
categories: [multidev]
cms: [--]
audience: [development]
product: [multidev]
integration: [--]
tags: [cms, logs]
contributors: [whitneymeredith]
showtoc: true
permalink: docs/guides/multidev/delete-multidev
---

This section provides steps on how to delete a branch environment and how to delete a branch.

## Delete a Branch Environment

A deleted branch environment will remain on the platform and must be removed manually.

1. [Go to the Site Dashboard](/guides/account-mgmt/workspace-sites-teams/sites#site-dashboard), then click **Multidev**.

1. Click **Multidev Environments** then click **Delete Environment**.


## Delete a Branch

Branches can be deleted locally and the commit can be pushed to Pantheon, but this may have unintended consequences if an environment is associated with it. We recommend that you use the Pantheon platform instead.

Follow the steps below to delete a branch with no environment associated with it.

1. [Go to the Site Dashboard](/guides/account-mgmt/workspace-sites-teams/sites#site-dashboard), then click **Multidev**.

1. Click **Git Branches** then click **Delete Git Branch**.


## More Resources

- [Frequently Asked Questions](/guides/multidev/multidev-faq)
