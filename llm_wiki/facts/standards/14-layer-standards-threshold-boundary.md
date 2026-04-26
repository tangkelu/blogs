---
fact_id: "standards-14-layer-standards-threshold-boundary"
title: "14-layer standards language must stay at hierarchy and caution level, not become reusable threshold tables"
topic: "14-layer standards threshold boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-document-revision-table"
  - "ipc-6012f-toc"
  - "ipc-6013e-toc"
  - "ipc-6012f-release"
  - "ipc-microvia-reliability-warning-2019"
  - "ipc-2226a-hdi-standard-page"
  - "ipc-2315-legacy-hdi-guide-page"
tags: ["14-layer", "standards", "ipc-6012", "ipc-6013", "ipc-2226", "threshold-boundary", "rigid-flex", "gap-control"]
---

# Canonical Summary

> Current public IPC metadata is strong enough to support guarded `14-layer` wording around standards hierarchy, rigid-board versus rigid-flex specification context, and HDI caution context. It is not strong enough to authorize reusable `Class 2 / Class 3`, annular-ring, registration, plating, or acceptance-threshold tables.

## Stable Facts

- A conservative `14-layer` rewrite may state that standards references belong to a hierarchy and applicability layer, not to a free numeric rule table.
- Public `IPC-6012F` metadata supports rigid-board qualification and performance-specification context for multilayer boards.
- Public `IPC-6013E` metadata supports flex and rigid-flex qualification and performance-specification context when a `14-layer` article branches into flex or rigid-flex construction.
- Public `IPC-2226A` and legacy `IPC/JPCA-2315` references support guarded HDI and design-reference context, not shop-floor feature-size or acceptance thresholds.
- IPC's public microvia-reliability warning supports caution language that complex interconnect structures can carry latent reliability risk beyond generic fabrication acceptance.
- These sources together support hierarchy wording such as `base rigid-board context`, `flex/rigid-flex branch`, `HDI design-reference context`, and `qualification language requires controlled authority`.
- These sources do not expose public `Class 2 / Class 3`, registration, annular-ring, or acceptance numerics that can be reused inside a `14-layer` evidence pack.

## Conditions And Methods

- Use this card when a `14-layer` draft mentions `IPC-6012`, `IPC-6013`, `Class 2`, `Class 3`, `annular ring`, `registration`, or HDI standards language near table-style thresholds.
- Pair this card with `facts/standards/ipc-rigid-flex-and-microvia-reliability-metadata.md`, `facts/standards/hdi-design-reference-status-metadata.md`, and `logs/p4-06-14-layer-bridge-prep.md`.
- Prefer wording such as `standards context exists`, `qualification language must not be improvised`, `rigid-flex invokes a different specification family`, and `public metadata does not expose reusable thresholds`.
- Keep standards references attached to hierarchy, applicability, and caution context rather than to factory-capability or acceptance-table claims.

## Limits And Non-Claims

- This card does not provide `Class 2 / Class 3` thresholds, annular-ring minima, registration limits, plating minima, coupon plans, or acceptance frequencies.
- It does not prove that any `14-layer` rigid, flex, or rigid-flex build is compliant, qualified, released, or accepted under any IPC family.
- It does not convert public TOCs, release pages, or warning notices into clause-level technical criteria.
- It does not authorize standards-threshold tables to re-enter a `14-layer` article as softened pseudo-rules.

## Open Questions

- Add a narrower follow-on only if future work needs a separate boundary between rigid-board hierarchy wording and rigid-flex qualification-branch wording.
- Reassess only after stronger public threshold authority exists for the exact claim class being proposed.

## Source Links

- https://www.ipc.org/ipc-document-revision-table
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf
- https://www.ipc.org/news-release/ipc-releases-ipc-6012f-qualification-and-performance-specification-rigid-printed
- https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high
- https://shop.ipc.org/IPC-2226A-English-D
- https://shop.ipc.org/IPC-JPCA-2315-English-D
