# P4-294 PCB资料 Package Evidence Expansion Batch 1

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_evidence_expansion_only`

## Purpose

Expand the `PCB资料` unified knowledge layer by landing the next safest `package` structural diagrams inside `pdf_evidence/pcb_ziliao/package/`.

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.
It does not create new `facts/local_pdf/` cards.

## What Landed

### New package evidence records

- `pdf_evidence/pcb_ziliao/package/no-lead-smd-footprint-variable-mapping-diagram.md`
- `pdf_evidence/pcb_ziliao/package/gull-wing-smd-footprint-variable-mapping-diagram.md`
- `pdf_evidence/pcb_ziliao/package/flat-laying-smd-footprint-variable-mapping-diagram.md`
- `pdf_evidence/pcb_ziliao/package/j-lead-smd-footprint-variable-mapping-diagram.md`

### Tracker alignment

- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Kept as `blocked_evidence` / evidence-only

- no-lead SMD geometry-variable mapping diagram from page `25`
- gull-wing SMD geometry-variable mapping diagram from page `26`
- flat-laying SMD geometry-variable mapping diagram from page `26`
- J-lead SMD geometry-variable mapping diagram from page `27`

Reason:

- the clean value is package-to-footprint variable correspondence, not a publishable equation set
- each figure remains too adjacent to compensation formulas and exact numeric expressions
- the current admitted package layer supports governance vocabulary, but not these diagrams as body-ready local facts

## Direct Blog-Consumable Outputs After This Pass

### Still directly consumable only through existing fact and wiki layers

- package-library governance vocabulary
- padstack, footprint-review, and package-family review flow
- non-numeric discussion of package-to-footprint review context

### Still not directly consumable from the local diagrams themselves

- compensation equations
- handbook numeric ranges
- package-family-specific footprint defaults
- owner-approved or standards-grade land-pattern rules

## Tracker Interpretation

- `P4-292` remains the first unified-slice landing pass
- `P4-294` is the first package follow-on evidence-only expansion batch
- `facts/local_pdf/` remains unchanged in this pass
