---
fact_id: "methods-surface-finish-selection-for-rf"
title: "Internal RF finish selection posture consistently separates silver, ENIG, and ENEPIG by real use case"
topic: "RF surface finish selection"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-pcb-surface-finishes-page-en"
  - "frontendhil-pcb-surface-finish-landing-en"
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
tags: ["internal", "surface-finish", "rf", "enig", "enepig", "immersion-silver", "methods"]
---

# Canonical Summary

> Your non-blog site content already expresses a fairly consistent internal RF finish-selection logic: `immersion silver` is favored when insertion loss and PIM behavior matter most, `ENIG` is the general planar default when assembly tolerance and durability matter, and `ENEPIG` is reserved for wire-bond or mixed assembly cases where its added complexity is justified.

## Stable Facts

- The APT surface-finish page explicitly frames `immersion silver` as the preferred choice for high-frequency RF and microwave applications where signal loss at the conductor surface matters.
- The same APT page frames `ENIG` as the broad general-purpose planar finish for fine-pitch assembly and long shelf life.
- The same APT page frames `ENEPIG` as the universal finish when soldering and wire bonding must coexist on the same board.
- The HIL high-frequency product JSON explicitly states that `immersion silver minimizes insertion loss and PIM`, while `ENEPIG` improves wire-bonding fit but introduces more high-GHz loss due to nickel.
- The HIL Rogers product JSON recommends `ENIG` and `immersion silver` for flat, low-roughness RF pads, while `ENEPIG` is preferred for wire-bond or mixed RF/analog assemblies.
- The APT high-frequency PCB page states `immersion silver offers low loss`, `ENIG balances solderability and durability`, and `ENEPIG` fits pads that also require wire bonding.
- The APT microwave page repeatedly frames finish choice as `silver vs ENEPIG vs ENIG based on application`, and also suggests mixed-finish planning where RF and digital/control areas have different needs.
- The HIL surface-finish landing page presents finish selection as an engineering decision tied to solderability, storage, contact behavior, and assembly route rather than a default one-size-fits-all choice.

## Conditions And Methods

- Treat this card as internal selection posture extracted from your own non-blog pages.
- Use it to support quoting logic, intake prompts, and future wiki pages about RF pad finish tradeoffs.
- If a published article needs exact thickness ranges, IPC clause references, or chemistry-specific failure modes, re-check against stronger primary sources first.

## Limits And Non-Claims

- This card does not prove one finish is universally best for all RF boards.
- It does not prove every project can freely mix finishes without cost, process, or masking tradeoffs.
- It does not replace board-level review of wire bonding, shelf life, contact wear, PIM target, or assembly sequence.

## Open Questions

- Add a follow-on internal card for `selective multi-finish strategy on hybrid RF + digital boards`
- Add a higher-trust external source layer for IPC finish standards such as `IPC-4552`, `IPC-4553`, `IPC-4554`, and `IPC-4556`

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-surface-finishes.json
- /code/hileap/frontendHIL/data/service-landings/en/pcb-surface-finish.json
- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
