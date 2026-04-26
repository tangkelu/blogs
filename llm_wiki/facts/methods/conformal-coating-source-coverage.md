---
fact_id: "methods-conformal-coating-source-coverage"
title: "Conformal-coating articles need separate standards, coating-family, and internal process anchors"
topic: "Conformal coating source coverage"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "ipc-cc-830c-toc"
  - "electrolube-conformal-coatings-archive"
  - "humiseal-conformal-coating-brochure"
  - "frontendapt-pcba-pcb-conformal-coating-page-en"
  - "frontendapt-pcb-pcb-conformal-coating-page-en"
tags: ["conformal-coating", "ipc-cc-830", "pcba", "coating-chemistry", "masking", "inspection", "source-coverage"]
---

# Canonical Summary

> Conformal coating should be sourced with three layers: IPC-CC-830 for standards metadata, coating manufacturers for chemistry/application context, and internal PCBA pages for process handoff and capability framing.

## Stable Facts

- IPC-CC-830C provides a public metadata anchor for qualification and performance of electrical insulating compounds for printed wiring assemblies.
- Electrolube provides manufacturer-controlled conformal-coating knowledge and product-family context.
- HumiSeal provides manufacturer-controlled brochure-level context for coating definitions, common chemistries, application methods, and standards families.
- The internal APT conformal-coating page supports process-context framing such as coating as a PCBA protection step.
- The APT PCB-side conformal-coating page widens the internal vocabulary to include acrylic, silicone, urethane, parylene, and multiple application-method frames that may appear in board-protection content.

## Conditions And Methods

- Use this card for conformal-coating articles, especially dense PCBA, HDI, high-voltage, environmental exposure, and masking/test-access topics.
- Keep standards metadata, coating chemistry, process planning, and product selection separate.
- Refresh coating product lists and standards revision metadata before publication.

## Limits And Non-Claims

- This card does not provide coating thickness limits, cure schedules, cleanliness limits, masking keep-out dimensions, or qualification pass/fail criteria.
- It does not compare acrylic, silicone, urethane, hybrid, or parylene systems as a final selection table.
- It does not certify that an internal coating process meets IPC-CC-830.

## Open Questions

- Add product-level datasheets for named coatings before publishing chemistry comparison tables.
- Add public workmanship guidance only if the target article needs more than standards metadata and manufacturer context.

## Source Links

- https://www.ipc.org/TOC/IPC-CC-830C-toc.pdf
- https://electrolube.com/knowledge-product-type/conformal-coatings/
- https://info.humiseal.com/hubfs/Product%20Brochure-v4%5B93%5D.pdf
- /code/hileap/frontendAPT/public/static/pcba/en/pcb-conformal-coating.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-conformal-coating.json
