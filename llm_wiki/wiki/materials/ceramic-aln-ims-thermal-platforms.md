---
wiki_id: "wiki-materials-ceramic-aln-ims-thermal-platforms"
title: "Ceramic, AlN, and IMS thermal-platform routing"
topic: "Ceramic / AlN / IMS thermal-platform selection"
category: "materials"
status: "active"
reviewed_at: "2026-05-03"
fact_ids:
  - "materials-ceramic-alumina-aln-class-source-coverage"
  - "materials-alumina-vs-aln-owner-scoped-comparison-boundary"
  - "materials-ltcc-class-definition-and-nonclaims"
  - "materials-thin-film-ceramic-circuit-technology-kyocera"
  - "materials-ceramic-platform-anchor-map"
  - "materials-parameter-scope-ventec-ims-material-values"
source_ids:
  - "frontendhil-ceramic-pcb-product-page-en"
  - "frontendhil-high-thermal-pcb-product-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
  - "ceramtec-ceramic-substrates-page"
  - "maruwa-aln-substrates-page"
  - "kyocera-ltcc-material-page"
  - "kyocera-thin-film-circuit-boards-page"
  - "kyocera-thin-film-technology-page"
  - "ventec-ims-family-overview"
tags: ["materials", "ceramic", "alumina", "aln", "ltcc", "thin-film", "ims", "thermal-management"]
---

# Use This Page For

- Routing drafts that say `ceramic PCB`, `alumina substrate`, `AlN substrate`, `LTCC`, `thin-film ceramic`, `IMS`, `MCPCB`, or generic `high thermal PCB`.
- Separating ceramic-substrate families from metal-base thermal-management families before any product-level selection is made.
- Preventing unsupported cross-vendor conductivity, metallization, suitability, cost, or lead-time claims from entering public copy.

# Core Routing Rule

- Start with platform class, not with one conductivity row.
- `Ceramic substrate`, `AlN substrate`, `LTCC`, `thin-film ceramic`, and `IMS` are adjacent thermal-platform lanes, not interchangeable synonyms.
- If a draft cannot say which lane it means, rewrite the draft before adding product or process detail.

# Platform Boundaries

## Ceramic Substrates: the broad class

- Use `ceramic substrate` when the source support is class-level and includes families such as alumina and aluminum nitride.
- CeramTec gives the local anchor that ceramic substrates include alumina and `AlN`.
- Do not collapse the whole ceramic class into `AlN`, `LTCC`, or `thin-film`.

## Alumina vs AlN: same class, different family direction

- Use `alumina` and `AlN` as distinct ceramic-substrate families.
- The current wiki only supports a guarded family-direction statement:
  one official owner-scoped comparison shows alumina as the cost/performance example and `AlN` as the higher-thermal example.
- Do not turn that owner-scoped comparison into a vendor-neutral default table.

## LTCC: process family, not the whole ceramic category

- Use `LTCC` only when the draft really means low-temperature co-fired ceramics.
- LTCC stays separate from generic ceramic substrates, alumina thick-film circuits, `AlN` substrates, and `IMS` unless a source explicitly connects them.
- LTCC class definition is supported; universal firing, shrinkage, hermeticity, layer-count, and RF-performance claims are not.

## Thin-Film Ceramic: precision process lane

- Use `thin-film ceramic` when the draft needs process vocabulary such as vacuum deposition or sputtering on ceramic substrates.
- Keep thin-film ceramic separate from LTCC, generic alumina boards, and `IMS`.
- Thin-film ceramic source support is process-framing support, not supplier-capability proof.

## IMS / MCPCB: metal-base thermal-management lane

- Use `IMS` or `MCPCB` when the draft means insulated metal substrate or metal-base laminate context.
- `IMS` is a separate thermal-management platform family, not a ceramic-substrate synonym.
- Ventec exact-product IMS cards can support material-parameter examples, but they do not prove finished-board thermal outcomes.

