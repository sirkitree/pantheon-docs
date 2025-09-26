# content/guides/errors-and-server-responses/01-Introduction.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/errors-and-server-responses/01-Introduction.md
> **Generated**: 2025-09-26 09:07:03

---

---
title: Errors and Server Responses
subtitle: Introduction
description: Learn more about errors and server responses on Pantheon.
tags: [services]
contributors: [whitneymeredith]
showtoc: true
permalink: docs/guides/errors-and-server-responses
contenttype: [guide]
innav: [true]
categories: [issues]
cms: [drupal, wordpress]
audience: [development]
product: [--]
integration: [--]
---

Pantheon serves error messages when a request cannot be fulfilled. These error messages cannot be customized for a particular site because of the low-level nature of these errors, and the fact that changes are system-wide, not site specific.

There are some extreme circumstances in which these error messages can be inadvertently triggered by your site code without an actual cloud server error. You should monitor plugins or modules that integrate with external applications closely, such as [services](https://www.drupal.org/project/services) for Drupal, to learn to distinguish actual errors from false alarms.

[Contact support](/guides/support/contact-support/) if you think that you have received an error mistakenly, and be sure to provide the full URL and the circumstances which led to the error.

## Error Messages

Review the [4xx errors page](/guides/errors-and-server-responses/4xx-errors) for 400-level error explanations and the [5xx errors page](/guides/errors-and-server-responses/5xx-errors) for 500-level error explanations.

## More Resources

- [PHP Errors and Exceptions](/guides/php/php-errors)

- [Database Connection Errors](/guides/mariadb-mysql/database-connection-errors)

- [Timeouts on Pantheon](/timeouts)