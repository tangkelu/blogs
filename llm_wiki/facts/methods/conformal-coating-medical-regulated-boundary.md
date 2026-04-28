---
fact_id: "methods-conformal-coating-medical-regulated-boundary"
title: "Medical imaging and wearable coating rewrites should stop at manufacturing-control language, not regulated-device proof"
topic: "conformal coating medical regulated boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-industry-medical-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-final-quality-inspection-page-en"
  - "ipc-cc-830c-toc"
  - "electrolube-conformal-coatings-archive"
  - "humiseal-conformal-coating-brochure"
tags: ["conformal-coating", "medical", "wearable", "regulated-boundary", "manufacturing-control", "inspection", "boundary"]
---

# Canonical Summary

> For `conformal-coating-medical-imaging-wearable`, the current source layer supports manufacturing-control wording only: contamination and moisture protection context, masking and keep-access planning, inspection and test handoff, and documentation-aware release flow. It does not support biocompatibility, sterilization compatibility, patient-contact suitability, FDA applicability, ISO 13485 proof, or device-release authority.

## Stable Facts

- The medical industry page supports application context for imaging, diagnostics, monitoring, and wearable electronics.
- The conformal-coating pages plus manufacturer sources support protection vocabulary, coating-family vocabulary, and application-method vocabulary.
- The PCBA quality, FCT, and final-inspection pages support staged governance around inspection, electrical or functional validation, identification, and release flow.
- IPC-CC-830C public metadata can anchor standards vocabulary at a high level, but not clause-level performance or acceptance detail.

## Safe Rewrite Posture

- Write the slug as a `medical-adjacent protection workflow` article, not a medical-compliance explainer.
- Focus on contamination and moisture exposure context, selective masking, keep-access decisions, later inspection or powered validation, and the need to keep role boundaries explicit.
- Use `medical imaging` and `wearable` only as packaging and documentation context that increases review discipline.
- Keep any standards mention at metadata level only.

## Conditions And Methods

- Use this card with `methods-medical-manufacturing-control-context-for-coating-tht-and-bga`, `methods-conformal-coating-lane-b-rewrite-gate`, and `processes-medical-imaging-wearable-empty-image-rewrite-gate`.
- Safe wording examples:
  `medical-adjacent assemblies may require tighter review of protected versus accessible regions`
  and
  `coating belongs inside manufacturing-control and validation-handoff planning, not inside public compliance proof`.
- If a draft starts discussing sterilization, patient contact, or certification, stop and record a gap.

## Limits And Non-Claims

- This card does not authorize biocompatibility, sterilization compatibility, patient-contact suitability, FDA approval, FDA registration, ISO 13485, or medical-device release claims.
- It does not authorize coating thickness, cure schedule, cleanliness thresholds, masking dimensions, or acceptance criteria.
- It does not prove that conformal coating is required for every medical-imaging or wearable board.

## Open Questions

- Add formal medical-material, sterilization, or biocompatibility sources only if a future rewrite genuinely needs those regulated topics.

## Source Links

- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/final-quality-inspection.json
- https://www.ipc.org/TOC/IPC-CC-830C-toc.pdf
- https://electrolube.com/knowledge-product-type/conformal-coatings/
- https://info.humiseal.com/hubfs/Product%20Brochure-v4%5B93%5D.pdf
