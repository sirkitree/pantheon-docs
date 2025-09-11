# content/partials/wp_get_environment_type.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/wp_get_environment_type.md
> **Generated**: 2025-09-11 03:18:39

---

---
contenttype: [partial]
categories: [config]
cms: [wordpress]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

WordPress 5.5 [introduced the `wp_get_environment_type` function](https://make.wordpress.org/core/2020/07/24/new-wp_get_environment_type-function-in-wordpress-5-5/). The Platform automatically defines `wp_get_environment_type` based on the environment variables set by the platform.

Note that the environment variables used by WordPress differ from the names used on Pantheon:

| Pantheon Environment | `wp_get_environment_type` |
|----------------------|---------------------------|
| dev / Multidev       | development               |
| test                 | staging                   |
| live                 | production                |
