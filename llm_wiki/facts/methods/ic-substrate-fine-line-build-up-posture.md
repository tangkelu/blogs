---
fact_id: "methods-ic-substrate-fine-line-build-up-posture"
title: "Internal IC substrate pages consistently frame fine-line SAP, stacked microvias, and ABF/BT build-up as the core substrate posture"
topic: "IC substrate fine-line build-up posture"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendhil-ic-substrate-pcb-product-page-en"
tags: ["internal", "ic-substrate", "sap", "microvia", "fine-line", "methods"]
---

# Canonical Summary

> The IC substrate page presents advanced packaging substrate work as a distinct capability class: fine-line SAP, stacked microvias, ABF/BT build-up, and flip-chip readiness are bundled together as the normal process posture for this part family.

## Stable Facts

- The HIL IC substrate page explicitly names fine-line SAP as a process basis for the substrate family.
- The same page pairs SAP with stacked microvias and ABF/BT build-up dielectrics.
- The page also frames the substrate as flip-chip ready with controlled warpage and impedance language.

## Conditions And Methods

- Use this card as internal support for substrate capability summaries and advanced-packaging positioning.
- Treat line/space, microvia, and warpage numbers as refresh-sensitive internal claims.
- If a customer-facing page needs exact substrate tolerances, refresh against current engineering data first.

## Limits And Non-Claims

- This card does not claim general PCB fabricators can produce the same substrate geometry.
- It does not convert page positioning into a guaranteed package-design outcome.

## Source Links

- /code/hileap/frontendHIL/public/static/products/en/ic-substrate-pcb.json
