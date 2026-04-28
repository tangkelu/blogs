---
topic_id: "materials-copper-foil-class-roughness-and-rf-boundaries"
title: "Copper Foil Class, Roughness, And RF Boundaries"
category: "materials"
status: "draft"
last_reviewed_at: "2026-04-28"
fact_ids:
  - "materials-copper-foil-classes-and-roughness-boundary"
source_ids:
  - "ipc-4562b-toc"
  - "jx-electrodeposited-copper-foil-page"
  - "jx-rolled-copper-foil-page"
  - "tex-rolled-copper-foil-page"
tags: ["copper-foil", "ed-foil", "rolled-foil", "ra-foil", "roughness", "rf-loss", "flex", "pcb-materials"]
---

# Definition

> Copper foil selection should be written as a material-form and surface-profile decision first, not as a universal RF-loss or bend-life table. Public IPC metadata and official foil-vendor pages support class vocabulary such as electrodeposited foil, wrought / rolled foil, foil profile, grade, and bond enhancement, but exact loss, roughness, adhesion, and flex-life claims need exact product data.

## Why This Topic Matters

- RF, high-speed, and flex PCB drafts often turn `RA`, `ED`, `HVLP`, and `low-profile` copper language into generic performance promises.
- The current source layer can make the terminology real, but it cannot yet produce a universal foil-property table.
- This page gives blog-writing prompts a safe place to consume copper-foil vocabulary without overclaiming finished-board performance.

## Stable Facts

- `IPC-4562B` public TOC metadata supports copper-foil category vocabulary, including foil type, foil grade, foil profile, bond-enhancement treatment, electrodeposited foil, wrought foil, thickness, peel strength, and treatment integrity.
- JX provides official product-family pages for electro-deposited copper foil and rolled copper foil.
- JX source-owner language supports rolled-vs-ED class distinction and source-scoped lower-roughness / flexibility positioning for rolled foil.
- Tex Technology provides an official rolled-copper-foil page that supports rolling / annealing process-route vocabulary and flexibility positioning.

## Engineering Boundaries

- Use `ED`, `rolled`, `wrought`, `profile`, and `bond treatment` as class vocabulary unless an exact foil product record is attached.
- Keep copper roughness values source-scoped to exact vendor pages or datasheets.
- Do not convert copper-foil class into finished-board insertion-loss, impedance, thermal, current, or bend-life claims without stackup and test evidence.
- Treat RF loss as a board-system result influenced by dielectric, copper profile, treatment, geometry, frequency, launch, and measurement setup.

## Common Misreadings

- Rolled foil is not automatically the best foil for every RF, high-speed, or flex design.
- ED foil is not one single roughness or loss category.
- `Low profile` or `smooth` wording does not provide enough data for insertion-loss calculations.
- A copper-foil standard metadata page does not prove a fabricator stocks or can process a specific foil.

## Must Refresh Before Publishing

- Any `Ra`, `Rz`, profile, peel-strength, elongation, thickness, or bond-treatment value
- Any insertion-loss, skin-effect, impedance, thermal, current, or bend-cycle claim
- Any supplier inventory, process compatibility, stackup availability, quote, cost, or lead-time claim

## Related Fact Cards

- `materials-copper-foil-classes-and-roughness-boundary`

## Primary Sources

- https://www.ipc.org/TOC/IPC-4562B-TOC.pdf
- https://www.jx-nmm.com/english/products/copper_foil_and_alloy/electrodeposited_copper_foil/
- https://www.jx-nmm.com/english/products/copper_foil/rolled_copper_foil/
- https://www.textech.co.jp/en/products/foil-stretched/
