---
fact_id: "methods-14-layer-rigid-flex-reliability-numeric-boundary"
title: "14-layer rigid-flex planning sources do not authorize bend, transition, or life-cycle numeric tables"
topic: "14-layer rigid-flex reliability numeric boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendapt-rigid-flex-pcb-capability-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendapt-flex-pcb-capability-page-en"
  - "frontendapt-pcba-flex-rigid-flex-page-en"
  - "ipc-6013e-toc"
  - "ipc-microvia-reliability-warning-2019"
tags: ["14-layer", "rigid-flex", "bend-radius", "cycle-life", "transition-zone", "boundary", "gap-control"]
---

# Canonical Summary

> Current rigid-flex, flex, and assembly-planning sources are strong enough to support guarded `14-layer` wording around branch selection, transition review, coverlay/stiffener coordination, and bend-sensitive process planning. They are not strong enough to authorize bend-radius tables, flex-life cycles, transition-tolerance numerics, or rigid-flex recipe defaults.

## Stable Facts

- A conservative `14-layer` rewrite may state that rigid-flex should be treated as a separate construction route rather than as a minor extension of the baseline rigid stackup.
- Internal rigid-flex and flex pages support guarded wording that bend-sensitive builds require coordinated material, coverlay, stackup, and assembly review.
- Internal rigid-flex capability-family pages support workflow language around branch scoping, transition handling, and special-process planning.
- The internal flex-rigid-flex assembly page supports the idea that tooling, stiffeners, placement control, and assembly-stage handling can affect reliability posture.
- Public `IPC-6013E` metadata supports the existence of a flex/rigid-flex qualification family, not reusable mechanical threshold tables.
- IPC's public microvia-reliability warning supports caution language that complex interconnect structures can fail outside simplistic acceptance assumptions.
- These sources can support statements such as `review the transition zone separately`, `bend-sensitive architecture changes the process route`, and `rigid-flex needs dedicated manufacturability review`.
- These sources cannot support bend-radius thresholds, cycle-life counts, neutral-axis recipes, transition-zone tolerances, dynamic-bend guarantees, or default `14R-4F` style cookbook constructions.

## Conditions And Methods

- Use this card when a `14-layer` draft mentions rigid-flex, dynamic bend, bend radius, flex life, transition zones, stiffeners, or reliability tables.
- Pair this card with `facts/methods/rigid-flex-stackup-and-bend-reliability-posture.md`, `facts/standards/ipc-rigid-flex-and-microvia-reliability-metadata.md`, and `logs/p4-06-14-layer-evidence-pack.md`.
- Prefer wording such as `separate branch review`, `bend-sensitive process route`, `transition-zone review required`, and `reliability numerics require controlled authority`.
- Keep rigid-flex references attached to workflow and review posture, not to default mechanical-rule numerics.
- When bend cycles, bend radii, transition tolerances, or survival counts appear, require separate governed authority rather than inheriting them from branch-planning pages.

## Limits And Non-Claims

- This card does not authorize bend-radius tables, cycle-life tables, transition tolerances, coverlay-thickness ladders, or dynamic-bend guarantees.
- It does not authorize rigid-flex recipe defaults, survival counts, thermal-cycle counts, or mechanical acceptance criteria.
- It does not prove that any `14-layer` rigid-flex structure is qualified, reliable, or production-ready.
- It does not convert internal routing or assembly vocabulary into transferable reliability proof.

## Open Questions

- Add a narrower follow-on only if future work needs separate containment for `transition-zone geometry` versus `life-cycle reliability` leakage.
- Reassess only after a later source layer provides primary authority for the exact mechanical or reliability claim being proposed.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/rigid-flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/rigid-flex-pcb-capabilities.json
- /code/hileap/frontendAPT/public/static/pcb/en/flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/flex-pcb-capabilities.json
- /code/hileap/frontendAPT/public/static/pcba/en/flex-rigid-flex.json
- https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf
- https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high
