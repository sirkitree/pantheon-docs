# content/guides/fastly-pantheon/07-fastly-splunk.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/guides/fastly-pantheon/07-fastly-splunk.md
> **Generated**: 2025-10-04 03:12:01

---

---
title: Fastly on Pantheon
subtitle: Integrate Your Fastly Account on Pantheon with Splunk
description: Learn how to use Splunk with your Fastly account on Pantheon.
tags: [cms, logs]
contributors: [whitneymeredith]
showtoc: true
permalink: docs/guides/fastly-pantheon/fastly-splunk
contenttype: [guide]
innav: [false]
categories: [cache]
cms: [--]
audience: [development]
product: [--]
integration: [fastly]
---

This section provides steps on how to use [Splunk](https://www.splunk.com/) as a logging endpoint with your Pantheon account. You can do this either through a Fastly account connected to Pantheon, or by manually uploading your Pantheon logs to Splunk.

## Before You Begin

Verify the following before you begin:

- You have already [connected your Fastly account to your Pantheon account](/guides/fastly-pantheon/connect-fastly).

- You have a [Splunk](https://www.splunk.com/) account.

## Integrate Splunk with Your Fastly Account on Pantheon

Follow the steps below to use Splunk with your Fastly and Pantheon with AGCDN accounts.

1. Verify that you have the [Fastly prerequisites](https://docs.fastly.com/en/guides/log-streaming-splunk#prerequisites).

1. Complete the steps to [add Splunk as a logging endpoint](https://docs.fastly.com/en/guides/log-streaming-splunk#adding-splunk-as-a-logging-endpoint).

1. Review the [recommended log format](https://docs.fastly.com/en/guides/log-streaming-splunk#recommended-log-format).

## Manually Upload Your Pantheon Logs to Splunk

Note that this method does not require a Fastly account or use of Pantheon's AGCDN. You can automate the process of accessing and maintaining your logs by creating a script. Follow the steps below to access and upload your Pantheon logs to Splunk.

1. Complete the steps to [create a script](/guides/logs-pantheon/automate-log-downloads#create-a-script).

1. Complete the steps to [collect your logs](/guides/logs-pantheon/automate-log-downloads#collect-logs).

1. [Upload your logs to Splunk](https://docs.splunk.com/Documentation/Splunk/8.2.6/Data/Uploaddata) for processing.

## More Resources

- [Pantheon Logs](/guides/logs-pantheon#available-logs)

- [New Relic](/guides/new-relic)

- [Log Streaming with Splunk](https://docs.fastly.com/en/guides/log-streaming-splunk)
