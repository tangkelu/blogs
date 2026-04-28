---
fact_id: "methods-antenna-system-feed-network-vs-performance-boundary"
title: "Antenna-system rewrites must keep feed-network execution separate from antenna-performance claims"
topic: "antenna-system feed-network versus performance boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "analog-devices-phased-array-radar"
  - "analog-devices-phase-shifters"
  - "qorvo-phase-shifters"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendhil-high-frequency-product-page-en"
tags: ["antenna-system", "feed-network", "beamforming", "mmwave", "rf-pcb", "boundary"]
---

# Canonical Summary

> The current public-vendor and internal RF source layer is strong enough to support `antenna system` language only at the feed-network and board-execution layer: routing discipline, launch review, grounded structures, cavity or shield coordination, and validation planning. It does not support antenna-performance claims such as gain, efficiency, radiation pattern, or chamber-proven behavior.

## Stable Facts

- Analog Devices and Qorvo sources support high-level phased-array, beam-steering, and phase-control context for antenna-related hardware.
- The internal APT antenna page supports antenna-PCB execution vocabulary including feed networks, launch tuning, cavity machining, shield features, and RF validation posture.
- The internal high-frequency and microwave pages reinforce that antenna-adjacent boards are reviewed through material, transition, grounding, shielding, and validation planning rather than as generic digital layouts.
- The internal HIL high-frequency page supports repeated RF process and validation framing for antenna-adjacent board work.
- Together, these sources support guarded language that antenna-system boards often need disciplined feed routing and project-specific RF verification.

## Conditions And Methods

- Use this card for `antenna-system-5g-telecom` when the rewrite should stay at PCB execution scope.
- Treat `antenna system` as hardware context, then pivot quickly into feed-network routing, return-path continuity, launch or transition review, connector attachment, and validation-access planning.
- Keep array, phase-control, and beamforming vocabulary tied to vendor context sources.
- Keep manufacturability, shielding, cavity, finish, and validation handoff language tied to internal antenna, microwave, and high-frequency pages.
- Pair this card with `facts/methods/beamforming-mmwave-conservative-generation-gate.md`, `facts/methods/cavity-machining-capability.md`, and `facts/methods/rf-validation-capability.md` before any draft.

## Limits And Non-Claims

- This card does not authorize gain, directivity, efficiency, radiation pattern, side-lobe, scan-angle, beamwidth, polarization, or chamber-result claims.
- It does not authorize EIRP, return loss, insertion loss, isolation, phase balance, amplitude balance, or calibration claims.
- It does not authorize antenna-spacing rules, feed dimensions, launch dimensions, grounded-via spacing, or cavity geometry numerics.
- It does not prove that HILPCB or APTPCB has qualified any named antenna array, base-station antenna, or over-the-air validation program.
- It does not replace antenna simulation, chamber measurement, or part-specific connector and component datasheets.

## Open Questions

- Add a separate chamber-test boundary card only if future rewrites need to discuss measurement environments or OTA workflow.
- Add narrower connector-launch sources only if a future draft must compare specific RF interface families.

## Source Links

- https://www.analog.com/en/solutions/aerospace-and-defense/phased-array.html
- https://www.analog.com/en/product-category/phase-shifters.html
- https://www.qorvo.com/products/control-products/phase-shifters
- /code/hileap/frontendAPT/public/static/pcb/en/antenna-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
