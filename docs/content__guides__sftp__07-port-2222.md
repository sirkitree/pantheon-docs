# content/guides/sftp/07-port-2222.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/sftp/07-port-2222.md
> **Generated**: 2025-09-29 00:27:22

---

---
title: SFTP on Pantheon
subtitle: Blocked Port 2222 Workaround
description: Learn how to access Port 2222 with an SSH tunnel if it's blocked.
innav: [false]
categories: [troubleshooting, sftp]
tags: [files, ssh]
cms: [drupal, wordpress]
audience: [development]
product: [dashboard]
integration: [--]
showtoc: true
permalink: docs/guides/sftp/port-2222
---

This section provides a workaround to allow you to access port 2222 if it is blocked.

You must have access to port 2222 to push and pull code to your Pantheon site. You will receive an error similar to the one below if the port is blocked as a result of a corporate firewall or router configuration.

```none
SSH: connect to host codeserver.dev.<site UUID>.drush.in port 2222: No route to host
Fatal: Could not read from remote repository.
```

## Workaround Prerequisites

You must have the following to use the workaround outlined in this section:

- SSH access to another server outside of your network that can access port 2222 and reach Pantheon's Git servers. 

- The ability to run the open tunnel command before performing any remote Git operations.

## Set up the SSH Tunnel

Open a terminal window and initiate the SSH tunnel:

```bash{promptUser: user}
ssh -L<local port #>:<pantheon server>:<pantheon port> user@other-server.com
```

The following example includes Pantheon credentials ([site UUID](/guides/account-mgmt/workspace-sites-teams/sites#retrieve-the-site-uuid) omitted). You can use the port numbers from this example (you must leave port 2222 in place).

```bash{promptUser: user}
ssh -L3333:codeserver.dev.<site UUID>.drush.in:2222 user@other-server.com
```

You should now be logged in to the other server, but simultaneously you've just set up your local port 3333 as a tunnel to your Pantheon Git repo.

## Clone the Repository

You must have a fully cloned repository to push and pull changes from.

1. Open a second terminal window.

1. Replace the repository URL before you run the command below to clone the repository.

    ```bash{promptUser: user}
    git clone <Pantheon repository URL>@localhost:3333/~/repository.git
    ```

    Here's an example with Pantheon credentials (site UUID omitted):

    ```bash{promptUser: user}
    git clone ssh://codeserver.dev.<site UUID>:3333/~/repository.git
    ```

### Add a Remote (Optional)

You can add a remote repository if you use GitHub or Bitbucket in parallel, for example.

1. Verify that the SSH tunnel is open.

1. Run code similar to the example below:

    ```bash{promptUser: user}
    git remote add pantheon ssh://codeserver.dev.<site UUID>@localhost:3333/~/repository.git
    ```

## Additional Information

### Git Commands Stopped Working

Follow the steps below if your Git commands stop working.

1. Navigate to the original terminal window.

1. Check if the tunnel has collapsed.

1. Close the tunnel and then reopen it.

Refer to the [Git over an ssh tunnel](https://randyfay.com/content/git-over-ssh-tunnel-through-firewall-or-vpn) article for more information.


## More Resources

- [Secure Connections to Pantheon Services via TLS or SSH Tunnels](/guides/secure-development/ssh-tunnels)
- [Generate and Add SSH Keys](/ssh-keys)