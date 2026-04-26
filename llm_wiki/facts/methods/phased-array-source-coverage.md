---
fact_id: "methods-phased-array-source-coverage"
title: "Phase-shifter PCB writing needs RF-system context plus PCB execution evidence"
topic: "Phased-array and phase-shifter source coverage"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "analog-devices-phased-array-radar"
  - "analog-devices-phase-shifters"
  - "qorvo-phase-shifters"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendhil-high-frequency-product-page-en"
tags: ["phased-array", "phase-shifter", "beamforming", "beam-steering", "rf-pcb", "microwave-pcb", "source-coverage"]
---

# Canonical Summary

> Phase-shifter PCB articles should distinguish RF-system behavior from PCB execution. Semiconductor-vendor sources can anchor phased-array and phase-shifter context, while internal PCB sources support layout, material, stackup, transition, and validation framing.

## Stable Facts

- Analog Devices provides phased-array architecture context that includes analog, digital, and hybrid beamforming language.
- Analog Devices and Qorvo provide phase-shifter category anchors that connect RF/microwave/mmWave phase control with phased-array and beam-steering applications.
- Internal APT/HIL high-frequency, microwave, and antenna PCB pages support board-level execution topics such as material choice, transition control, grounding, shielding, and validation access.

## Conditions And Methods

- Use this card for phase-shifter PCB, phased-array antenna PCB, radar PCB, and 5G RF PCB articles.
- Keep beamforming/phase-control theory sourced to RF semiconductor/system sources.
- Keep PCB stackup, material, fabrication, and validation claims sourced to internal capability cards plus official material datasheets.

## Limits And Non-Claims

- This card does not provide beamforming equations, phase quantization rules, calibration algorithms, or part-level phase-shifter specifications.
- It does not claim any internal board can meet a specific frequency, insertion-loss, phase-error, thermal-drift, or calibration requirement without project review.
- It does not freeze RF vendor product lineups, supported bands, inventory, or lifecycle status.

## Open Questions

- Add tutorial-style phased-array theory sources if future articles need equations or array-factor explanation.
- Add specific phase-shifter datasheets only when a blog references a named component or application band.

## Source Links

- https://www.analog.com/en/solutions/aerospace-and-defense/phased-array.html
- https://www.analog.com/en/product-category/phase-shifters.html
- https://www.qorvo.com/products/control-products/phase-shifters
- /code/hileap/frontendAPT/public/static/products/en/antenna-pcb.json
- /code/hileap/frontendAPT/public/static/products/en/microwave-pcb.json
- /code/hileap/frontendAPT/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
