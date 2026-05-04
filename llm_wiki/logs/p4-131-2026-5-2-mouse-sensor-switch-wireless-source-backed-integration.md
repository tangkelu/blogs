# P4-131 2026-05-02 Mouse Sensor / Switch / Wireless Source-Backed Integration

Date: 2026-05-02
Scope: `P4-129 lane 2`
Status: `source_backed_fact_layer_partial`

## Purpose

Convert the second ranked `P4-129` queue lane into a narrow reusable boundary layer for mouse sensor identity, mouse switch identity, wireless terminology, and consumer-compliance entry context.

This pass keeps the lane narrow:

- PixArt optical mouse sensor family identity
- Omron mouse switch family identity
- Bluetooth standards-owner terminology
- FCC equipment-authorization entry context
- EU `RED` entry context

It does not unlock:

- DPI / CPI
- tracking accuracy
- polling rate
- latency
- switch-life proof
- battery-life proof
- wireless-range proof
- `HILPCB` capability proof

## Inputs Reviewed

- `logs/p4-129-2026-5-2-hilpcb-blog1-13-source-recovery-queue-note.md`
- `logs/p4-130b-2026-5-2-keyboard-wireless-compliance-official-source-scout.md`
- `facts/methods/hilpcb-blog1-13-input-device-draft-consumption-boundary.md`
- `facts/standards/interface-wireless-and-positioning-product-level-boundary.md`

## Source Records Added

- `sources/registry/methods/pixart-optical-navigation-products-page.md`
- `sources/registry/methods/pixart-paw3399dm-t4qu-product-page.md`
- `sources/registry/methods/omron-d2fc-mouse-switch-page.md`

Reused existing source records:

- `sources/registry/standards/bluetooth-core-specification-page.md`
- `sources/registry/standards/bluetooth-qualification-process-page.md`
- `sources/registry/standards/fcc-equipment-authorization-page.md`
- `sources/registry/standards/eu-radio-equipment-directive-page.md`

## Fact Card Added

- `facts/standards/mouse-sensor-switch-wireless-and-compliance-boundary.md`

## Integration Result

The `HILPCB Blog1-13` mouse residual lane now has a narrow official-source-backed route for:

- PixArt optical mouse sensor family identity
- exact named sensor-family vocabulary such as `PAW3399DM-T4QU`
- Omron mouse switch family identity
- Bluetooth standards-owner wireless terminology
- FCC equipment-authorization entry context
- EU `RED` framework-entry context

## Safe Reuse Now

- optical mouse sensor family identity
- exact named sensor-family vocabulary
- mouse switch family identity
- Bluetooth terminology in mouse product context
- product-level wireless compliance-entry wording using `FCC equipment authorization` and `RED`

## Still Blocked

- DPI / CPI, IPS, tracking accuracy, lift-off, latency, polling, or debounce claims
- switch-life, tactile-feel, or reliability-outcome claims
- battery life, charging speed, antenna performance, range, and coexistence claims
- Bluetooth qualification proof
- FCC authorization proof, FCC ID proof, `CE` / DoC proof, or market-placement proof
- HILPCB capability, lead time, quality, inspection, or regulated-program claims

## Next Likely Lane

Per `P4-129`, the remaining official-source lane after this one is:

- `MIDI / USB-MIDI / BLE-MIDI compatibility boundary`
