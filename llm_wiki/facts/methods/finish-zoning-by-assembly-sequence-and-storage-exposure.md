---
fact_id: "methods-finish-zoning-by-assembly-sequence-and-storage-exposure"
title: "Internal finish-selection logic already separates board zones by assembly path, storage window, and contact duty"
topic: "Finish zoning by assembly sequence and storage exposure"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcb-surface-finishes-page-en"
  - "frontendhil-pcb-surface-finish-landing-en"
  - "frontendapt-antenna-pcb-page-en"
tags: ["internal", "surface-finish", "zoning", "assembly-sequence", "storage", "methods"]
---

# Canonical Summary

> Your internal non-blog finish pages already support a zoning mindset: finish is not chosen once for the whole board by habit, but matched to how each area will be assembled, how long it may sit before use, and whether that area is for soldering, RF contact, wire bonding, or repeated insertion.

## Stable Facts

- The APT surface-finish page explicitly supports `selective finish application` when one finish cannot satisfy the whole board.
- The same APT page gives concrete mixed-finish examples such as `ENIG on SMD pads plus hard gold on edge fingers` and `OSP on general pads with ENEPIG on wire-bond areas`.
- The same APT page repeatedly separates finish choice by assembly behavior: fine-pitch SMT, wire bonding, press-fit insertion, RF loss, repeated reflow, and long storage are treated as different decision drivers.
- The APT finish page also ties finish choice to storage exposure, explicitly distinguishing longer-life finishes such as `ENIG / ENEPIG / LF-HASL` from shorter-life options such as `OSP`, `immersion silver`, and `immersion tin`.
- The HIL surface-finish landing page frames finish planning around `solderability`, `storage window`, `contact performance`, and assembly process rather than a one-size-fits-all finish default.
- The APT antenna page reinforces zone-based logic on RF boards by pairing cavity and antenna structures with `selective ENIG / soft gold` and RF-specific finish planning.

## Conditions And Methods

- Treat this as an internal design-and-quoting posture card.
- Use it to support future wiki pages about finish planning on hybrid RF + digital boards, mixed-assembly products, and prototype-to-production continuity.
- If a published article needs exact shelf-life limits, chemistry thickness ranges, or IPC finish clauses, check stronger primary sources first.

## Limits And Non-Claims

- This card does not mean every board should use multiple finishes.
- It does not prove every finish combination is process-neutral in cost, masking complexity, or yield risk.
- It also does not replace project-level review of assembly order, storage time, packaging plan, wire-bond need, or connector wear target.

## Open Questions

- Add a follow-on card for `prototype-to-production finish continuity`
- Add a follow-on card for `wire-bond-zone and edge-contact zoning strategy`

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-surface-finishes.json
- /code/hileap/frontendHIL/data/service-landings/en/pcb-surface-finish.json
- /code/hileap/frontendAPT/public/static/pcb/en/antenna-pcb.json
