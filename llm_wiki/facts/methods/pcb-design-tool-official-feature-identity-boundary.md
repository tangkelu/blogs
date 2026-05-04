---
fact_id: "methods-pcb-design-tool-official-feature-identity-boundary"
title: "PCB design-tool drafts can cite official feature identity, but not rankings, pricing, or recommendation claims"
topic: "PCB design tool official feature identity boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-29"
source_ids:
  - "kicad-official-pcb-design-suite-page"
  - "autodesk-eagle-fusion-features-page"
  - "autodesk-eagle-subscription-faq"
  - "autodesk-fusion-pcb-design-software-page"
tags: ["pcb-design-tool", "eda", "kicad", "autodesk", "eagle", "fusion", "tool-comparison-boundary"]
---

# Canonical Summary

> Official KiCad and Autodesk pages support dated, vendor-scoped feature identity for PCB design tools. They do not support neutral "best tool" rankings, pricing advice, licensing generalizations, feature-parity claims, or recommendations for a specific user without a dated requirements and source pack.

## Stable Facts

- The official KiCad page identifies KiCad as a cross-platform, open-source PCB design suite.
- The official KiCad page supports feature vocabulary for schematic capture, PCB layout, integrated SPICE simulation, electrical rules checking, and 3D viewer context.
- Autodesk's EAGLE / Fusion features page supports feature vocabulary for schematic editing, PCB layout, routing, design-rule checking, libraries, and 3D PCB model context.
- Autodesk's PCB design software page supports Autodesk Fusion workflow vocabulary across schematic design, PCB layout, validation, ECAD-MCAD context, and manufacturing handoff.
- Autodesk's EAGLE subscription FAQ states, as checked on `2026-04-29`, that EAGLE is available with Autodesk Fusion and that Autodesk will no longer sell or support EAGLE effective `2026-06-07`.

## Conditions And Methods

- Use this card for `kicad-vs-eagle.md`, `pcb-design-tools.md`, and adjacent EDA-tool drafts when the article needs official feature identity.
- Date any EAGLE availability or support statement and refresh after `2026-06-07`.
- Keep vendor pages as vendor claims. For neutral recommendations, add independent requirements, current pricing/licensing evidence, version-specific feature checks, and a dated methodology.
- Separate tool feature identity from fabrication readiness: using a tool does not prove the exported package is complete or manufacturable.
- Pair this card with `methods-cam-data-exchange-format-boundary` when the topic moves from design tools to manufacturing-file handoff.

## Limits And Non-Claims

- This card does not say KiCad, EAGLE, or Fusion is better, easier, cheaper, more professional, or more suitable for beginners or teams.
- It does not freeze current prices, licensing terms, cloud requirements, platform support, feature depth, library completeness, or version cadence.
- It does not support current "best PCB design software" rankings.
- It does not prove a tool's DFM output quality, CAM acceptance, Gerber correctness, or manufacturing success.

## Open Questions

- Add official Altium, Cadence, Siemens, EasyEDA, or LibrePCB source cards only if future drafts need those tools.
- Add a dated tool-comparison methodology before publishing recommendation or ranking content.

## Source Links

- https://www.kicad.org/
- https://www.autodesk.com/products/eagle/features
- https://www.autodesk.com/solutions/eagle-subscription-faq
- https://www.autodesk.com/solutions/pcb-design-software
