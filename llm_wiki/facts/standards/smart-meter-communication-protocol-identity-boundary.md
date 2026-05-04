---
fact_id: "standards-smart-meter-communication-protocol-identity-boundary"
title: "DLMS/COSEM, IEC 62056, PRIME, G3-PLC, Wi-SUN, Zigbee, NB-IoT, and LTE-M sources support smart-meter communication identity, not interoperability or field behavior"
topic: "Smart-meter communication protocol identity boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-01"
source_ids:
  - "dlms-core-specifications-page"
  - "iec-62056-5-3-2023-product-page"
  - "iec-62056-6-2-2017-product-page"
  - "prime-alliance-advanced-metering-page"
  - "g3-alliance-g3-technologies-page"
  - "wi-sun-fan-page"
  - "csa-zigbee-faq"
  - "3gpp-the-cellular-internet-of-things-page"
  - "3gpp-nb-iot-complete-page"
tags: ["smart-meter", "dlms", "cosem", "iec-62056", "prime", "g3-plc", "wi-sun", "zigbee", "nb-iot", "lte-m", "plc", "rf-mesh"]
---

# Canonical Summary

> Current DLMS UA, IEC, PRIME Alliance, G3 Alliance, Wi-SUN Alliance, CSA, and 3GPP public pages support one narrow smart-meter communication identity lane only. `DLMS/COSEM` may be used as the named application-layer plus object-model family for smart-meter data exchange, with public linkage to the `IEC 62056` suite. `IEC 62056-5-3` may be used as the named DLMS/COSEM application-layer document family, and `IEC 62056-6-2` may be used as the named COSEM interface-classes document family. `PRIME` and `G3-PLC` may be used as named PLC technology families. `Wi-SUN`, `Zigbee`, `NB-IoT`, and `LTE-M` may be used as named wireless communication technology families. None of these sources prove that a specific PCB, meter, module, supplier, or factory is interoperable, certified, utility-approved, secure, region-ready, or field-proven.

## Stable Facts

- DLMS UA publicly states that its core specifications include an object-oriented data model, an application-layer protocol, and media-specific communication profiles.
- DLMS UA publicly states that its core specifications are published in IEC under the `IEC 62056` suite and distinguishes `DLMS` from `COSEM` and from communication profiles.
- IEC publicly identifies `IEC 62056-5-3:2023` as `Electricity metering data exchange - The DLMS/COSEM suite - Part 5-3: DLMS/COSEM application layer`.
- The IEC `IEC 62056-5-3:2023` product page publicly states that the document specifies the DLMS/COSEM application layer and defines rules to specify communication profiles.
- IEC publicly identifies `IEC 62056-6-2:2017` as `Electricity metering data exchange - The DLMS/COSEM suite - Part 6-2: COSEM interface classes`.
- The IEC `IEC 62056-6-2:2017` product page publicly states that the document specifies a model of a meter as seen through its communication interface or interfaces.
- PRIME Alliance publicly states that `PRIME` initially defines lower OSI layers of a narrowband PLC data-transmission system over the electricity grid.
- G3 Alliance publicly identifies `G3-PLC` as a powerline-communication technology and publicly distinguishes `G3-PLC` from `G3-Hybrid`.
- Wi-SUN Alliance publicly states that `Wi-SUN FAN` provides a communications infrastructure for very large-scale outdoor networks and includes smart meters as an example industrial device context.
- CSA publicly describes `Zigbee` as a technology based on `IEEE 802.15.4`.
- 3GPP publicly states that Release 13 developed `LTE-M`, `NB-IoT`, and `EC-GSM-IoT` for the Cellular Internet of Things.
- 3GPP publicly states that `NB-IoT` standardization was completed in Release 13 and positions it alongside `eMTC`.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2026.4.29/en/smart-meter-pcb.md` only when the rewrite needs exact communication nouns such as `DLMS/COSEM`, `IEC 62056`, `PRIME`, `G3-PLC`, `Wi-SUN`, `Zigbee`, `NB-IoT`, `LTE-M`, `PLC`, or `RF mesh`.
- Keep layer separation explicit:
  treat `DLMS/COSEM` and `IEC 62056` as the application-layer, object-model, and communication-profile standards family; treat `PRIME` and `G3-PLC` as named PLC technology families; treat `Wi-SUN` and `Zigbee` as named wireless network technology families; treat `NB-IoT` and `LTE-M` as named 3GPP cellular-IoT technology families.
- Safe `PLC` posture:
  use `power line communication (PLC)` only as a generic technology-family noun or when paired with exact named families such as `PRIME` or `G3-PLC`.
- Safe `RF mesh` posture:
  use `RF mesh` only as a generic network-label noun, not as a synonym for `Wi-SUN`, `Zigbee`, or any one certification program.
- Safe `head-end` posture:
  use `utility head-end system` only as a utility-side endpoint label when the rewrite needs naming-level context. Do not imply exact network architecture, protocol binding, or concentrator behavior from this card.
- Pair this card with `facts/standards/smart-meter-standards-and-metrology-identity-boundary.md` and `wiki/processes/power-energy-pcb-pcba-review-boundaries.md` when the rewrite also needs metrology standards, board partitioning, or production-workflow context.

## Limits And Non-Claims

- This card does not authorize `DLMS certified`, `IEC 62056 compliant`, `PRIME certified`, `G3-PLC certified`, `Wi-SUN certified`, `Zigbee certified`, `NB-IoT capable`, `LTE-M certified`, `utility approved`, or equivalent product claims.
- It does not authorize exact interoperability, conformance, security, encryption, key-management, or certification-program outcomes for any specific board, meter, gateway, concentrator, or head-end system.
- It does not authorize exact RF bands, PLC bandplans, data rates, latency, range, node counts, power consumption, or region-specific deployment claims.
- It does not authorize exact antenna rules, impedance targets, coupling topology, transformer isolation, cellular-module choice, or stack-integration architecture.
- It does not authorize treating `DLMS/COSEM`, `PRIME`, `G3-PLC`, `Wi-SUN`, `Zigbee`, `NB-IoT`, and `LTE-M` as interchangeable same-layer protocols.
- It does not authorize `supports AMI interoperability`, `supports utility head-end integration`, or `best protocol for region X` claims.
- It does not authorize exact metrology, lifetime, anti-tamper, safety, supplier-readiness, or documentation-support claims from the same draft.

## Open Questions

- Recover narrower `IEC 62056-8-x`, `wireless M-Bus`, `OMS`, or utility-specific network-profile sources only if future rewrites must retain those exact nouns.
- Add exact product, certification, or operator-support records only if a future rewrite needs approved-device or interoperable-network language.

## Source Links

- https://www.dlms.com/core-specifications/
- https://webstore.iec.ch/en/publication/67915
- https://webstore.iec.ch/en/publication/34317
- https://www.prime-alliance.org/solutions/advanced-metering/
- https://g3-alliance.com/technologies/
- https://wi-sun.org/fan/
- https://csa-iot.org/all-solutions/zigbee/zigbee-faq/
- https://www.3gpp.org/news-events/3gpp-news/c-iot
- https://www.3gpp.org/news-events/3gpp-news/nb-iot-complete
