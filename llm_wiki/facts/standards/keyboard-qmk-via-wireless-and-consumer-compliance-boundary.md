---
fact_id: "standards-keyboard-qmk-via-wireless-and-consumer-compliance-boundary"
title: "QMK, VIA, Bluetooth, FCC, and RED sources support keyboard firmware and wireless/compliance boundary wording, not performance or certification proof"
topic: "Keyboard firmware, wireless, and consumer-compliance boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-02"
source_ids:
  - "qmk-firmware-documentation-page"
  - "qmk-info-json-reference-page"
  - "via-configuring-qmk-page"
  - "via-keyboard-definition-specification-page"
  - "bluetooth-core-specification-page"
  - "bluetooth-qualification-process-page"
  - "fcc-equipment-authorization-page"
  - "eu-radio-equipment-directive-page"
tags: ["keyboard", "qmk", "via", "bluetooth", "fcc", "red", "wireless", "consumer-compliance", "boundary"]
---

# Canonical Summary

> Current QMK, VIA, Bluetooth SIG, FCC, and European Commission public pages support one narrow keyboard lane only. `QMK` may be used as the named firmware ecosystem and documentation authority for programmable keyboard context. `VIA` may be used as the named keyboard-configuration ecosystem, but compatibility must stay configuration-dependent rather than automatic. `Bluetooth` may be used as standards-owner wireless terminology, and FCC equipment authorization plus the EU Radio Equipment Directive may be used only as compliance-entry context for wireless keyboard products. None of these sources prove `NKRO`, RGB behavior, battery life, latency, wireless range, Bluetooth qualification, FCC authorization, CE conformity, or HILPCB capability.

## Stable Facts

- QMK publicly provides official documentation for a keyboard/input-device firmware ecosystem and related keyboard-definition vocabulary.
- QMK publicly documents keyboard metadata and definition structure through `info.json` reference material.
- VIA publicly documents compatibility setup through QMK-linked configuration and keyboard-definition vocabulary.
- VIA public documentation shows that compatibility depends on supported firmware configuration rather than being an automatic property of all keyboard PCBs.
- Bluetooth SIG publicly provides the Bluetooth Core Specification page and a separate qualification-process entry page, so Bluetooth identity and Bluetooth qualification entry must remain separate layers.
- The FCC publicly provides an equipment-authorization entry page for radio-frequency-device compliance context.
- The European Commission publicly provides an entry page for the Radio Equipment Directive as EU wireless-product framework context.

## Conditions And Methods

- Use this card when a keyboard PCB article needs exact nouns such as `QMK`, `VIA`, `Bluetooth`, `FCC equipment authorization`, or `RED`.
- Safe `QMK` posture:
  use `QMK` as firmware-ecosystem and keyboard-definition vocabulary only.
- Safe `VIA` posture:
  use `VIA` as configuration-ecosystem vocabulary and describe compatibility as dependent on supported firmware setup and definition files, not as a universal default.
- Safe wireless/compliance posture:
  use `Bluetooth` as standards-owner wireless terminology; use FCC equipment authorization and RED only as product-level compliance-entry context for wireless keyboards.
- Pair this card with `facts/standards/interface-wireless-and-positioning-product-level-boundary.md` when broader Bluetooth boundary wording is needed, and keep supplier/capability language blocked unless dated internal evidence exists.

## Limits And Non-Claims

- This card does not authorize `QMK-compatible`, `VIA-compatible`, or `Bluetooth keyboard` claims for an unnamed PCB unless exact official support context is attached.
- It does not authorize universal host compatibility, plug-and-play behavior, firmware support across all controllers, or automatic VIA support.
- It does not authorize `NKRO`, anti-ghosting, RGB electrical behavior, battery life, latency, polling rate, coexistence, RF range, or performance claims.
- It does not authorize Bluetooth qualification proof, FCC authorization proof, CE-mark proof, declaration-of-conformity proof, or any other certification/compliance status claim for a product, PCB, module, or supplier.
- It does not authorize HILPCB lead time, yield, inspection, quality, or regulated-program capability claims.

## Open Questions

- Add a later split only if a future rewrite genuinely needs exact hot-swap socket vendor identity, `USB-C` keyboard-connectivity vocabulary beyond the current USB-IF boundary, or named-product VIA support-list treatment.
- Add mouse-vendor and MIDI-protocol lanes separately; do not stretch this card into those families.

## Source Links

- https://docs.qmk.fm/
- https://docs.qmk.fm/reference_info_json
- https://caniusevia.com/docs/configuring_qmk/
- https://caniusevia.com/docs/specification/
- https://www.bluetooth.com/specifications/specs/core-specification/
- https://www.bluetooth.com/develop-with-bluetooth/qualify/
- https://www.fcc.gov/engineering-technology/laboratory-division/general/equipment-authorization
- https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en
