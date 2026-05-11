# P4-299 PCB资料 Package Blocked Exact-Data Evidence Batch 2

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_blocked_evidence_inventory_only`

## Purpose

Expand the `PCB资料` unified knowledge layer by preserving high-value but still blocked `package` exact-data candidates inside `pdf_evidence/pcb_ziliao/package/`.

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.
It does not create new `facts/local_pdf/` cards.

## What Landed

### New package evidence records

- `pdf_evidence/pcb_ziliao/package/pin-compensation-calculation-rule-diagram.md`
- `pdf_evidence/pcb_ziliao/package/flash-calculation-rule-diagram.md`
- `pdf_evidence/pcb_ziliao/package/bga-pitch-to-pad-diameter-table.md`

### Tracker alignment

- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Kept as `blocked_evidence` / evidence-only

- pin-compensation calculation rule diagram from page `24`
- flash-calculation rule diagram from page `24`
- BGA pitch-to-pad-diameter table from page `28`

Reason:

- each asset is exact-data dominant rather than structurally blog-ready
- they are still useful for future authority-recovery and deletion-safe provenance
- promoting them to `local_pdf_fact` would overstate secondary-PDF formulas and generic BGA defaults as reusable body authority

## Direct Blog-Consumable Outputs After This Pass

### Still directly consumable only through existing fact and wiki layers

- non-numeric package-library governance vocabulary
- previously promoted local package structural-visual facts

### Still not directly consumable from the new local evidence itself

- pin-compensation formulas
- flash-construction formulas
- generic BGA pitch-to-pad tables
- package-owner or standards-equivalent land-pattern rules

## Tracker Interpretation

- `P4-292` remains the first unified-slice landing pass
- `P4-299` adds a blocked-exact-data preservation layer inside `package` evidence
- `facts/local_pdf/` remains unchanged in this pass
