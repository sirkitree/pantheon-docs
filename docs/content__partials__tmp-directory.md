# content/partials/tmp-directory.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/tmp-directory.md
> **Generated**: 2025-09-30 03:17:45

---

---
contenttype: [partial]
categories: [issues, files]
cms: [drupal]
product: [--]
integration: [modules]
tags: [--]
reviewed: ""
---

## Using the tmp Directory

**Issue:** Extensions that require the use of the `/tmp` directory are not supported. With multiple application containers, as exists on Live environments, it's assumed the `/tmp` directory will be on the same application container. However, as we run a distributed application container matrix, the `/tmp` directory is not shared.

**Solution:** For more details, see [Temporary File Management](/guides/filesystem/tmp).
