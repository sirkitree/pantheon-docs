# content/partials/migrate/deploy-dev.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/migrate/deploy-dev.md
> **Generated**: 2025-08-18 06:10:21

---

---
contenttype: [partial]
categories: [migrate]
cms: [--]
product: [--]
integration: [--]
tags: [--]
reviewed: "2022-11-03"
---

Now that you've committed your code additions locally, push the commits to Pantheon to deploy them to your Dev environment:

```bash{promptUser: user}
terminus connection:set $SITE.dev git
git push origin master
```
