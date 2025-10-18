# content/guides/environment-configuration/01-introduction.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/environment-configuration/01-introduction.md
> **Generated**: 2025-10-18 09:06:19

---

---
title: Environment Configuration
subtitle: Environment Configuration on Pantheon
description: Learn about environment configurations on Pantheon.
tags: [site, terminus, workflow, webops]
contributors: [whitneymeredith]
showtoc: true
permalink: docs/guides/environment-configuration
contenttype: [guide]
innav: [true]
categories: [config]
cms: [--]
audience: [development]
product: [--]
integration: [--]
---

Each site on Pantheon comes with three environments: Dev, Test, and Live. This allows you to develop and test features without impacting your Live site. Additional development environments are available with [Multidev](/guides/multidev). Refer to the [Pantheon WebOps Workflow](/pantheon-workflow) documentation for more details.


## Code and Configuration in Separate Environments

The separation of configuration and code also helps improve security and makes it easy to restore an individual environment to a backup version.

This guide shows you how to:

- Read environment configuration

- Install an indicator to receive updates on your Pantheon site and environments

- Restore an environment

- Configure WordPress-specific environments and Drupal-specific environments

## More Resources

- [Configuration Management](/pantheon-workflow#configuration-management)

- [Content Staging](/content-staging)