---
fact_id: "methods-pcba-mixed-technology-assembly-flow"
title: "Internal PCBA pages frame SMT, THT, selective solder, and inspection as one coordinated assembly flow"
topic: "PCBA mixed-technology assembly flow"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendhil-smt-assembly-product-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
tags: ["internal", "pcba", "smt", "tht", "selective-solder", "process-flow", "methods"]
---

# Canonical Summary

> The internal non-blog PCBA pages describe assembly as a coordinated flow across stencil and paste engineering, SMT placement, reflow, selective or wave solder for through-hole content, inspection, electrical test, and functional validation rather than as isolated SMT and THT services.

## Stable Facts

- The APT SMT/THT page describes stencil and paste engineering, SMT placement, selective and wave solder, and inspection/test as connected modules in one assembly flow.
- The same page places DFX/tooling review, line setup, SMT execution, selective/wave solder, and ICT/FCT inside one process sequence.
- The APT turnkey assembly page frames PCB fabrication, component sourcing, SMT/THT, testing/inspection, box build, and logistics as one end-to-end service scope.
- The HIL SMT page frames print, placement, reflow profile logging, SPI/AOI/X-ray, and ICT/FCT as part of one SMT process-control stack.
- The HIL through-hole page frames THT, wave/selective solder, press-fit, AOI/X-ray, ICT/FCT, and mixed-technology sequencing as related assembly controls.
- The HIL turnkey page reinforces the same single-workflow framing from BOM review through SMT/THT, inspection, test, and box-build handoff.

## Conditions And Methods

- Treat this as an internal capability and workflow-structuring card.
- Use it for PCBA topic pages where the writing needs to explain why SMT, THT, soldering, inspection, and test cannot be planned independently.
- Refresh exact line counts, placement accuracy, lead time, and volume claims before using them as firm customer-facing commitments.

## Limits And Non-Claims

- This card does not prove every PCBA order receives every inspection or test step.
- It does not claim all SMT/THT builds require the same test coverage.
- It does not replace project-level DFM/DFA/DFT review, fixture planning, BOM status review, or process engineering approval.

## Open Questions

- Add a later topic wiki page for `pcba-assembly-flow-from-smt-to-box-build`.
- Add dedicated fact cards for `selective-solder-and-through-hole-process-control` and `SMT process window management`.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendAPT/public/static/pcba/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/smt-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json

