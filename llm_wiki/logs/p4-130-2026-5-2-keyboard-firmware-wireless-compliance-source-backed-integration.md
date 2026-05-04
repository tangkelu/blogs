# P4-130 2026-05-02 Keyboard Firmware / Wireless / Consumer-Compliance Source-Backed Integration

Date: 2026-05-02
Scope: `P4-129 lane 1`
Status: `source_backed_fact_layer_partial`

## Purpose

Convert the first ranked `P4-129` queue lane into a narrow reusable boundary layer for keyboard firmware, wireless terminology, and consumer-compliance entry context.

This pass keeps the lane narrow:

- `QMK` identity
- `VIA` identity and configuration-dependent compatibility boundary
- Bluetooth terminology boundary
- FCC equipment-authorization entry context
- EU `RED` entry context

It does not unlock:

- keyboard performance
- wireless performance
- certification proof
- product support proof
- `HILPCB` capability proof

## Inputs Reviewed

- `logs/p4-129-2026-5-2-hilpcb-blog1-13-source-recovery-queue-note.md`
- `logs/p4-130a-2026-5-2-keyboard-qmk-via-official-source-scout.md`
- `logs/p4-130b-2026-5-2-keyboard-wireless-compliance-official-source-scout.md`
- `facts/methods/hilpcb-blog1-13-input-device-draft-consumption-boundary.md`
- `facts/standards/interface-wireless-and-positioning-product-level-boundary.md`

## Source Records Added

- `sources/registry/methods/qmk-firmware-documentation-page.md`
- `sources/registry/methods/qmk-info-json-reference-page.md`
- `sources/registry/methods/via-configuring-qmk-page.md`
- `sources/registry/methods/via-keyboard-definition-specification-page.md`
- `sources/registry/standards/bluetooth-qualification-process-page.md`
- `sources/registry/standards/fcc-equipment-authorization-page.md`
- `sources/registry/standards/eu-radio-equipment-directive-page.md`

Reused existing source records:

- `sources/registry/standards/bluetooth-core-specification-page.md`

## Fact Card Added

- `facts/standards/keyboard-qmk-via-wireless-and-consumer-compliance-boundary.md`

## Integration Result

The `HILPCB Blog1-13` keyboard residual lane now has a narrow official-source-backed route for:

- `QMK` as firmware-ecosystem identity
- `VIA` as configuration-ecosystem identity
- configuration-dependent `QMK` / `VIA` compatibility wording
- Bluetooth standards-owner wireless terminology
- FCC equipment-authorization entry context for wireless consumer devices
- EU `RED` framework-entry context for wireless consumer devices

## Safe Reuse Now

- `QMK` keyboard firmware ecosystem wording
- `VIA` configuration ecosystem wording
- careful phrasing that `VIA` support depends on supported firmware configuration rather than being automatic
- Bluetooth terminology in keyboard product context
- product-level wireless compliance-entry wording using `FCC equipment authorization` and `RED`

## Still Blocked

- `NKRO`, anti-ghosting, and RGB behavior
- battery life, latency, polling rate, coexistence, and wireless range
- Bluetooth qualification proof
- FCC authorization proof, FCC ID proof, `CE` / DoC proof, or market-placement proof
- hot-swap durability, pad strength, and socket life
- `HILPCB` manufacturing capability, lead time, quality, inspection, or regulated-program claims

## Next Likely Lane

Per `P4-129`, the next official-source lane after this one is:

- `mouse sensor / switch / wireless boundary`

The `MIDI / USB-MIDI / BLE-MIDI` compatibility lane remains after that.
