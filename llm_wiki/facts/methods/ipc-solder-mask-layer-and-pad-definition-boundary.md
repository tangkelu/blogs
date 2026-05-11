---
fact_id: "methods-ipc-solder-mask-layer-and-pad-definition-boundary"
title: "IPC and official format-owner metadata support solder-mask layer identity and guarded pad-definition terminology, while NSMD/SMD and via-tenting definitions remain incomplete"
topic: "IPC solder mask layer and pad definition boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-09"
source_ids:
  - "ipc-t50-terms-and-definitions-toc"
  - "ipc-7093a-toc"
  - "ipc-6012f-release"
  - "ucamco-gerber-format-page"
  - "intel-an114-bga-land-pad-dimensions"
tags: ["ipc", "solder-mask", "solder-resist", "nsmd", "smd", "via-tenting", "pad-definition", "gerber", "manufacturing-data"]
---

# Canonical Summary

> Current repo-backed official coverage is strong enough to land one narrow terminology and boundary card for solder-mask handling. `Solder mask` is a real manufacturing-data layer family in released fabrication data, not just a visual design-canvas concept. Public IPC metadata also shows that solder-mask design, solder-mask-defined versus non-solder-mask-defined pad discussion, and via-tenting discussion belong to an IPC-controlled document family. However, the current public source layer is still not strong enough to publish exact IPC definitions or universal rules for `NSMD`, `SMD`, `via tenting`, or `solder mask bridge`.

## Stable Facts

- `IPC-T-50N` is the public IPC terminology-family anchor for interconnecting and packaging electronic-circuit vocabulary.
- Ucamco, as Gerber format owner, publicly treats `solder mask` as part of fabrication-data layer scope alongside copper, legend, drill, and route data.
- That format-owner layer is strong enough to support one manufacturing-data statement: solder-mask expression belongs in the released fabrication package, not only in canvas intent.
- The public `IPC-7093A` table of contents shows that IPC maintains a document family with chapter-level treatment of solder-mask design, solder-mask-defined versus non-solder-mask-defined pad topics, and tented-via / via-in-pad related discussion.
- The public `IPC-6012F` release page is strong enough to support one guarded standards-family statement: solder-mask-related treatment belongs to the rigid-board qualification and performance revision context, but exact requirements remain revision-sensitive and unpublished in public summary text.
- Intel AN 114 is strong enough to support vendor-scoped identity that `SMD` and `NSMD` are real land-pad distinction terms in manufacturer guidance.
- Intel AN 114 is not an IPC terminology source and must not be rewritten as universal cross-vendor or standards-owner truth.

## Conditions And Methods

- Use this card when a prompt needs guarded wording for `solder mask` as released manufacturing data.
- Use this card when a prompt needs guarded wording that `IPC` has a standards-family lane for solder-mask design and pad-definition topics.
- Use `NSMD` and `SMD` only as:
  - existing vendor-scoped land-pad distinction terms when explicitly tied to owner guidance such as Intel
  - not yet as repo-wide IPC-defined universal terminology
- Keep `via tenting`, `solder mask bridge`, `mask-defined`, and `non-solder-mask-defined` as controlled terminology gaps unless stronger public or licensed source text is recovered.
- Pair this card with:
  - [cam-data-exchange-format-boundary.md](/code/blogs/llm_wiki/facts/methods/cam-data-exchange-format-boundary.md)
  - [padstack-origin-pin1-and-footprint-review-governance-boundary.md](/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md)
- When exact land-pad geometry is needed, route to package-owner cards rather than this boundary:
  - [intel-bga-land-pad-guidelines-common-pitches-and-vbga.md](/code/blogs/llm_wiki/facts/methods/intel-bga-land-pad-guidelines-common-pitches-and-vbga.md)
  - [ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md](/code/blogs/llm_wiki/facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md)
  - [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md)

## Safe Blog Usage

- Explain that solder-mask data must be carried explicitly in the fabrication release package.
- Explain that solder-mask omission is a manufacturing-data completeness problem, not only a drawing-visibility problem.
- Explain that IPC has a standards-family context for solder-mask design and pad-definition topics.
- Explain that `SMD/NSMD` may be named as vendor-guideline vocabulary when tied to a named official owner source.
- Explain that exact pad-type selection, via-tenting rules, bridge rules, and opening geometry still need stronger evidence.

## Limits And Non-Claims

- This card does not provide exact IPC definitions for `mask-defined`, `non-solder-mask-defined`, `via tenting`, or `solder mask bridge`.
- It does not authorize opening-expansion values, bridge-width values, via-opening rules, or pad-type selection thresholds.
- It does not authorize universal statements that one pad-definition style is always preferred.
- It does not authorize acceptance criteria, workmanship criteria, or fabrication capability claims.
- It does not authorize tool-UI workflows, export recipes, checker sufficiency, or supplier-process guarantees.

## Open Questions

- Recover stronger public or licensed source text for exact `IPC` definitions of `mask-defined`, `non-solder-mask-defined`, `via tenting`, and `solder mask bridge`.
- Recover stronger official terminology support later if the corpus needs a reusable `NSMD/SMD` standards-owner normalization layer instead of vendor-scoped examples only.

## Source Links

- https://www.electronics.org/TOC/IPC-T-50N_TOC.pdf
- https://www.electronics.org/TOC/IPC-7093A.pdf
- https://www.ipc.org/news-release/ipc-releases-ipc-6012f-qualification-and-performance-specification-rigid-printed
- https://www.ucamco.com/en/gerber
- https://www.intel.co.jp/content/www/jp/ja/docs/programmable/683481/current/surface-land-pad-dimension
