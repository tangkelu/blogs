---
fact_id: "methods-mmwave-routing-sensitivity-vs-metric-claims-boundary"
title: "mmWave rewrites may describe routing sensitivity, not RF metric outcomes"
topic: "mmWave routing sensitivity versus metric claims boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "3gpp-38-series"
  - "analog-devices-phased-array-radar"
  - "analog-devices-phase-shifters"
  - "qorvo-phase-shifters"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendhil-rogers-product-page-en"
tags: ["mmwave", "routing", "rf-pcb", "beamforming", "boundary", "validation"]
---

# Canonical Summary

> The current source layer supports only a conservative `mmWave` writing lane: mmWave hardware raises sensitivity around laminate selection, transitions, grounding, shielding, cavity coordination, cleanliness, and validation planning. It does not support metric claims about RF performance, standards bands, chamber outcomes, or supplier-qualified mmWave execution.

## Stable Facts

- The 3GPP 38-series index is sufficient to confirm that mmWave-adjacent 5G topics belong in a broader NR standards family, but not to freeze current band or range statements without dated checking.
- Analog Devices and Qorvo sources support high-level phased-array and phase-control context for mmWave-class hardware.
- Internal antenna, high-frequency, microwave, and Rogers pages support repeated board-execution language around hybrid stackups, launches, cavities, shielding, and RF validation planning for sensitive RF builds.
- The internal HIL high-frequency and Rogers pages reinforce that validation, coupons, and project-specific VNA/TDR review are part of the RF workflow.
- Together, these sources support guarded statements that mmWave programs are less tolerant of weak transition control and undisciplined build execution.

## Conditions And Methods

- Use this card for `mmwave-5g-5g-telecom` when the article should stay at manufacturability and validation-planning scope.
- Open with mmWave only as a sensitivity label, then move into laminate review, mixed-material boundaries, launch or backdrill review, shield or cavity planning, cleanliness, and reserved validation access.
- Pair this card with `facts/methods/beamforming-mmwave-conservative-generation-gate.md`, `facts/methods/hybrid-rf-stackup-capability.md`, `facts/methods/backdrill-control-capability.md`, and `facts/methods/rf-validation-capability.md`.
- Prefer wording such as `tightens board-execution margins`, `raises sensitivity to transitions and materials`, and `needs project-specific validation`.

## Limits And Non-Claims

- This card does not authorize FR2 numerics, mmWave band values, link budget language, range, coverage, throughput, latency, or conformance claims.
- It does not authorize insertion loss, return loss, phase error, gain, EIRP, isolation, or antenna efficiency claims.
- It does not authorize copper-roughness numbers, weave-effect claims, launch dimensions, via-stub targets, or impedance numerics.
- It does not prove chamber results, calibration method, OTA behavior, field deployment success, or supplier qualification.
- It does not prove that any internal service page equals a named mmWave product-family qualification.

## Open Questions

- Add a future measurement-boundary card only if drafts must discuss VNA versus chamber versus OTA evidence.
- Add dated public standards or architecture sources only if later rewrites need specific NR band or subsystem language.

## Source Links

- https://www.3gpp.org/dynareport?code=38-series
- https://www.analog.com/en/solutions/aerospace-and-defense/phased-array.html
- https://www.analog.com/en/product-category/phase-shifters.html
- https://www.qorvo.com/products/control-products/phase-shifters
- /code/hileap/frontendAPT/public/static/pcb/en/antenna-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
