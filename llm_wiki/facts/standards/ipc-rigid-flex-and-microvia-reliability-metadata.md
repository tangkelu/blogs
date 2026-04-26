---
fact_id: "standards-ipc-rigid-flex-and-microvia-reliability-metadata"
title: "IPC rigid-board, flex-board, and microvia-reliability references should be handled as metadata and caution context, not threshold tables"
topic: "IPC rigid flex microvia reliability metadata"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "ipc-document-revision-table"
  - "ipc-6012f-toc"
  - "ipc-6013e-toc"
  - "ipc-6012f-release"
  - "ipc-microvia-reliability-warning-2019"
tags: ["ipc", "ipc-6012", "ipc-6013", "rigid", "rigid-flex", "microvia", "reliability", "metadata"]
---

# Canonical Summary

> IPC-6012F and IPC-6013E are valid public anchors for rigid-board and flexible/rigid-flex performance-specification references, and IPC's 2019 microvia warning is valid public context for reliability caution, but none of these public sources justify copying threshold tables or acceptance criteria into blog evidence packs.

## Stable Facts

- IPC-6012F is the current rigid printed-board qualification and performance specification family anchor in the public IPC corpus.
- IPC-6012F publicly covers rigid board constructions including multilayer boards, blind/buried via and microvia constructions, and metal-core variants.
- IPC-6013E is the public flexible printed-board qualification and performance specification family anchor and is relevant when rigid-flex or flex-performance language appears in manufacturing articles.
- IPC publicly warned in 2019 that latent microvia failures in high-performance products could escape traditional fabrication acceptance and appear later during reflow, assembly stress, or field use.
- IPC publicly tied newer IPC-6012 revision work to stronger treatment of complex interconnected via structures and microvia-reliability concerns.

## Conditions And Methods

- Use this card when a layer-count or advanced-fabrication article needs to anchor rigid-board qualification context, rigid-flex qualification context, or cautionary microvia-reliability framing.
- Pair this card with current process documents, customer requirements, and licensed standards before making any claim about acceptance thresholds, qualification criteria, or required test methods.
- Treat this card as a guardrail against overstating stacked-microvia, hole-registration, or rigid-flex reliability claims from generic blog copy.

## Limits And Non-Claims

- This card does not provide plating-thickness thresholds, bow-and-twist limits, annular-ring limits, conductor geometry thresholds, IST-cycle thresholds, or workmanship criteria.
- It does not prove that a given stackup, microvia structure, or rigid-flex build is compliant with IPC-6012 or IPC-6013.
- It does not establish mandatory test flows for microvia reliability.

## Open Questions

- Add a separate public metadata and context layer for `IST` and related interconnect-reliability test framing.
- Decide whether layer-count evidence packs need a dedicated card for rigid-board addendums such as automotive, medical, or space variants.

## Source Links

- https://www.ipc.org/ipc-document-revision-table
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf
- https://www.ipc.org/news-release/ipc-releases-ipc-6012f-qualification-and-performance-specification-rigid-printed
- https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high
