# source/releasenotes/2016-07-01-tls-1-0-deprecated.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/source/releasenotes/2016-07-01-tls-1-0-deprecated.md
> **Generated**: 2025-08-14 09:57:36

---

---
title: TLS 1.0 Deprecated
published_date: "2016-07-01"
categories: [deprecated]
---
In keeping with the recommendations of PCI DSS, we no longer support TLS 1.0 for customer sites. [Older browsers and mobile devices](https://en.wikipedia.org/wiki/Transport_Layer_Security#Web_browsers) that do not support TLS 1.1 and 1.2 will likely experience problems and security vulnerabilities. If you need to continue support for TLS 1.0, you can do so with [Cloudflare](/cloudflare). For details, see [Cloudflare's documentation](https://support.cloudflare.com/hc/en-us/articles/205043158-PCI-3-1-and-TLS-1-2).
