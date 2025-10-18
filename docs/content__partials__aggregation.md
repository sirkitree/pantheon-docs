# content/partials/aggregation.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/aggregation.md
> **Generated**: 2025-10-18 15:06:10

---

---
contenttype: [partial]
categories: [cache]
cms: [drupal]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

Pantheon uses HTTP/2 which allows files to download in parallel. This can *potentially* make aggregation unnecessary for your site. Aggregation depends on several factors, including:

- File sizes
- Number of files
- End users' browsers

We recommend that you keep aggregation enabled if you aren't familiar with how aggregation factors apply to your site. 
