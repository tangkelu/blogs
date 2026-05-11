---
fact_id: "standards-ipc-flex-printed-board-type-taxonomy-boundary"
title: "IPC publicly separates single-sided, double-sided, multilayer flex, and rigid-flex board types as structure taxonomy, not as material or rule closure"
topic: "IPC flex printed board type taxonomy boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-09"
source_ids:
  - "ipc-2223e-toc"
  - "ipc-6013e-toc"
  - "ipc-2223e-flex-rigid-flex-design-standard-page"
tags: ["ipc", "ipc-2223", "ipc-6013", "flex", "fpc", "rigid-flex", "type-taxonomy", "single-sided", "double-sided", "multilayer"]
---

# Canonical Summary

> IPC's public flex standards metadata is strong enough to support one narrow taxonomy card for the `E6` article lane: the public IPC sources separate `Type 1` single-sided flexible printed boards, `Type 2` double-sided flexible printed boards, `Type 3` multilayer flexible printed boards, `Type 4` multilayer rigid-flexible printed boards, and `Type 5` flexible or rigid-flexible printed boards without plated through holes. This public layer is safe for structure-family naming and routing only. It does not authorize bend-radius rules, material-stack defaults, layer-limit claims, or supplier capability claims.

## Stable Facts

- IPC publicly identifies `IPC-2223E` as a sectional design standard for flexible and rigid-flexible printed boards.
- The public `IPC-2223E` TOC exposes `Type 1 Single-Sided Flexible Printed Boards` as a visible design-side board-type heading.
- The public `IPC-6013E` TOC publicly names these board families:
  - `Type 1 - Single-Sided Flexible Printed Boards`
  - `Type 2 - Double-Sided Flexible Printed Boards`
  - `Type 3 - Multilayer Flexible Printed Boards`
  - `Type 4 - Multilayer Rigid-Flexible Printed Boards`
  - `Type 5 - Flexible or Rigid-Flexible Printed Boards without Plated Through Holes`
- These public IPC records support treating `rigid-flex` as a distinct structure family rather than as a synonym for every multilayer `FPC`.

## Conditions And Methods

- Use this card when a draft needs standards-backed naming for `single-sided`, `double-sided`, `multilayer flex`, or `rigid-flex` board families.
- Use this card to separate board-construction taxonomy from material-class language such as `PI`, `LCP`, or `FRCC`.
- Pair this card with material cards or vendor design guides if the draft needs laminate choice, bend behavior, or stack details.
- Keep `Type 5` scoped to the visible public wording only; do not infer extra plated-hole design rules from the title alone.

## Safe Blog Usage

- Explain that public IPC standards metadata already distinguishes multiple flex-board structure families instead of treating all `FPC` builds as one category.
- Explain that `rigid-flex` is a structure class with its own type identity, not just another name for ordinary multilayer flex.
- Explain that a comparison such as `single-layer vs double-layer vs multilayer FPC` is safe only at taxonomy and tradeoff-direction level unless stronger design guidance is added.

## Limits And Non-Claims

- This card does not provide bend-radius values, bend-cycle counts, copper-type rules, coverlay defaults, adhesive-system rules, conductor geometry, or via-design thresholds.
- It does not prove any universal layer-count limit for commercial `FPC` production.
- It does not prove HIL, APT, or any other supplier capability, quality level, lead time, or cost posture.
- It does not convert article diagrams into standards-backed dimensional guidance.

## Relationship To Local PCB资料 Intake

- This card advances `单层双面多层FPC有何区别？.pdf` from `claim_family_level_only` to one narrow `official_fact-backed` surface for structure taxonomy only.
- It does not promote the same PDF's material comparisons, manufacturability judgments, or any hidden numeric defaults.
- It keeps the rest of `E6` package, BOM, procurement, and `0R` subfamilies on their existing routed or hold-only boundaries.

## Source Links

- https://www.electronics.org/TOC/IPC-2223E-toc.pdf
- https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf
- https://shop.electronics.org/ipc-2223/ipc-2223-standard-only/Revision-e/english
