# content/guides/errors-and-server-responses/04-retries-server-containers.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/errors-and-server-responses/04-retries-server-containers.md
> **Generated**: 2025-09-11 15:06:45

---

---
title: Errors and Server Responses
subtitle: Retries Across Application Server Containers (High Availability)
description: Learn more about application server containers on Pantheon.
tags: [services]
contributors: [whitneymeredith]
showtoc: true
permalink: docs/guides/errors-and-server-responses/retries-server-containers
contenttype: [guide]
innav: [false]
categories: [issues]
cms: [drupal, wordpress]
audience: [development]
product: [--]
integration: [--]
---

This section provides information on how to resolve Pantheon server container errors.

## Retries Across Application Server Containers (High Availability)

[Higher plan levels on Pantheon](https://pantheon.io/plans/pricing) deploy [multiple containers](/application-containers#multiple-application-containers) for the Live environment. Rather than just supporting scale, Pantheon also uses the extra containers for high-availability. Review the examples below for different cases when Pantheon's edge may retry a request against a different application container.

### Failed Connections

Pantheon's edge randomly distributes requests to application containers. nginx uses a short request queue (about 128) to allow sites to fully use the capacity of every container. Containers will refuse to queue more requests when they reach queue capacity. A refused connection causes the Pantheon edge to reattempt the request to all other healthy containers, and even a few unhealthy containers (an unhealthy container is any container with a failed connection or 5xx code in the last 10 minutes).

### HTTP 502 or 560 Response to Requests with Idempotent HTTP Methods

Pantheon regularly updates application container software and configuration. These updates result in reloads and restarts that can briefly cause the first requests to return HTTP 502 responses. The system will automatically retry the request against to a few healthy application containers when the HTTP method of the request is idempotent (is safe to re-attempt). This includes all methods except POST, PUT, DELETE, and PATCH on Pantheon.

Additionally, the customer code may determine that a resource necessary to process a request is unavailable. The application can trigger the same reattempts under the same conditions as an HTTP 502 response by sending an HTTP 560 response.

## More Resources

- [5xx Level Errors](/guides/errors-and-server-responses/5xx-errors)

- [All About Application Containers](/application-containers)
