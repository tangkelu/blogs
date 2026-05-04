# Maker / Smart-Home PCB Evidence Pack

**Pack ID**: `consumption-maker-smart-home`
**Date**: 2026-05-03
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Maker / Smart-Home PCB/PCBA (ESP32, Raspberry Pi, RP2040, Matter/Thread/Zigbee IoT platforms)"
scope: |
  Conservative evidence pack for maker and smart-home PCB/PCBA content.

  Supports platform-identity vocabulary for ESP32-C6, ESP32-H2, Raspberry Pi 5/CM5,
  Pico/RP2040, Pico 2, and protocol-identity vocabulary for Matter, Thread, Zigbee,
  and ESP-IDF/ESP-Matter frameworks.

  No Matter/Thread/Zigbee certification proof, ecosystem compatibility claims
  (HomeKit/Google Home/Alexa), production-readiness guarantees, product rankings,
  or commercial deployment claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  # Application boundary
  - "applications-maker-smart-home-coverage-gap-map"

  # Platform identity
  - "methods-maker-platform-official-identity-boundary"

  # Protocol identity
  - "standards-smart-home-protocol-identity-boundary"

  # Wireless boundary
  - "standards-interface-wireless-positioning-product-level-boundary"

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

wiki_framing_support:
  - "wiki/applications/maker-and-smart-home-platform-boundaries"

must_refresh:
  - claim: "Matter protocol version or new device category support"
    value: true
  - claim: "Thread or Zigbee certification program revision"
    value: true
  - claim: "ESP32 or Raspberry Pi product availability or EOL status"
    value: true
  - claim: "Ecosystem partnership or compatibility announcements"
    value: true

excluded_claim_classes:
  - "Matter/Thread/Zigbee certification proof or DCL product listing"
  - "Ecosystem compatibility (HomeKit, Google Home, Alexa, Home Assistant) without official source"
  - "Production readiness, commercial readiness, or manufacturing suitability claims"
  - "Deterministic real-time guarantees for RP2040/Pico"
  - "Product ranking, recommendation, or best-platform claims"
  - "Vendor security mentions as product security proof"
  - "Cost, lead-time, yield, and MOQ claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `ESP32 PCB`, `Raspberry Pi PCB`, `RP2040 board`, `Matter PCB`, `IoT PCB`, `smart home board` |
| **Page Type** | `query` |
| **Search Intent** | Maker platform PCBs, IoT device prototyping, smart-home device manufacturing, hobbyist/prototype boards |
| **Target Reader** | Makers, IoT device designers, smart-home product developers, prototype-to-production engineers |
| **Site** | `HILPCB` |

**Working Posture**: `go_now_conservative` — platform identity vocabulary and protocol identity vocabulary supported; certification proof, ecosystem compatibility, and production-readiness claims blocked.

---

## 3. Platform Families (Evidence Scope)

### 3.1 ESP32-C6

| Aspect | Evidence Support |
|--------|-----------------|
| SoC identity | Espressif ESP32-C6: Wi-Fi 6 / Bluetooth 5 / IEEE 802.15.4 (Thread/Zigbee) / Matter capable — source-backed identity |
| Board-context vocabulary | Compact IoT board layout, antenna keep-out, RF ground-plane context |
| Protocol context | Wi-Fi/BT/Thread/Zigbee/Matter vocabulary as stated by Espressif source |
| RF performance, FCC/CE certification proof, production yield | ❌ Blocked |

### 3.2 ESP32-H2

| Aspect | Evidence Support |
|--------|-----------------|
| SoC identity | Espressif ESP32-H2: IEEE 802.15.4 / Thread / Zigbee / Matter capable — source-backed identity |
| Board-context vocabulary | Compact 802.15.4 IoT board layout context |
| Protocol context | Thread/Zigbee/Matter vocabulary as stated by Espressif source |
| RF performance, radio certification proof | ❌ Blocked |

### 3.3 Raspberry Pi 5 / CM5

| Aspect | Evidence Support |
|--------|-----------------|
| SBC/CM identity | Raspberry Pi 5 (SBC) and Compute Module 5 (CM) — official product identity |
| PCIe context | CM5 PCIe interface vocabulary per official product documentation |
| Feature vocabulary | Vendor-scoped features only (as stated in official product page) |
| Production-ready guarantees, longevity/lifetime claims | ❌ Blocked without official production-life statement |

### 3.4 Pico / RP2040

