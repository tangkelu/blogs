---
topic_id: "processes-rf-surface-finish-selection"
title: "RF Surface Finish Selection"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "methods-surface-finish-selection-for-rf"
  - "methods-selective-multi-finish-strategy"
  - "methods-finish-zoning-by-assembly-sequence-and-storage-exposure"
  - "methods-press-fit-finish-selection"
source_ids:
  - "frontendapt-pcb-surface-finishes-page-en"
  - "frontendhil-pcb-surface-finish-landing-en"
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-pcb-drilling-page-en"
  - "frontendapt-backplane-pcb-page-en"
tags: ["rf", "surface-finish", "enig", "enepig", "immersion-silver", "press-fit", "processes"]
---

# Definition

> RF surface finish selection is a board-level engineering decision that separates RF loss, wire-bond compatibility, contact wear, storage window, and connector insertion needs instead of treating finish as a default menu item.

## Why This Topic Matters

- RF and microwave boards often mix conflicting needs across RF pads, digital/control areas, wire-bond zones, and connector interfaces.
- Your internal non-blog pages already express a usable selection posture, but the logic was previously scattered across atomic fact cards.
- This topic page gives prompt writing and future blog drafting one stable aggregation point before pulling in standards metadata like `IPC-4552` or `IPC-4556`.

## Stable Facts

- Your current internal site content consistently frames `immersion silver` as the preferred option when RF insertion loss and PIM behavior matter most.
- The same internal content frames `ENIG` as the broad planar default when assembly robustness, solderability, and shelf-life practicality matter more than pushing the lowest RF conductor-surface loss.
- `ENEPIG` is consistently reserved for mixed-assembly cases, especially when soldering and wire bonding must coexist.
- Internal pages already imply that RF boards should not be forced into one finish when RF pads, digital/control pads, edge connectors, and wire-bond areas have different duties.
- Selective multi-finish support is already part of the internal process posture, including examples such as `ENIG + hard gold` and `OSP + ENEPIG`.
- Finish planning is repeatedly tied to assembly route, storage exposure, contact behavior, and connector mechanics, not only to nominal electrical category.
- `Press-fit` finish choice is an adjacent but important boundary case: the current internal posture places `immersion tin` first for press-fit insertion behavior, but only when hole control and connector integration are handled together.

## Engineering Boundaries

- Do not write "best finish for RF PCB" as if one finish fits all RF assemblies.
- Keep `RF pad loss`, `wire-bond need`, `storage window`, `contact wear`, and `assembly sequence` as separate decision axes.
- Treat selective multi-finish as a process-planning tool, not as a free option without masking, yield, and cost implications.
- Keep press-fit logic adjacent to RF finish discussions, but do not merge them into the same default rule set.
- If a page needs exact plating thickness, nickel-stack detail, shelf-life values, or IPC acceptance language, refresh from official standards or manufacturer/process documents first.

## Common Misreadings

- `Immersion silver` being low loss does not mean it is the universal finish for every RF board.
- `ENIG` being general-purpose does not mean it is electrically neutral in all high-GHz use cases.
- `ENEPIG` should not be described as a premium default if wire bonding or mixed assembly is not actually required.
- "Selective finish supported" does not mean every finish combination is cheap, simple, or production-neutral.
- `Press-fit finish` is not solved by finish chemistry alone; drilling and hole-tolerance control remain part of the same decision.

## Must Refresh Before Publishing

- Any exact IPC standard references or revision-level finish requirements
- Any numeric claim about shelf life, plating thickness, or current process-window limits
- Any claim that a given finish is "recommended" for a specific customer stack without checking the latest engineering review

## Related Fact Cards

- `methods-surface-finish-selection-for-rf`
- `methods-selective-multi-finish-strategy`
- `methods-finish-zoning-by-assembly-sequence-and-storage-exposure`
- `methods-press-fit-finish-selection`

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-surface-finishes.json
- /code/hileap/frontendHIL/data/service-landings/en/pcb-surface-finish.json
- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/antenna-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json
- /code/hileap/frontendAPT/public/static/pcb/en/backplane-pcb.json
