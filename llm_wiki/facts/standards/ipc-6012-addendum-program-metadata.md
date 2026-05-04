---
fact_id: "standards-ipc-6012-addendum-program-metadata"
title: "Public IPC-6012 addendum metadata supports program-specific medical, automotive, and space-military framing for rigid boards, not reusable acceptance tables"
topic: "IPC-6012 addendum program metadata"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "ipc-6011a-toc"
  - "ipc-6012f-release"
  - "ipc-6012f-toc"  # refreshed 2026-05-03
  - "ipc-6012em-medical-addendum-release"
  - "ipc-6012em-medical-addendum-page"
  - "ipc-6012fa-automotive-addendum-page"
  - "ipc-6012fa-toc"
  - "ipc-6012fs-space-military-addendum-page"
  - "ipc-6012-addendum-taxonomy-page"
  - "ipc-6012fs-toc"
tags: ["ipc", "ipc-6012", "ipc-6012em", "ipc-6012fa", "ipc-6012fs", "medical", "automotive", "space", "military", "class-3", "metadata"]
---

# Canonical Summary

> Public IPC metadata is now strong enough to support a clearer rigid-board program hierarchy in `llm_wiki`: `IPC-6011A` as the generic printed-board framework for the broader `IPC-601X` family, `IPC-6012F` as the current rigid printed-board base specification, `IPC-6012EM` as a medical-applications addendum layer, `IPC-6012FA` as an automotive-applications addendum layer, and `IPC-6012FS` as a current space/military avionics addendum layer. These public sources still do not expose reusable acceptance thresholds or test tables.

## Stable Facts

- IPC publicly identifies `IPC-6011A` as the generic performance specification for printed boards associated with the `IPC-601X` series and publicly states that procurement documentation defines product class and any exceptions.
- IPC publicly identifies `IPC-6012F` as the current rigid printed-board qualification and performance specification and explicitly frames it as the base document for medical, military/space, and automotive addenda.
- IPC's public `IPC-6012EM` release and product metadata show that medical rigid-board work may invoke a dedicated medical addendum layer rather than relying on generic `Class 3` vocabulary alone.
- IPC publicly states that `IPC-6012EM` applies when required by procurement documentation/drawings, which makes it a program-triggered addendum rather than a default rule set for every rigid printed board.
- IPC's public `IPC-6012FA` product metadata and TOC show that automotive rigid-board work may also invoke a dedicated addendum layer tied to procurement documentation rather than defaulting to generic `IPC-6012F` wording alone.
- The public `IPC-6012FA` TOC shows that the automotive addendum is not standalone, supplements `IPC-6012F`, and publicly exposes clause-family coverage for automotive application requirements, solder mask thickness methodology, technical cleanliness, and qualification/reliability test sections without exposing the controlled criteria themselves.
- IPC's public `IPC-6012FS` product metadata shows that the current space/military avionics addendum provides exceptions to `IPC Performance Class 3` requirements of `IPC-6012F` and supersedes `IPC-6012ES`.
- IPC's public `IPC-6012` addendum taxonomy page shows that the base rigid-board specification now sits inside a broader addendum family that includes medical, space/military, and automotive branches rather than one flat `Class 3` namespace.
- The public `IPC-6012FS` TOC shows that the addendum touches clause families including annular ring, bow and twist, plating integrity, hole copper plating, plated copper filled vias, electrical continuity/isolation, thermal shock, destructive physical analysis, and repair.
- The public `IPC-6012FS` TOC also explicitly states that the addendum is not a standalone document and applies with procurement-document precedence over the base standard where invoked.

## Conditions And Methods

- Use this card when a `22-layer` or other hi-rel rigid-board draft needs to distinguish generic `IPC-6012` / `Class 3` framing from program-specific medical, automotive, or space/military addendum framing.
- Use this card when a `22-layer` or other hi-rel rigid-board draft needs to distinguish the generic `IPC-601X` framework layer from sectional rigid-board and addendum layers.
- Pair it with the existing hi-rel program, traceability, configuration-control, and FDA cards before making any statement about regulated-program scope or documentation burden.
- Use this card to support wording such as `program-specific addendum`, `procurement-triggered requirements`, `space/military avionics addendum`, `medical applications addendum`, or `automotive applications addendum`.

## Limits And Non-Claims

- This card does not provide annular-ring values, plating-thickness minima, bow/twist limits, thermal-cycle counts, sample sizes, test frequencies, or any other acceptance thresholds.
- It does not turn `IPC-6011A` quality-assurance headings into reusable lot-acceptance, sampling, or conformance-testing rules.
- It does not turn the IPC addendum taxonomy/listing page into proof of technical coverage, current customer applicability, or a free substitute for paid addendum text.
- It does not prove that any supplier is approved, compliant, certified, or qualified under `IPC-6012EM`, `IPC-6012FA`, or `IPC-6012FS`.
- It does not justify rewriting public addendum metadata into universal rules for all `22-layer` boards.

## Open Questions

- Reassess `22-layer` readiness only after current public addendum metadata is integrated with any future supplier-evidence layer or stronger official qualification-program evidence.

## Source Links

- https://www.electronics.org/TOC/IPC-6011A_TOC.pdf
- https://www.ipc.org/news-release/ipc-releases-ipc-6012f-qualification-and-performance-specification-rigid-printed
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://www.electronics.org/news-release/ipc-releases-ipc-6012em-medical-applications-addendum-ipc-6012e-qualification-and
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-e/english-0
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-f/english-0
- https://www.electronics.org/TOC/IPC-6012FA-TOC.pdf
- https://shop.electronics.org/ipc-6012/ipc-6012-addendum/Revision-f/english
- https://shop.electronics.org/taxonomy/term/792
- https://www.electronics.org/TOC/IPC-6012FS_TOC.pdf
