# content/partials/terminus/site-create.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/terminus/site-create.md
> **Generated**: 2025-09-28 03:23:13

---

---
contenttype: [partial]
categories: [create]
cms: [--]
product: [terminus]
integration: [--]
tags: [--]
reviewed: ""
---

## Available Region Codes

<!--
Terminus command examples don't play well with partial files.
If you're here to edit this info,
update terminus-available-regions-table.md as well.
-->

| Name           | Code |
|----------------|------|
| Australia      | au   |
| Canada         | ca   |
| European Union | eu   |
| United States  | us   |

For example (replace `my-eu-site-name`, `My EU Site Name`, `WordPress`, `My Workspace Name`, and the `eu` region accordingly):

```bash{outputLines: 2-4}
terminus site:create my-eu-site-name "My EU Site Name" "WordPress" --org "My Workspace Name" --region eu
[notice] Creating a new site...
[notice] Deploying CMS...
[notice] Deployed CMS
```