# Safe Selection Language

- Say `ceramic substrates include alumina and AlN families` when the draft needs class framing.
- Say `AlN is a ceramic-substrate family` rather than `AlN is the default ceramic PCB`.
- Say `LTCC is a distinct ceramic process family` rather than `all ceramic PCBs are LTCC`.
- Say `IMS is a metal-base thermal-management platform` rather than `IMS is a ceramic board`.
- Use owner-scoped wording when referencing alumina-versus-`AlN` directionality.
- Use exact-product IMS values only when the draft preserves product name, thickness context, and material-scope limits.

# Unsafe Selection Language

- Do not publish a vendor-neutral thermal-conductivity ranking across ceramic, alumina, `AlN`, LTCC, and `IMS` from the current fact base.
- Do not claim `DBC`, `AMB`, `DPC`, thin film, or thick film are universally available across ceramic suppliers.
- Do not claim direct-bond copper, metallization stack, brazing path, or package compatibility from class-level sources alone.
- Do not claim one platform is universally best for power, RF, LED, automotive, aerospace, medical, or semiconductor work.
- Do not convert IMS material examples into board-level heat-spreading, junction-temperature, or reliability proof.
- Do not write cost, lead-time, or yield guidance on this page.

# When To Route To Each Lane

| Draft signal | Route to | Reason |
| --- | --- | --- |
| `ceramic PCB` used generically | ceramic substrate framing first | the draft may still mean alumina or `AlN`, not LTCC or `IMS` |
| `best cost/performance ceramic` | alumina vs `AlN` boundary review | current support is owner-scoped, not universal |
| `co-fired ceramic`, `glass ceramic`, `copper conductors in ceramic` | LTCC lane | local support exists only at class-definition level |
| `vacuum deposition`, `sputtering`, `fine ceramic patterns` | thin-film ceramic lane | these are process-family signals |
| `metal core`, `MCPCB`, `insulated metal substrate`, `LED heat sink board` | `IMS` lane | this is metal-base thermal-management framing |

# Numeric-Claim Discipline

- The current local corpus supports boundary framing first and owner-scoped examples second.
- It does not support a permanent cross-vendor ceramic comparison table.
- If a draft truly needs numeric material examples, route to the matching fact card and keep the owner and scope attached.
- If the draft does not need exact numbers, prefer platform-selection wording and remove speculative numerics.

# Blocked Claims

- thermal conductivity comparisons
- direct-bond and metallization proofs
- substrate suitability guarantees
- cost, lead-time, and yield claims

# Must Refresh Before Publishing

- Any conductivity, dielectric, CTE, dielectric-strength, thickness, or metallization number used outside the current owner-scoped fact context
- Any claim that compares ceramic families across multiple suppliers
- Any claim that connects `LTCC`, `thin-film`, `DBC`, `AMB`, `DPC`, and `IMS` into one universal process ladder
- Any statement about HIL/APT ceramic manufacturing capability, qualification, or supply posture

# Related Fact Cards

- `materials-ceramic-alumina-aln-class-source-coverage`
- `materials-alumina-vs-aln-owner-scoped-comparison-boundary`
- `materials-ltcc-class-definition-and-nonclaims`
- `materials-thin-film-ceramic-circuit-technology-kyocera`
- `materials-ceramic-platform-anchor-map`
- `materials-parameter-scope-ventec-ims-material-values`

# Local Source Records

- `frontendhil-ceramic-pcb-product-page-en`
- `frontendhil-high-thermal-pcb-product-page-en`
- `frontendapt-pcb-ceramic-pcb-page-en`
- `ceramtec-ceramic-substrates-page`
- `maruwa-aln-substrates-page`
- `kyocera-ltcc-material-page`
- `kyocera-thin-film-circuit-boards-page`
- `kyocera-thin-film-technology-page`
- `ventec-ims-family-overview`
