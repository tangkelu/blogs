---
fact_id: "standards-mouse-sensor-switch-wireless-and-compliance-boundary"
title: "PixArt, Omron, Bluetooth, FCC, and RED sources support mouse sensor/switch/wireless boundary wording, not performance or certification proof"
topic: "Mouse sensor, switch, wireless, and compliance boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-02"
source_ids:
  - "pixart-optical-navigation-products-page"
  - "pixart-paw3399dm-t4qu-product-page"
  - "omron-d2fc-mouse-switch-page"
  - "bluetooth-core-specification-page"
  - "bluetooth-qualification-process-page"
  - "fcc-equipment-authorization-page"
  - "eu-radio-equipment-directive-page"
tags: ["mouse", "sensor", "switch", "bluetooth", "fcc", "red", "wireless", "boundary", "gaming-mouse"]
---

# Canonical Summary

> Current PixArt, Omron, Bluetooth SIG, FCC, and European Commission public pages support one narrow mouse lane only. PixArt may be used for optical-mouse-sensor family identity, including exact named sensor-family vocabulary such as `PAW3399DM-T4QU`. Omron may be used for exact mouse-switch family identity and mouse-operation context. Bluetooth may be used as standards-owner wireless terminology, and FCC equipment authorization plus the EU Radio Equipment Directive may be used only as compliance-entry context for wireless mouse products. None of these sources prove DPI/CPI, tracking accuracy, latency, switch life, battery life, wireless range, Bluetooth qualification, FCC authorization, CE conformity, or HILPCB capability.

## Stable Facts

- PixArt publicly provides optical-navigation product-family vocabulary, including optical mouse sensor categories.
- PixArt publicly provides exact named mouse sensor product vocabulary such as `PAW3399DM-T4QU`.
- Omron publicly provides exact mouse-switch product vocabulary through the D2FC ultra-subminiature basic switch page.
- Omron's mouse-switch page uses mouse-operation and long-life wording, but that does not prove lifetime, feel, or reliability outcomes for a specific product.
- Bluetooth SIG publicly provides Bluetooth identity and separate qualification-process vocabulary, so Bluetooth terminology and qualification must remain separate layers.
- FCC equipment-authorization and EU RED pages provide compliance-entry context for wireless consumer devices, not proof of authorization or conformity.

## Conditions And Methods

- Use this card when a mouse PCB article needs exact nouns such as an optical mouse sensor family, a mouse switch family, Bluetooth, FCC equipment authorization, or RED.
- Safe sensor posture:
  use PixArt product or product-family names only as vendor identity and family vocabulary.
- Safe switch posture:
  use Omron mouse-switch identity and mouse-operation vocabulary only as family context.
- Safe wireless/compliance posture:
  use Bluetooth as standards-owner wireless terminology; use FCC equipment authorization and RED only as product-level compliance-entry context for wireless mice.
- Pair this card with `facts/standards/interface-wireless-and-positioning-product-level-boundary.md` when broader Bluetooth boundary wording is needed.

## Limits And Non-Claims

- This card does not authorize `PixArt-approved`, `Omron-approved`, `Bluetooth-qualified`, `FCC-authorized`, `CE-marked`, or similar product claims for an unnamed PCB, module, or supplier.
- It does not authorize DPI/CPI, IPS, tracking accuracy, lift-off distance, polling rate, latency, debounce timing, click lifetime, battery life, charging speed, antenna performance, RF range, or coexistence claims.
- It does not authorize gaming-performance, esports-performance, or product-ranking claims.
- It does not authorize HILPCB capability, yield, lead time, inspection, quality, or regulated-program claims.

## Open Questions

- Add a later split only if a future rewrite genuinely needs a named wireless-module vendor or exact mouse-sensor performance-lane treatment.
- Do not stretch this card into keyboard hot-swap, MIDI, or audio-control claims.

## Source Links

- https://www.pixart.com/products/
- https://www.pixart.com/products-detail/130/PAW3399DM-T4QU
- https://components.omron.com/us-en/products/switches/D2FC
- https://www.bluetooth.com/specifications/specs/core-specification/
- https://www.bluetooth.com/develop-with-bluetooth/qualify/
- https://www.fcc.gov/engineering-technology/laboratory-division/general/equipment-authorization
- https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en
