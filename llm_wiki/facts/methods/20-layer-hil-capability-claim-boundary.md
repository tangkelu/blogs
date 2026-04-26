---
fact_id: "methods-20-layer-hil-capability-claim-boundary"
title: "20-layer HIL-specific capability claims must stay separate from public any-layer, method, and material-form vocabulary"
topic: "20-layer HIL capability claim boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-2226a-hdi-standard-page"
  - "ipc-jpca-4104-toc"
  - "ipc-2315-legacy-hdi-guide-page"
  - "ipc-microvia-reliability-warning-2019"
  - "ipc-tr-486-ist-round-robin-page"
  - "ipc-tm650-test-methods-index"
  - "ipc-tm650-method-development-packet-page"
  - "ats-hdi-anylayer-page"
  - "ventec-vt-47lt-datasheet-page"
  - "ventec-ultrathin-build-up-datasheet-page"
  - "isola-sequential-lamination-in-pcbs-note"
tags: ["20-layer", "hil", "capability-claim", "any-layer", "stacked-microvia", "boundary", "gap-control"]
---

# Canonical Summary

> Current public `HDI`, any-layer, method, and process-sensitivity sources are strong enough to support guarded `20-layer` wording around architecture vocabulary, reliability sensitivity, and evaluation workflow. They are not strong enough to prove HIL-specific board capability claims such as stacked-layer span, transferable geometry freedom, validated manufacturability, or production-ready shop strength.

## Stable Facts

- A conservative `20-layer` rewrite may use guarded architecture vocabulary such as `any-layer`, `ELIC`, or stacked-microvia context without turning it into HIL-specific capability proof.
- Public `IPC` `HDI` and legacy `microvia` metadata support architecture and method vocabulary, not supplier capability claims.
- IPC's public microvia-reliability warning supports the claim that demanding interconnect structures deserve caution, not that a specific supplier capability quote is proven.
- Public `IPC-TR-486` and `TM-650` metadata support named evaluation context, not board-level capability certification.
- Public supplier-side any-layer and build-up pages support architecture-positioning vocabulary, not `up to N layers`, `supports X geometry`, or `qualified at scale` claims for HIL.
- Public sequential-lamination notes support process-sensitivity wording, not validated HIL stacked-structure capability.
- These sources together support guarded wording such as `may require validation`, `can increase sensitivity`, and `is one possible architecture`, not `HIL can build`.

## Conditions And Methods

- Use this card when a `20-layer` draft risks rewriting public architecture/method sources into HIL-specific capability claims.
- Pair this card with `facts/methods/20-layer-geometry-and-factory-capability-boundary.md`, `facts/methods/20-layer-any-layer-vocabulary-vs-shop-capability-boundary.md`, and `facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`.
- Prefer wording such as `publicly positioned as`, `may involve`, `should be validated`, and `does not prove supplier capability by itself`.
- Keep public any-layer, stacked-microvia, and method references attached to architecture or workflow context rather than HIL marketing promises.

## Limits And Non-Claims

- This card does not prove HIL-specific stacked-microvia span, geometry capability, manufacturability readiness, or production approval.
- It does not prove that HIL can build a `20-layer` any-layer or `ELIC` board at any stated geometry or complexity level.
- It does not turn public `HDI`/method vocabulary into HIL supplier evidence.
- It does not provide dated shop-capability records, accepted build history, or released production evidence.

## Open Questions

- Add a dated supplier-evidence layer only if future work truly needs HIL capability claims.
- Reassess `20-layer` readiness only after HIL capability wording is fully contained from prompt retrieval.

## Source Links

- https://shop.electronics.org/ipc-2226/ipc-2226-standard-only/Revision-a/english
- https://www.electronics.org/TOC/IPC-JPCA-4104.pdf
- https://shop.electronics.org/ipc-2315/ipc-2315-standard-only/Revision-0/english
- https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high
- https://shop.electronics.org/technical-reports-white-papers/studytechnical-report
- https://www.electronics.org/test-methods
- https://www.ipc.org/ipc-tm-650-method-development-packet
- https://ats.net/en/products/hdi-printed-circuit-boards/
- https://www.ventec-group.com/cht/products/lead-free-assembly/vt-47lt/datasheet/
- https://www.ventec-group.com/cht/products/special-applications/ultrathin/datasheet/
- https://www.isola-group.com/wp-content/uploads/Sequential-Lamination-in-PCBs.pdf
