---
topic_id: "processes-mixed-technology-solder-route-selection"
title: "Mixed-Technology Solder Route Selection"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-27"
fact_ids:
  - "methods-pcba-mixed-technology-assembly-flow"
  - "methods-selective-wave-solder-and-mixed-technology-sequencing"
  - "methods-tht-heavy-assemblies-power-and-medical-context"
  - "methods-mixed-technology-lane-b-rewrite-gate"
source_ids:
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-pcba-pcb-stencil-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-industry-medical-page-en"
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "ipc-document-revision-table"
  - "ipc-j-std-001j-toc"
  - "ipc-a-610h-toc"
tags: ["mixed-technology", "selective-solder", "wave-solder", "tht", "medical", "power-electronics", "assembly-flow"]
---

# Definition

> Mixed-technology solder route selection is the assembly-planning decision that keeps SMT, through-hole insertion, selective solder, wave solder, manual solder, inspection, and electrical validation inside one coordinated workflow. In the current corpus, the strongest reusable value is route selection by component population and interface type, not detailed thresholds or compliance proof.

## Why This Topic Matters

- Mixed-technology articles become weak when they describe selective solder, wave solder, or THT as isolated services instead of interacting choices inside one build plan.
- The current source layer already supports a clearer frame: route choice depends on part mix, nearby SMD density, mechanical and power interfaces, and downstream inspection or test.
- This topic page gives later rewrites one controlled place to discuss compact medical electronics and power or inverter hardware without drifting into unsupported standards, process windows, or power numerics.

## Stable Facts

- The current internal source layer frames SMT, THT, selective solder, wave solder, inspection, and electrical validation as one mixed-technology flow.
- The current source layer supports selective solder as a targeted route for through-hole content when localized heating and nearby SMD sensitivity matter.
- The current source layer supports wave solder as a viable route for THT-dense populations when board layout and component mix allow it.
- The current source layer supports THT retention for connectors, relays, transformers, inductors, terminals, shielding attachments, power entry, and other mechanically stressed or larger hardware.
- The medical application page supports imaging, monitoring, and wearable hardware context, while the power-energy page supports inverter, converter, storage, charging, and protection-electronics context.
- Inspection, functional validation, and final release are supported as downstream gates in the same broader assembly workflow.

## Engineering Boundaries

- Do not write about selective solder, wave solder, or THT as if one route is universally superior.
- Use medical and power-energy pages for hardware-context framing, not for compliance, qualification, or device-performance proof.
- Keep route choice, component classes, access constraints, thermal-mass concerns, inspection scope, and electrical-validation scope as separate review items.
- Keep IPC references at standards-family level unless stronger public threshold support is added later.
- Treat power-stage performance, current handling, connector retention, and medical safety thresholds as refresh-required claim classes rather than stable public facts from this corpus.

## Common Misreadings

- A medical mixed-technology board is not automatically a selective-solder-only board.
- A THT-heavy section does not mean the whole product is predominantly through-hole.
- Selective solder is not simply `wave solder but more precise`; its value depends on the actual board neighborhood and access constraints.
- THT is not automatically a reliability guarantee; the broader inspection and validation flow still matters.
- An inverter or power-electronics context does not by itself prove current, temperature-rise, efficiency, or lifetime outcomes.

## Must Refresh Before Publishing

- Any IPC class-specific acceptability or hole-fill threshold
- Any nozzle, pallet, flux, preheat, nitrogen, dwell, or cleanliness process window
- Any medical compliance, sterilization compatibility, or biocompatibility claim
- Any inverter current, contact-resistance, thermal-rise, efficiency, service-life, or qualification claim
- Any cost, lead-time, throughput, or supplier-capability claim

## Related Fact Cards

- `methods-pcba-mixed-technology-assembly-flow`
- `methods-selective-wave-solder-and-mixed-technology-sequencing`
- `methods-tht-heavy-assemblies-power-and-medical-context`
- `methods-mixed-technology-lane-b-rewrite-gate`

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-stencil.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/power-energy-pcb.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- https://www.ipc.org/ipc-document-revision-table
- https://www.ipc.org/TOC/IPC-J-STD-001J_TOC.pdf
- https://www.ipc.org/TOC/IPC-A-610H-toc.pdf
