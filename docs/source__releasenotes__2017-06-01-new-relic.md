# source/releasenotes/2017-06-01-new-relic.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/source/releasenotes/2017-06-01-new-relic.md
> **Generated**: 2025-08-14 09:58:13

---

---
title: New Relic
published_date: "2017-06-01"
categories: [infrastructure, performance, tools-apis]
---
New Relic's APM Availability Monitoring has [known incompatibilities](/guides/new-relic) with SNI, which our HTTPS uses. Instead, we recommend configuring the free availability monitoring service within New Relic’s Synthetics Lite tool. For details, refer to [New Relic APM Pro](/guides/new-relic/).
