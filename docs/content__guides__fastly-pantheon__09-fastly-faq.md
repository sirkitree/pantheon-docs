# content/guides/fastly-pantheon/09-fastly-faq.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/fastly-pantheon/09-fastly-faq.md
> **Generated**: 2025-10-09 12:10:56

---

---
title: Fastly on Pantheon
subtitle: Fastly on Pantheon FAQs
description: Get answers to your Fastly on Pantheon questions. 
tags: [cms, logs]
contributors: [whitneymeredith]
showtoc: true
permalink: docs/guides/fastly-pantheon/fastly-faq
contenttype: [guide]
innav: [false]
categories: [cache]
cms: [--]
audience: [development]
product: [--]
integration: [fastly]
---

This section provides answers to frequently asked questions about using Fastly on the Pantheon platform.

## Can I use my own Fastly account with the Pantheon Global CDN?

Yes. If you're using Fastly TLS services with WordPress, you'll want to check for the `HTTP_FASTLY_SSL` header so that WordPress can build URLs to your CSS and JS assets correctly. Do this by adding the following to `wp-config.php`:

```php:title=wp-config.php
if (!empty( $_SERVER['HTTP_FASTLY_SSL'])) {
  $_SERVER['HTTPS'] = 'on';
}
```

## Are there other logging endpoints I can use with my Fastly account on Pantheon?

Yes. You can use any of the [Fastly logging endpoints](https://docs.fastly.com/en/guides/integrations#_logging-endpoints) if you have [connected your Fastly account to your Pantheon account](/guides/fastly-pantheon/connect-fastly).

## How Can I Test My Fastly Caching Features?

You can test your Fastly caching features by [confirming that your experience protection works](/guides/global-cdn#confirm-that-experience-protection-works).

## Who sets up the Fastly edge configuration files?

Advanced Global CDN is supported by Pantheon’s experienced [Professional Services](/guides/professional-services) team, who can set up, configure, and maintain your Fastly edge configurations.

## Why is the timeout still set to 59 seconds, after setting up the time out for 120 seconds?

All web requests are set to 59 seconds. Fastly's GCDN terminates the request if the backend does not respond after 59 seconds. PHP will continue to process the request until it hits the PHP `max_execution_time`. However, the results will not be relayed to the user browser because the connection has already terminated.

All non-web requests, such as those that do not pass Fastly's CDN, have a maximum timeout of 120 seconds. This includes requests from Terminus or PHP scripts via SSH.

<Alert title="Note"  type="info" >

The request will timeout at 59 seconds if it passes through port 80 and 443. 

</Alert>

## More Resources

- [Fastly Resources FAQ](https://www.fastly.com/resources/?q=faq)

- [Fastly logging endpoints](https://docs.fastly.com/en/guides/integrations#_logging-endpoints)
