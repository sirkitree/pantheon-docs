# content/guides/custom-upstream/07-switch-custom-upstream.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/custom-upstream/07-switch-custom-upstream.md
> **Generated**: 2025-09-24 12:11:11

---

---
title: Custom Upstreams on Pantheon
subtitle: Switch Your Custom Upstream
description: Learn how to switch your Custom Upstream.
tags: [upstreams, workflow, webops, D8, D9, D10 ]
showtoc: true
permalink: docs/guides/custom-upstream/switch-custom-upstream
contenttype: [guide]
innav: [false]
categories: [custom-upstreams]
cms: [drupal, wordpress]
audience: [development]
product: [custom-upstreams]
integration: [--]
reviewed: "2022-12-13"
---

This section provides steps to switch an existing site's Custom Upstream to a different Custom Upstream.

<Alert title="Warning" type="danger">

Switching the upstream of an existing site is risky. It is safer to create a new site from your Custom Upstream and migrate the contents. [Back up](/guides/backups) your site first and consider our documentation on [upstream merge conflicts](/core-updates/#apply-upstream-updates-manually-from-the-command-line-to-resolve-merge-conflicts) if you must switch upstreams.

</Alert>

## Switch Your Custom Upstream

Review the [Terminus Switch Upstream example](/terminus/examples#switch-upstreams) before following the steps below to switch your Custom Upstream.

1. Run the command below to locate your Custom Upstream's machine name, replacing `$org` with your organization name.
    
    ```bash
    terminus org:upstream:list $org
    ```

1. Run the command below to change the upstream, setting or replacing the variables `$site` and `$upstream_id` with your site name and upstream machine name, respectively.

    ```bash{promptUser: user}
    terminus site:upstream:set $site $upstream_id
    ```

## More Resources

- [Terminus Set Upstream Steps](/terminus/commands/site-upstream-set#terminus-error-permission-to-change-the-upstream-of-this-site) 