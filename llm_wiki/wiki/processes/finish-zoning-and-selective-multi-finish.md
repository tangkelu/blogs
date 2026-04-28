---
topic_id: "processes-finish-zoning-and-selective-multi-finish"
title: "Finish Zoning And Selective Multi-Finish"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "methods-finish-zoning-by-assembly-sequence-and-storage-exposure"
  - "methods-selective-multi-finish-strategy"
  - "methods-surface-finish-selection-for-rf"
  - "methods-press-fit-finish-selection"
  - "standards-ipc-finish-standards-metadata"
  - "standards-ipc-surface-finish-taxonomy-osp-hasl-extension"
  - "standards-edge-contact-gold-finger-standards-metadata-boundary"
source_ids:
  - "frontendapt-pcb-surface-finishes-page-en"
  - "frontendhil-pcb-surface-finish-landing-en"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendhil-rogers-product-page-en"
  - "frontendapt-pcb-drilling-page-en"
  - "frontendapt-backplane-pcb-page-en"
  - "ipc-document-revision-table"
  - "ipc-4552b-toc"
  - "ipc-4553a-chinese-toc"
  - "ipc-4554-am1-toc"
  - "ipc-4555-toc"
  - "ipc-4556-toc"
  - "ipc-6012f-toc"
  - "ipc-a-600k-toc"
  - "ipc-status-of-standardization"
tags: ["surface-finish", "selective-finish", "rf", "wire-bond", "press-fit", "edge-fingers", "processes"]
---

# Definition

> Finish zoning and selective multi-finish is the board-level practice of assigning different finishes to different areas based on assembly sequence, storage exposure, RF performance, wire-bond need, connector wear, and press-fit behavior instead of forcing one finish onto the whole board.

## Why This Topic Matters

- Mixed-function boards routinely combine RF pads, digital pads, wire-bond areas, edge fingers, and press-fit connector zones that do not share the same finish requirement.
- Your internal non-blog pages already support a zoning posture, but the logic is split across finish-selection, RF, press-fit, and standards metadata cards.
- This topic page gives one stable aggregation point for later wiki use without turning IPC references into process claims.

## Stable Facts

- The internal finish pages explicitly support `selective finish application` when one finish cannot satisfy the whole board.
- The same internal pages give concrete mixed-finish examples such as `ENIG on SMD pads plus hard gold on edge fingers` and `OSP on general pads with ENEPIG on wire-bond areas`.
- The selective-finish posture is tied to `precision masking` and `sequential processing`, which means finish zoning is a process-planning decision, not just a material preference.
- The RF finish cards consistently separate `immersion silver`, `ENIG`, and `ENEPIG` by actual use case, so RF pads are one zone while digital or control areas can remain on a different finish.
- The press-fit finish card treats `immersion tin` as the primary press-fit-oriented finish, but only inside a broader connector-and-hole-control workflow.
- The finish-zone card ties finish choice to `storage exposure`, which means shelf life and packaging window are part of the decision even before assembly starts.
- The IPC finish-standard card is a metadata anchor only: it is useful for document identity and revision status, but not for clause-level, thickness, or acceptance claims unless the licensed standard text is available.
- The P4-37 finish-taxonomy extension adds `IPC-4555` as the OSP public anchor and clarifies that `IPC-4554` is immersion tin, not HASL.
- HASL / Pb-free solder-coating discussion should be anchored through rigid-board surface-finish / solder-coating metadata such as `IPC-6012F` public TOC context unless a more specific primary source is added.
- The P4-38 edge-contact boundary adds a dedicated metadata route for gold fingers and edge contacts through `IPC-6012F`, `IPC-A-600K`, `IPC-4552B`, and `IPC-4556`, while keeping thickness, bevel, insertion-cycle, contact-resistance, and acceptance claims blocked without licensed standards, drawings, or dated process records.

## Engineering Boundaries

- Do not treat masking as a minor implementation detail; selective multi-finish depends on it.
- Do not separate process sequence from finish choice; the order of operations is part of the manufacturing decision.
- Do not assume selective multi-finish is automatically good for yield or cost; it can add complexity, inspection burden, and quoting risk.
- Do not ignore storage window or shelf life when a board may sit before assembly or shipping.
- Do not collapse wire bonding, RF pads, edge fingers, and press-fit into one finish rule.
- Do not use IPC metadata as a substitute for licensed standard text, clause interpretation, or thickness claims.
- Do not map HASL to `IPC-4554`; that standard identity belongs to immersion tin in the current public metadata layer.
- Do not write press-fit finish guidance without keeping hole control and connector integration in view.
- Do not write gold-finger or edge-contact thickness, bevel, insertion durability, or contact-resistance claims from public IPC TOCs alone.

## Common Misreadings

- `Selective finish supported` does not mean every finish combination is cheap or easy to mask.
- `RF finish choice` does not automatically override wire-bond or edge-contact requirements.
- `ENIG` being a common default does not make it the correct choice for every RF pad, connector finger, or storage window.
- `ENEPIG` should not be treated as the default premium answer when wire bonding is not required.
- `Immersion tin` for press-fit does not mean finish chemistry can compensate for weak drill control or connector mismatch.
- IPC revision metadata is not the same thing as a process rule.
- OSP being represented by an IPC public TOC does not authorize universal shelf-life, reflow-count, or cost-advantage claims.
- A public IPC gold-finger / edge-contact metadata route does not mean the shop can manufacture or inspect every hard-gold edge-finger requirement.

## Must Refresh Before Publishing

- Any exact shelf-life, storage-window, or finish-thickness value
- Any clause-level IPC claim or revision interpretation beyond public metadata
- Any yield, cost, or masking-effort statement that depends on a specific fab workflow
- Any claim about guaranteed compatibility between a finish choice and a specific wire-bond, RF, edge-finger, or press-fit implementation
- Any exact gold-finger thickness, bevel geometry, insertion-cycle life, contact resistance, or edge-contact acceptance threshold

## Related Fact Cards

- `methods-finish-zoning-by-assembly-sequence-and-storage-exposure`
- `methods-selective-multi-finish-strategy`
- `methods-surface-finish-selection-for-rf`
- `methods-press-fit-finish-selection`
- `standards-ipc-finish-standards-metadata`
- `standards-ipc-surface-finish-taxonomy-osp-hasl-extension`
- `standards-edge-contact-gold-finger-standards-metadata-boundary`

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-surface-finishes.json
- /code/hileap/frontendHIL/data/service-landings/en/pcb-surface-finish.json
- /code/hileap/frontendAPT/public/static/pcb/en/antenna-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-frequency-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/microwave-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rogers-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/pcb-drilling.json
- /code/hileap/frontendAPT/public/static/pcb/en/backplane-pcb.json
- https://www.ipc.org/ipc-document-revision-table
- https://www.ipc.org/TOC/IPC-4552B-toc.pdf
- https://www.ipc.org/TOC/IPC-4553A-Chinese.pdf
- https://www.ipc.org/TOC/IPC-4554Am1.pdf
- https://www.ipc.org/TOC/IPC-4555_TOC.pdf
- https://www.ipc.org/TOC/IPC-4556.pdf
- https://www.ipc.org/TOC/IPC-6012F-TOC.pdf
- https://www.electronics.org/TOC/IPC-A-600K-toc.pdf
- https://www.ipc.org/Status
