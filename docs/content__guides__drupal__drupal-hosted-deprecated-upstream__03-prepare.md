# content/guides/drupal/drupal-hosted-deprecated-upstream/03-prepare.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/drupal/drupal-hosted-deprecated-upstream/03-prepare.md
> **Generated**: 2025-08-17 15:05:43

---

---
title: Upgrade a Site That Was Created Using a Deprecated Upstream to the Latest Version of Drupal
subtitle: Prepare
description: 
tags: [code, launch, migrate, site, updates]
contributors: [wordsmither]
showtoc: true
permalink: docs/guides/drupal-hosted-deprecated-upstream/prepare
editpath: drupal/drupal-hosted-deprecated-upstream/03-prepare.md
reviewed: "2022-12-13"
contenttype: [guide]
innav: [false]
categories: [migrate, update]
cms: [drupal9, drupal, drupal8, drupal10]
audience: [development]
product: [terminus, composer]
integration: []
draft: true
---

This page provides steps on preparing your site for migration to [Drupal with Composer Upstream](/guides/integrated-composer).

## Use Terminus to Confirm the Drupal Upstream

Run the command `terminus site:info $SITE` to display the site's basic information and properties.

The following is an abridged example of the output for a site upstream set to `drupal-project`:

```bash{outputLines:2-13}
terminus site:info $SITE
------------------ -------------------------------------------------------------------------------------
ID                 abdc3ea1-fe0b-1234-9c9f-3cxeAA123f88
Name               anita-drupal
Label              AnitaDrupal
Created            2019-12-02 18:28:14
Framework          drupal8
...
//highlight-start
Upstream           e96c6794-77fe-4931-9a20-48a2fe1a3789: https://github.com/pantheon-upstreams/drupal-project.git
//highlight-end
...
------------------ -------------------------------------------------------------------------------------
```
Use these values to determine which upstream a site is using:

| Framework | Upstream | Site upstream is...
|---|---|---
|drupal8|https://github.com/pantheon-upstreams/drupal-recommended.git|drupal-recommended
|drupal8|https://github.com/pantheon-upstreams/drupal-project.git|drupal-project



## Prepare the Local Environment

<Partial file="drupal/prepare-local-environment-no-clone.md" />
