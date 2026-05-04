---
topic_id: "processes-mixed-technology-solder-route-selection"
title: "Mixed-Technology Solder Route Selection"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "methods-pcba-mixed-technology-assembly-flow"
  - "methods-selective-wave-solder-and-mixed-technology-sequencing"
  - "methods-tht-heavy-assemblies-power-and-medical-context"
  - "methods-mixed-technology-lane-b-rewrite-gate"
  - "methods-parameter-scope-pcba-selective-solder-tht-route-context"
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

# Governance Summary

> Mixed-technology solder route selection is an assembly-boundary decision, not a method-superiority claim. In the local corpus, the safe active posture is to choose among selective solder, wave solder, hand-solder exceptions, and THT-heavy mixed assembly by board population, component class, access, thermal sensitivity, and downstream verification needs while keeping standards thresholds, process windows, regulated qualification, and commercial claims out of scope.

## Route Selection Model

| Route question | Safe decision frame | What the corpus supports |
|---|---|---|
| Should the board stay SMT-first with targeted through-hole soldering? | Dense SMT neighborhoods, localized joints, and bottom-side protection needs | Selective solder as a localized mixed-technology route |
| Should broader through-hole exposure stay on the table? | THT-dense populations and layouts that can tolerate broader exposure with the right support | Wave solder as a viable route when board population and layout permit |
| Why does through-hole content remain at all? | Connectors, relays, transformers, inductors, terminals, shielding attachments, and other mechanically stressed or larger hardware | THT retention for interface and hardware reasons, not a separate quality regime |
| What closes the route decision? | Inspection, electrical validation, and release workflow | Post-solder verification belongs to the same assembly flow |

## What This Page Controls

- Use this page when a draft needs to explain how SMT, THT insertion, solder-route choice, inspection, and electrical validation stay inside one coordinated assembly flow.
- Treat `selective solder`, `wave solder`, `manual solder exceptions`, and `THT-heavy mixed assembly` as route options inside one program, not as isolated services.
- Keep medical and power-electronics context at packaging, hardware-class, and release-workflow level only.
- Use this page to decide which route story is safe before a draft moves into fixture planning, connector routing, or application-specific framing.

## Stable Facts

- The current internal PCBA source layer frames stencil and paste engineering, SMT placement, through-hole insertion, selective or wave solder, inspection, and electrical test as one coordinated assembly flow.
- The current source layer supports selective solder as a targeted route for mixed-technology boards when localized heating and nearby SMD sensitivity matter.
- The current source layer supports wave solder as a route that can fit THT-dense populations when board layout and board population permit it.
- The current source layer supports THT retention for connectors, relays, transformers, inductors, terminals, shielding attachments, power entry, and other mechanically stressed or larger hardware.
- The current medical and power-energy source layer supports scenario framing for imaging, monitoring, wearables, inverters, converters, storage, charging, and protection electronics without turning those scenarios into qualification proof.
- The current quality and test source layer keeps inspection, functional validation, and release gating downstream of the solder-route decision rather than separate from it.

## Assembly Boundary Rules

### Keep These Lanes Separate

- `route choice`: selective solder, wave solder, hand-solder exception, or broader THT-heavy mixed assembly
- `component reason`: connector, relay, transformer, terminal, inductive part, shield, or other mechanically stressed hardware
- `board-neighborhood constraint`: nearby SMT density, overhang, shielding, access, and thermal-mass interaction
- `verification handoff`: visual inspection, X-ray as applicable, ICT/FCT access, and release workflow

### Safe Selection Guidance

- Favor selective solder framing when the board has localized through-hole content near dense SMT or heat-sensitive neighborhoods.
- Keep wave solder framing available when the board has broader THT population and the layout can support that route.
- Use THT-heavy framing when the key issue is interface hardware, power hardware, or mechanically stressed parts rather than a universal reliability story.
- Keep manual solder as a bounded exception path, not the default explanation for every mixed-technology build.

## Medical And Power Context Boundaries

- Medical context here means compact packaging, interface mix, shielding, monitoring, imaging, wearable, or medical-power module framing.
- Power context here means inverter, converter, charger, storage, protection-electronics, terminal, relay, magnetic, or other larger interface hardware framing.
- Neither context authorizes compliance, qualification, performance, lifetime, or sector-approval claims from this page.

## Common Misreadings

- Mixed-technology does not mean selective solder is automatically the best route.
- A THT-heavy section does not mean the whole product is predominantly through-hole.
- Medical-adjacent assembly context does not prove a regulated qualification outcome.
- Power-electronics context does not prove current handling, temperature-rise, efficiency, or lifetime performance.
- IPC document families in the source layer do not turn this page into a standards-threshold reference.

## Explicit Blocked Claims

- `standards-threshold claims`: do not publish IPC class-specific acceptability thresholds, hole-fill thresholds, or workmanship tables from this page.
- `process-window guarantees`: do not publish nozzle sizes, pallet rules, preheat windows, nitrogen settings, dwell times, flux chemistry, or cleanliness limits from this page.
- `medical/power qualification claims`: do not publish medical compliance proof, sterilization compatibility, biocompatibility, inverter qualification, current rating, thermal-rise, efficiency, or service-life claims from this page.
- `cost, lead-time, and yield claims`: do not publish commercial or throughput outcomes from this page.

## Must Refresh Before Publishing

- any IPC class-specific threshold or acceptability table
- any detailed selective-solder, wave-solder, or manual-solder process window
- any medical or power-sector qualification, approval, or performance claim
- any current, resistance, contact-force, temperature-rise, efficiency, or lifetime numeric
- any cost, lead-time, throughput, or yield statement

## Related Fact Cards

- `methods-pcba-mixed-technology-assembly-flow`
- `methods-selective-wave-solder-and-mixed-technology-sequencing`
- `methods-tht-heavy-assemblies-power-and-medical-context`
- `methods-mixed-technology-lane-b-rewrite-gate`
- `methods-parameter-scope-pcba-selective-solder-tht-route-context`

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
