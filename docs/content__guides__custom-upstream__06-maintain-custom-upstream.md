# content/guides/custom-upstream/06-maintain-custom-upstream.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/custom-upstream/06-maintain-custom-upstream.md
> **Generated**: 2025-09-17 03:14:42

---

---
title: Custom Upstreams on Pantheon
subtitle: Custom Upstream Best Practices
description: Detailed information on how to maintain Custom Upstreams.
tags: [git, upstreams, workflow, D8, D9, D10]
showtoc: true
permalink: docs/guides/custom-upstream/maintain-custom-upstream
contenttype: [guide]
innav: [false]
categories: [custom-upstreams]
cms: [drupal, wordpress]
audience: [development]
product: [custom-upstreams]
integration: [--]
reviewed: "2023-04-17"
---

This section provides information to help you manage and maintain your Custom Upstream.

## Upstream Configuration File

Use the `pantheon.upstream.yml` file when working with Custom Upstreams to set default values for advanced site configurations to be used downstream. Review the [Pantheon YAML Configuration Files](/pantheon-yml) documentation for details.

## Redirects

We normally suggest [PHP redirects](/guides/redirect) be placed into `wp-config.php` for WordPress and `settings.php` for Drupal. You will lose any customizations to your PHP files every time you update your Custom Upstream. It will also be difficult to implement site-specific configurations added on these files.

You can use a `require_once` statement to point to an external file since this file is shared on all environments, including Multidevs. It is also separate from the Custom Upstream and unique to each site:

```php
if ( file_exists( dirname( __FILE__ ) . '/guides/redirect.php' ) && isset( $_ENV['PANTHEON_ENVIRONMENT'] ) ) {
  require_once( dirname( __FILE__ ) . '/guides/redirect.php' );
}
```

Remember that this file is not included in the Custom Upstream and must exist uniquely on each site. You can then expand the conditional statement to load on specific environments using the FAQ section in the [wp-config-php doc](/guides/php/wp-config-php#how-can-i-write-logic-based-on-the-pantheon-server-environment).

WordPress sites can also store redirects in an [MU-Plugin](/guides/wordpress-configurations/mu-plugin).

## WordPress MU-Plugins

Be sure to include and update the [MU-Plugins](https://github.com/pantheon-systems/WordPress/tree/6.2/wp-content/mu-plugins/pantheon-mu-plugin) if you are using WordPress.

Refer to the [WordPress Configuration](/guides/wordpress-configurations) guide for more information about [MU-Plugins on the platform](/guides/wordpress-configurations/mu-plugin).

## More Resources

- [Clear Upstream Cache](/terminus/commands/site-upstream-clear-cache)

- [Troubleshoot a Custom Upstream](/guides/custom-upstream/troubleshooting)

- [Autopilot for Custom Upstreams](/guides/autopilot-custom-upstream)
