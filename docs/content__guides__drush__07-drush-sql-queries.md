# content/guides/drush/07-drush-sql-queries.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/drush/07-drush-sql-queries.md
> **Generated**: 2025-09-30 06:09:55

---

---
title: Drupal Drush Command-Line Utility on Pantheon
subtitle: Drush SQL Queries
description: Learn how to use Drush SQL queries.
tags: [migrate, terminus, drush]
permalink: docs/guides/drush/drush-sql-queries
contenttype: [guide]
innav: [false]
categories: [cli]
cms: [drupal]
audience: [development]
product: [--]
integration: [drush]
---

This section provides information on how to run SQL queries with Drush on Pantheon.

The `drush sql-cli` and `drush sql-connect` commands are not supported on Pantheon. For security reasons, the SQL database is not directly accessible from your local machine.

You can, however, use Terminus as follows:

```bash{promptUser: user}
echo 'SELECT * FROM users WHERE uid=1;' | terminus drush SITENAME.ENV sql:cli
```

Note that certain characters such as `;` cannot be used in the query. You will receive an error message if you use an illegal character:

> Command not supported as typed.

Note that the trailing `;` in the SQL query is optional in this context.

## More Resources

- [MariaDB and MySQL on Pantheon](/guides/mariadb-mysql/mysql-workbench)
- [Database Connection Errors](/guides/mariadb-mysql/database-connection-errors)
- [Database Workflow Tool](/guides/mariadb-mysql/database-workflow-tool)