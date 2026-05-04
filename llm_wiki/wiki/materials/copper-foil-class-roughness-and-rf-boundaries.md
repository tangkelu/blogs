---
topic_id: "materials-copper-foil-class-roughness-and-rf-boundaries"
title: "Copper Foil Class, Roughness, And RF Boundaries"
category: "materials"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "materials-copper-foil-classes-and-roughness-boundary"
  - "materials-copper-foil-exact-product-profile-anchor-map"
source_ids:
  - "ipc-4562b-toc"
  - "jx-electrodeposited-copper-foil-page"
  - "jx-rolled-copper-foil-page"
  - "jx-rigid-ed-copper-foil-page"
  - "jx-jxefl-fpc-ed-copper-foil-page"
  - "furukawa-fz-ws-copper-foil-page"
  - "furukawa-gts-std-gts-mp-copper-foil-page"
  - "tex-rolled-copper-foil-page"
tags: ["copper-foil", "ed-foil", "rolled-foil", "ra-foil", "roughness", "rz", "rf-loss", "flex", "jx", "furukawa", "pcb-materials"]
---

# Definition

> Copper foil selection should be written as a material-form and surface-profile decision first, not as a universal RF-loss or bend-life table. The wiki now has both class-level vocabulary (IPC-4562B, JX family pages, Tex) and narrow exact-product Rz anchors (JX rigid `JTCS-P1`/`JDLC`/`HLP-II`, JX FPC `JXEFL-V2`/`JXEFL-BHM`, Furukawa `FZ-WS`/`GTS-STD`/`GTS-MP`). Exact roughness values remain owner-scoped to the product row and source; they do not produce a supplier-neutral roughness table.

## Why This Topic Matters

- RF, high-speed, and flex PCB drafts often turn `RA`, `ED`, `HVLP`, and `low-profile` copper language into generic performance promises.
- The current source layer now supports both class vocabulary and narrow owner-scoped Rz examples, but it cannot produce a universal foil-property or RF-loss table.
- This page gives blog-writing prompts a safe place to consume copper-foil vocabulary and example product rows without overclaiming finished-board performance.

## Routing Guidance

- Route `ED`, `rolled`, `wrought`, `RA`, `HVLP`, and `bond treatment` prompts to class vocabulary first unless the draft explicitly names a source-backed foil product row.
- Route `JTCS-P1`, `JDLC`, `HLP-II`, `JXEFL-V2`, `JXEFL-BHM`, `FZ-WS`, `GTS-STD`, and `GTS-MP` to owner-scoped exact-product examples only, with each `Rz` claim tied back to the supplier page.
- Route RF and high-speed prompts to this page only for copper-profile boundary framing; move to stackup-, geometry-, dielectric-, and measurement-level evidence before making any board-loss statement.
- Route flex-language prompts carefully: rolled-foil and flexibility positioning can be discussed as class framing, but not as a blanket proof of bend-life superiority.
- Keep this page as a boundary layer between foil vocabulary and finished-board performance claims.

## Exact-Product Profile Anchor Map

| Product | Supplier | Segment | Profile / Rz | Official Source |
|---------|----------|---------|-------------|-----------------|
| JTCS-P1 | JX | Rigid ED | Per product page | `jx-rigid-ed-copper-foil-page` |
| JDLC | JX | Rigid ED | Per product page | `jx-rigid-ed-copper-foil-page` |
| HLP-II | JX | Rigid ED | Per product page | `jx-rigid-ed-copper-foil-page` |
| JXEFL-V2 | JX | FPC ED | Per product page | `jx-jxefl-fpc-ed-copper-foil-page` |
| JXEFL-BHM | JX | FPC ED | Per product page | `jx-jxefl-fpc-ed-copper-foil-page` |
| FZ-WS | Furukawa | H-VLP2 ED | Per product page | `furukawa-fz-ws-copper-foil-page` |
| GTS-STD | Furukawa | Standard ED | Per product page | `furukawa-gts-std-gts-mp-copper-foil-page` |
| GTS-MP | Furukawa | MP ED | Per product page | `furukawa-gts-std-gts-mp-copper-foil-page` |

## Stable Facts

