# content/partials/export-database.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/export-database.md
> **Generated**: 2025-09-20 21:05:46

---

---
contenttype: [partial]
categories: [create]
cms: [--]
product: [local]
integration: [--]
tags: [--]
reviewed: ""
---

### Via Dashboard

1. Navigate to the Site Dashboard.

1. Select **Database / Files**, select **Export**, and then select **Export Database** to create an on-demand backup.

1. Select **Backups**, select **Backup Log**, and then select **Database download link** to download the backup.

1. Import the database into your local environment with your MySQL client:

  ```bash{promptUser: user}
  gunzip < database.sql.gz | mysql -uUSER -pPASSWORD DATABASENAME
  ```

  <Alert title="Note" type="info">

  Replace `database.sql.gz` with the name of the database archive downloaded from Pantheon.

  </Alert>

### Via Terminus

1. Create and get the database with Terminus commands:

    ```bash{promptUser: user}
    terminus backup:create $SITE.$ENV --element=db
    terminus backup:get $SITE.$ENV --element=db
    ```

1. Run the command below to import the archive into your local MySQL database:

    ```bash{promptUser: user}
    gunzip < database.sql.gz | mysql -uUSER -pPASSWORD DATABASENAME
    ```
