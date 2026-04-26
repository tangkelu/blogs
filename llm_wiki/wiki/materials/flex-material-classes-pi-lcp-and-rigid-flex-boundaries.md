---
topic_id: "materials-flex-material-classes-pi-lcp-and-rigid-flex-boundaries"
title: "Flex Material Classes: PI, LCP, And Rigid-Flex Boundaries"
category: "materials"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "materials-flex-polyimide-and-lcp-class-source-coverage"
source_ids:
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "panasonic-felios-series-page"
  - "panasonic-felios-lcp-page"
tags: ["materials", "flex-pcb", "rigid-flex", "polyimide", "lcp", "felios"]
---

# Definition

> Flex-material governance means keeping `polyimide`, `LCP`, `flex PCB`, and `rigid-flex` in the right buckets. Material class, board architecture, and current property data are related, but they are not interchangeable claims.

## Why This Topic Matters

- HIL/APT already use flex and rigid-flex service language, so prompt consumers need a page that separates material class from board form factor.
- Panasonic FELIOS and FELIOS LCP now give the wiki official flexible-material anchors for both generic flex family framing and LCP-specific context.
- The main risk is collapsing `PI`, `LCP`, and `rigid-flex` into a single vague "flex material" story with unstated numeric assumptions.

## Stable Facts

- HIL/APT non-blog pages include flex PCB and rigid-flex PCB service contexts.
- Panasonic's FELIOS series page provides official flexible circuit-board material family context.
- Panasonic's FELIOS LCP page provides official LCP flexible circuit-board material context.
- These sources support class-level framing for flex material choices, especially when distinguishing generic flexible materials from LCP-specific discussion.

## Engineering Boundaries

- Use `polyimide` and `LCP` as material-class labels, not as proof of a particular board architecture.
- Use `rigid-flex` as an architecture/manufacturing context, not as a material name.
- Keep bend reliability, copper type, adhesiveless construction, Dk, loss, thickness, and cycle-life claims behind current product data.
- Do not assume Panasonic FELIOS is the exact material source used in HIL/APT builds unless separately evidenced.
- Treat any RF/mobile performance claim for LCP as refresh-required unless backed by current supplier material data.

## Common Misreadings

- `Flex PCB` is not the same thing as `polyimide`.
- `Rigid-flex` is not a material class.
- `LCP` is not a universal replacement for all flex materials.
- A flexible-material family page does not provide qualification, bend-cycle, or IPC acceptance data by itself.

## Must Refresh Before Publishing

- Any bend-radius or bend-cycle statement
- Any Dk, loss, or thickness value
- Any claim about adhesive versus adhesiveless constructions
- Any statement that names a specific Panasonic grade or current lineup
- Any comparison that turns flex-material classes into fixed performance rankings

## Related Fact Cards

- `materials-flex-polyimide-and-lcp-class-source-coverage`

## Primary Sources

- /code/hileap/frontendHIL/public/static/products/en/flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/rigid-flex-pcb.json
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/lineup/felios-series
- https://industrial.panasonic.com/ww/products/pt/felios/felioslcp
