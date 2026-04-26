---
fact_id: "methods-internal-capability-family-map"
title: "APT capabilities pages form a stable six-family PCB capability map for prompt routing and scope control"
topic: "Internal capability family map"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-capabilities-index-page-en"
  - "frontendapt-ceramic-pcb-capability-page-en"
  - "frontendapt-flex-pcb-capability-page-en"
  - "frontendapt-hdi-pcb-capability-page-en"
  - "frontendapt-metal-pcb-capability-page-en"
  - "frontendapt-rigid-flex-pcb-capability-page-en"
  - "frontendapt-rigid-pcb-capability-page-en"
tags: ["internal", "capabilities", "pcb", "rigid-pcb", "flex-pcb", "hdi", "rigid-flex", "metal-core", "ceramic"]
---

# Canonical Summary

> The current APT `capabilities` layer is a stable internal map across six PCB families: rigid, flex, HDI, rigid-flex, metal-core, and ceramic. It is suitable for capability discovery, prompt routing, and scope framing, but it should not be treated as a frozen parameter sheet.

## Stable Facts

- The APT capabilities overview page organizes the public capability layer around six recurring manufacturing families: rigid PCB, flex PCB, HDI PCB, rigid-flex PCB, metal-core PCB, and ceramic PCB.
- The individual capability pages consistently position each family with a mix of application framing, process-language framing, and manufacturability-support language.
- The rigid PCB page is the general anchor for multilayer, heavy-copper, HDI-adjacent, and impedance-oriented rigid-board work.
- The flex and rigid-flex pages separate pure bendable-circuit framing from combined rigid-plus-flex stackup framing, which is useful when prompts need to distinguish flex-only and rigid-flex design problems.
- The HDI page frames density around microvias, sequential build-up, fine-line routing, and controlled-impedance support.
- The metal-core and ceramic pages position thermal-management platforms as distinct capability families rather than as generic "high thermal" variants of standard rigid boards.

## Conditions And Methods

- Use this card when a draft or prompt first needs to decide which internal capability family is actually in scope.
- Treat the overview page as a taxonomy anchor and the individual capability pages as family-specific framing support.
- When a prompt crosses families, split the problem explicitly: for example, HDI plus rigid-flex, or thermal platform plus assembly integration.
- Refresh all numeric limits, lead-time statements, and material-specific claims before publication.

## Limits And Non-Claims

- This card does not prove current production windows for layer count, trace/space, drill size, copper weight, thermal conductivity, bend radius, or lead time.
- It does not claim every option mentioned on one capability page is available on every production line or in every region.
- It does not replace official material datasheets, test standards, or current engineering release data.

## Open Questions

- Add a follow-on card if later batches need the capabilities layer joined to APT PCB service pages and HIL product pages as one cross-site portfolio map.
- Add deeper method cards only when prompts require stronger treatment of thermal-platform selection, flex reliability, or HDI process windows.

## Source Links

- /code/hileap/frontendAPT/public/static/capabilities/en/index.json
- /code/hileap/frontendAPT/public/static/capabilities/en/ceramic-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/flex-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/hdi-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/metal-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/rigid-flex-pcb.json
- /code/hileap/frontendAPT/public/static/capabilities/en/rigid-pcb.json
