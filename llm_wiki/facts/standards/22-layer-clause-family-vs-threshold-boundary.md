---
fact_id: "standards-22-layer-clause-family-vs-threshold-boundary"
title: "22-layer clause-family visibility must stay separate from technical thresholds or acceptance numerics"
topic: "22-layer clause family versus threshold boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-a-600k-toc"
  - "ipc-6011a-toc"
  - "ipc-6012f-toc"
  - "ipc-6012fa-toc"
  - "ipc-6012fs-toc"
  - "ipc-6012fa-automotive-addendum-page"
  - "ipc-6012fs-space-military-addendum-page"
  - "ipc-6012-addendum-taxonomy-page"
tags: ["22-layer", "clause-family", "threshold-boundary", "ipc-6012", "ipc-6012fa", "ipc-6012fs", "toc", "acceptance"]
---

# Canonical Summary

> Public TOCs and product metadata are strong enough to show that hi-rel rigid-board standards expose clause-family visibility around topics such as plating, annular ring, bow/twist, electrical continuity, destructive physical analysis, and repair. They are not strong enough to expose the technical thresholds, frequencies, sample sizes, or pass/fail values inside those clause families.

## Stable Facts

- A conservative `22-layer` rewrite may state that public `IPC-6012` and addendum metadata reveals which technical areas exist without revealing the criteria inside them.
- Public `IPC-6012FA` and `IPC-6012FS` TOCs support guarded wording that automotive and space/military addenda touch multiple clause families rather than one isolated requirement.
- Public `IPC-6012FS` TOC supports guarded clause-family visibility across areas such as annular ring, bow and twist, plating integrity, hole copper plating, filled vias, electrical continuity/isolation, thermal shock, destructive physical analysis, and repair.
- Public `IPC-6011A` TOC supports guarded generic framework vocabulary around quality assurance and procurement-context structure without exposing sectional rigid-board criteria.
- Public `IPC-A-600K` TOC supports guarded visibility that bare-board acceptability and inspection occupy their own document layer distinct from the `IPC-6012` performance-specification layer.
- Public addendum taxonomy pages support guarded wording that clause families can branch by program context without authorizing threshold reconstruction.
- These sources together support `clause-family visibility` and `document hierarchy` wording, not numeric reuse.

## Conditions And Methods

- Use this card when a `22-layer` draft is tempted to infer technical values from TOC headings, clause names, or addendum summaries.
- Pair this card with `facts/standards/22-layer-class-3-and-addendum-threshold-boundary.md`, `facts/standards/22-layer-high-reliability-rewrite-guardrail.md`, and `facts/standards/22-layer-hi-rel-acceptance-workflow-boundary.md`.
- Prefer wording such as `publicly shows the topic exists`, `reveals clause-family scope`, `does not expose criteria`, and `must not be reconstructed from headings`.
- Keep TOC-based evidence attached to topic visibility and hierarchy only.

## Limits And Non-Claims

- This card does not provide clause text, criteria values, sample plans, thresholds, or pass/fail tables.
- It does not justify deriving acceptance numbers from headings such as `thermal shock`, `plating`, `repair`, or `DPA`.
- It does not prove applicability, compliance, or acceptance authority for any supplier or `22-layer` build.
- It does not turn public topic visibility into reusable program rules.

## Open Questions

- Add a narrower TOC-boundary card only if future work needs to separate base-document clause visibility from addendum-only clause visibility.
- Reassess `22-layer` readiness only after clause-family visibility is no longer the main source of threshold leakage in prompt retrieval.

## Source Links

- https://www.electronics.org/TOC/IPC-A-600K-EN_TOC.pdf
- https://www.electronics.org/TOC/IPC-6011A_TOC.pdf
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://www.electronics.org/TOC/IPC-6012FA-TOC.pdf
- https://www.electronics.org/TOC/IPC-6012FS_TOC.pdf
- https://shop.electronics.org/taxonomy/term/792
