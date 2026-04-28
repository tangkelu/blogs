---
fact_id: "methods-manual-solder-rework-boundary-for-mixed-technology"
title: "Manual solder in mixed-technology assembly should be framed as controlled touch-up, rework, prototype, or low-density exception work, not the default production route"
topic: "Manual solder and rework boundary for mixed-technology assembly"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-bga-reballing-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-industry-medical-page-en"
  - "frontendapt-blog-hand-solder-best-practices-en"
  - "frontendapt-blog-through-hole-soldering-basics-en"
  - "ipc-document-revision-table"
  - "ipc-j-std-001j-toc"
  - "ipc-a-610h-toc"
tags: ["manual-solder", "hand-solder", "touch-up", "rework", "mixed-technology", "medical", "wearable", "inspection", "traceability"]
---

# Canonical Summary

> In the current corpus, the safe position is that manual solder belongs inside mixed-technology assembly as prototype work, low-density through-hole completion, controlled touch-up, or rework. It should not be written as the default volume-production route when selective solder, wave solder, inspection, and electrical validation are already part of the same planned flow.

## Stable Facts

- The internal SMT/THT and through-hole assembly pages place manual, selective, and wave-related solder activity inside one broader mixed-technology process chain rather than as isolated alternatives with the same production posture.
- The internal quality-system page supports a layered control model that includes design review, incoming checks, in-process inspection, hidden-joint inspection when needed, functional validation, cleaning, and final release.
- The first-article and traceability pages support the idea that build deviations, setup confirmation, and release evidence belong in recorded gates rather than in undocumented bench decisions.
- The BGA reballing and X-ray pages support a broader principle for rework: once assembly leaves first-pass flow and enters recovery or touch-up, inspection and revalidation remain necessary and may change by defect type and visibility.
- The medical industry page supports imaging, monitoring, diagnostics, and wearable context, but only at application and quality-flow level, not as proof that any manual solder route is medically acceptable by itself.
- The internal hand-solder and THT blogs consistently frame manual solder as useful for prototypes, low-count through-hole work, additions, repair, and touch-up, while also exposing repeatability, cleanliness, and documentation concerns.

## Conditions And Methods

- Use this card for `tht-through-hole-soldering-medical-imaging-wearable` and as supporting boundary context for `selective-wave-soldering-medical-imaging-wearable`.
- Safe rewrite pattern: manual solder can be positioned as a controlled method for prototypes, engineering changes, isolated connectors or wires, repair, touch-up, or recovery after inspection finds a defect.
- Safe rewrite pattern: on mixed-technology boards, manual solder is usually the exception path when THT count is low, access is limited, rework is localized, or a board still needs engineering iteration.
- Safe rewrite pattern: for production-route comparison, say manual solder trades automation and repeatability for flexibility and localized intervention.
- Tie manual solder claims to downstream records and checks such as visual inspection, defect review, continuity or functional recheck, cleaning review, and traceability of the intervention.
- For medical imaging and wearable contexts, keep the risk discussion focused on compact layouts, nearby sensitive components, contamination control, heat localization, and operator-to-operator consistency rather than on device compliance.

## Supported Claims

- Hand solder is appropriate to describe as a prototype, repair, touch-up, jumper/wire-addition, or low-count completion method.
- Hand solder can be described as part of mixed-technology builds when a small number of through-hole or post-assembly operations do not justify a broader automated route.
- Manual rework should be described as controlled recovery work that triggers renewed inspection and, where appropriate, electrical or functional recheck.
- In compact medical imaging and wearable assemblies, uncontrolled manual solder or rework can increase risk around residue, local overheating, nearby part disturbance, and inconsistent workmanship between operators.
- A stronger production route such as selective or wave solder should be evaluated before presenting hand solder as the main plan for recurring volume builds.

## Limits And Non-Claims

- This card does not prove hand solder is the preferred route for heat-sensitive components, medical electronics, or wearable boards.
- It does not authorize IPC class-specific manual-solder acceptance thresholds, wetting angles, fillet geometry rules, barrel-fill percentages, or circumferential-wetting claims.
- It does not authorize claims about maximum rework count, allowable touch-up count, tip temperature, dwell time, preheat method, or mandatory cleaning chemistry.
- It does not support claims that certified operators alone make manual solder equal to automated consistency across sustained volume production.
- It does not support cost, lead-time, yield, or throughput rules for when hand solder becomes cheaper or faster than selective or wave solder.
- It does not support medical compliance, sterilization compatibility, biocompatibility, or field-reliability proof from manual solder practice alone.

## Fail Patterns

- Writing hand solder as the normal mass-production path for mixed-technology boards without explaining why selective or wave solder are not the main route.
- Treating hand solder as inherently safer for dense medical or wearable boards without discussing contamination, heat spread, access, and inspection limits.
- Turning IPC names into unsupported manual-solder acceptance tables or class-specific thresholds.
- Publishing numeric rules for temperatures, dwell, barrel fill, lead length, rework count, or operator yield from this source layer.
- Presenting touch-up as a cosmetic-only step that does not need logging, inspection, or retest.

## Open Questions

- Add stronger public sources later if future rewrites need explicit contamination-control or cleanliness-method language after rework.
- Add a later boundary card if future inverter content needs a sharper split between soldered terminals, press-fit interfaces, and service-replaceable hardware.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/bga-reballing.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- /code/hileap/frontendAPT/public/static/blogs/2025/06/en/hand-solder-best-practices.md
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/through-hole-soldering-basics.md
- https://www.ipc.org/ipc-document-revision-table
- https://www.ipc.org/TOC/IPC-J-STD-001J_TOC.pdf
- https://www.ipc.org/TOC/IPC-A-610H-toc.pdf
