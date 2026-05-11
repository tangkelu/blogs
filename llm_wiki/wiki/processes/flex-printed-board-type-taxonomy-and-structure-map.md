---
topic_id: "processes-flex-printed-board-type-taxonomy-and-structure-map"
title: "Flex Printed Board Type Taxonomy And Structure Map"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-09"
fact_ids:
  - "standards-ipc-flex-printed-board-type-taxonomy-boundary"
  - "standards-ipc-flex-rigid-flex-standards-hierarchy-boundary"
  - "materials-flex-polyimide-and-lcp-class-source-coverage"
source_ids:
  - "ipc-2223e-toc"
  - "ipc-6013e-toc"
  - "ipc-2223e-flex-rigid-flex-design-standard-page"
tags: ["flex", "fpc", "rigid-flex", "type-taxonomy", "structure", "ipc", "processes"]
---

# Routing Summary

> Route `single-sided`, `double-sided`, and `multilayer flex` as structure-family terms first. Route `rigid-flex` as a separate hybrid board-construction family, not as a generic synonym for multilayer `FPC`. Keep material-class wording such as `PI`, `LCP`, and `FRCC` on a different authority layer.

## Quick Classification Matrix

| Term | Route As | Safe Use | Do Not Collapse Into |
| --- | --- | --- | --- |
| `single-sided FPC` | structure family | one conductive-layer flex-board taxonomy | bend-rule closure, material choice |
| `double-sided FPC` | structure family | two-sided flex-board taxonomy | rigid-flex, capability proof |
| `multilayer FPC` | structure family | multi-layer flex-board taxonomy | every rigid-flex build |
| `rigid-flex` | hybrid structure family | rigid plus flexible zone architecture | pure flex material class |
| `PI` / `LCP` / `FRCC` | material class | laminate or film identity | board-type taxonomy |

## What This Page Governs

- Use this page when a prompt or article compares `单层`, `双面`, and `多层 FPC`.
- Use this page when a draft starts treating `rigid-flex` as just another word for `multilayer flex`.
- Use this page to keep board-type taxonomy separate from material, bend, and supplier-capability claims.

## Public IPC Type Surface

The current public IPC layer is strong enough to support these structure families:

- `Type 1 - Single-Sided Flexible Printed Boards`
- `Type 2 - Double-Sided Flexible Printed Boards`
- `Type 3 - Multilayer Flexible Printed Boards`
- `Type 4 - Multilayer Rigid-Flexible Printed Boards`
- `Type 5 - Flexible or Rigid-Flexible Printed Boards without Plated Through Holes`

This is a taxonomy surface, not a full design-rule surface.

## Safe Prompting Rules

- If the draft says `FPC`, first decide whether it means a structure family or a material family.
- If the draft says `multilayer FPC`, do not silently upgrade it into `rigid-flex`.
- If the draft says `rigid-flex`, keep the next authority step in construction, design-standard, and performance-specification language.
- If the draft starts asking about bend radius, coverlay, adhesive, copper type, or stiffener rules, stop using this page alone and add stronger primary guidance.

## Non-Claims And Stop Lines

- This page does not provide bend-radius values or bend-life claims.
- This page does not provide universal layer-count ceilings.
- This page does not prove supplier process capability.
- This page does not provide material-stack defaults.

## Related Fact Cards

- `standards-ipc-flex-printed-board-type-taxonomy-boundary`
- `standards-ipc-flex-rigid-flex-standards-hierarchy-boundary`
- `materials-flex-polyimide-and-lcp-class-source-coverage`

## Primary Sources

- https://www.electronics.org/TOC/IPC-2223E-toc.pdf
- https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf
- https://shop.electronics.org/ipc-2223/ipc-2223-standard-only/Revision-e/english
