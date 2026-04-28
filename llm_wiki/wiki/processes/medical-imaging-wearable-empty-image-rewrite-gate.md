---
topic_id: "processes-medical-imaging-wearable-empty-image-rewrite-gate"
title: "Medical Imaging Wearable Empty-Image Rewrite Gate"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-27"
fact_ids:
  - "methods-pcba-medical-traceability-dhr-dmr-boundary"
  - "methods-medical-manufacturing-control-context-for-coating-tht-and-bga"
  - "methods-pcba-mes-traceability-and-medical-documentation-boundary"
  - "methods-conformal-coating-lane-b-rewrite-gate"
  - "methods-mixed-technology-lane-b-rewrite-gate"
  - "methods-tht-heavy-assemblies-power-and-medical-context"
  - "methods-low-void-bga-conservative-generation-gate"
source_ids:
  - "frontendapt-industry-medical-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
  - "frontendhil-small-batch-assembly-product-page-en"
  - "frontendhil-large-volume-assembly-product-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
  - "frontendapt-pcba-pcb-stencil-page-en"
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-bga-qfn-fine-pitch-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-x-ray-inspection-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "ipc-1782b-traceability-standard-page"
  - "fda-21cfr-82065-traceability-page"
  - "fda-21cfr-820181-device-master-record-page"
  - "fda-21cfr-820184-device-history-record-page"
  - "fda-udi-basics-page"
  - "ipc-cc-830c-toc"
  - "electrolube-conformal-coatings-archive"
  - "humiseal-conformal-coating-brochure"
  - "indium-reflow-profile-to-paste-spec"
  - "indium-8-9hf-solder-paste-pds"
  - "kester-standard-reflow-profile"
tags: ["medical", "wearable", "rewrite-gate", "traceability", "conformal-coating", "tht", "low-void-bga", "empty-image"]
---

# Definition

> This gate classifies the current medical-imaging and wearable empty-image candidates by what the evidence layer can safely support before drafting. It exists to keep public rewrites at manufacturing-control scope and to block medical-compliance, release, threshold, and acceptance-criteria inflation.

## Core Rule

- Use `medical imaging` and `wearable` as application context that changes packaging pressure, documentation sensitivity, and review discipline.
- Keep public claims at process planning, traceability posture, access planning, dense-assembly review, inspection handoff, and build-record workflow.
- Block any move from manufacturing-control language to medical compliance proof unless a separate, narrower, refresh-checked source layer exists.

## Slug Classification

### `traceability-mes-medical-imaging-wearable-2`

- Status:
  `go_now_conservative`
- Safe article frame:
  MES-linked build history, lot and source visibility, traveler-linked records, build packet discipline, and documentation-aware release workflow.
- Required posture:
  explain `DMR`, `DHR`, and `UDI` only as adjacent vocabulary for why some regulated programs ask for stronger documentation.
- Blocked claims:
  FDA approval, FDA registration, ISO 13485 certification, finished-device `DHR` ownership by the board supplier, retention-period rules, serialization-schema rules, patient-safety proof, and release authority.

### `conformal-coating-medical-imaging-wearable`

- Status:
  `needs_refresh_then_go`
- Why:
  the current coating gate is usable, but it is explicitly refresh-sensitive and medical language tends to drift into biocompatibility or sterilization overclaim.
- Safe article frame:
  protection-workflow planning, masking and keep-access decisions, contamination and moisture exposure context, and inspection or test handoff.
- Blocked claims:
  biocompatibility, sterilization compatibility, patient-contact suitability, FDA applicability, ISO 13485, coating thickness, cure schedule, cleanliness threshold, masking dimension, and acceptance-threshold proof.

### `tht-through-hole-soldering-medical-imaging-wearable`

- Status:
  `go_now_conservative`
- Safe article frame:
  why some interfaces stay through-hole inside mostly SMT medical-adjacent hardware, how mixed-technology route selection works, and how inspection plus functional validation stays in the same workflow.
- Required posture:
  treat THT as interface, packaging, or mechanical-load context, not as a separate medical quality regime.
- Blocked claims:
  medical-device release, patient-safety proof, sterilization claims, compliance proof, solder-joint acceptance thresholds, hole-fill thresholds, and universal reliability superiority claims.

### `low-void-bga-reflow-medical-imaging-wearable`

- Status:
  `hold_for_new_sources`
- Why:
  this slug combines medical-adjacent framing with a process family that commonly drifts into void thresholds, reflow recipes, X-ray acceptance, reliability numerics, and release language.
- Safe current use:
  only as internal context for documentation-aware dense-package review, measured profiling, hidden-joint inspection, and first-build confirmation.
- Blocked claims:
  BGA void percentage, X-ray threshold, ramp or peak or TAL recipe, reliability gain, wearable-life outcome, device safety, FDA applicability, or release-authority proof.

## Shared Blocked Claim Classes

- FDA approval, FDA registration, ISO 13485 certification, medical-device release, patient-safety proof, sterilization compatibility, and biocompatibility claims
- Retention-period claims, acceptance-threshold claims, or customer-specific release-criteria claims
- Coating thickness, cure schedule, cleanliness limit, masking keep-out number, BGA void percentage, X-ray grading threshold, solder-joint acceptance, or hole-fill threshold claims
- Supplier-proof, qualification-proof, and universal capability claims

## Drafting Use Notes

- If a rewrite starts from `medical compliance`, stop and reframe around manufacturing control.
- If a rewrite needs exact medical regulatory language, refresh the FDA and eCFR sources first and keep the role boundary explicit.
- If a rewrite needs numeric process windows or acceptance rules, hold until narrower primary sources are added.

## Primary Sources

- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/small-batch-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/large-volume-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-stencil.json
- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-qfn-fine-pitch.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/x-ray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- https://shop.electronics.org/ipc-1782/ipc-1782-standard-only/Revision-b/english
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.65
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.181
- https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820/section-820.184
- https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics
- https://www.ipc.org/TOC/IPC-CC-830C-toc.pdf
- https://electrolube.com/knowledge-product-type/conformal-coatings/
- https://info.humiseal.com/hubfs/Product%20Brochure-v4%5B93%5D.pdf
- https://www.indium.com/blog/matching-a-reflow-profile-to-a-solder-paste-spec/
- https://www.indium.com/wp-content/uploads/2025/01/Indium8.9HF-High-Reliability-Solder-Paste-PDS-99702-R7.pdf
- https://www.kester.com/Portals/0/Documents/Knowledge%20Base/Standard_Profile.pdf
