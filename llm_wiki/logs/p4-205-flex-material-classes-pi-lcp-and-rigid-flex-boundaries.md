---
task_id: "P4-205"
title: "Flex material classes: PI, LCP, and rigid-flex boundaries"
status: "completed"
owner: "codex"
lane: "flex-material-class-promotion"
started_at: "2026-05-03"
completed_at: "2026-05-03"
write_scope:
  - "/code/blogs/llm_wiki/wiki/materials/flex-material-classes-pi-lcp-and-rigid-flex-boundaries.md"
  - "/code/blogs/llm_wiki/logs/p4-205-flex-material-classes-pi-lcp-and-rigid-flex-boundaries.md"
blocked_claims:
  - "bend-cycle guarantees"
  - "Dk / Df claims without datasheet support"
  - "architecture-to-material substitution claims"
  - "cost, lead-time, and yield claims"
status_history:
  - status: "in_progress"
    at: "2026-05-03"
    note: "Read ASSESSMENT, target wiki, material fact cards, and IPC flex/rigid-flex hierarchy boundary."
  - status: "completed"
    at: "2026-05-03"
    note: "Promoted target wiki from draft to active routing page using local fact coverage only."
---

# Execution Summary

## Inputs Read

- `ASSESSMENT.md`
- `wiki/materials/flex-material-classes-pi-lcp-and-rigid-flex-boundaries.md`
- `facts/materials/flex-polyimide-and-lcp-class-source-coverage.md`
- `facts/materials/flex-exact-product-anchor-map.md`
- `facts/standards/ipc-flex-rigid-flex-standards-hierarchy-boundary.md`

## Changes Landed

- Reframed the page as an `active` routing surface instead of a descriptive draft.
- Added an explicit classification matrix separating:
  - `PI` as material class
  - `LCP` as material class
  - `FRCC` as narrow material/form-factor lane
  - `rigid-flex` as architecture class
- Preserved exact-product anchor boundaries for `UPILEX-S`, `Kapton HN`, `85N`, `85NT`, `N7000-3F`, `R-F705S`, and `R-FR10`.
- Added prompt-routing and stop-line language so downstream agents do not collapse architecture into material identity.
- Kept all blocked claim classes explicit.

## Residual Risks

- The corpus still does not support reusable bend-radius or bend-cycle rules.
- `FRCC` remains Panasonic-centric and should not be generalized beyond the exact-product branch without new facts.
- `LCP` and `PI` remain class routes; comparative performance writing still needs exact-product datasheet support.
