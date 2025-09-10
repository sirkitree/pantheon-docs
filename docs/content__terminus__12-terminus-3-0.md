# content/terminus/12-terminus-3-0.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/terminus/12-terminus-3-0.md
> **Generated**: 2025-09-10 12:10:25

---

---
title: Terminus Guide
subtitle: Terminus 3
description: Learn what's new with the latest Terminus major version upgrade.
terminuspage: true
type: terminuspage
layout: terminuspage
contributors: [greg-1-anderson]
tags: [reference, cli, local, terminus, workflow]
permalink: docs/terminus/terminus-3-0
contenttype: [guide]
innav: [false]
categories: [cli]
cms: [drupal, wordpress]
audience: [development]
product: [terminus]
integration: [--]
---

This section provides information about Terminus 3.0. Terminus 3.0 is the most recent major version of Terminus and is recommended in place of Terminus 2.0.

<Alert title="Note" type="info" >

We suggest you read from the beginning of the [Terminus Guide](/terminus) if you're not already familiar with Terminus. This section is specifically geared at existing Terminus users who need to update existing implementations.

</Alert>

These commands or their output have changed in a significant way that may affect your existing scripting of Terminus.

## Deprecated Commands
No commands were deprecated in the Terminus 3.0 release.

## New Commands
The following commands are new to Terminus as of version 3.0:
- `self:plugin:install`: Install Terminus plugins.
- `self:plugin:list`: List installed Terminus plugins.
- `self:plugin:search` Find Terminus plugins on Packagist.
- `self:plugin:uninstall` Uninstall Terminus plugins.
- `self:plugin:update` Update already-installed Terminus plugins.

## Additional Changes
- Support for EOL versions of PHP have been removed from Terminus 3. PHP 7.4 or later is required.

## More Resources

- [Terminus on GitHub](https://github.com/pantheon-systems/terminus)
- [Terminus Guide](/terminus)
- [Terminus PHP Compatibility](/terminus/supported-terminus#php-version-compatibility-matrix)