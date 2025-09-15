# content/partials/migrate/troubleshooting-wordpress.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/migrate/troubleshooting-wordpress.md
> **Generated**: 2025-09-15 09:08:14

---

---
contenttype: [partial]
categories: [troubleshooting, cmss]
cms: [wordpress]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

## WordPress Issues

### CDN Blocking POST requests

**Cause:** This error can occur on sites using a content delivery network (CDN) service that is not configured to allow the POST HTTP method.

**Solution:**  [Temporarily set POST as an allowed HTTP method within the CDN's configuration](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesAllowedHTTPMethods) and restart the migration process. The POST HTTP method can be disabled after the site has been successfully migrated.

### Very Large Site Footprints

**Cause:** Imports can also fail for very large sites, which may time out while importing.

**Solution:** Restart the migration by going to the browser tab containing your WordPress dashboard, and click **Migrate**

![Copying and pasting info](../../../images/migrate-site-wp-blogvault.png)


### Could not import code, the import file does not appear to contain a valid code directory.

**Cause:** The migration tool could not find the core files. This prevents the migration from completing because the site modules, plugins, and/or themes cannot be imported. This error also occurs when multiple `settings.php` files are present.

**Solution:** Check that the archive includes a valid code root with all core files. If multiple `settings.php` files are present, delete them from the archive. Archives for WordPress sites should include `index.php` at the code root level, along with the following directories:

```none
├── index.php
├── wp-activate.php
├── wp-config.php
├── wp-comments-post.php
├── wp-blog-header.php
├── wp-admin
├── wp-cron.php
├── wp-load.php
├── wp-links-opml.php
├── wp-includes
├── xmlrpc.php
├── wp-trackback.php
├── wp-signup.php
├── wp-settings.php
├── wp-mail.php
├── wp-login.php
├── wp-content
    ├── index.php
    ├── mu-plugins
    ├── themes
    ├── plugins

```

### Multiple file directories found within the import archive

**Cause:** The migration tool found more than one potential location for files within the archive. 

**Solution:** All files must be moved into `/wp-content/uploads`. For more details, see [Files](/guides/filesystem/) and [Symlinks and Assumed Write Access](/symlinks-assumed-write-access).

