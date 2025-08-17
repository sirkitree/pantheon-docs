# content/partials/terminus/site-upstream-set.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/terminus/site-upstream-set.md
> **Generated**: 2025-08-17 00:30:48

---

---
contenttype: [partial]
categories: [custom-upstreams]
cms: [--]
product: [terminus]
integration: [--]
tags: [--]
reviewed: ""
---

## Example

```bash{promptUser: user}
terminus site:upstream:set my-site "My Custom Upstream"
```

You can use any valid identifier (upstream name, upstream machine name, upstream UUID) returned in [upstream:list](/terminus/commands/upstream-list) to set a new upstream. For example, the upstream name "My Custom Upstream" is used above.

As a safeguard, Terminus will prevent a framework switch such as moving from Drupal to WordPress or vice versa.

<Alert title={"Note"} type={"info"}>

To set an empty upstream for Composer-managed sites, see [Serving Sites from the Web Subdirectory](/nested-docroot/).

</Alert>

After setting the upstream, you must bring in the new codebase by applying updates to the site.

### Terminus Error: Permission to change the upstream of this site

If you encounter an error when setting a site's upstream:

```bash{outputLines: 2}
terminus site:upstream:set $SITE $UPSTREAM
 [error]  You do not have permission to change the upstream of this site.
```

Confirm that the user you are authenticated as has the correct [Site-level permissions](/guides/account-mgmt/workspace-sites-teams/teams#site-level-roles-and-permissions).

To check the currently authenticated user:

```bash{promptUser: user}
terminus auth:whoami
```
