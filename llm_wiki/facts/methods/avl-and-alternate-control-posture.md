---
fact_id: "methods-avl-and-alternate-control-posture"
title: "AVL and alternate control should be framed as sourcing governance, not supplier approval proof"
topic: "AVL and alternate control posture"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-01"
source_ids:
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendapt-pcba-component-sourcing-page-en"
  - "frontendapt-pcba-components-bom-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendhil-turnkey-assembly-product-page-en"
  - "frontendhil-box-build-assembly-product-page-en"
  - "frontendapt-materials-index-page-en"
tags: ["avl", "alternate", "sourcing", "bom", "traceability", "governance", "methods"]
---

# Canonical Summary

> AVL is a sourcing-governance problem: the build needs controlled source identity, lifecycle review, alternates control, and traceability, but those controls do not by themselves prove availability, cost, lead time, or supplier approval.

## Stable Facts

- The turnkey assembly and component-sourcing pages tie sourcing to BOM review, lifecycle checks, authenticity review, alternates, and traceability.
- The components-BOM and quality-system pages reinforce that source identity and build records are part of manufacturing control.
- The box-build pages extend the same governance into later integration and logistics stages when the program needs it.

## Conditions And Methods

- Use this card when a draft needs to explain how AVL review fits into turnkey assembly or NPI.
- Keep alternate control, lifecycle review, and revision-controlled release together as one sourcing-governance flow.
- Treat AVL as part of the evidence chain, not as proof of supplier capability or commercial advantage.

## Limits And Non-Claims

- This card does not prove pricing, lead time, stock, or supplier status.
- It does not authorize generic supplier-approval language.
- It does not replace a live BOM scrub or project-specific sourcing decision.

## Open Questions

- Add a separate supplier-status card later if a future batch needs refreshed availability or lifecycle metadata.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/turnkey-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/component-sourcing.json
- /code/hileap/frontendAPT/public/static/pcba/en/components-bom.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendHIL/public/static/products/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/box-build-assembly.json
- /code/hileap/frontendAPT/public/static/materials/en/index.json
