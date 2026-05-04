---
fact_id: "materials-alumina-vs-aln-owner-scoped-comparison-boundary"
title: "Alumina versus AlN substrate comparison is source-owner-specific, not a generic ceramic table"
topic: "Alumina vs AlN ceramic substrates"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "ceramtec-ceramic-substrates-page"
  - "maruwa-aln-substrates-page"
tags: ["ceramic", "alumina", "aln", "comparison", "thermal-platform", "owner-scoped"]
---

# Canonical Summary

> Current official ceramic-substrate sources support a conservative `alumina vs AlN` comparison only when the comparison is kept source-owner-specific. CeramTec's current substrate page gives one side-by-side example table for `Al2O3` and `AlN`, while MARUWA's current AlN page reinforces the `AlN` family identity and one vendor-scoped set of AlN grades and processing families. These sources do not justify a frozen vendor-neutral ceramic property table.

## Stable Facts

- CeramTec's current substrate page includes a side-by-side comparison table for `Al2O3` and `AlN` under the same source owner.
- In that CeramTec table, `Al2O3` is listed with example values of `500 MPa` bending strength, `3.0 MPa*sqrt(m)` fracture toughness, `7-9 x10^-6/K` CTE, `24 W/mK` thermal conductivity, and `15 kV/mm` dielectric strength.
- In that same CeramTec table, `AlN` is listed with example values of `450 MPa` bending strength, `3.0 MPa*sqrt(m)` fracture toughness, `5-6 x10^-6/K` CTE, `170 W/mK` thermal conductivity, and `15 kV/mm` dielectric strength.
- CeramTec currently positions alumina as the `best cost/performance ratio` and the `most commonly used substrate in high-performance electronics`.
- CeramTec currently positions `AlN` around high thermal conductivity and a CTE very close to silicon.
- MARUWA's current AlN page reinforces `AlN` as a ceramic substrate family and lists current vendor-scoped AlN grades plus available processing families such as thin film, thick film, `DBC`, `AMB`, and `DPC`.

## Conditions And Methods

- Use this card only for guarded directionality such as `alumina and AlN are distinct ceramic-substrate families` and `one official source owner currently shows AlN as the higher-thermal example and alumina as the cost/performance example`.
- Keep every numeric row explicitly tied to the current CeramTec page unless a newer exact datasheet is added.
- Keep MARUWA process and grade details explicitly tied to MARUWA's own AlN substrate family.

## Limits And Non-Claims

- This card does not prove universal alumina or universal `AlN` property values across suppliers.
- It does not prove that every `AlN` board is better than every alumina board for every design.
- It does not prove that `DBC`, `AMB`, thin film, thick film, or `DPC` are available from every ceramic PCB manufacturer.
- It does not validate HIL/APT current ceramic capability, pricing, lead time, quality, or certification claims.

## Open Questions

- Add a current primary-source alumina product datasheet if future ceramic drafts need a second owner-specific alumina row beyond the CeramTec comparison page.
- Add exact process-owner records if future drafts need reusable `DBC` or `AMB` workflow facts rather than vendor-scoped existence only.

## Source Links

- https://www.ceramtec-group.com/en/ceramtec-us/substrates
- https://www.maruwa-g.com/e/products/ceramic/000314.html
