---
fact_id: "standards-22-layer-class-3-and-addendum-threshold-boundary"
title: "22-layer Class 3 and addendum language must stay at hierarchy/context level, not become reusable threshold tables"
topic: "22-layer Class 3 and addendum threshold boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-a-600k-toc"
  - "ipc-6011a-toc"
  - "ipc-6012f-toc"
  - "ipc-6012em-medical-addendum-release"
  - "ipc-6012em-medical-addendum-page"
  - "ipc-6012fa-automotive-addendum-page"
  - "ipc-6012fa-toc"
  - "ipc-6012fs-space-military-addendum-page"
  - "ipc-6012fs-toc"
  - "ipc-6012-addendum-taxonomy-page"
tags: ["22-layer", "class-3", "class-3a", "ipc-6012", "ipc-6012em", "ipc-6012fa", "ipc-6012fs", "threshold-boundary", "addendum"]
---

# Canonical Summary

> Public IPC metadata is strong enough to support guarded `22-layer` wording that separates base rigid-board hierarchy, procurement-triggered addendum branches, and bare-board acceptability context. It is not strong enough to provide reusable `Class 3 / 3A` thresholds, sample plans, frequencies, or acceptance tables.

## Stable Facts

- A conservative `22-layer` rewrite may state that `Class 3` and addendum references belong to a standards hierarchy and procurement-context layer rather than a free numeric rule table.
- Public `IPC-6011A` metadata supports a generic printed-board framework layer where procurement documentation defines class and exceptions.
- Public `IPC-6012F` metadata supports the current rigid-board base-specification layer under that broader framework.
- Public `IPC-6012EM`, `IPC-6012FA`, and `IPC-6012FS` metadata support procurement-triggered medical, automotive, and space/military addendum branches beyond flat base-specification wording.
- Public `IPC-6012FS` metadata explicitly frames the space/military avionics branch as exceptions to `Class 3`-adjacent base requirements rather than as a standalone free rule set.
- Public `IPC-A-600K` metadata supports a separate bare-board inspection/acceptability layer distinct from assembly workmanship and distinct from supplier-status claims.
- Public IPC addendum-taxonomy metadata supports guarded wording that high-reliability rigid-board work can sit inside a branched addendum family rather than one flat `Class 3` namespace.
- These sources together support guarded hierarchy wording such as `base document`, `procurement-triggered addendum`, `exception layer`, and `acceptability context`, but not free thresholds.

## Conditions And Methods

- Use this card when a `22-layer` draft mentions `Class 3`, `Class 3A`, `IPC-6012`, `IPC-A-600`, or addendum names and risks collapsing them into reusable numeric criteria.
- Pair this card with `facts/standards/ipc-6012-addendum-program-metadata.md`, `facts/standards/22-layer-high-reliability-rewrite-guardrail.md`, and `facts/standards/22-layer-clause-family-vs-threshold-boundary.md`.
- Prefer wording such as `may invoke`, `sits under`, `adds exceptions`, `is procurement-triggered`, and `does not expose public thresholds`.
- Keep `Class 3` and addendum references attached to hierarchy and applicability context, not to specific numeric acceptance claims.

## Limits And Non-Claims

- This card does not provide annular-ring, plating, bow/twist, thermal-shock, solder-float, or hole-quality thresholds.
- It does not provide `Class 3A` acceptance values, frequencies, sample sizes, or lot-acceptance tables.
- It does not prove that any `22-layer` board or supplier is compliant, qualified, approved, or accepted under any addendum branch.
- It does not turn public TOCs, release pages, or taxonomy pages into clause-level technical criteria.

## Open Questions

- Add a narrower follow-on only if future work needs a separate boundary between bare-board acceptability vocabulary and procurement-triggered addendum applicability.
- Reassess `22-layer` readiness only after stronger public threshold authority exists for the exact claim class.

## Source Links

- https://www.electronics.org/TOC/IPC-A-600K-EN_TOC.pdf
- https://www.electronics.org/TOC/IPC-6011A_TOC.pdf
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://www.electronics.org/news-release/ipc-releases-ipc-6012em-medical-applications-addendum-ipc-6012e-qualification-and
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-e/english-0
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-f/english-0
- https://www.electronics.org/TOC/IPC-6012FA-TOC.pdf
- https://shop.electronics.org/taxonomy/term/792
- https://www.electronics.org/TOC/IPC-6012FS_TOC.pdf
