# source/releasenotes/2017-04-01-bug-fixes.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/source/releasenotes/2017-04-01-bug-fixes.md
> **Generated**: 2025-08-14 09:58:05

---

---
title: Bug Fixes
published_date: "2017-04-01"
categories: [performance]
---
In some cases, ssh operations to the platform would hang on connection if a user has ed25519 ssh keys in their agent keychain. This bug has been fixed. Note that we still don’t support ed25519 keys.
