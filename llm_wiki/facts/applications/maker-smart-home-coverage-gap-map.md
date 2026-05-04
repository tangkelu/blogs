---
fact_id: "applications-maker-smart-home-coverage-gap-map"
title: "Maker / Smart-Home application coverage gap map: which platform families have wiki-level routing and which remain overview-only"
topic: "Maker and smart-home PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-187 initial build; sourced from wiki/applications/maker-and-smart-home-platform-boundaries.md (active as of P4-180), related maker/platform/protocol standards and method cards"
source_ids:
  - "espressif-esp32-c6-product-page"
  - "espressif-esp32-h2-product-page"
  - "espressif-esp-idf-programming-guide"
  - "espressif-esp-matter-programming-guide"
  - "raspberry-pi-5-product-page"
  - "raspberry-pi-compute-module-5-product-page"
  - "raspberry-pi-rp2040-product-page"
  - "raspberry-pi-pico-product-page"
  - "raspberry-pi-pico-2-product-page"
  - "csa-matter-faq"
  - "thread-group-what-is-thread-overview"
  - "csa-zigbee-faq"
tags: ["maker-platform", "smart-home", "esp32", "raspberry-pi", "rp2040", "matter", "thread", "zigbee", "iot", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-187 initial build, the maker/smart-home application family has a dedicated wiki boundary page (`wiki/applications/maker-and-smart-home-platform-boundaries.md`) and that page is now `active`. This fact card maps what the current source layer supports, which platform families are addressable, and which certification/performance layers remain blocked.

## Platform Family Coverage State

### Supported at Platform Identity + Board-Context Level

All entries below are supported by official vendor product/SDK pages and official protocol organization FAQ pages. They support platform-identity vocabulary and PCB/PCBA board-context language. They do NOT prove production readiness, ecosystem certification, interoperability, or commercial deployment.

| Platform | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **ESP32-C6** | Wi-Fi/Bluetooth/IEEE 802.15.4 SoC; maker IoT project context | SoC identity vocabulary; Wi-Fi/BT/802.15.4/Thread/Zigbee/Matter vocabulary where stated by Espressif; compact board layout context |
| **ESP32-H2** | 802.15.4/Thread/Zigbee SoC; IoT project context | SoC identity vocabulary; 802.15.4/Thread/Zigbee/Matter vocabulary where stated by Espressif; compact board layout context |
| **Raspberry Pi 5 / CM5** | SBC/compute module; edge/prototype compute context | SBC/CM identity vocabulary; PCIe context on CM5; vendor-scoped feature vocabulary; NOT production-ready guarantees |
| **Pico / RP2040** | MCU/PIO microcontroller; embedded control context | MCU identity vocabulary; PIO/SDK vocabulary; compact embedded board context; NOT deterministic real-time guarantees |
| **Pico 2** | Next-gen RP2040-family MCU context | Product identity vocabulary; vendor-scoped feature vocabulary only |

### Protocol Identity Coverage State

| Protocol | Source | What Is Supported |
|---|---|---|
| **Matter** | CSA Matter FAQ | Open smart-home protocol identity; Bluetooth LE setup, Wi-Fi/Thread/Ethernet device connection vocabulary; NOT certification, DCL records, device category support proof |
| **Thread** | Thread Group overview | IEEE 802.15.4-based IPv6 IoT network identity; border router context vocabulary; NOT Thread certification or network interoperability proof |
| **Zigbee** | CSA Zigbee FAQ | IEEE 802.15.4-based CSA technology identity; Matter/Zigbee bridge context vocabulary; NOT Zigbee certification or native Matter interoperability |
| **ESP-IDF / ESP-Matter** | Espressif docs | Framework identity; development context; NOT production firmware stability, compliance proof |

### Fact Cards Supported

| Fact Card | What It Supports |
|---|---|
| `methods-maker-platform-official-identity-boundary` | Maker platform official identity boundary (ESP32, Raspberry Pi, RP2040) |
| `standards-smart-home-protocol-identity-boundary` | Smart home protocol identity boundary (Matter, Thread, Zigbee) |
| `standards-interface-wireless-positioning-product-level-boundary` | Wireless/Bluetooth/Wi-Fi product-level positioning boundary |

## Stable Facts

- The source layer supports 5 distinct maker platforms at official vendor product/SDK identity level.
- Protocol vocabulary (Matter, Thread, Zigbee, ESP-IDF/Matter) is supported at official FAQ and framework identity level only; certification, interoperability, and deployment-readiness claims are NOT supported.
- Smart-home ecosystem vocabulary (HomeKit, Google Home, Alexa, Home Assistant) requires separate official ecosystem sources; these are NOT currently recovered.
- For custom PCBs targeting production scale: board-level design guides and dated manufacturer capability records are required before any manufacturing suitability, yield, quality, or lead-time claim.
- "Platform identity is not a project recommendation" — naming a SoC or module does not make a project production-ready.

## Conditions And Methods

- Use this card to confirm what vocabulary is safe before writing a maker/smart-home PCB article.
- For wireless/Bluetooth/Wi-Fi vocabulary, route to `facts/standards/interface-wireless-positioning-product-level-boundary`.
- For smart home protocol vocabulary, route to `facts/standards/smart-home-protocol-identity-boundary`.
- For maker platform identity vocabulary, route to `facts/methods/maker-platform-official-identity-boundary`.
- For industrial control transition (production-scale maker), route to `wiki/applications/industrial-control-pcb-pcba-boundary-map.md`.
- Update `last_reconciled_at` when a new maker/smart-home wiki boundary page is created.

## Limits And Non-Claims

- Matter/Thread/Zigbee certification proof, DCL records, or interoperability proof is NOT supported.
- Ecosystem compatibility (HomeKit, Google Home, Alexa, Home Assistant) is NOT supported without separate official sources.
- Production readiness, commercial readiness, yield, quality, or lead-time claims are NOT supported.
- Deterministic real-time guarantees for Pico/RP2040 are NOT supported.
- "Best project", ranking, or recommendation claims are NOT supported.
- Vendor security mentions are NOT proof of product security.
- Price, MOQ, supplier capability, test result, or performance claims require dated records.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Dedicated maker/smart-home wiki boundary page | Closed — created and promoted to `active` in P4-180 |
| Companion fact card (this file) | Closed — created in P4-187 |
| Matter certification vocabulary (DCL / product listing) | Official CSA DCL or matter certification page with stable URL |
| Thread certification vocabulary | Official Thread Group certification program page |
| Zigbee certification vocabulary | Official CSA Zigbee certification page |
| HomeKit / Apple Home ecosystem vocabulary | Official Apple developer documentation page |
| Google Home ecosystem vocabulary | Official Google Home developer documentation page |
| Amazon Alexa ecosystem vocabulary | Official Amazon Alexa Connect Kit documentation page |
| Home Assistant / OpenThread vocabulary | Official Home Assistant and OpenThread documentation pages |
| RP2040 / Pico 2 dated production-life statement | Official Raspberry Pi production-life or longevity documentation |
| ESP32-C6/H2 radio certification records | Espressif FCC/CE/IC certificate page with stable URL |
