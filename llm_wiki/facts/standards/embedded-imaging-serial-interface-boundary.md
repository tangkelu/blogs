---
fact_id: "standards-embedded-imaging-serial-interface-boundary"
title: "MIPI and LVDS sources support embedded imaging interface context, not PCB compliance or performance"
topic: "embedded imaging serial interface boundary"
category: "standards"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "mipi-csi-2-spec-page"
  - "mipi-d-phy-spec-page"
  - "mipi-dsi-2-spec-page"
  - "mipi-display-command-set-page"
  - "ti-lvds-overview-page"
tags: ["mipi", "csi-2", "d-phy", "dsi-2", "display-command-set", "lvds", "embedded-imaging", "serial-interface", "display-interface", "compliance-boundary"]
---

# Canonical Summary

> Official MIPI Alliance and TI sources support a conservative embedded-imaging serial-interface boundary for writing: `MIPI CSI-2`, `MIPI D-PHY`, `MIPI DSI-2`, `MIPI Display Command Set`, and `LVDS` are valid standards-owner or vendor-family interface nouns for camera-sensor, display, and serial-link context. These sources do not prove that a PCB, layout, supplier, or lot meets exact lane counts, bitrates, latency, interoperability, or compliance outcomes.

## Stable Facts

- MIPI Alliance provides the standards-owner pages for `CSI-2`, `D-PHY`, `DSI-2`, and `Display Command Set`, making these safe interface-family nouns for embedded imaging and display paths.
- `CSI-2` is the safe sensor-facing noun family when a draft needs guarded camera serial interface vocabulary.
- `D-PHY` is the safe physical-layer noun family when a draft needs guarded MIPI serial-link vocabulary below the protocol family.
- `DSI-2` and `Display Command Set` are safe display-facing noun families when a draft needs guarded compact-display or display-command vocabulary.
- TI's official LVDS overview provides a vendor-family anchor for guarded `LVDS` signaling vocabulary in imaging and display-adjacent drafts.

## Conditions And Methods

- Use this card when `night-vision-pcb.md`, `thermal-imaging-pcb.md`, `surveillance-pcb.md`, or `targeting-pcb.md` need a safer route than generic `high-speed video` marketing for imaging sensor or display interface sections.
- Prefer phrases such as `sensor-interface family`, `camera serial interface context`, `display-interface family`, `serial-link context`, or `designed around` unless narrower compliance or test evidence is attached.
- Pair this lane with `methods-eo-ir-detector-owner-identity-and-interface-boundary` when a draft also names exact detector families.
- Pair this lane with `methods-fire-control-platform-interface-boundary` when a targeting draft also crosses into broader platform buses or vehicle links.

## Limits And Non-Claims

- This card does not authorize lane-count, bitrate, clock, jitter, ripple, latency, skew, frame-rate, or eye-diagram claims.
- It does not authorize `LVDS-compliant PCB`, `MIPI-compliant PCB`, interoperability proof, serializer / deserializer proof, or product-level certification claims.
- It does not authorize `PAL/NTSC`, `RS-170`, `STANAG 3350`, `HDMI`, `SDI`, `GigE Vision`, `USB3 Vision`, `PCIe`, `DDR4`, `MIL-STD-1553`, or `CAN` claims unless separately sourced.
- It does not prove that HILPCB or any supplier can build, validate, or qualify a finished imaging product for these interfaces.

## Open Questions

- Add narrower public sources later if future rewrites must retain `C-PHY`, exact serializer/deserializer families, or specific display-panel command / init claims.
- Add stronger public sources later if future rewrites must retain exact output-video standards or performance numerics rather than interface-family vocabulary only.

## Source Links

- https://www.mipi.org/specifications/csi-2
- https://www.mipi.org/specifications/d-phy
- https://www.mipi.org/specifications/dsi-2
- https://www.mipi.org/specifications/display-command-set
- https://www.ti.com/product-category/interface/lvds/overview.html
