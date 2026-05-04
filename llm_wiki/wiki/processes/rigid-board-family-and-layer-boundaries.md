---
topic_id: "processes-rigid-board-family-and-layer-boundaries"
title: "Rigid Board Family And Layer Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "standards-rigid-board-family-identity-boundary"
  - "methods-pcb-prototype-quickturn-and-volume-routing"
  - "methods-pcb-stackup-special-process-and-baseline-families"
source_ids:
  - "ipc-6012f-toc"
  - "mil-prf-55110-general-spec-page"
  - "frontendhil-single-double-layer-pcb-product-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
tags: ["rigid-board", "baseline", "double-sided", "multilayer", "4-layer", "family-boundary", "stackup-routing", "processes"]
---

# Routing Summary

> Rigid-board family routing should separate baseline low-layer boards from multilayer rigid boards before any stackup, capability, or commercial language appears. The active process boundary is simple: single-sided and double-sided boards stay in the baseline rigid-board family, while 4-layer boards and above belong to the multilayer rigid-board family. That family split is not the same thing as a stackup recipe, capability proof, or supplier recommendation.

## Family Boundary Map

| Board Family | Safe Identity | What Changes Next |
|---|---|---|
| single-sided / double-sided rigid board | baseline low-layer rigid-board branch | routing complexity, plated-through-hole context, later routing-mode choice |
| 4-layer and above rigid board | multilayer rigid-board branch | stackup architecture, registration, via strategy, impedance and lamination planning |

## What This Page Governs

- Use this page when a draft needs to place a rigid board into the correct family before discussing process details.
- Keep family identity separate from stackup design.
- Keep family identity separate from prototype, quick-turn, NPI, or volume route selection.
- Keep family identity separate from manufacturer selection, quote framing, or commercial comparison.

## Baseline Low-Layer Branch

- Single-sided and double-sided rigid boards belong to the baseline rigid-board branch.
- Double-sided boards may still require plated-through-hole interconnection and process review.
- Baseline does not mean trivial, low-quality, or universally sufficient.
- This branch should be described as lower-complexity relative to multilayer work, not as universally simple.

## Multilayer Rigid-Board Branch

- A 4-layer board belongs to the multilayer rigid-board family, not to the single/double-sided baseline branch.
- Multilayer routing is the point where stackup architecture, registration control, via planning, and impedance posture become more prominent.
- Multilayer identity alone does not prove HDI, backdrill, low-loss materials, or advanced special-process requirements.

## Separation Rules

### Family Boundary vs Stackup

- Family identity tells you which branch the board belongs to.
- It does not tell you the default stackup, plane assignment, impedance structure, or lamination recipe.
- Move to stackup planning only after the family branch is fixed.

### Family Boundary vs Capability

- Family identity does not prove current manufacturing thresholds.
- Family identity does not prove one shop can build every board in that family.
- Family identity does not prove qualification, reliability, or repeatability outcomes.

### Family Boundary vs Commercial Framing

- Do not translate the baseline-versus-multilayer split into `best manufacturer`, `top supplier`, or recommendation language.
- Do not turn family identity into quote-speed, lead-time, MOQ, or price posture.
- Do not imply that being strong in double-sided work proves multilayer strength, or the reverse.

## Safe Prompting Rules

- If the draft says `double-sided`, route it into the baseline rigid-board branch first.
- If the draft says `4-layer`, route it into the multilayer rigid-board branch first.
- If the draft starts asking about stackup, impedance, or lamination, leave this page and route into stackup-planning facts.
- If the draft starts asking who is best, fastest, cheapest, or most reliable, stop: that is outside this page.

## Blocked Claims

- exact capability guarantees
- yield and reliability guarantees
- supplier-proof claims
- cost/lead-time/yield claims

## Non-Claims And Stop Lines

- This page does not provide exact capability guarantees.
- This page does not prove yield or reliability outcomes.
- This page does not provide supplier-proof claims.
- This page does not support cost, lead-time, or yield claims.
- This page does not authorize default 4-layer stackups, impedance geometry, thermal outcomes, or commercial ranking language.

## Related Fact Cards

- `standards-rigid-board-family-identity-boundary`
- `methods-pcb-prototype-quickturn-and-volume-routing`
- `methods-pcb-stackup-special-process-and-baseline-families`
