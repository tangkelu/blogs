---
fact_id: "materials-copper-foil-exact-product-profile-anchor-map"
title: "JX and Furukawa sources now support narrow exact-product copper-foil profile and Rz anchors, not supplier-neutral roughness or RF-loss tables"
topic: "Copper-foil exact-product profile anchors"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-02"
source_ids:
  - "jx-rigid-ed-copper-foil-page"
  - "jx-jxefl-fpc-ed-copper-foil-page"
  - "furukawa-fz-ws-copper-foil-page"
  - "furukawa-gts-std-gts-mp-copper-foil-page"
  - "ipc-4562b-toc"
tags: ["copper-foil", "roughness", "rz", "profile", "jx", "furukawa", "exact-product", "materials"]
---

# Canonical Summary

> Copper-foil coverage now has narrow exact-product anchors for selected JX and Furukawa rows, including `JTCS-P1`, `JDLC`, `HLP-II`, `JXEFL-V2`, `JXEFL-BHM`, `FZ-WS`, `GTS-STD`, and `GTS-MP`. These anchors support owner-scoped profile and `Rz` wording only. They do not authorize supplier-neutral roughness tables, universal `ED` versus rolled rankings, RF-loss claims, bend-life claims, or finished-board performance claims.

## Stable Facts

- `IPC-4562B` public TOC metadata still provides the class vocabulary for foil type, grade, profile, and treatment, but not universal numeric roughness rules.
- JX publicly provides exact rigid-board electrodeposited copper-foil rows for `JTCS-P1`, `JDLC`, and `HLP-II`, with thickness and `Surface roughness : Rz` values on the current owner page.
- JX publicly provides exact FPC electrodeposited copper-foil rows for `JXEFL-V2` and `JXEFL-BHM`, with thickness and `Surface roughness : Rz` values on the current owner page.
- Furukawa publicly provides exact `FZ-WS` rows with `H-VLP2` lineup framing and page-level `Surface roughness Rz` values.
- Furukawa publicly provides exact `GTS-STD` and `GTS-MP` rows with page-level `Surface roughness Rz` values.
- These product rows are owner-scoped examples, not a single vendor-neutral copper-foil ladder.

## Conditions And Methods

- Use this card when a draft needs exact copper-foil product nouns or owner-scoped `Rz` / profile examples.
- Keep each `Rz` value tied to the exact product name, thickness row, and source owner.
- Use these anchors to separate `exact product row` from `class vocabulary` in copper-foil writing.
- Pair this card with `facts/materials/copper-foil-classes-and-roughness-boundary.md` when broader foil-class wording is needed.

## Limits And Non-Claims

- This card does not authorize supplier-neutral copper-foil roughness tables.
- It does not authorize claims that one profile is universally lower loss, better for RF, better for flex, or better for every multilayer build.
- It does not authorize insertion-loss, impedance, current, thermal, bend-cycle, peel-strength ranking, or manufacturing-yield claims at board level.
- It does not prove stock, sourcing, lamination compatibility, quote readiness, lead time, or HIL/APT capability.

## Open Questions

- Add owner-scoped rolled-foil exact-product rows later only if a future draft truly needs exact RA / wrought foil product examples rather than class language.
- Add a separate process lane only if future writing needs bond-treatment or foil-profile workflow vocabulary beyond current product rows.
- Do not stretch this card into supplier-neutral RF copper selection guidance.

## Source Links

- https://www.jx-nmm.com/english/products/copper_foil_and_alloy/electrodeposited_copper_foil/rigid/
- https://www.jx-nmm.com/english/products/copper_foil_and_alloy/electrodeposited_copper_foil/jxefl/
- https://www.furukawaelectric.com/foil/en/product/print/fz-ws.html
- https://www.furukawaelectric.com/foil/en/product/print/gts.html
- https://www.ipc.org/TOC/IPC-4562B-TOC.pdf
