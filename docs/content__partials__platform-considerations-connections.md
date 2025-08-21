# content/partials/platform-considerations-connections.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/platform-considerations-connections.md
> **Generated**: 2025-08-21 06:10:03

---

---
contenttype: [partial]
categories: [overview]
cms: [--]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

### Platform Considerations

Connections will change from time to time due to the containerized nature of the platform. For security reasons, using the `$_ENV` superglobal inside PHP applications is not supported. As an alternative, consider using a Bash script and Terminus connection. You can view an example in the [Create Secure Connection to MySQL using TLS](/guides/secure-development/ssh-tunnels#create-secure-connection-to-mysql-using-tls) documentation.
