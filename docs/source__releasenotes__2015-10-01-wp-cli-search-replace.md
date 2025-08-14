# source/releasenotes/2015-10-01-wp-cli-search-replace.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/source/releasenotes/2015-10-01-wp-cli-search-replace.md
> **Generated**: 2025-08-14 09:57:15

---

---
title: wp-cli search-replace
published_date: "2015-10-01"
categories: [tools-apis]
---
We improved Pantheon's use of `wp-cli search-replace` on clone/deploy operations and now replace strings in all database tables. Previously, we only replaced strings in tables registered with the $wpdb object. In most cases this was core WordPress tables only, since most plugin authors don't register tables they create with the $wpdb object.
