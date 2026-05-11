# P4-303 PCB资料 Package Naming-Grammar Evidence Batch 4

Date: 2026-05-08
Parent slice: `P4-292`
Execution mode: `controller_owned_evidence_expansion_only`

## Purpose

Expand the `PCB资料` unified knowledge layer by landing the remaining page-`22` package naming-grammar inventory items inside `pdf_evidence/pcb_ziliao/package/`.

This pass stays strictly inside `/code/blogs/tmps/PCB资料`.
It does not reopen `/code/blogs/tmps/materias_pdf`.
It does not create new `facts/local_pdf/` cards.

## What Landed

### New package evidence records

- `pdf_evidence/pcb_ziliao/package/via-padstack-naming-grammar.md`
- `pdf_evidence/pcb_ziliao/package/thermal-pad-or-flash-naming-grammar.md`
- `pdf_evidence/pcb_ziliao/package/irregular-pad-and-shape-naming-grammar.md`

### Tracker alignment

- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Promotion Judgment

### Kept as `blocked_evidence` / evidence-only

- via-padstack naming-grammar text from page `22`
- thermal-pad or flash naming-grammar text from page `22`
- irregular-pad and shape naming-grammar text from page `22`

Reason:

- the safe reusable value is naming-inventory provenance only
- the admitted wording today supports governance posture, not handbook house-grammar promotion
- these text examples still do not justify `local_pdf_fact` promotion because stronger package-owner, CAD-owner, or standards-backed naming authority is still missing

## Direct Blog-Consumable Outputs After This Pass

### Still directly consumable only through existing fact and wiki layers

- package-family governance vocabulary
- padstack and footprint-review governance posture

### Still not directly consumable from the local text itself

- house-formatted naming strings as universal grammar
- standards-grade library naming conventions
- direct footprint-library naming prescriptions

## Tracker Interpretation

- `P4-292` remains the first unified-slice landing pass
- `P4-303` is the next `package` evidence-only expansion batch
- `facts/local_pdf/` remains unchanged in this pass
