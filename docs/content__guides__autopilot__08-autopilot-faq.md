# content/guides/autopilot/08-autopilot-faq.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/autopilot/08-autopilot-faq.md
> **Generated**: 2025-09-07 21:05:42

---

---
title: Pantheon Autopilot
subtitle: Autopilot FAQs
description: Get answers to your Autopilot questions.
tags: [autopilot, webops, D8, D9, D10]
type: guide
showtoc: true
permalink: docs/guides/autopilot/autopilot-faq/
reviewed: "2022-12-14"
contenttype: [guide]
innav: [false]
categories: [automate, test, update, faq]
cms: [--]
audience: [development]
product: [autopilot]
integration: [--]
---

This section provides answers to frequently asked questions about Autopilot.

## Is Autopilot configurable per site?

Yes. Access to Autopilot is account-based and individual sites in that account can turn Autopilot on and off as desired. See [Enable Autopilot](/guides/autopilot/enable-autopilot).

## Will Autopilot email VRT results?

Yes. Configure [Autopilot activity digests and notifications](/guides/autopilot/enable-autopilot/#enable-autopilot-email-notifications) in your Personal Workspace settings **Notifications** tab.

## Does Autopilot work with Integrated Composer?

Yes. If your site is using [Integrated Composer](/guides/integrated-composer) (`build_step` is `true` in the `pantheon.yml` [file](/pantheon-yml)), Autopilot will be able to update it.

## Does Autopilot work with Build Tools?

Not yet. [Autopilot](/guides/autopilot) is not compatible with [Build Tools](/guides/build-tools/) or other workflows that use external Git repositories.

## What versions of Drupal are supported by Autopilot?

Autopilot supports all versions of Drupal, as follows:

- Drupal sites that use Integrated Composer are compatible with Autopilot.

- Sites on Drupal 7 or 8 that are **not** using Integrated Composer, must use Drush 8 to be compatible with Autopilot.


## Does Autopilot support Terminus actions?

Refer to the [Autopilot Terminus plugin documentation](https://github.com/pantheon-systems/terminus-autopilot-plugin#readme) for information on supported actions.

## Where do my updates go if I select the Do Not Deploy destination option?

Your updates will appear under **Ready to Deploy** if the updates pass VRT. Your updates will appear under **Needs Review** if the updates fail VRT. The updates must be deployed manually from either location. Refer to [Update Destination & Frequency](/guides/autopilot/enable-autopilot/#update-destination--frequency) for more information.

## Can I stop updates at the Multidev?

Yes. You must select the Do Not Deploy option under [Destination & Frequency](/guides/autopilot/enable-autopilot/#update-destination--frequency). This stops updates at the Autopilot Multidev. Your updates will be tested but not deployed to any environment if you select this option. Your updates will appear under **Ready to Deploy** if the updates pass VRT. Your updates will appear under **Needs Review** if the updates fail VRT. The updates must be deployed manually from either location.

## Does Autopilot automatically deploy changes to the Live environment?

You can specify the environments to which Autopilot deploys. See the [configuration options](/guides/autopilot/enable-autopilot).

## Does Autopilot clone the database from Live to Dev before doing the updates?

Autopilot tests updates against a Multidev cloned from the current Dev environment by default. Opt into the [Sync Environment](/guides/autopilot/enable-autopilot/#schedule) feature in the site's **Configuration** tab to sync your Live environment before Autopilot checks for updates.

## Does the Autopilot Multidev count towards the Multidev limit?

No. If you encounter any issues about Multidev limits, [contact Support](/guides/support/contact-support).

## Does Autopilot perform tests on authenticated pages?

Not yet. Currently, Autopilot only supports tests on anonymous access versions of pages. Support for authenticated (logged-in user) page tests is planned for a future release.

## What does Autopilot specifically check for?

Autopilot only checks for changes and updates to modules, themes, and core. You should take time to carefully review and test changes that fall outside of Autopilot's scope, including:

- Code changes

- PHP changes

- Templates changes

- Other backend changes

## Is there a limit to the number screenshots Autopilot will take?

Yes. Depending on your [Account](/guides/support#support-features-and-response-times), Autopilot can be set for up to 25 pages on each site. It will check for updates once a week, and can also be run on demand.

## Is Autopilot compatible with premium and paid WordPress plugins?

Yes, Autopilot is compatible with premium and paid WordPress plugins. Refer to [Configure Autopilot for Premium and Paid Plugins](/guides/autopilot/enable-autopilot/#configure-autopilot-for-premium-and-paid-plugins) for more information.

## More Resources

- [Apply Autopilot Updates](/guides/autopilot/apply-updates)

- [Autopilot Custom Upstream Guide](/guides/autopilot-custom-upstream)
