---
fact_id: "methods-parameter-scope-rigid-flex-bend-guidance"
title: "Rigid-flex bend ratios are design-guide context, not universal acceptance thresholds"
topic: "Rigid-flex bend guidance parameter scope"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "minco-flex-circuits-design-guide-2019"
  - "minco-designing-flex-circuit-for-flexibility"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "ipc-6013e-toc"
tags: ["rigid-flex", "flex", "bend-radius", "bend-ratio", "static-bend", "dynamic-flex", "parameter-scope"]
---

# Canonical Summary

> Public design guides can support bend-ratio discussion for flex and rigid-flex articles, but bend ratios must stay scoped to design guidance, circuit thickness, layer count, bend type, and manufacturer review. They are not universal acceptance thresholds, cycle-life guarantees, or HIL/APT capability promises.

## Source-Backed Guidance

- Minco defines bend ratio as the ratio of bend radius to circuit thickness.
- Minco's flexibility guide gives example minimum bend ratios of `10:1` for single-layer circuits, `10:1` for double-sided circuits, and `20:1` for multilayer circuits in static applications intended to be bent once for installation.
- Minco's flex-circuit design guide gives standard design recommendations of `12 x circuit thickness` for double-layer flex and `24 x circuit thickness` for multilayer flex, and notes circuit thickness is approximately `0.006 in / 0.150 mm` per layer.
- Minco's design guide says tighter reliable bend radii can be possible with specialized factory forming when the circuit is flexed only one time, but this should not be generalized.
- Minco's design guidance also points to reducing flex-area thickness, using adhesiveless base materials, avoiding copper plating on conductors in the flex area, balancing conductor weights around the neutral bend axis, and considering unbonded flexible substrates as reliability-oriented design strategies.
- Internal APT/HIL rigid-flex pages support the need for bend-zone and transition-zone review, but their page claims remain public-site/internal-site context rather than independent mechanical proof.
- Public `IPC-6013E` metadata supports the existence of a flex/rigid-flex performance-specification family; it does not expose reusable threshold tables.

## Conditions And Methods

- Use this card when a draft needs to explain why flex thickness, layer count, bend type, forming, coverlay, adhesive, and copper layout matter.
- Keep Minco ratios attached to Minco design-guide context.
- Treat static bend, bend-to-install, dynamic flex, and repeated-motion designs as different cases.
- Pair this card with exact material cards only when material examples are needed; material cards do not prove bend life.

## Limits And Non-Claims

- This card does not authorize a universal bend-radius table for all flex or rigid-flex boards.
- It does not prove cycle-life, survival count, transition-zone tolerance, Class 3 acceptance, IPC-6013 compliance, or released-lot status.
- It does not turn Minco design guidance into HIL/APT manufacturing capability, customer acceptance, or warranty language.
- It does not make flex-only guidance automatically valid for all rigid-flex constructions.

## Blog Usage

- Supports `14-layer`, rigid-flex, flex PCB, medical/wearable, industrial-control, and compact-assembly drafts as design-review guidance.
- Use wording such as `design-guide example`, `bend ratio depends on circuit thickness`, `static and dynamic bend cases must be separated`, and `manufacturer review is required for tighter bends`.
- Avoid wording such as `guaranteed bend life`, `IPC requires this exact ratio` unless a licensed standard or project-specific authority is attached.

## Source Links

- https://www.minco.com/wp-content/uploads/Minco-Flex-Circuits-Design-Guide-2019.pdf
- https://www.minco.com/wp-content/uploads/Designing-a-Flex-Circuit-for-Flexibility.pdf
- /code/hileap/frontendAPT/public/static/pcb/en/rigid-flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- https://www.ipc.org/TOC/IPC-6013E-EN_TOC.pdf
