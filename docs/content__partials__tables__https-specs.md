# content/partials/tables/https-specs.md

> **Source**: https://github.com/pantheon-systems/documentation/blob/main/content/partials/tables/https-specs.md
> **Generated**: 2025-09-27 15:06:04

---

---
contenttype: [partial]
categories: [cert]
cms: [--]
product: [--]
integration: [--]
tags: [--]
reviewed: ""
---

|                                                                       | Global CDN with Let's Encrypt   | Global CDN with a Custom Certificate  |
|:--------------------------------------------------------------------- |:------------------------------- |:------------------------------------- |
| **Certificate Type**                                                  | Issued by Let's Encrypt         | Bring your own                        |
| **Renewal**                                                           | Automatic                       | Self-managed (up to you)              |
| **Inbound IP**                                                        | Static (shared)                 | Static (shared)                       |
| **Client Support**                                                    | 95.55% of Browsers <br />Some very old browsers not supported <sup> [1](https://caniuse.com/#search=TLS%201.2) [2](https://caniuse.com/#search=SNI)</sup> | 95.55% of Browsers <br />Some very old browsers not supported <sup>[1](https://caniuse.com/#search=TLS%201.2) [2](https://caniuse.com/#search=SNI)</sup> * |
| [**SSL Labs Rating**](https://www.ssllabs.com/ssltest/)               | A+ [with HSTS](/pantheon-yml/#enforce-https-+-hsts)     | A+ [with HSTS](/pantheon-yml/#enforce-https-+-hsts) * |
| **Protocol**                                                          | TLS 1.3 with SNI                | TLS 1.3 with SNI                      |
| **Ciphers**                                                           | No Weak 3DES cipher             | No Weak 3DES cipher                   |
| **Delivery**                                                          | [Global CDN](/guides/global-cdn)  | [Global CDN](/guides/global-cdn)        |
| **Encryption Endpoint**                                               | Application Container           | Application Container                 |

\* The browser compatibility and SSL Labs scores are guaranteed for Pantheon-provided Let’s Encrypt certificates. The same results are typical for a custom certificate from a mainstream CA with mainstream attributes, but not guaranteed.  For custom certificates, compatibility and SSL Labs score depends on attributes of that certificate, such as number of SAN entries, CA and signing algorithm.
