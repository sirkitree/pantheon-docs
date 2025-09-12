# content/guides/autopilot-custom-upstream/02-autopilot-custom-upstream-config.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/autopilot-custom-upstream/02-autopilot-custom-upstream-config.md
> **Generated**: 2025-09-12 09:06:49

---

---
title: Autopilot for Custom Upstreams
subtitle: Configure a Custom Upstream for Autopilot
description: Learn how to configure your Custom Upstream to use Autopilot.
tags: [autopilot, upstreams, D8, D9, D10]
contributors: [whitneymeredith]
showtoc: true
permalink: docs/guides/autopilot-custom-upstream/autopilot-custom-upstream-config
contenttype: [guide]
innav: [false]
categories: [automate]
cms: [--]
audience: [development]
product: [autopilot]
integration: [--]
reviewed: "2022-12-13"
---

There are three use cases for combining Autopilot and Custom Upstreams on the Pantheon platform.

## Autopilot Enabled on Downstream Sites Only

This use case is considered the standard use case for Autopilot. Autopilot always checks for an upstream in Pantheon’s upstream library or a Custom Upstream created by the user. Autopilot applies the updates from the upstream alongside other modules, plugins, and themes. This scenario makes the most sense if you are using your Custom Upstream as a boilerplate template.

<Alert title="Note: Drupal Users"  type="info" >

Autopilot Enabled on Downstream Sites Only is the best option if you are using Drupal with Integrated Composer. Updates cannot occur on both the upstream and the downstream or there will be continual conflicts due to technical configurations, including a single `composer.lock` file.

</Alert>

**Pros**:

- Easy to set up

- Follows Autopilot's default workflow and is less likely to run into errors

**Cons**:

- A new site created from the upstream might be out of date because Autopilot is not maintaining the upstream

### Enable Autopilot on Downstream Sites

1. [Create your Custom Upstream](/guides/autopilot-custom-upstream) if you haven't already created it.

1. Follow the steps in the [Enable Autopilot](/guides/autopilot/enable-autopilot/#enable-autopilot) section to enable Autopilot on your downstream sites.

    - Make sure you do not select to activate your Custom Upstream from the list of available sites in step 4 of the [Enable Autopilot](/guides/autopilot/enable-autopilot/#enable-autopilot) section.

1. Complete the steps in the [Configuration](/guides/autopilot/enable-autopilot/#configuration), [Schedule](/guides/autopilot/enable-autopilot/#configuration), and [Visual Review](/guides/autopilot/enable-autopilot/#visual-review) sections of the [Autopilot Setup Wizard](/guides/autopilot/enable-autopilot/#autopilot-setup-wizard).

## Autopilot Enabled on Custom Upstream and Downstream Sites

This use case requires you to set up your Custom Upstream as a Pantheon site and enable Autopilot. This setup is beneficial if you have broad portfolios of similar sites (such as universities). We recommend that the child sites exclude certain updates coming from the upstream (such as common plugins or modules) so out-of-sync updates do not accidentally get applied.

**Pros**:

- Two layers of testing

- Upstream is always up to date

**Cons**:

- You must exclude certain plugins and themes at the site level to avoid merge conflicts with the upstream

### Enable Autopilot on Your Custom Upstream and Downstream Sites

1. [Create your Custom Upstream](/guides/custom-upstream/create-custom-upstream) if you haven't already created it.

1. Follow the steps in the [Enable Autopilot](/guides/autopilot/enable-autopilot/#enable-autopilot) section to enable Autopilot on your Custom Upstream and downstream sites.

    - Make sure you select to activate your Custom Upstream and your downstream sites from the list of available sites in step 4 of the [Enable Autopilot](/guides/autopilot/enable-autopilot/#enable-autopilot) section.

1. Complete the steps in the [Configuration](/guides/autopilot/enable-autopilot/#configuration), [Schedule](/guides/autopilot/enable-autopilot/#configuration), and [Visual Review](/guides/autopilot/enable-autopilot/#visual-review) sections of the [Autopilot Setup Wizard](/guides/autopilot/enable-autopilot/#autopilot-setup-wizard).


## Autopilot Enabled on Custom Upstream Only

This use case requires you to set up your Custom Upstream as a Pantheon site with Autopilot enabled. However, you must ensure that your downstream sites do not have Autopilot enabled. This setup makes sense if you have thousands of sites and do not want to go through the process of maintaining Autopilot on each one. You might want to use Terminus commands to apply updates from the upstream if you use this setup.

**Pros**:

- All updates are maintained at one level

- Fewer VRT results to review

**Cons**:

- Does not fully take advantage of Autopilot's benefits

- Manual deployment of downstream updates

### Enable Autopilot on Your Custom Upstream

1. [Create your Custom Upstream](/guides/custom-upstream/create-custom-upstream) if you haven't already created it.

1. Follow the steps in the [Enable Autopilot](/guides/autopilot/enable-autopilot/#enable-autopilot) section to enable Autopilot on your Custom Upstream.

    - Make sure you only select to activate your Custom Upstream site from the list of available sites in step 4 of the [Enable Autopilot](/guides/autopilot/enable-autopilot/#enable-autopilot) section.

1. Complete the steps in the [Configuration](/guides/autopilot/enable-autopilot/#configuration), [Schedule](/guides/autopilot/enable-autopilot/#configuration), and [Visual Review](/guides/autopilot/enable-autopilot/#visual-review) sections of the [Autopilot Setup Wizard](/guides/autopilot/enable-autopilot/#autopilot-setup-wizard).


## More Resources

- [Autopilot Apply Updates](/guides/autopilot/apply-updates/)

- [Autopilot FAQs](/guides/autopilot/apply-updates/)

- [Custom Upstream Guide](/guides/custom-upstream)