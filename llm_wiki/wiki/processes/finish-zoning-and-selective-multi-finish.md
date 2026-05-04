---
topic_id: "processes-finish-zoning-and-selective-multi-finish"
title: "Finish Zoning And Selective Multi-Finish"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
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
tags: ["surface-finish", "selective-finish", "multi-finish", "rf", "wire-bond", "edge-fingers", "press-fit", "storage-window", "process-boundary"]
---

# Definition

> Finish zoning and selective multi-finish is a process-planning topic, not a single-finish comparison table. The current local source layer is strong enough to support a board-level zoning posture in which different areas are assigned different finishes based on RF behavior, wire-bond need, edge-contact wear, press-fit insertion, assembly sequence, and storage exposure. It is not strong enough to support exact thickness, durability, yield, or qualification claims from finish names alone.

## Why This Topic Matters

- Mixed-function boards often combine RF pads, digital/control pads, wire-bond areas, edge fingers, and press-fit connector zones with different finish demands.
- The landed facts already support a real zoning workflow, but the logic was scattered across RF-finish, press-fit, selective-finish, and storage-exposure cards.
- This page turns that into one active process boundary so future AI workers can describe multi-finish planning as a routing problem instead of falling back to one-finish-for-the-whole-board copy.

## Multi-Finish Boundary Model

### Layer 1: Functional Zoning

| Zone | Safe routing posture | What it does not prove |
|---|---|---|
| **RF pads / RF paths** | Zone finish by RF-specific signal and contact needs | Universal lowest loss, PIM target, or exact high-GHz performance |
| **General digital / control pads** | May use a different general-purpose planar finish than RF or bond zones | Lowest cost or universal best default |
| **Wire-bond areas** | Separate zone when soldering and wire bonding must coexist | Bond success or exact finish-stack authority |
| **Edge fingers / edge contacts** | Separate zone for repeated insertion or connector-contact duty | Thickness, insertion-cycle, contact-resistance, or durability proof |
| **Press-fit connector zones** | Separate zone tied to immersion-tin-first posture plus hole-control review | Guaranteed press-fit success from finish chemistry alone |

### Layer 2: Process Sequence

| Process factor | Safe meaning |
|---|---|
| **Precision masking** | Selective multi-finish depends on masking and regional process control |
| **Sequential processing** | Multi-finish is a manufacturing sequence decision, not just a material menu choice |
| **Assembly behavior** | Finish choice should follow soldering, bonding, insertion, and contact-use path |
| **Inspection / release** | More finish regions can add planning and review burden even when technically justified |

### Layer 3: Storage And Exposure

| Factor | Safe meaning |
|---|---|
| **Storage window** | Shelf-life and exposure before use are part of finish selection |
| **Packaging / delay risk** | A board that sits before assembly may need a different finish posture than an immediately assembled board |
| **Repeated contact duty** | Connector and insertion zones should not be treated as ordinary solder-pad zones |

## Stable Facts

- Internal finish pages explicitly support `selective finish application` and `selective multi-finish combinations` when one finish cannot satisfy the whole board.
- The same internal layer gives concrete mixed-finish examples such as `ENIG on SMD pads plus hard gold on edge fingers` and `OSP on general pads with ENEPIG on wire-bond areas`.
- The selective-finish posture is tied to `precision masking` and `sequential processing`, which makes multi-finish planning a process decision rather than a simple chemistry preference.
- Internal RF finish-selection pages consistently separate `immersion silver`, `ENIG`, and `ENEPIG` by actual RF use case instead of treating one finish as the universal RF answer.
- Internal RF pages also support zoning logic in which RF pads and digital/control areas may sit on different finish postures when the application justifies it.
- The press-fit finish card supports `immersion tin` as the primary press-fit-oriented finish posture, but only inside a broader hole-control, connector-fit, and backplane-integration workflow.
- The storage-exposure card ties finish selection to storage window and assembly timing, which means finish planning starts before soldering or bonding actually begins.
- Public IPC metadata remains useful for finish-family identity and taxonomy anchoring, but not for clause-level interpretation, exact thickness, acceptance, or durability claims without licensed text.
- The edge-contact boundary supports a separate metadata route for gold fingers and edge contacts while keeping bevel, thickness, insertion-cycle, contact-resistance, and acceptance claims blocked without stronger evidence.

## Active Process Guidance

### Use This Page For

- boards mixing RF, digital, wire-bond, edge-contact, and press-fit zones
- selective multi-finish planning language
- finish choice tied to assembly order and storage exposure
- explaining why one board may need more than one finish family

### Safe Vocabulary

- `finish zoning`
- `selective multi-finish`
- `functional area routing`
- `precision masking`
- `sequential finish processing`
- `storage-window-sensitive finish choice`
- `press-fit zone`
- `edge-contact zone`

### Recommended Routing Flow

- Start with **functional zones** on the board.
- Check **assembly sequence**: soldering, wire bonding, insertion, repeated contact.
- Check **storage exposure** and release timing.
- Then decide whether one finish is enough or selective multi-finish is justified.
- Keep **IPC references** at taxonomy / metadata level unless stronger text exists.

## Engineering Boundaries

- Do not treat selective finish as a cosmetic add-on; it depends on process sequence and masking discipline.
- Do not collapse RF pads, wire-bond zones, edge fingers, press-fit holes, and ordinary SMT pads into one finish rule.
- Do not let RF finish language override wire-bond, edge-contact, or storage-window needs without explicit zoning logic.
- Do not write as if finish chemistry alone solves connector wear, press-fit insertion, bonding success, or RF loss behavior.
- Keep IPC metadata separate from clause-level or acceptance-level process claims.

## Common Misreadings

- `Selective multi-finish means any finish combination is easy or neutral to manufacture.`
- `ENIG is the default answer for every RF, connector, and bond zone.`
- `ENEPIG should be used everywhere once wire bonding appears anywhere on the board.`
- `Immersion tin by itself guarantees press-fit reliability.`
- `Gold-finger or edge-contact metadata proves durability or qualification.`
- `Storage-window concerns disappear once the finish family is named.`

## Must Refresh Before Publishing

- any exact thickness, durability, bevel, insertion-cycle, or contact-resistance claim
- any IPC clause-level or acceptance-level claim without licensed standard text
- any shelf-life, storage-window, or reflow-count claim stated as exact authority
- any qualification or pass-status claim for wire-bond, RF, edge-contact, or press-fit execution
- any yield, masking-effort, cost, or lead-time statement tied to selective multi-finish

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
