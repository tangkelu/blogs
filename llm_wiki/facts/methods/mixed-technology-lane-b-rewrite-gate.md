---
fact_id: "methods-mixed-technology-lane-b-rewrite-gate"
title: "Lane B mixed-technology assembly rewrites need a route-selection gate that blocks standards-threshold and power-performance overclaim"
topic: "mixed technology lane B rewrite gate"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-27"
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
tags: ["mixed-technology", "selective-solder", "wave-solder", "tht", "medical", "inverter", "rewrite-gate", "lane-b"]
---

# Canonical Summary

> The current mixed-technology source layer is strong enough to support concrete Lane B articles when the draft behaves like a solder-route and assembly-handoff guide. It is not strong enough for standards-threshold tables, detailed process windows, medical compliance proof, or inverter current and lifetime numerics.

## Stable Facts

- The internal mixed-technology source layer consistently frames SMT, through-hole insertion, selective solder, wave solder, inspection, and electrical validation as one coordinated assembly flow.
- The current source layer supports selective solder as a targeted route for through-hole content on mixed-technology boards when nearby SMDs or localized heating concerns matter.
- The current source layer supports wave solder as a route that can fit THT-dense boards when board population and layout permit it.
- The current source layer supports THT retention for connectors, relays, transformers, inductors, terminals, mechanically stressed interfaces, and other larger or power-related hardware.
- The medical and power-energy application pages support scenario framing, not compliance proof or quantified operating performance.

## Rewrite Gate

### Required To Pass

- The draft must open by stating that solder-route choice depends on board population, component classes, access, thermal sensitivity, and inspection strategy rather than a universal `best method`.
- The draft must include at least one selection frame that helps the reader choose among selective solder, wave solder, hand solder, and THT-heavy mixed assembly.
- The draft must identify the kinds of parts or interfaces that drive the route choice:
  connectors, relays, transformers, terminals, mechanically stressed interfaces, or dense SMT-adjacent through-hole content.
- The draft must include a post-solder verification or release section that ties inspection and electrical validation back into the same workflow.
- The draft must include a buyer or engineer checklist covering THT content, nearby SMD density, thermal-mass concerns, connector or terminal interfaces, access constraints, and test expectations.
- For `selective-wave-soldering-medical-imaging-wearable`, the draft must keep the medical angle at packaging, component mix, and release-workflow level rather than standards-compliance or sterilization-proof level.
- For `tht-through-hole-soldering-medical-imaging-wearable`, the draft must keep the article focused on mechanically stressed or service-critical interfaces inside a broader mixed-technology build rather than on security, encryption, or device approval claims.
- For `tht-through-hole-soldering-renewable-energy-inverter`, the draft must keep the explanation at the level of larger power hardware, mixed-technology split, and validation workflow rather than current, temperature-rise, lifetime, or efficiency numerics.

### Strong Signals Of Top-Tier Quality

- The article helps the reader decide why a board is selective-solder candidate, wave-solder candidate, or still partly hand-soldered.
- It gives the reader a usable distinction between `through-hole because of interface or mechanics` and `through-hole because the entire board is THT-heavy`.
- It explains how solder-route choice interacts with downstream inspection and electrical validation rather than presenting soldering as a disconnected shop step.
- It turns application framing into reviewable inputs, such as whether a wearable board has compact mixed-signal neighborhoods or whether an inverter board has larger magnetic and terminal hardware.

### Fail Patterns

- Publishing IEC 60601, ISO 13485, ISO 10993, or other regulated-market claims as if the current source layer proves them.
- Publishing nozzle sizes, solder-pot settings, preheat windows, nitrogen requirements, flux chemistry rules, hole-fill thresholds, bridging thresholds, or cleanliness limits from this source layer.
- Publishing current ratings, contact-resistance numerics, temperature-rise numerics, service-life numerics, creepage values, or efficiency percentages for inverter programs.
- Treating selective solder as always safer than wave solder, or THT as always more reliable than SMT, without project-specific evidence.

## Conditions And Methods

- Use this card for `selective-wave-soldering-medical-imaging-wearable`, `tht-through-hole-soldering-medical-imaging-wearable`, and `tht-through-hole-soldering-renewable-energy-inverter`.
- Pair this card with `methods-selective-wave-solder-and-mixed-technology-sequencing`, `methods-tht-heavy-assemblies-power-and-medical-context`, and `methods-pcba-mixed-technology-assembly-flow`.
- Prefer prompt instructions that require `route selection`, `component classes`, `inspection handoff`, and `buyer checklist` outputs.
- Keep any mention of IPC standards at metadata or family level unless stronger public threshold authority is added later.

## Limits And Non-Claims

- This card does not authorize IPC class-specific acceptability claims, solder-joint threshold tables, hole-fill requirements, nozzle geometry, pallet design dimensions, or cleanliness limits.
- It does not authorize medical compliance, sterilization compatibility, or biocompatibility proof.
- It does not authorize inverter current, resistance, thermal-rise, efficiency, lifetime, or qualification claims.
- It does not prove that selective solder or THT is categorically required for any medical or power-electronics program.

## Prompt Blocks

- Block `standards-threshold leakage`:
  do not let standards names become unsourced acceptability or compliance tables.
- Block `process-window certainty`:
  do not publish detailed solder settings, nozzle rules, or cleanliness criteria from this source layer.
- Block `power-numeric inflation`:
  do not publish busbar current, contact resistance, temperature-rise, or service-life math.
- Block `method-superiority filler`:
  do not allow the article to claim that selective solder, wave solder, or THT wins universally.

## Open Questions

- Add public design-for-access sources if future selective-solder rewrites need stronger pallet, nozzle-path, or keep-clear guidance.
- Add a later press-fit versus solder boundary card if future inverter rewrites need to split terminal and bus-interface routes more sharply.
- Add formal regulated-market sources before any medical mixed-technology rewrite claims device-safety or compliance outcomes.

## Source Links

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
