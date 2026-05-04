---
fact_id: "methods-eo-ir-detector-owner-identity-and-interface-boundary"
title: "EO/IR imaging writing is source-backed only at detector owner identity and interface-boundary level"
topic: "eo-ir detector owner identity and interface boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "exosens-image-intensifier-tube-page"
  - "sony-starvis-technology-page"
  - "sony-security-camera-image-sensor-products-page"
  - "lynred-about-our-technologies-page"
tags: ["eo-ir", "night-vision", "thermal-imaging", "targeting", "image-intensifier-tube", "cmos-image-sensor", "infrared-detector", "optical-sensor-interface", "owner-identity"]
---

# Canonical Summary

> Current Exosens, Sony, and Lynred owner sources support one narrow EO/IR lane only: imaging and targeting drafts may name exact detector families such as `image intensifier tube`, `STARVIS` CMOS image sensor, and `cooled` / `uncooled infrared detector` families, and may use guarded detector-chain and optical-sensor-interface vocabulary at subsystem level. The current evidence layer does not support turning that into detector-performance proof, optics or video-chain proof, target-recognition proof, military-program proof, or qualification claims.

## Stable Facts

- Exosens publishes image intensifier tube families and supports owner-scoped detector-chain vocabulary around `photocathode`, `microchannel plate`, and `phosphor screen`.
- Sony publishes `STARVIS` and `STARVIS 2` as real CMOS image-sensor technology families and keeps security-imaging vocabulary anchored at owner level.
- Sony's security image-sensor product page provides a direct owner anchor for security-camera CMOS image-sensor family naming rather than generic draft-only `digital night vision` language.
- Lynred publishes cooled and uncooled infrared-detector technologies, making it safe to keep thermal-imaging detector nouns at owner-backed family level rather than at unsupported performance-claim level.
- Across these owner sources, it is safe to describe the EO/IR subset of a board as a detector-integration lane rather than as generic surveillance, targeting, or military-system authority.

## Conditions And Methods

- Use this card when `night-vision-pcb.md`, `thermal-imaging-pcb.md`, `surveillance-pcb.md`, or the optical-sensor subset of `targeting-pcb.md` need a safer route than generic `EO/IR`, `digital night vision`, or `thermal camera` marketing.
- Safe posture: keep the board role at detector power, interface, readout, conditioning, processing-board context, power / thermal / isolation review, compact packaging, and staged validation language.
- Pair this lane with `methods-fire-control-platform-interface-boundary` when a targeting draft also discusses platform-bus or control-board interface sections.
- Pair this lane with DFM, first-article, and qualification-boundary cards when the draft also discusses mixed-signal execution or regulated-program workflow.
- Keep image intensifier, low-light CMOS, and thermal infrared detector families as separate owner-backed lanes instead of collapsing them into one universal `EO/IR board` doctrine.

## Limits And Non-Claims

- This card does not authorize `CCD`, detector-generation proof, detector-material claims such as `InSb`, `HgCdTe`, `VOx`, or `a-Si`, or exact microbolometer architecture unless separately sourced.
- It does not authorize exact sensitivity, `QE`, lux, `NETD`, range, resolution, frame-rate, dynamic-range, or cryocooler-performance claims at detector, board, or system level.
- It does not authorize optics, lens, image-registration, video-output, target-tracking, target-recognition, or fire-control outcome claims.
- It does not authorize military qualification, defense-program, export-control, supplier-readiness, or HILPCB deployment / customer proof.

## Open Questions

- Add narrower serial-interface sources later if a future rewrite must retain exact `LVDS`, `MIPI CSI-2`, or display-interface language around EO/IR sensor modules.
- Add stronger detector-owner or standards sources later if a future rewrite must retain detector-material, cryocooler, or exact optical-performance claims.

## Source Links

- https://www.exosens.com/products/image-intensifier-tube
- https://www.sony-semicon.com/en/technology/security/index.html
- https://www.sony-semicon.com/en/products/is/security/index.html
- https://www.lynred.com/about-our-technologies
