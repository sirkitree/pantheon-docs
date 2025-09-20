# content/partials/drupal/custom-modules-themes.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/drupal/custom-modules-themes.md
> **Generated**: 2025-09-20 03:14:53

---

---
contenttype: [partial]
categories: [update]
cms: [drupal9]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

To move **modules**, use the following commands:

<TabList>

<Tab title="With Nested Docroot" id="code-docroot" active={true}>

```bash{promptUser:user}
git checkout master web/modules/custom
git mv web/modules/custom web/modules/
git commit -m "Copy custom modules"
```

</Tab>

<Tab title="Without Nested Docroot" id="code-nodocroot">

<Partial file="drupal/custom-modules-themes-no-docroot.md" />

</Tab>

</TabList>

To move **themes**, use the following commands:

<TabList>

<Tab title="With Nested Docroot" id="code-docroot" active={true}>

```bash{promptUser:user}
git checkout master web/themes/custom
git mv web/themes/custom web/themes/
git commit -m "Copy custom themes"
```

</Tab>

<Tab title="Without Nested Docroot" id="code-nodocroot">

```bash{promptUser:user}
git checkout master themes/custom
git mv themes/custom web/themes/
git commit -m "Copy custom themes"
```

</Tab>

</TabList>
