# content/guides/domains/07-hosts-file.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/domains/07-hosts-file.md
> **Generated**: 2025-08-20 03:23:34

---

---
title: Domains on Pantheon
subtitle: Modify the Local Hosts File
description: Use your local hosts file to test domain-specific settings and DNS records.
tags: [cli, dns, local]
contributors: [alexfornuto]
showtoc: true
permalink: docs/guides/domains/hosts-file
contenttype: [guide]
innav: [false]
categories: [domains]
cms: [--]
audience: [development]
product: [--]
integration: [--]
---

This section provides information on how to modify your local `hosts` file.

The `hosts` file exists on all major operating systems. The `hosts` file provides a list of IP addresses and domains that take precedence over DNS assigned values. You can modify your `hosts` file for the following purposes:

- Test domain-specific settings leading up to a migration
- Test DNS records before updates
- Help with [local development](/guides/local-development)

<Partial file="_hosts-file.md" />

## Configure Your Hosts File with a Local Alias to Your Pantheon Environment

1. Use `dig` to get the IP address of your Pantheon environment to use in your `hosts` file. Replace `dev-example.pantheonsite.io` with your site's domain:

 ```bash{outputLines:2}
 dig +short dev-example.pantheonsite.io
 203.0.113.42
 ```

1. Edit the `hosts` file as shown below to map the result to an alias for easier local development:

 ```none
 203.0.113.42    dev-example
 ```