- `IPC-4562B` public TOC metadata supports copper-foil category vocabulary, including foil type, foil grade, foil profile, bond-enhancement treatment, electrodeposited foil, wrought foil, thickness, peel strength, and treatment integrity.
- JX provides official product-family pages for electro-deposited copper foil and rolled copper foil, plus separate exact-product pages for rigid ED (`JTCS-P1`, `JDLC`, `HLP-II`) and FPC ED (`JXEFL-V2`, `JXEFL-BHM`) rows with stated `Surface roughness: Rz` values.
- Furukawa provides exact-product pages for `FZ-WS` (H-VLP2 lineup) and `GTS-STD`/`GTS-MP` rows with page-level `Surface roughness Rz` values.
- JX source-owner language supports rolled-vs-ED class distinction and source-scoped lower-roughness / flexibility positioning for rolled foil.
- Tex Technology provides an official rolled-copper-foil page that supports rolling / annealing process-route vocabulary and flexibility positioning.
- All Rz values are owner-scoped to the exact product row and page; they are not vendor-neutral roughness defaults.

## Engineering Boundaries

- Use `ED`, `rolled`, `wrought`, `profile`, and `bond treatment` as class vocabulary unless an exact foil product record is attached.
- Keep copper roughness (Rz) values source-scoped to the exact product name, thickness row, and source owner.
- Do not merge JX and Furukawa Rz rows into a single supplier-neutral roughness ladder.
- Do not convert copper-foil class or product-row Rz into finished-board insertion-loss, impedance, thermal, current, or bend-life claims without stackup and test evidence.
- Treat RF loss as a board-system result influenced by dielectric, copper profile, treatment, geometry, frequency, launch, and measurement setup.

## Blocked Claims

- finished-board loss claims
- supplier-neutral ranking claims
- roughness-to-performance guarantees
- cost, lead-time, and yield claims

## Common Misreadings

- Rolled foil is not automatically the best foil for every RF, high-speed, or flex design.
- ED foil is not one single roughness or loss category; `HLP-II`, `FZ-WS`, and `GTS-STD` are different rows with different profiles.
- `Low profile` or `smooth` wording does not provide enough data for insertion-loss calculations.
- A copper-foil standard metadata page does not prove a fabricator stocks or can process a specific foil.
- Rz values from exact-product pages are not transferable to other foil products or suppliers.

## Must Refresh Before Publishing

- Any `Ra`, `Rz`, profile, peel-strength, elongation, thickness, or bond-treatment value
- Any insertion-loss, skin-effect, impedance, thermal, current, or bend-cycle claim
- Any claim that one foil class is universally smoother, lower loss, or better for RF than another
- Any claim that roughness directly guarantees channel, antenna, or finished-board behavior
- Any supplier inventory, process compatibility, stackup availability, quote, cost, or lead-time claim

## Related Facts And Source Scope

- `materials-copper-foil-classes-and-roughness-boundary` is the safe class-vocabulary layer for `IPC-4562B`, JX family pages, and Tex rolled-foil framing.
- `materials-copper-foil-exact-product-profile-anchor-map` is the safe exact-product layer for JX and Furukawa owner-scoped `Rz` examples.
- Keep class vocabulary separate from exact-product rows; the current corpus does not support a unified cross-supplier copper-foil ranking table.
- Use this page to stop prompts from converting copper-profile nouns into board-level SI, RF, thermal, or bend-life claims without new local evidence.

## Related Fact Cards

- `materials-copper-foil-classes-and-roughness-boundary` — class vocabulary, IPC-4562B, JX/Tex family-level anchors
- `materials-copper-foil-exact-product-profile-anchor-map` — JX rigid/FPC and Furukawa exact-product Rz rows

## Primary Sources

- https://www.ipc.org/TOC/IPC-4562B-TOC.pdf
- https://www.jx-nmm.com/english/products/copper_foil_and_alloy/electrodeposited_copper_foil/
- https://www.jx-nmm.com/english/products/copper_foil/rolled_copper_foil/
- https://www.jx-nmm.com/english/products/copper_foil_and_alloy/electrodeposited_copper_foil/rigid/
- https://www.jx-nmm.com/english/products/copper_foil_and_alloy/electrodeposited_copper_foil/jxefl/
- https://www.furukawaelectric.com/foil/en/product/print/fz-ws.html
- https://www.furukawaelectric.com/foil/en/product/print/gts.html
- https://www.textech.co.jp/en/products/foil-stretched/
