---
fact_id: "methods-rf-validation-capability"
title: "Internal RF validation posture consistently centers on TDR, VNA, coupons, and traceability"
topic: "RF validation capability"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
tags: ["internal", "rf-validation", "tdr", "vna", "coupons", "methods"]
---

# Canonical Summary

> Your own non-blog site pages already converge on one internal RF validation model: impedance coupons, TDR correlation, sample-based or project-based VNA work, and build traceability are presented as the default RF verification stack.

## Stable Facts

- The HIL Rogers product JSON explicitly lists `VNA S-Parameter & TDR Validation` in the trust bar.
- The same HIL source repeatedly ties impedance verification to `TDR`, `VNA S-parameters`, coupon correlation, and MES/data traceability.
- The HIL high-frequency product JSON also presents `controlled impedance ±5%` with `TDR/VNA validation` and repeated VNA frequency-range claims in page copy.
- The APT high-frequency PCB page states `TDR and VNA S-parameters up to 40 GHz` in FAQ and structured-data content.
- The APT microwave PCB page frames microwave board verification around `Impedance coupons`, `VNA/S-parameters`, and environmental testing.
- Across these internal pages, RF validation is not described as AOI-only or electrical-test-only; it is framed as a combined metrology and traceability stack.

## Conditions And Methods

- Treat this as an internal capability-pattern card, not as a certified lab accreditation statement.
- Use it to support wiki pages about quote intake, validation planning, and RF build expectations.
- Any exact frequency ceiling or report scope should still be re-confirmed before publication or customer-facing commitment.

## Limits And Non-Claims

- This card does not prove every project receives the same VNA depth or the same maximum test frequency.
- It also does not prove all validation is available as standard scope without quote review.

## Open Questions

- Add a separate internal card distinguishing `standard validation`, `prototype validation`, and `customer-requested advanced validation`

## Source Links

- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