| Aspect | Evidence Support |
|--------|-----------------|
| MCU identity | Raspberry Pi RP2040 microcontroller and Pico board — official product identity |
| PIO / SDK vocabulary | Programmable IO (PIO) and Pico SDK framework vocabulary |
| Compact embedded board context | Embedded control board layout vocabulary |
| Deterministic real-time guarantees, RTOS certification, production lifecycle claims | ❌ Blocked |

### 3.5 Pico 2

| Aspect | Evidence Support |
|--------|-----------------|
| Product identity | Pico 2 next-gen RP2040-family board — vendor-scoped identity vocabulary |
| Feature vocabulary | As stated in official Raspberry Pi product page only |
| Performance comparisons, production-life statements | ❌ Blocked without official dated documentation |

---

## 4. Protocol Families (Identity Only)

| Protocol | Safe Use | Blocked Use |
|---|---|---|
| **Matter** | Open smart-home protocol identity; Bluetooth LE commissioning / Wi-Fi / Thread / Ethernet device connectivity vocabulary | Device certification, DCL listing, specific device-category support proof |
| **Thread** | IEEE 802.15.4-based IPv6 IoT mesh-network identity; border router vocabulary | Thread certification, network interoperability proof, mesh performance |
| **Zigbee** | IEEE 802.15.4-based CSA technology identity; Matter/Zigbee bridge context | Zigbee certification, native Matter interoperability, network behavior |
| **ESP-IDF / ESP-Matter** | Espressif framework identity; development context vocabulary | Production firmware stability, security compliance, certification claim |

---

## 5. Allowed vs Blocked

### 5.1 Allowed (Platform Identity and Protocol Context)

| Claim Pattern | Example |
|---|---|
| Platform identity framing | "ESP32-C6 integrates Wi-Fi 6, Bluetooth 5, and IEEE 802.15.4 in a single SoC for IoT applications" |
| Protocol context framing | "Matter uses Bluetooth LE for device setup and supports Wi-Fi, Thread, and Ethernet for ongoing connectivity" |
| Board-context vocabulary | "IoT boards targeting Thread or Zigbee require 802.15.4-capable SoCs and careful RF antenna layout" |
| Framework identity | "ESP-IDF and ESP-Matter provide the development framework context for ESP32-based smart-home boards" |
| Transition routing | "Maker projects scaling toward production should consider the design and qualification standards that apply to commercial IoT products" |

### 5.2 Blocked (Certification / Ecosystem / Performance)

| Blocked Claim | Reason |
|---|---|
| "Matter certified device" | Matter certification requires CSA testing; the PCB alone cannot hold it |
| "Works with Apple Home, Google Home, and Alexa" | Ecosystem compatibility requires separate official source verification |
| "Best board for IoT projects" | Ranking claim — not supportable from wiki layer |
| "Production-ready RP2040 design" | Production-readiness requires dated capability records |
| "Secure by design — ESP32" | Vendor security mention ≠ product security proof |

---

## 6. Handoff

**Core Answer**:

> Maker and smart-home PCBs are supported through platform-identity vocabulary covering ESP32-C6/H2, Raspberry Pi 5/CM5, Pico/RP2040, and Pico 2, plus protocol-identity vocabulary for Matter, Thread, and Zigbee. The current evidence supports named platform context, protocol framing, and board-layout vocabulary. It does not support certification proof, ecosystem compatibility claims, production-readiness guarantees, or product rankings.

**Safe Reusable Shapes**:

- "Matter, Thread, and Zigbee are safer named as protocol-context framing than as certification-readiness proof — the path from SoC identity to Matter device certification involves testing beyond the PCB."
- "Platform identity (ESP32-C6, Raspberry Pi, RP2040) is a design-context anchor — it describes the SoC and framework; it is not a manufacturing-suitability claim."
- "Maker platforms transitioning to production volume require the same PCB design discipline (DFM, DFT, inspection, traceability) as commercial electronics."

---

## 7. Pre-flight

- [x] Maker/smart-home wiki boundary page referenced
- [x] Application fact card referenced (`facts/applications/maker-smart-home-coverage-gap-map.md`)
- [x] All 4 fact_ids from existing landed records — no new records required
- [x] All 12 source_ids from existing landed registry records
- [x] Matter/Thread/Zigbee certification and ecosystem compatibility blocked claims explicitly documented
- [x] Platform identity limited to vendor-official source scope
- [x] `must_refresh` items identified for protocol versions, product availability, and ecosystem status

**Verdict**: ✅ `go_now_conservative` — platform identity and protocol identity context. Exclude all certification proof, ecosystem compatibility, production-readiness, and ranking claims.

---

*This evidence pack follows `policies/prompt-consumption-specification.md`*
