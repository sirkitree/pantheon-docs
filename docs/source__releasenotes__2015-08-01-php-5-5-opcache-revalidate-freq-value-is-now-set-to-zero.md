# source/releasenotes/2015-08-01-php-5-5-opcache-revalidate-freq-value-is-now-set-to-zero.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/source/releasenotes/2015-08-01-php-5-5-opcache-revalidate-freq-value-is-now-set-to-zero.md
> **Generated**: 2025-08-14 09:57:06

---

---
title: PHP 5.5 opcache revalidate-freq Value is Now Set to Zero
published_date: "2015-08-01"
categories: [drupal, wordpress]
---
Previously, for sites on PHP 5.5 (WordPress sites default, Drupal sites can [upgrade now](/guides/php/php-versions)), code changes were only refreshed every 60 seconds, regardless of the environment. Now, Dev/Multidev environments on 5.5 will immediately see code changes, and Test/Live now refresh every 2 seconds.
