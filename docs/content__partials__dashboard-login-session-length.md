# content/partials/dashboard-login-session-length.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/dashboard-login-session-length.md
> **Generated**: 2025-11-01 12:09:41

---

---
contenttype: [partial]
categories: [accounts]
cms: [--]
product: [dashboard]
integration: [--]
tags: [--]
reviewed: ""
---

The session length for users logged into the Pantheon Dashboard is 14 hours, after which users are forcibly logged out and prompted to log back in.

[Terminus](/terminus/install) sessions are authenticated via a machine token and refreshed based on activity. After 30 days of inactivity, Terminus users will be prompted to re-authenticate via the `auth:login` command.
