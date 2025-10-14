# content/partials/ssh-ServerAliveInterval.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/ssh-ServerAliveInterval.md
> **Generated**: 2025-10-14 21:06:10

---

---
contenttype: [partial]
categories: [ssh]
cms: [--]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

### "Connection to server closed by remote host" returned by long-running CLI operations
Long-running Drush and/or WP-CLI commands may timeout due to the [idle timeout limit](/timeouts) on SSH connections. You can avoid this by configuring your local machine to send an SSH `keepalive` packet every 60 seconds. Add this to your `$HOME/.ssh/ssh_config` file:

```ini
Host *.drush.in
  ServerAliveInterval 60
```

