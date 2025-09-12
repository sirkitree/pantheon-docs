# content/guides/redirect/05-primary-domain.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/redirect/05-primary-domain.md
> **Generated**: 2025-09-12 18:08:10

---

---
title: Redirects Guide
subtitle: Set the Primary Domain
description: Learn how to set the primary domain for your site.
contenttype: [guide]
innav: [false]
categories: [domains]
cms: [--]
audience: [development]
product: [--]
integration: [--]
tags: [dns, https, redirects]
contributors: [wordsmither]
reviewed: "2022-08-01"
showtoc: true
permalink: docs/guides/redirect/primary-domain
---

Pantheon uses the term **primary domain** to refer to a single domain used to serve all traffic from a site. For example, configuring `www.example.com` as the primary domain means that requests to `example.com` (or any other custom domain connected to the environment) all get redirected to `www.example.com`. This assumes that you have added **both** `example.com` and `www.example.com` to the Site Dashboard.

Redirecting all traffic to a primary domain is a best practice for SEO since it avoids duplicate content. It also prevents session strangeness, where a user can be logged in to one domain but logged out of other domains at the same time, and it can make it easier to measure and monitor website traffic.

<Partial file="primary-domain.md" />

<Partial file="remove-primary-domain.md" />
