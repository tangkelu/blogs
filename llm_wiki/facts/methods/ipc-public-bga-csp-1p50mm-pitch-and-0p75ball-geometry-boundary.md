---
fact_id: "methods-ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary"
title: "Public IPC BGA/CSP guidance supports a narrow 1.50/1.27 mm pitch to nominal-ball and land-pattern-geometry boundary, not a universal exact row"
topic: "IPC public BGA/CSP 1.50/1.27 mm pitch and 0.75 mm ball geometry boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-11"
exact_data_class: "boundary_convention"
scope_type: "ipc_public_bga_pitch_variation_and_land_pattern_geometry_boundary"
canonical_unit_policy: "Preserve the IPC paper's pitch, nominal-ball, land-diameter, and solder-mask-opening wording as a public technical-paper boundary. Do not normalize this into a universal 1.50 mm pitch conversion table or a formal IPC-7095 public exact row."
source_ids:
  - "ipc-bga-csp-technology-paper-1p50mm-pitch-and-0p75ball-geometry"
tags: ["ipc", "bga", "csp", "1.50-mm-pitch", "1.27-mm-pitch", "0.75-mm-ball", "land-pattern", "mask-opening", "boundary"]
---

# Canonical Summary

> The public IPC-hosted paper `Principles for Implementing BGA and CSP Technology` is strong enough to support one narrow standards-adjacent geometry boundary for the `PCB资料` `1.50 mm` lane: the local corpus may state that the visible `1.50 / 1.27 mm` pitch family maps to nominal `0.75 mm` ball class in the paper, and that the same public paper exposes round-land geometry guidance with visible `0.75 mm` ball example values. This is stronger than metadata-only family framing, but it is still not a formal public IPC standard row and it does not authorize a universal `1.50 mm pitch -> land pattern` rule.

## Stable Facts

- The public IPC paper lists JEDEC optional BGA contact-pitch variations including:
  - `1.50 mm`
  - `1.27 mm`
  - `1.0 mm`
  - `0.8 mm`
  - `0.75 mm`
  - `0.65 mm`
  - `0.5 mm`
- The same public table maps the `1.50 / 1.27 mm` pitch family to nominal `0.75 mm` ball diameter.
- The paper states that BGA land-pattern geometry is typically:
  - `round`
  - adjusted for `pitch`
  - adjusted for `size variation`
- The public `0.75 mm` ball example in the paper exposes:
  - nominal land diameter `0.55`
  - land variation `0.60 to 0.50`
  - solder-mask opening `0.85 to 0.90`

## Conditions And Methods

- Use this card when a prompt needs public IPC-hosted geometry support above metadata-only `1.50 mm` family framing.
- Use it to explain that the current public non-owner chain can safely be written as:
  - `1.50 / 1.27 mm` pitch family exists in public IPC-hosted BGA/CSP guidance
  - that public guidance maps the family to nominal `0.75 mm` ball class
  - that the same public paper exposes round-land and mask-opening example geometry for that nominal ball class
- Pair this card with:
  - [iec-square-bga-1mm-or-larger-outline-and-variation-boundary.md](/code/blogs/llm_wiki/facts/methods/iec-square-bga-1mm-or-larger-outline-and-variation-boundary.md)
  - [iec-area-array-land-pattern-geometry-family-boundary.md](/code/blogs/llm_wiki/facts/methods/iec-area-array-land-pattern-geometry-family-boundary.md)
  - [nxp-1p50mm-bga225-reflow-footprint.md](/code/blogs/llm_wiki/facts/methods/nxp-1p50mm-bga225-reflow-footprint.md)
  - [renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md](/code/blogs/llm_wiki/facts/methods/renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md)
  - [amd-bg225-bgg225-1p50mm-bga-footprint-row.md](/code/blogs/llm_wiki/facts/methods/amd-bg225-bgg225-1p50mm-bga-footprint-row.md)
- Keep this card inside `public IPC technical-paper geometry boundary` scope only.

## Safe Blog Usage

- Explain that public IPC-hosted material exposes more than mere standards existence for coarse-pitch BGA work.
- Explain that one public IPC paper visibly links `1.50 / 1.27 mm` pitch to nominal `0.75 mm` ball class and to round-land geometry logic.
- Explain that the visible geometry values remain standards-adjacent public guidance, not a universal exact replacement row for every `1.50 mm` package.

## Limits And Non-Claims

- This card does not authorize a formal public `IPC-7095A` exact table row.
- It does not authorize one universal `1.50 mm` BGA pad-diameter rule across all vendors and package families.
- It does not authorize direct closure of the handbook `1.50 mm` row without package-owner or paid-standard context.
- It does not prove that every `1.50 mm` package should reuse the same `0.55` land diameter or `0.85 to 0.90` solder-mask opening.

## Relationship To Local PCB资料 Intake

- This card raises the `1.50 mm` lane above `IEC metadata + family framing + owner exact rows only` by adding one public IPC-hosted geometry surface.
- It gives the repo a cleaner non-owner explanation for why `1.50 / 1.27 mm` pitch can be discussed together with nominal `0.75 mm` ball and round-land geometry.
- It still does not close the blocked handbook `1.50 mm` row as a universal public standard replacement.

## Source Links

- https://www.ipc.org/system/files/technical_resource/E31%26S01-4_Solberg.pdf
